import requests

class apiCalls:
    def __init__(self):
        self.base_urls = [
            'http://127.0.0.1:8000/',
            'http://127.0.0.2:8000/',
            'http://127.0.0.3:8000/'
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
        self.get_level_url = self.base_url + 'user/level/get'
        self.delete_user_url = self.base_url + 'user/delete/'

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
        return self.try_request('get', 'question/getQuestion/', params={'user_id': user_id})

    def set_answer(self, user_id, question_id, answer):
        return self.try_request('put', 'question/setAnswer/', params={'user_id': user_id, 'question_id': question_id, 'answer': answer})

    def update_level(self, user_id, level_adjustment):
        return self.try_request('put', 'user/level/update/', params={'user_id': user_id, 'level_adjustment': level_adjustment})

    def get_level(self, user_id):
        return self.try_request('get', 'user/level/get', params={'user_id': user_id})

    def delete_user(self, user_id):
        return self.try_request('delete', 'user/delete/', params={'user_id': user_id})
