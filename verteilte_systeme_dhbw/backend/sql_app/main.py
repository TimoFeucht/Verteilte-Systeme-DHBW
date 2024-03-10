from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from . import crud, models_vs, schemas
# import models
# import crud
# import schemas
from .database import SessionLocal, engine

models_vs.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_model=schemas.Message, status_code=status.HTTP_200_OK)
def read_root():
    return schemas.Message(message="Welcome to the Verteilte Systeme API.")


@app.post("/connect/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user(db: Session = Depends(get_db)):
    new_user = crud.create_new_user(db)
    if new_user:
        return new_user
    else:
        raise HTTPException(status_code=400, detail="User creation failed.")


@app.get("/question/", response_model=schemas.Question, status_code=status.HTTP_200_OK)
def get_question(user_id: int, db: Session = Depends(get_db)):
    # ToDo: check for various error cases -> sent http exception
    # user_id not found
    # no more questions for user_id
    # ...
    question = crud.get_question_for_user_id(db, user_id)
    if question:
        return question
    else:
        raise HTTPException(status_code=400, detail="Question retrieval failed.")


@app.put("/answer/", response_model=schemas.Message, status_code=status.HTTP_200_OK)
def set_answer(user_id: int, question_id, answer: bool, db: Session = Depends(get_db)):
    answered_question = crud.set_answer(db, user_id, question_id, answer)
    if not answered_question:
        raise HTTPException(status_code=404, detail="Answer could not be set. User-ID or Question-ID not found.")

    # update user level if answer is correct
    if answer:
        user = crud.update_user_level(db, user_id, 1)
        if not user:
            raise HTTPException(status_code=403, detail="User level not in range 1-10.")

    return schemas.Message(message="Answer set successfully.")


@app.put("/updateUserLevel/", response_model=schemas.Message, status_code=status.HTTP_200_OK)
def update_user_level(user_id: int, level_adjustment: int, db: Session = Depends(get_db)):
    # raise http exception, if level_adjustment is not -1 or 1
    if level_adjustment not in (-1, 1):
        raise HTTPException(status_code=403, detail="Only a level adjustment of +/- 1 is allowed.")

    user = crud.update_user_level(db, user_id, level_adjustment)
    if not user:
        raise HTTPException(status_code=403, detail="User level not in range 1-10.")

    return schemas.Message(message="Level successfully updated.")


@app.get("/userLevel/", response_model=schemas.User, status_code=status.HTTP_200_OK)
def get_user_level(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user_level(db, user_id)
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail=f"No user with user_id={user_id} found.")


@app.delete("/deleteUser/", response_model=schemas.Message, status_code=status.HTTP_200_OK)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.delete_user(db, user_id)
    if user:
        raise HTTPException(status_code=404, detail=f"No user with user_id={user_id} found.")

    return schemas.Message(message=f"User with user_id={user_id} successfully deleted.")

# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)
#
#
# @app.get("/users/", response_model=list[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users
#
#
# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user
#
#
# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#         user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)
#
#
# @app.get("/items/", response_model=list[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items
