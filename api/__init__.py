import jsonpickle
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String


def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    db = SQLAlchemy(app)

    class Flashcard(db.Model):
        __tablename__ = 'flashcards'

        id = Column('id', Integer, primary_key=True)
        question = Column('question', String, nullable=False)
        answer = Column('answer', String, nullable=False)

    db.create_all()

    @app.route('/api/cards')
    def cards():
        return jsonpickle.encode(list(Flashcard.query.all()), unpicklable=False)

    return app
