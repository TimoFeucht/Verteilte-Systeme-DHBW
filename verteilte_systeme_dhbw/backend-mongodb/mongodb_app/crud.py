import uuid

from fastapi import Request
from fastapi.encoders import jsonable_encoder
from sqlalchemy import text, select

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
    # search for false answered question in user of level x
    if user["answered_questions"]:
        for answered_question in user["answered_questions"]:
            if not answered_question["answer"]:
                old_question = request.app.database["questions"].find_one(
                    {"_id": answered_question["question_id"], "level": user["level"]})
                if old_question:
                    return old_question

    new_question = request.app.database["questions"].find_one({"level": user["level"], "question_id": {
        "$nin": [answered_question["question_id"] for answered_question in user["answered_questions"]]}})
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


def set_answer(request: Request, user: models.User, question_id: uuid.uuid4, answer: bool):
    """
    Set answer for user_id and question_id
    :param request: database session
    :param user: schemas.User
    :param question_id: int for question_id
    :param answer: bool for answer
    :return: schemas.AnsweredQuestion | None
    Returns a new entry in answered_questions or updates an existing entry.
    """
    # update answer for question if already answered
    update_result = request.app.database["users"].update_one(
        {"_id": user["_id"], "answered_questions.question_id": question_id},
        {"$set": {"answered_questions.$.answer": answer}},
    )
    # if question not answered yet, add new entry
    if update_result.modified_count == 0:
        update_result = request.app.database["users"].update_one(
            {"_id": user["_id"]},
            {"$push": {"answered_questions": {"question_id": question_id, "answer": answer}}}
        )

    return update_result


def delete_user(request: Request, user: models.User):
    # delete user
    try:
        request.app.database["users"].delete_one({"_id": user["_id"]})
        return True
    except Exception as e:
        return e
