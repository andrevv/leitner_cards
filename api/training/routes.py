from flask import Blueprint, jsonify, request, Response
from sqlalchemy import select

from api import db
from api.flashcards.models import Flashcard
from api.training.models import TrainingSession, TrainingSessionFlashcard

bp = Blueprint('training', __name__, url_prefix='/api')


@bp.route('/training', methods=['GET'])
def session():
    active = request.args.get('active')
    query = select(TrainingSession)
    if active:
        query = query.where(TrainingSession.active)
    result = db.session.execute(query).fetchone()
    if result is None:
        return jsonify()
    return jsonify(result[0])


@bp.route('/training', methods=['POST'])
def create_session():
    training_session = TrainingSession(active=True)
    for card in db.session.execute(select(Flashcard)).scalars():
        training_session.flashcards.append(TrainingSessionFlashcard(session_id=training_session.id, flashcard_id=card.id))
    db.session.add(training_session)
    db.session.commit()
    response = jsonify(training_session)
    response.status = 201
    return response
