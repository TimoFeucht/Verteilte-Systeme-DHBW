from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
from . import models

router = APIRouter()


@router.get("/random/", response_description="get a random question", status_code=status.HTTP_200_OK, response_model=models.Question)
def get_random_question(request: Request):
    question = request.app.database["questions"].find_one()
    print("Questions successfully retrieved.")
    print(question)
    return question


@router.post("/create/", response_description="Create a new question", status_code=status.HTTP_201_CREATED,
             response_model=models.Question)
def create_new_question(request: Request):
    test_question = {
        "level": 2,
        "topic": "geographie",
        "question": "Wie viele Kontinente hat die Erde?",
        "solution": {
            "a": "5",
            "b": "6",
            "c": "7",
            "correct_answer": "c",
            "explanation": "Heute gibt es auf der Erde nicht mehr nur einen, sondern insgesamt sieben "
                           "Kontinente: Nordamerika, Südamerika, Europa, Afrika, Asien, Australien und "
                           "Antarktika."
        }
    }
    # convert test_question to model.Question
    question = models.Question(**test_question)
    print(question)
    question = jsonable_encoder(question)
    print(question)
    new_question = request.app.database["questions"].insert_one(question)
    created_question = request.app.database["questions"].find_one(
        {"_id": new_question.inserted_id}
    )

    return created_question
