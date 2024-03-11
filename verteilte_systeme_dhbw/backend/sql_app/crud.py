from typing import Any

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
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        return user
    else:
        return None


def get_question_for_user_id(db: Session, user: schemas.User):
    # get question with user level = question level
    # ToDo: check if question is already answered by user -> if yes, get next question
    # use table answered_questions
    question = db.query(models.Question).filter(models.Question.level == user.level).first()
    # get topic name
    topic = db.query(models.Topic).filter(models.Topic.id == question.t_id).first()
    # get solution
    solution = db.query(models.Solution).filter(models.Solution.id == question.s_id).first()

    solution_class = schemas.Solution(a=solution.a, b=solution.b, c=solution.c,
                                      correct_answer=solution.correct_answer, explanation=solution.explanation)

    # return question with topic name and solution
    return schemas.Question(id=question.id, level=question.level, topic=topic.name, question=question.question,
                            solution=solution_class)


def update_user_level(db: Session, user: schemas.User, increment: int = -1 | 1):
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
