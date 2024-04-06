from fastapi import FastAPI, status
from dotenv import dotenv_values
from pymongo import MongoClient

# from . import crud, models, schemas
from . import schemas
# import models
# import crud
# import schemas

config = dotenv_values(".env")
app = FastAPI()


@app.on_event("startup")
async def startup_event():
    app.mongodb_client = MongoClient(config["MONGODB_URL"])
    app.mongodb = app.mongodb_client[config["MONGODB_NAME"]]
    print("Connected to MongoDB.")


@app.on_event("shutdown")
async def shutdown_event():
    app.mongodb_client.close()
    print("Disconnected from MongoDB.")


@app.get("/", response_model=schemas.Message, status_code=status.HTTP_200_OK)
def read_root():
    return schemas.Message(message="Welcome to the Verteilte Systeme API.")

#
#
# @app.post("/user/connect/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
# def create_user(db: Session = Depends(get_db)):
#     new_user = crud.create_new_user(db)
#     if new_user:
#         return new_user
#     else:
#         raise HTTPException(status_code=400, detail="User creation failed.")
#
#
# @app.get("/question/getQuestion/", response_model=schemas.Question, status_code=status.HTTP_200_OK)
# def get_question(user_id: int, db: Session = Depends(get_db)):
#     user = crud.verify_user(db, user_id)
#     if not user:
#         raise HTTPException(status_code=404, detail=f"No user with user_id={user_id} found.")
#
#     question = crud.get_question_for_user_id(db, user)
#     if question:
#         return question
#     else:
#         raise HTTPException(status_code=400, detail="Question retrieval failed. All questions in level answered "
#                                                     "correctly?")
#
#
# @app.put("/question/setAnswer/", response_model=schemas.Message, status_code=status.HTTP_200_OK)
# def set_answer(user_id: int, question_id: int, answer: bool, db: Session = Depends(get_db)):
#     user = crud.verify_user(db, user_id)
#     if not user:
#         raise HTTPException(status_code=404, detail=f"Answer could not be set. No user with user_id={user_id} found.")
#
#     answered_question = crud.set_answer(db, user, question_id, answer)
#     if not answered_question:
#         raise HTTPException(status_code=404, detail=f"Answer could not be set. question-ID={question_id} not found.")
#
#     # update user level if answer is correct
#     if answer:
#         user = crud.update_user_level(db, user, 1)
#         if not user:
#             raise HTTPException(status_code=403, detail="User level not in range 1-10.")
#
#     return schemas.Message(message="Answer set successfully.")
#
#
# @app.put("/user/level/update/", response_model=schemas.Message, status_code=status.HTTP_200_OK)
# def update_user_level(user_id: int, level_adjustment: int, db: Session = Depends(get_db)):
#     # raise http exception, if level_adjustment is not -1 or 1
#     if level_adjustment not in (-1, 1):
#         raise HTTPException(status_code=403, detail="Only a level adjustment of +/- 1 is allowed.")
#
#     user = crud.verify_user(db, user_id)
#     if not user:
#         raise HTTPException(status_code=404, detail=f"No user with user_id={user_id} found.")
#
#     user = crud.update_user_level(db, user, level_adjustment)
#     if not user:
#         raise HTTPException(status_code=403, detail="User level not in range 1-10.")
#
#     return schemas.Message(message="Level successfully updated.")
#
#
# @app.get("/user/level/get/", response_model=schemas.User, status_code=status.HTTP_200_OK)
# def get_user_level(user_id: int, db: Session = Depends(get_db)):
#     user = crud.verify_user(db, user_id)
#     if not user:
#         raise HTTPException(status_code=404, detail=f"No user with user_id={user_id} found.")
#
#     return user
#
#
# @app.delete("/user/delete/", response_model=schemas.Message, status_code=status.HTTP_200_OK)
# def delete_user(user_id: int, db: Session = Depends(get_db)):
#     user = crud.verify_user(db, user_id)
#     if not user:
#         raise HTTPException(status_code=404, detail=f"No user with user_id={user_id} found.")
#
#     ret = crud.delete_user(db, user)
#     if ret is not True:
#         raise HTTPException(status_code=400, detail=f"User with user_id={user_id} could not be deleted.")
#
#     return schemas.Message(message=f"User with user_id={user_id} successfully deleted.")
