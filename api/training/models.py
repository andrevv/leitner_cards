from dataclasses import dataclass
from typing import List

from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from api import db
from api.flashcards.models import Flashcard


@dataclass
class TrainingSession(db.Model):
    __tablename__ = 'training_sessions'
    id: int
    active: bool
    flashcards: List

    id = Column('id', Integer, primary_key=True)
    active = Column('active', Boolean, nullable=False)
    flashcards = relationship('TrainingSessionFlashcard')

    def __init__(self, active):
        self.active = active
        self.flashcards = []


@dataclass
class TrainingSessionFlashcard(db.Model):
    flashcard: Flashcard

    __tablename__ = 'training_session_flashcards'
    session_id = Column(ForeignKey('training_sessions.id'), primary_key=True)
    flashcard_id = Column(ForeignKey('flashcards.id'), primary_key=True)
    flashcard = relationship('Flashcard')

    def __init__(self, session_id, flashcard_id):
        self.session_id = session_id
        self.flashcard_id = flashcard_id
