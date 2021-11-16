# from flask import Blueprint, jsonify, request, Response
# from sqlalchemy import select, delete
#
# from api import db
# from api.flashcards.models import Flashcard
# from api.training.models import TrainingSession, TrainingSessionFlashcard
#
# bp = Blueprint('training', __name__, url_prefix='/api')
#
#
# @bp.route('/training', methods=['GET'])
# def session():
#     active = request.args.get('active')
#     query = select(TrainingSession)
#     if active:
#         query = query.where(TrainingSession.active)
#     result = db.session.execute(query).fetchone()
#     if result is None:
#         return Response(status=404)
#     return jsonify(result[0])
#
#
# @bp.route('/training/sessions', methods=['POST'])
# def create_session():
#     training_session = TrainingSession(active=True)
#     for card in db.session.execute(select(Flashcard)).scalars():
#         training_session.flashcards.append(TrainingSessionFlashcard(session_id=training_session.id, flashcard_id=card.id))
#     db.session.add(training_session)
#     db.session.commit()
#     response = jsonify(training_session)
#     response.status = 201
#     return response
#
#
# @bp.route('/training/<int:session_id>', methods=['DELETE'])
# def delete_session(session_id):
#     db.session.execute(delete(TrainingSessionFlashcard).where(TrainingSessionFlashcard.session_id == session_id))
#     db.session.execute(delete(TrainingSession).where(TrainingSession.id == session_id))
#     db.session.commit()
#     return Response(status=200)
#
#
# @bp.route('/training/sessions/<int:session_id>/flashcards/<int:flashcard_id>/answer', methods=['POST'])
# def submit_answer(session_id, flashcard_id):
#     sess = db.session.execute(select(TrainingSession).where(TrainingSession.id == session_id)).fetchone()[0]
#     for card in sess.flashcards:
#         if card.flashcard.id == flashcard_id:
#             if card.flashcard.answer == request.json['answer']:
#                 return 'correct'
#     return 'incorrect'
