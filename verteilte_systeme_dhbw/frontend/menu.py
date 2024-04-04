import requests
from select_answer import *
import os



while True:
    # menu for user
    print("\n")
    print("****************************************")
    print("       Welcome to the quiz game!")
    print("****************************************")
    print("\n")
    print("- You're going to get questions and you have to answer them by choosing between the options a, b or c.")
    print("- On the top of the screen you can see the current level and the number of correct and wrong answers.")
    print("- The difficulty level of the questions will increase with every correct answer. False answers are not "
          "going to cost you levels.")
    print("- You can increase or decrease your level manually by pressing L.")
    print("\n")

    while True:

        user_input = input("Press S (Start) or Q(Quit)")

        if user_input == "S":
            # clear the console
            print("\n" * 100)
            os.system('cls' if os.name == 'nt' else 'clear')
            start_game()

        elif user_input == "Q":
            print("Goodbye!")
            exit()
        else:
            print("Please enter a valid input!")
            continue






