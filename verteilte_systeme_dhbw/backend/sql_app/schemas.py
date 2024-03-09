from pydantic import BaseModel


class UserBase(BaseModel):
    # Base class for User
    level: int = 1


class UserCreate(UserBase):
    # Class for creating a new User, inherits from UserBase
    pass


class User(UserBase):
    # Class for returning and reading a User, inherits from UserBase
    id: int

    class Config:
        orm_mode = True


class Message(BaseModel):
    message: str


class SolutionBase(BaseModel):
    a: str
    b: str
    c: str
    correct_answer: str
    explanation: str


class QuestionBase(BaseModel):
    id: int
    level: int
    topic: str
    question: str
    solution: SolutionBase


class Question(QuestionBase):
    pass
