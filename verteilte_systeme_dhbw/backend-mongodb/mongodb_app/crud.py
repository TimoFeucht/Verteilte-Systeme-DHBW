import uuid

from fastapi import Request
from fastapi.encoders import jsonable_encoder

from . import models


# import models
# import schemas


def create_new_user(request: Request):
    db_user = models.User(level=1)
    request.app.database["users"].insert_one(jsonable_encoder(db_user))
    return db_user


def verify_user(request: Request, user_id: uuid.uuid4):
    """
    Verify user_id
    :param request: database session
    :param user_id: schemas.User.id
    :return: schemas.User | None
    Returns a user if the user_id is valid, otherwise None. Use for verifying user_id before using it in other functions.
    """
    user = request.app.database["users"].find_one({"_id": user_id})
    if user:
        return user
    else:
        return None


def verify_question(request: Request, question_id: uuid.uuid4):
    """
    Verify question_id
    :param request: database session
    :param question_id: schemas.Question.id
    :return: schemas.Question | None
    Returns a question if the question_id is valid, otherwise None. Use for verifying question_id before using it in other functions.
    """
    question = request.app.database["questions"].find_one({"_id": question_id})
    if question:
        return question
    else:
        return None


def get_question_for_user(request: Request, user: models.User):
    """
    Get a question for a user_id
    :param request: database session
    :param user: schemas.User
    :return: schemas.Question
    Returns a question for a user_id and the users level which has been answered false.
    If the user has already answered all questions correct, a new question is returned for the same level.
    """
    # extract question_id's from answered_questions where answer is false in user's level
    repeated_question_ids = [answered_question["question_id"] for answered_question in user["answered_questions"]
                             if not answered_question["answer"] and answered_question["level"] == user["level"]]

    # remove correct answered questions from repeated_question_ids
    for answered_question in user["answered_questions"]:
        if answered_question["answer"] and answered_question["level"] == user["level"]:
            repeated_question_ids.remove(answered_question["question_id"])

    # return old question with wrong answer, if all questions have been answered correctly, return a new question
    if repeated_question_ids:
        print("Old question with wrong answer found.")
        question = request.app.database["questions"].find_one({"_id": repeated_question_ids[0]})
        return question

    excluded_question_ids = [answered_question["question_id"] for answered_question in user["answered_questions"]]
    new_question = request.app.database["questions"].find_one({"level": user["level"], "_id": {
        "$nin": excluded_question_ids}})
    return new_question


def update_user_level(request: Request, user: models.User, increment: int = -1 | 1):
    """
    Update user level
    :param request: database session
    :param user: schemas.User
    :param increment:  -1 | 1
    :return: schemas.User
    Returns a user with updated level or None if the new level is not in the range 1-10.
    """
    new_user_level = user["level"] + increment
    # user level not in range 1-10
    if new_user_level < 1 or new_user_level > 10:
        return None

    # update user level
    update_result = request.app.database["users"].update_one(
        {"_id": user["_id"]}, {"$set": {"level": new_user_level}}
    )

    return update_result


def set_answer(request: Request, user: models.User, question: models.Question, answer: bool):
    """
    Set answer for user_id and question_id
    :param question: models.Question
    :param request: database session
    :param user: models.User
    :param answer: bool for answer
    :return: schemas.AnsweredQuestion | None
    Returns a new entry in answered_questions or updates an existing entry.
    """
    update_result = request.app.database["users"].update_one(
        {"_id": user["_id"]},
        {"$push": {
            "answered_questions": {"question_id": question["_id"], "level": question["level"], "answer": answer}}}
    )
    return update_result


def delete_user(request: Request, user: models.User):
    # delete user
    try:
        request.app.database["users"].delete_one({"_id": user["_id"]})
        return True
    except Exception as e:
        return e
