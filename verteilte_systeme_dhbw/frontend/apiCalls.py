import requests


# Doku: http://127.0.0.1:8000/docs#/
class apiCalls:
    connect_user_url = 'http://user/connect/'
    get_question_url = 'http://question/getQuestion/'
    set_answer_url = 'http://question/setAnswer/'
    update_level_url = 'http://user/level/update/'
    get_level_url = 'http://user/level/get'
    delete_user_url = 'http://user/delete/'

    def connect_user(self):
        response = requests.post(self.connect_user_url)
        return response.json()

    # params required: user_id
    def get_question(self, user_id):
        response = requests.get(self.get_question_url, params={'user_id': user_id})
        return response.json()

    # params required: user_id, question_id, answer
    def set_answer(self, user_id, question_id, answer):
        response = requests.put(self.set_answer_url, params={'user_id': user_id, 'question_id': question_id, 'answer': answer})
        return response.json()

    # params required: user_id, level_adjustment
    def update_level(self, user_id, level_adjustment):
        response = requests.put(self.update_level_url, params={'user_id': user_id, 'level_adjustment': level_adjustment})
        return response.json()

    # params required: user_id
    def get_level(self, user_id):
        response = requests.get(self.get_level_url, params={'user_id': user_id})
        return response.json()

    # params required: user_id
    def delete_user(self, user_id):
        response = requests.delete(self.delete_user_url, params={'user_id': user_id})
        return response.json()