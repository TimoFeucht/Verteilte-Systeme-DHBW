from fastapi import APIRouter, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from . import models

from . import crud

router = APIRouter()


@router.get("/getRandom/", response_description="get a random question", status_code=status.HTTP_200_OK,
            response_model=models.Question)
def get_random_question(request: Request):
    question = request.app.database["questions"].find_one()
    print("Questions successfully retrieved.")
    print(question)
    return question


@router.get("/getQuestion/", response_description="get a question with the user's level",
            status_code=status.HTTP_200_OK, response_model=models.Question)
def get_question(request: Request, user_id: str):
    user = crud.verify_user(request, user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"No user with user_id={user_id} found.")

    question = crud.get_question_for_user(request, user)
    if question:
        return question
    else:
        raise HTTPException(status_code=400, detail="Question retrieval failed. All questions in level answered "
                                                    "correctly?")


@router.put("/setAnswer/", response_description="set answer for a question", status_code=status.HTTP_200_OK,
            response_model=models.Message)
def set_answer(request: Request, user_id: str, question_id: str, answer: bool):
    user = crud.verify_user(request, user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"Answer could not be set. No user with user_id={user_id} found.")

    question = crud.verify_question(request, question_id)
    if not question:
        raise HTTPException(status_code=404, detail=f"Answer could not be set. No question with question_id={question_id} found.")

    updated_user = crud.set_answer(request, user, question, answer)
    if updated_user.modified_count == 0:
        raise HTTPException(status_code=404, detail=f"Answer could not be set.")

    # update user level if answer is correct
    if answer:
        user = crud.update_user_level(request, user, 1)
        if not user:
            raise HTTPException(status_code=403, detail="User level not in range 1-10.")

    return models.Message(message="Answer set successfully.")


@router.get("/quantity/", response_description="get the quantity of questions", status_code=status.HTTP_200_OK,
            response_model=models.QuestionQuantity)
def get_quantity(request: Request, user_id: str):
    user = crud.verify_user(request, user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"No user with user_id={user_id} found.")

    total_questions = 0
    correct_answers = 0
    wrong_answers = 0

    for answered_question in user["answered_questions"]:
        total_questions += 1
        if answered_question["answer"]:
            correct_answers += 1
        else:
            wrong_answers += 1

    quantity = models.QuestionQuantity(total_questions=total_questions, correct_answers=correct_answers, wrong_answers=wrong_answers)

    return quantity



# @router.post("/create/", response_description="Create a new questions", status_code=status.HTTP_201_CREATED,
#              response_model=models.Question)
# def create_new_question(request: Request):
#     test_question = {
#         "level": 2,
#         "topic": "geographie",
#         "question": "Wie viele Kontinente hat die Erde?",
#         "solution": {
#             "a": "5",
#             "b": "6",
#             "c": "7",
#             "correct_answer": "c",
#             "explanation": "Heute gibt es auf der Erde nicht mehr nur einen, sondern insgesamt sieben "
#                            "Kontinente: Nordamerika, Südamerika, Europa, Afrika, Asien, Australien und "
#                            "Antarktika."
#         }
#     }
#     # convert test_question to model.Question
#     question = models.Question(**test_question)
#     question = jsonable_encoder(question)
#
#     new_question = request.app.database["questions"].insert_one(question)
#     created_question = request.app.database["questions"].find_one(
#         {"_id": new_question.inserted_id}
#     )
#
#     return created_question
