from flask import Blueprint, send_from_directory

bp = Blueprint('home', __name__)


@bp.route('/', methods=['GET'])
def home():
    return send_from_directory(directory='../build', path='index.html')
