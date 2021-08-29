from flask import Flask, jsonify, request, Response
from flask_cors import CORS

from api.db import Flashcard


def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(app)

    from api.db import db
    db.init_app(app)
    db.create_all(app=app)

    @app.route('/api/flashcards', methods=['GET'])
    def get_flashcards():
        return jsonify(Flashcard.query.all())

    @app.route('/api/flashcards', methods=['POST'])
    def add_flashcard():
        print('here', request)
        data = request.json
        print(data)
        flashcard = Flashcard(question=data['question'], answer=data['answer'])
        db.session.add(flashcard)
        db.session.commit()
        return Response(status=201)

    return app
