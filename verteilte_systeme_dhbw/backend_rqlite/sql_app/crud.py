from typing import Any

from sqlalchemy import text, select
from sqlalchemy.orm import Session

from . import models, schemas


# import models
# import schemas


def create_new_user(db: Session):
    db_user = models.User(level=1)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def verify_user(db: Session, user_id: int):
    """
    Verify user_id
    :param db: database session
    :param user_id: schemas.User.id
    :return: schemas.User | None
    Returns a user if the user_id is valid, otherwise None. Use for verifying user_id before using it in other functions.
    """
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        return user
    else:
        return None


def get_question_for_user_id(db: Session, user: schemas.User):
    """
    Get a question for a user_id
    :param db: database session
    :param user: schemas.User
    :return: schemas.Question
    Returns a question for a user_id and the users level which has been answered false.
    If the user has already answered all questions correct, a new question is returned for the same level.
    """
    sql_query_get_old_question_with_false_answer = text("SELECT q.q_id FROM questions AS q INNER JOIN "
                                                        "answered_questions AS a ON q.q_id = a.q_id WHERE "
                                                        "a.answer=false AND a.u_id = :u_id AND q.level= :level;")

    sql_query_get_new_question = text("SELECT q.q_id FROM questions AS q WHERE q.level = :level EXCEPT SELECT a.q_id "
                                      "FROM answered_questions AS a WHERE a.u_id = :u_id;")

    sql_query_get_question_data = text("SELECT q.q_id, q.level, q.question, s.a, s.b, s.c, s.correct_answer, "
                                       "s.explanation, t.name FROM questions AS q INNER JOIN solutions AS s ON q.s_id "
                                       "= s.s_id INNER JOIN topics AS t ON q.t_id = t.t_id WHERE q.q_id = :q_id;")

    result = db.execute(sql_query_get_old_question_with_false_answer, {"u_id": user.id, "level": user.level}).fetchone()
    if not result:
        result = db.execute(sql_query_get_new_question, {"u_id": user.id, "level": user.level}).fetchone()

    data = db.execute(sql_query_get_question_data, {"q_id": result[0]}).fetchone()

    solution = schemas.Solution(a=data[3], b=data[4], c=data[5], correct_answer=data[6], explanation=data[7])
    question = schemas.Question(id=data[0], level=data[1], topic=data[8], question=data[2], solution=solution)

    return question


def update_user_level(db: Session, user: schemas.User, increment: int = -1 | 1):
    """
    Update user level
    :param db: database session
    :param user: schemas.User
    :param increment:  -1 | 1
    :return: schemas.User
    Returns a user with updated level or None if the new level is not in the range 1-10.
    """
    new_user_level = user.level + increment
    # user level not in range 1-10
    if new_user_level < 1 or new_user_level > 10:
        return None

    # update user level
    user.level = new_user_level
    db.commit()
    db.refresh(user)
    return user


def set_answer(db: Session, user: schemas.User, question_id: int, answer: bool):
    """
    Set answer for user_id and question_id
    :param db: database session
    :param user: schemas.User
    :param question_id: int for question_id
    :param answer: bool for answer
    :return: schemas.AnsweredQuestion | None
    Returns a new entry in answered_questions or updates an existing entry.
    """
    # new entry in answered_questions
    # set answer for user_id and question_id only if user_id and question_id are valid
    question = db.query(models.Question).filter(models.Question.id == question_id).first()
    if not question:
        return None

    db_answered_question = db.query(models.AnsweredQuestion).filter(
        models.AnsweredQuestion.u_id == user.id, models.AnsweredQuestion.q_id == question_id).first()

    if db_answered_question:
        # update answer if already answered
        db_answered_question.answer = answer
    else:
        # set answer
        db_answered_question = models.AnsweredQuestion(u_id=user.id, q_id=question_id, answer=answer)
        db.add(db_answered_question)

    db.commit()
    db.refresh(db_answered_question)

    return db_answered_question


def delete_user(db: Session, user: schemas.User):
    # delete user
    try:
        db.delete(user)
        db.commit()
        return True
    except Exception as e:
        return e
