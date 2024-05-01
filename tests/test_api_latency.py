from locust import HttpUser, TaskSet, task, between


class TestAPILatency(HttpUser):
    wait_time = between(1, 2)
    _example_user_id = "13cc528d-ada0-47a7-9aa9-2c3c0e46f373"
    _example_question_id = "08cda6d9-b2ba-4867-b096-8bacb290da05"

    @task
    def index_page(self):
        self.client.get("/")

    @task
    def get_question_for_user(self):
        # example url
        # http://127.0.0.1:8000/question/getQuestion/?user_id=13cc528d-ada0-47a7-9aa9-2c3c0e46f373
        self.client.get("/question/getQuestion/" + str("?user_id=") + str(self._example_user_id))

    @task
    def put_set_answer(self):
        # example url
        # http://127.0.0.1:8000/question/setAnswer/?user_id=13cc528d-ada0-47a7-9aa9-2c3c0e46f373&question_id=08cda6d9-b2ba-4867-b096-8bacb290da05&answer=true
        self.client.put(
            "/question/setAnswer/" + str("?user_id=") + str(self._example_user_id) + str("&question_id=") + str(
                self._example_question_id) + str("&answer=false"))

    @task
    def get_question_quantity(self):
        self.client.get("/question/quantity/" + str("?user_id=") + str(self._example_user_id))

    # @task
    # def put_user_level_update(self):
    #     self.client.put(
    #         "/user/level/update/" + str("?user_id=") + str(self._example_user_id) + str("&level_adjustment=1"))

    @task
    def get_user_level(self):
        self.client.get("/user/level/get/" + str("?user_id=") + str(self._example_user_id))
