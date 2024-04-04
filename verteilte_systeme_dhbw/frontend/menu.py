import requests
from select_answer import *
import os

url = 'http://127.0.0.1:8000'
url1 = 'http://127.0.0.1:8000/connect/'
url2 = 'http://127.0.0.1:8000/question/'

while True:
    # menu for user
    print("\n")
    print("****************************************")
    print("       Welcome to the quiz game!")
    print("****************************************")
    print("\n")
    print("- You're going to get questions and you have to answer them by choosing between the options a, b or c.")
    print("- On the top of the screen you can see the current level and the number of correct answers.")
    print("- The difficulty level of the questions will increase with every correct answer. False answers are not "
          "going to cost you levels.")
    print("\n")
    user_input = input("Press S (Start) or Q(Quit)")

    if user_input == "S":
        # clear the console
        print("\n" * 100)
        os.system('cls' if os.name == 'nt' else 'clear')
        start_game()

    elif user_input == "Q":
        print("Goodbye!")
        exit()






