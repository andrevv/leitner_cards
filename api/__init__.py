import os

import click
from flask import Flask
from flask.cli import with_appcontext
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__, static_folder='../ui/build/static', static_url_path='/static')
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

    from api import flashcards, home
    app.register_blueprint(flashcards.bp)
    app.register_blueprint(home.bp)

    CORS(app)

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
