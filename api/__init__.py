from dataclasses import dataclass, field
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String


def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    CORS(app)

    db = SQLAlchemy(app)

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

    db.create_all()

    f1 = Flashcard(question='What is the capital of Germany?', answer='Berlin')
    f2 = Flashcard(question='What is the capital of France?', answer='Paris')

    db.session.add(f1)
    db.session.add(f2)
    db.session.commit()

    @app.route('/api/flashcards')
    def cards():
        return jsonify(Flashcard.query.all())

    return app
