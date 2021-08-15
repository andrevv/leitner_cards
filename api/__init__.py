from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    @app.route('/api/cards')
    def cards():
        return 'cards'

    return app
