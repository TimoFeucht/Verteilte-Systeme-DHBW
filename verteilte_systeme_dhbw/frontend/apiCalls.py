import requests


# Doku: http://127.0.0.1:8000/docs#/
class apiCalls:


    def __init__(self):
        self.base_url = self.get_base_url()
        self.connect_user_url = self.base_url + 'user/connect/'
        self.get_question_url = self.base_url + 'question/getQuestion/'
        self.set_answer_url = self.base_url + 'question/setAnswer/'
        self.update_level_url = self.base_url + 'user/level/update/'
        self.get_level_url = self.base_url + 'user/level/get'
        self.delete_user_url = self.base_url + 'user/delete/'

    def get_base_url(self):
        """
            base_url='http://127.0.0.1:8000'
            base_url1 = 'http://192.180.65'
            base_url2 = 'http://192.180.66'
            base_url3= 'http://192.180.67'
            """
        base_urls = [
            'http://127.0.0.1:8000/',
            'http://127.0.0.2:8000/',
            'http://127.0.0.3:8000/'
        ]
        for base_url in base_urls:
            try:
                response = requests.get(base_url)
                if response.status_code == 200:
                    return base_url
            except requests.exceptions.RequestException as e:
                print(f"Error connecting to {base_url}: {e}")
        print("No connection to any server possible")


    def connect_user(self):
        response = requests.post(self.connect_user_url)
        # catch when status code not starting with 2
        if response.status_code != 200 and response.status_code != 201:
            print(self.connect_user_url)
            print("Error: " + str(response.status_code) + " " + str(response.text))
            return None
        return response.json()

    # params required: user_id
    def get_question(self, user_id):
        response = requests.get(self.get_question_url, params={'user_id': user_id})
        if response.status_code != 200 and response.status_code != 201:
            print("Error: " + str(response.status_code))
            return None
        return response.json()

    # params required: user_id, question_id, answer
    def set_answer(self, user_id, question_id, answer):
        response = requests.put(self.set_answer_url,
                                params={'user_id': user_id, 'question_id': question_id, 'answer': answer})
        if response.status_code != 200 and response.status_code != 201:
            print("Error: " + str(response.status_code))
            return None
        return response.json()

    # params required: user_id, level_adjustment
    def update_level(self, user_id, level_adjustment):
        response = requests.put(self.update_level_url,
                                params={'user_id': user_id, 'level_adjustment': level_adjustment})
        if response.status_code != 200 and response.status_code != 201:
            print("Error: " + str(response.status_code))
            return None
        return response.json()

    # params required: user_id
    def get_level(self, user_id):
        response = requests.get(self.get_level_url, params={'user_id': user_id})
        if response.status_code != 200 and response.status_code != 201:
            print("Error: " + str(response.status_code))
            return None
        return response.json()

    # params required: user_id
    def delete_user(self, user_id):
        response = requests.delete(self.delete_user_url, params={'user_id': user_id})
        if response.status_code != 200 and response.status_code != 201:
            print("Error: " + str(response.status_code))
            return None
        return response.json()
