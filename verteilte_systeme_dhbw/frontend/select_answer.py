import requests
import os
from apiCalls import apiCalls
from user import User


def start_game():
    api = apiCalls()
    user = User()

    # fetch user_id and level from the server
    user_response = api.connect_user()
    if not user_response:
        print("Failed to connect to the server. Please try again later.")
        return
    user.user_id = user_response['_id']

    # clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        level_info = api.get_level(user.user_id)
        if not level_info:
            print("Failed to fetch user level.")
            continue
        user.level = level_info['level']

        answer_count = api.get_question_quantity(user.user_id)
        if not answer_count:
            print("Failed to fetch answer count.")
            continue

        print("********************************************************************************")
        print(
            f"Your current level is: {user.level}      Correct answers: {answer_count['correct_answers']}      Wrong answers: {answer_count['wrong_answers']}")
        print("********************************************************************************")

        question = api.get_question(user.user_id)
        if question is None:
            print("\n\nSorry, no questions left in this level! Please adjust your level.\n")
            adjust_level(api, user)  # Funktion zum Anpassen des Levels
            continue

        print_question(question)
        user_answer = get_user_answer(question)

        if user_answer == question['solution']['correct_answer']:
            print("Correct!")
            api.set_answer(user.user_id, question['_id'], True)
        else:
            print("False!")
            api.set_answer(user.user_id, question['_id'], False)

        user_input = input("Press Q to quit, L to adjust your level, or any other key to continue... ")

        if user_input == "Q":
            print("Goodbye!")
            api.delete_user(user.user_id)
            exit()
        elif user_input == "L":
            adjust_level(api, user)


def adjust_level(api, user):
    while True:
        level_adjustment = input("Increase or decrease level by typing 1 or -1: ")
        if level_adjustment in ['1', '-1']:
            level_adjustment = int(level_adjustment)
            api.update_level(user.user_id, level_adjustment)
            print("Level increased!" if level_adjustment == 1 else "Level decreased!")
            break
        else:
            print("Please type 1 or -1!")


def print_question(question):
    print("\n\n")
    print(question['question'])
    print("\n")
    print("a) " + question['solution']['a'])
    print("b) " + question['solution']['b'])
    print("c) " + question['solution']['c'])
    print("\n")
    print("Is it a, b or c?")
    print("\n\n")


def get_user_answer(question):
    while True:
        user_answer = input("Your answer: ")
        if user_answer in ['a', 'b', 'c']:
            return user_answer
        print("Please type a, b or c!")
