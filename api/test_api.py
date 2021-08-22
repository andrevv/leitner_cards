import os
import tempfile
import pytest

from api import create_app


@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app()
    with app.test_client() as client:
        yield client
    os.close(db_fd)
    os.unlink(db_path)


def test_api_get_flashcards(client):
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


def test_api_add_flashcard(client):
    resp = client.post('/api/flashcards', json={
        'question': 'What is the capital of Belgium?',
        'answer': 'Brussels'
    })
    assert resp.status_code == 200
