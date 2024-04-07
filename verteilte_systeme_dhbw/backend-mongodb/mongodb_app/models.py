import uuid
from uuid import uuid4
from typing import Optional
from pydantic import BaseModel, Field


class AnsweredQuestion(BaseModel):
    question_id: str
    answer: bool


class User(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    level: int = 1
    answered_questions: Optional[list[AnsweredQuestion]] = []

    class Config:
        scheme_extra = {
            "example": {
                "_id": "661141bf76a678c8895f1585",
                "level": 1,
                "answered_questions": [
                    {
                        "question_id": "661141bf76a678c8895f1585",
                        "answer": True
                    }
                ]
            }
        }


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


class Message(BaseModel):
    message: str
