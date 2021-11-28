from flask import jsonify, request, Blueprint, Response, abort, session
from sqlalchemy import select, func, asc

import constants
from api import db
from api.auth.routes import requires_auth
from api.flashcards.models import Flashcard, AttemptResult, TrainingSession

bp = Blueprint('flashcards', __name__, url_prefix='/api')


@bp.route('/flashcards', methods=['GET'])
@requires_auth
def get_flashcards():
    return jsonify(Flashcard.query.all())


@bp.route('/flashcards/<int:flashcard_id>', methods=['GET'])
@requires_auth
def get_flashcard_by_id(flashcard_id):
    query = select(Flashcard).where(Flashcard.id == flashcard_id)
    flashcard = db.session.execute(query).scalars().first()
    if not flashcard:
        abort(404, description='Flashcard not found.')
    return jsonify(flashcard)


@bp.route('/flashcards/buckets/<int:bucket>', methods=['GET'])
@requires_auth
def get_flashcards_bucket(bucket):
    query = select(Flashcard).where(Flashcard.bucket == bucket)
    result = db.session.execute(query).scalars()
    return jsonify(list(result))


@bp.route('/flashcards', methods=['POST'])
@requires_auth
def add_flashcard():
    data = request.json
    flashcard = Flashcard(question=data['question'], answer=data['answer'], bucket=0)
    db.session.add(flashcard)
    db.session.commit()
    return Response(status=201)


@bp.route('/flashcards/<int:flashcard_id>/attempt', methods=['POST'])
@requires_auth
def attempt_flashcard(flashcard_id):
    query = select(Flashcard).where(Flashcard.id == flashcard_id)
    flashcard = db.session.execute(query).scalars().first()
    if not flashcard:
        abort(404, description='Flashcard not found.')
    if flashcard.answer != request.json['answer']:
        return jsonify(AttemptResult(is_correct=False))
    flashcard.bucket = flashcard.bucket + 1
    db.session.commit()
    return jsonify(AttemptResult(is_correct=True))


@bp.route('/flashcards/session', methods=['GET'])
@requires_auth
def get_session():
    query = select(Flashcard).order_by(asc(Flashcard.id))
    flashcards = db.session.query(query).all()
    return flashcards


@bp.route('/flashcards/sessions', methods=['POST'])
@requires_auth
def create_session():
    query = select(func.min(Flashcard.id))
    min_id = db.session.execute(query).scalars().first()
    training_session = TrainingSession(current_flashcard_id=min_id)
    db.session.add(training_session)
    db.session.commit()
    return jsonify(training_session), 201
