import os
import tempfile
import pytest

from api import create_app


@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client


def test_api_cards(client):
    db_fd, db_path = tempfile.mkstemp()
    resp = client.get('/api/flashcards')
    assert resp.status_code == 200
    assert resp.json == [{
        'id': 1,
        'question': 'What is the capital of Germany?',
        'answer': 'Berlin'
    }, {
        'id': 2,
        'question': 'What is the capital of France?',
        'answer': 'Paris'
    }]
    os.close(db_fd)
    os.unlink(db_path)
