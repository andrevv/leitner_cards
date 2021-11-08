from flask import jsonify, request, Blueprint, Response

from api import db
from api.flashcards.models import Flashcard

bp = Blueprint('flashcards', __name__, url_prefix='/api')


@bp.route('/flashcards', methods=['GET'])
def get_flashcards():
    return jsonify(Flashcard.query.all())


@bp.route('/flashcards', methods=['POST'])
def add_flashcard():
    data = request.json
    flashcard = Flashcard(question=data['question'], answer=data['answer'], bucket=0)
    db.session.add(flashcard)
    db.session.commit()
    return Response(status=201)
