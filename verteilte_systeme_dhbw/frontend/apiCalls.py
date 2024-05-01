import requests


class apiCalls:

    def __init__(self, local_urls=True):
        self.base_urls = [
            'http://127.0.0.1:8000/',
            'http://127.0.0.2:8000/',
            'http://127.0.0.3:8000/'
        ] if local_urls else [
            'http://10.8.0.1:9999/',
            'http://10.8.0.2:9999/',
        ]
        self.base_url = self.get_base_url()
        self.update_urls()

    def get_base_url(self):
        for base_url in self.base_urls:
            try:
                response = requests.get(base_url)
                if response.status_code == 200:
                    print(f"Connected to {base_url}")
                    return base_url
            except requests.exceptions.RequestException as e:
                print(f"Error connecting to {base_url}: {e}")
        return None  # Falls back to None if no servers are available

    def update_urls(self):
        self.connect_user_url = self.base_url + 'user/connect/'
        self.get_question_url = self.base_url + 'question/getQuestion/'
        self.set_answer_url = self.base_url + 'question/setAnswer/'
        self.update_level_url = self.base_url + 'user/level/update/'
        self.get_level_url = self.base_url + 'user/level/get/'
        self.delete_user_url = self.base_url + 'user/delete/'
        self.get_question_quantity_url = self.base_url + 'question/quantity/'

    def try_request(self, method, url_suffix, **kwargs):
        full_url = self.base_url + url_suffix
        try:
            response = getattr(requests, method)(full_url, **kwargs)
            if response.status_code in [200, 201]:
                return response.json()
            else:
                raise requests.exceptions.HTTPError(f"Error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error with {full_url}: {e}")
            self.base_url = self.get_base_url()  # Attempt to find a new working server
            if self.base_url:
                self.update_urls()  # Update all URLs to reflect the new base URL
                return self.try_request(method, url_suffix, **kwargs)  # Recursive call with updated URL
            else:
                return None  # Return None if no servers are available after rechecking

    def connect_user(self):
        return self.try_request('post', 'user/connect/')

    def get_question(self, user_id):
        """
        Get a question for the user with the given ID.
        Problem came up that Server sends 400 if no question is available, so it needs to be handled.

        :param user_id:
        :return:
        """

        full_url = self.base_url + 'question/getQuestion/'
        try:
            response = requests.get(full_url, params={'user_id': user_id})
            if response.status_code == 200:
                return response.json()  # Return the data if the request was successful
            elif response.status_code == 400:

                return None  # Handle the 400 error without retrying
            else:
                raise requests.exceptions.HTTPError(f"HTTP Error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Network or HTTP error occurred: {e}")
            # Optionally try to find a new server or log the error based on the failure
            self.base_url = self.get_base_url()  # Try to find a new working server
            if self.base_url:
                self.update_urls()  # Update URLs to the new base URL
                return self.get_question(user_id)  # Recursive call with updated URL
            else:
                print("No available servers to handle the request.")
                return None  # Return None if no servers are available after rechecking

    def set_answer(self, user_id, question_id, answer):
        return self.try_request('put', 'question/setAnswer/',
                                params={'user_id': user_id, 'question_id': question_id, 'answer': answer})

    def update_level(self, user_id, level_adjustment):
        """
        Update the user's level by the given adjustment value.

        Problem occurred that an infinity loop was created when the level was already at the minimum or maximum level, and the user tried to adjust it further.
        Fixed by adding checks for the minimum and maximum level boundaries.

        :param user_id:
        :param level_adjustment:
        :return:
        """

        # Fetch current level first to ensure the level adjustment is valid
        current_level_info = self.get_level(user_id)
        if current_level_info is None:
            print("Failed to retrieve current level. Please try again.")
            return None

        # Define the minimum and maximum level boundaries
        min_level = 1
        max_level = 5
        current_level = current_level_info['level']

        # Calculate the new level after adjustment
        new_level = current_level + level_adjustment

        # Check if the new level is within the allowed range
        if new_level < min_level:
            print("\nYou are already at the lowest level. Please only increase\n")
            return None
        elif new_level > max_level:
            print("\nYou are already at the highest level. Please only decrease\n")
            return None

        # If the level adjustment is valid, proceed to update the level
        try:
            response = self.try_request('put', 'user/level/update/',
                                        params={'user_id': user_id, 'level_adjustment': level_adjustment})
            if response:
                print("Level updated successfully to:", new_level)
                return response
            else:
                return None
        except Exception as e:
            print(f"Error updating level: {e}")
            return None

    def get_level(self, user_id):
        return self.try_request('get', 'user/level/get/', params={'user_id': user_id})

    def delete_user(self, user_id):
        return self.try_request('delete', 'user/delete/', params={'user_id': user_id})

    def get_question_quantity(self, user_id):
        return self.try_request('get', 'question/quantity/', params={'user_id': user_id})
