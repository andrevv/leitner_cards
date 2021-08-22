from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String


db = SQLAlchemy()


@dataclass
class Flashcard(db.Model):
    __tablename__ = 'flashcards'
    id: int
    question: str
    answer: str

    id = Column('id', Integer, primary_key=True)
    question = Column('question', String, nullable=False)
    answer = Column('answer', String, nullable=False)

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
