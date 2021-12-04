from dataclasses import dataclass
from typing import List

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api import db


@dataclass
class Flashcard(db.Model):
    __tablename__ = 'flashcards'
    id: int
    question: str
    answer: str
    bucket: int
    deck_id: int

    id = Column('id', Integer, primary_key=True)
    question = Column('question', String, nullable=False)
    answer = Column('answer', String, nullable=False)
    bucket = Column('bucket', Integer, nullable=False)
    deck_id = Column('deck_id', Integer, ForeignKey('decks.id'), nullable=False)

    def __init__(self, question, answer, bucket):
        self.question = question
        self.answer = answer
        self.bucket = bucket


@dataclass
class Deck(db.Model):
    __tablename__ = 'decks'
    id: int
    name: str
    flashcards: List[Flashcard]

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String, nullable=False)
    flashcards = relationship('Flashcard')

    def __init__(self, name):
        self.name = name


@dataclass
class TrainingSession(db.Model):
    __tablename__ = 'training_sessions'
    id: int
    current_flashcard: Flashcard

    id = Column('id', Integer, primary_key=True)
    current_flashcard_id = Column('current_flashcard_id', Integer, ForeignKey('flashcards.id'), nullable=False)
    current_flashcard = relationship('Flashcard')

    def __init__(self, current_flashcard_id):
        self.current_flashcard_id = current_flashcard_id


@dataclass
class AttemptResult:
    is_correct: bool
    answer: str

    def __init__(self, is_correct, answer):
        self.is_correct = is_correct
        self.answer = answer
