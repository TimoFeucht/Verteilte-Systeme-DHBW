import requests
import os
url = 'http://127.0.0.1:8000'
url1 = 'http://127.0.0.1:8000/connect/'
url2 = 'http://127.0.0.1:8000/question/'


def start_game():
    data2 = {
        "user_id": 1
    }
    # clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

    response = requests.get(url)
    print(response.status_code)

    print("Current level:         Correct answers: ")
    print("\n")
    print("Answer with a, b or c")


