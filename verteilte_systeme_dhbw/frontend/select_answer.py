import requests
import os
from apiCalls import apiCalls
from user import User


def start_game():
    api = apiCalls()
    user = User()

    # fetch user_id and level from the server
    user.user_id = api.connect_user()['_id']
    user.level = api.get_level(user.user_id)['level']

    # clear the console
    os.system('cls' if os.name == 'nt' else 'clear')



    while True:

        user.level = api.get_level(user.user_id)
        print("********************************************************************************")
        print("Your current level is: " + str(user.level['level']) + "        Correct answers: " + "        Wrong answers: ")
        print("********************************************************************************")
        # Todo add correct answer counter api call
        # get question from the server
        question = api.get_question(user.user_id)
        print("\n\n")
        print(question['question'])
        print("\n")

        print("a) " + question['solution']['a'])
        print("b) " + question['solution']['b'])
        print("c) " + question['solution']['c'])
        print("\n")
        print("Is it a, b or c?")
        print("\n\n")

        while True:
            user_answer = input("Your answer: ")

            if user_answer != "a" and user_answer != "b" and user_answer != "c":
                print("Please type a, b or c!")
                continue
            else:
                break

        correct_answer = question['solution']['correct_answer']
        print("\n" * 100)
        os.system('cls' if os.name == 'nt' else 'clear')

        # check if answer is correct
        if user_answer == correct_answer:
            print("Correct!")
            api.set_answer(user.user_id, question['_id'], True)

        elif user_answer != correct_answer:
            print("False!")
            api.set_answer(user.user_id, question['_id'], False)

        user_input = input("Press Q to quit, L to adjust your level or any other key to continue... ")

        # quit game and delete user
        if user_input == "Q":
            print("Goodbye!")
            api.delete_user(user.user_id)
            exit()
        # adjust level
        elif user_input == "L":
            # catch invalid input
            while True:
                level_adjustment = int(input("Increase or decrease level by typing 1 or -1: "))
                # check if level is in the range from 1 to 10
                if level_adjustment != 1 and level_adjustment != -1:
                    print("Please type 1 or -1!")
                    continue
                else:
                    break

            # set new level
            api.update_level(user.user_id, level_adjustment)

            if level_adjustment == 1:
                print("Level increased!")
            elif level_adjustment == -1:
                print("Level decreased!")

            input("Press any key to continue... ")

        # continue game
        print("\n" * 100)
        os.system('cls' if os.name == 'nt' else 'clear')