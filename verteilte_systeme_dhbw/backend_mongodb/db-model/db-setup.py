import json
import uuid

from dotenv import dotenv_values
from fastapi.encoders import jsonable_encoder
from pymongo import MongoClient
from pydantic import BaseModel, Field

config = dotenv_values("../.env")

mongodb_client = MongoClient(config["MONGODB_URL"])
database = mongodb_client[config["MONGODB_NAME"]]

db_questions = database["questions"]


class Solution(BaseModel):
    a: str
    b: str
    c: str
    correct_answer: str
    explanation: str

    class Config:
        scheme_extra = {
            "example": {
                "a": "5",
                "b": "6",
                "c": "7",
                "correct_answer": "c",
                "explanation": "Heute gibt es auf der Erde nicht mehr nur einen, sondern insgesamt sieben "
                               "Kontinente: Nordamerika, Südamerika, Europa, Afrika, Asien, Australien und "
                               "Antarktika."
            }
        }


class Question(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    level: int
    question: str
    topic: str
    solution: Solution

    class Config:
        arbitrary_types_allowed = True
        populate_by_name = True
        scheme_extra = {
            "example": {
                "_id": "661141bf76a678c8895f1585",
                "level": 1,
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
        }


# convert data.json to list of dictionaries
with open("data.json", "r") as file:
    questions = json.load(file)

# insert questions into database
for question in questions:
    question = Question(**question)
    question = jsonable_encoder(question)
    db_questions.insert_one(question)
