import click
from flask import Flask
from flask.cli import with_appcontext
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.cli.add_command(init_db_command)

    app.url_map.strict_slashes = False

    from api import flashcards
    app.register_blueprint(flashcards.bp)

    from api import training
    app.register_blueprint(training.bp)

    with app.app_context():
        init_db()

    CORS(app)

    return app


def init_db():
    db.create_all()


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    print('DB initialized.')
