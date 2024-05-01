import unittest
import time
from verteilte_systeme_dhbw.frontend.apiCalls import apiCalls


class TestAPILatency:
    def __init__(self):
        self.api = apiCalls(local_urls=False)
        self.user_id = self.get_user_id()
        self.question_id = self.get_question_id()

    def get_user_id(self):
        response = self.api.connect_user()
        return response['_id']

    def get_question_id(self):
        response = self.api.get_question(self.user_id)
        return response['_id']

    def test_average_latency(self):
        # List all routes to be tested
        functions = [
            apiCalls.get_question(self.api, self.user_id),
            apiCalls.set_answer(self.api, self.user_id, self.question_id, True),
            apiCalls.update_level(self.api, self.user_id, 1),
            apiCalls.get_level(self.api, self.user_id),
            apiCalls.get_question_quantity(self.api, self.user_id),
            apiCalls.delete_user(self.api, self.user_id),
        ]
        total_time = 0
        num_requests = len(functions)

        for fun in functions:
            start_time = time.time()
            response = fun
            print(response)
            end_time = time.time()
            print(f"Time: {end_time - start_time:.8f} seconds")
            total_time += (end_time - start_time)

        average_latency = total_time / num_requests
        print(f"Average Latency: {average_latency:.4f} seconds")


if __name__ == '__main__':
    t = TestAPILatency()
    t.test_average_latency()
