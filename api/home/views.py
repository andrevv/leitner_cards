from flask import Blueprint, send_from_directory

from api.auth.routes import requires_auth

bp = Blueprint('home', __name__)


@bp.route('/', methods=['GET'])
@requires_auth
def home():
    return send_from_directory(directory='../build', path='index.html')
