from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from api import db


@dataclass
class Flashcard(db.Model):
    __tablename__ = 'flashcards'
    id: int
    question: str
    answer: str
    bucket: int

    id = Column('id', Integer, primary_key=True)
    question = Column('question', String, nullable=False)
    answer = Column('answer', String, nullable=False)
    bucket = Column('bucket', Integer, nullable=False)

    def __init__(self, question, answer, bucket):
        self.question = question
        self.answer = answer
        self.bucket = bucket
