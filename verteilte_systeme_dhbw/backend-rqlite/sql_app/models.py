from sqlalchemy import Column, ForeignKey, Integer, Text, CheckConstraint, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Topic(Base):
    __tablename__ = 'topic'
    id = Column('T_ID', Integer, primary_key=True)
    name = Column(Text, nullable=False)


class Solution(Base):
    __tablename__ = 'solutions'
    id = Column('S_ID', Integer, primary_key=True)
    a = Column(Text, nullable=False)
    b = Column(Text, nullable=False)
    c = Column(Text, nullable=False)
    correct_answer = Column(Text, nullable=False)
    CheckConstraint("correct_answer IN ('a', 'b', 'c')", name='correct_answer_constraint')
    explanation = Column(Text)


class Question(Base):
    __tablename__ = 'questions'
    id = Column('Q_ID', Integer, primary_key=True)
    s_id = Column('S_ID', Integer, ForeignKey('solutions.S_ID'), nullable=False)
    t_id = Column('T_ID', Integer, ForeignKey('topic.T_ID'), nullable=False)
    level = Column(Integer, nullable=False, default=1)
    CheckConstraint('level >= 1 AND level <= 10', name='level_constraint')
    question = Column(Text, nullable=False)

    topic = relationship("Topic")
    solution = relationship("Solution")


class User(Base):
    __tablename__ = 'user'
    id = Column('U_ID', Integer, primary_key=True)
    level = Column(Integer, nullable=False, default=1)
    CheckConstraint('level >= 1 AND level <= 10')

    answered_questions = relationship("AnsweredQuestion", cascade="all, delete")


class AnsweredQuestion(Base):
    __tablename__ = 'answered_questions'
    u_id = Column('U_ID', Integer, ForeignKey('user.U_ID', ondelete='CASCADE'), primary_key=True)
    q_id = Column('Q_ID', Integer, ForeignKey('questions.Q_ID'), primary_key=True)
    answer = Column(Boolean, nullable=False)

    user = relationship("User")
    question = relationship("Question")
