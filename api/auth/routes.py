import os
from functools import wraps

from authlib.integrations.flask_client import OAuth
from flask import Blueprint, session, url_for, redirect, current_app, abort
from six.moves.urllib.parse import urlencode

import constants

bp = Blueprint('auth', __name__, url_prefix='/api/auth')

AUTH0_CALLBACK_URL = os.getenv(constants.AUTH0_CALLBACK_URL)
AUTH0_CLIENT_ID = os.getenv(constants.AUTH0_CLIENT_ID)
AUTH0_CLIENT_SECRET = os.getenv(constants.AUTH0_CLIENT_SECRET)
AUTH0_DOMAIN = os.getenv(constants.AUTH0_DOMAIN)
AUTH0_BASE_URL = 'https://' + AUTH0_DOMAIN
AUTH0_AUDIENCE = os.getenv(constants.AUTH0_AUDIENCE)

oauth = OAuth()

auth0 = oauth.register(
    'auth0',
    client_id=AUTH0_CLIENT_ID,
    client_secret=AUTH0_CLIENT_SECRET,
    api_base_url=AUTH0_BASE_URL,
    access_token_url=AUTH0_BASE_URL + '/oauth/token',
    authorize_url=AUTH0_BASE_URL + '/authorize',
    client_kwargs={
        'scope': 'openid profile email',
    },
)


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if constants.PROFILE_KEY not in session:
            # return abort(401)
            return redirect('/api/auth/login')
        return f(*args, **kwargs)

    return decorated


@bp.route('login')
def login():
    print('login')
    return auth0.authorize_redirect(redirect_uri=AUTH0_CALLBACK_URL, audience=AUTH0_AUDIENCE)


@bp.route('logout')
def logout():
    print('logout')
    session.clear()
    params = {'returnTo': url_for('home.home', _external=True), 'client_id': AUTH0_CLIENT_ID}
    return redirect(auth0.api_base_url + '/v2/logout?' + urlencode(params))


@bp.route('callback')
def auth0_callback():
    print('callback')
    auth0.authorize_access_token()
    resp = auth0.get('userinfo')
    userinfo = resp.json()

    session[constants.JWT_PAYLOAD] = userinfo
    session[constants.PROFILE_KEY] = {
        'user_id': userinfo['sub'],
        'name': userinfo['name'],
        'picture': userinfo['picture']
    }
    return redirect('/')
