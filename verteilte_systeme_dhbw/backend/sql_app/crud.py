from typing import Any

from sqlalchemy.orm import Session

from . import models_vs, schemas


# import models
# import schemas


def create_new_user(db: Session):
    db_user = models_vs.User(level=1)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_question_for_user_id(db: Session, user_id: int):
    # get user level
    user = db.query(models_vs.User).filter(models_vs.User.id == user_id).first()
    # get question with user level = question level
    # ToDo: check if question is already answered by user -> if yes, get next question
    # use table answered_questions
    question = db.query(models_vs.Question).filter(models_vs.Question.level == user.level).first()
    # get topic name
    topic = db.query(models_vs.Topic).filter(models_vs.Topic.id == question.t_id).first()
    # get solution
    solution = db.query(models_vs.Solution).filter(models_vs.Solution.id == question.s_id).first()

    solution_class = schemas.SolutionBase(a=solution.a, b=solution.b, c=solution.c,
                                          correct_answer=solution.correct_answer, explanation=solution.explanation)

    # return question with topic name and solution
    return schemas.Question(id=question.id, level=question.level, topic=topic.name, question=question.question,
                            solution=solution_class)


def update_user_level(db: Session, user_id: int, increment: int = -1 | 1):
    # update user level
    user = db.query(models_vs.User).filter(models_vs.User.id == user_id).first()

    new_user_level = user.level + increment
    # user level not in range 1-10
    if new_user_level < 1 or new_user_level > 10:
        return None

    # update user level
    user.level = new_user_level
    db.commit()
    db.refresh(user)
    return user


def set_answer(db: Session, user_id: int, question_id: int, answer: bool):
    # new entry in answered_questions
    # set answer for user_id and question_id only if user_id and question_id are valid
    user = db.query(models_vs.User).filter(models_vs.User.id == user_id).first()
    question = db.query(models_vs.Question).filter(models_vs.Question.id == question_id).first()
    if not user or not question:
        return None

    db_answered_question = db.query(models_vs.AnsweredQuestion).filter(
        models_vs.AnsweredQuestion.u_id == user_id, models_vs.AnsweredQuestion.q_id == question_id).first()

    if db_answered_question:
        # update answer if already answered
        db_answered_question.answer = answer
    else:
        # set answer
        db_answered_question = models_vs.AnsweredQuestion(u_id=user_id, q_id=question_id, answer=answer)
        db.add(db_answered_question)

    db.commit()
    db.refresh(db_answered_question)

    return db_answered_question


def get_user_level(db: Session, user_id: int):
    user = db.query(models_vs.User).filter(models_vs.User.id == user_id).first()
    return user


def delete_user(db: Session, user_id: int):
    # delete user
    user = db.query(models_vs.User).filter(models_vs.User.id == user_id).first()
    db.delete(user)
    db.commit()
    return user

# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()
#
#
# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()
#
#
# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()
#
#
# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()
#
#
# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
