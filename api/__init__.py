import os

import click
from flask import Flask
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy

import constants

db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__, static_folder='../build/static', static_url_path='/static')
    app.secret_key = os.getenv(constants.SECRET_KEY)

    if test_config:
        app.config['SQLALCHEMY_DATABASE_URI'] = test_config['SQLALCHEMY_DATABASE_URI']
    else:
        db_uri = os.environ['DATABASE_URL']
        if db_uri.startswith('postgres://'):
            db_uri = db_uri.replace('postgres://', 'postgresql://', 1)
        app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.cli.add_command(init_db_command)

    app.url_map.strict_slashes = False

    from api.auth import oauth
    oauth.init_app(app)

    from api import flashcards, home, auth
    app.register_blueprint(flashcards.bp)
    app.register_blueprint(home.bp)
    app.register_blueprint(auth.bp)

    return app


def init_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    print('DB initialized.')
