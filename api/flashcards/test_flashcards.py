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
    assert resp.json == []


def test_api_add_flashcard(client):
    resp = client.post('/api/flashcards', json={
        'question': 'What is the capital of Belgium?',
        'answer': 'Brussels'
    })
    assert resp.status_code == 201
    resp = client.get('/api/flashcards')
    assert resp.status_code == 200
    print(resp.json)
    assert resp.json == [{
        'id': 1,
        'question': 'What is the capital of Belgium?',
        'answer': 'Brussels',
        'bucket': 0
    }]


def test_api_create_session(client):
    # Create flashcards
    resp = client.post('/api/flashcards', json={
        'question': 'What is the capital of Belgium?',
        'answer': 'Brussels'
    })
    assert resp.status_code == 201
    resp = client.post('/api/flashcards', json={
        'question': 'What is the capital of Italy?',
        'answer': 'Rome'
    })
    assert resp.status_code == 201

    # Create a session
    resp = client.post('/api/training/sessions')
    assert resp.status_code == 201
    assert resp.json == {
        'id': 1,
        'active': True,
        'flashcards': [{
            'flashcard': {
                'id': 1,
                'question': 'What is the capital of Belgium?',
                'answer': 'Brussels',
                'bucket': 0
            }
        }, {
            'flashcard': {
                'id': 2,
                'question': 'What is the capital of Italy?',
                'answer': 'Rome',
                'bucket': 0
            }
        }]
    }
    resp = client.get('/api/training')
    assert resp.status_code == 200
    assert resp.json == {
        'id': 1,
        'active': True,
        'flashcards': [{
            'flashcard': {
                'id': 1,
                'question': 'What is the capital of Belgium?',
                'answer': 'Brussels',
                'bucket': 0
            }
        }, {
            'flashcard': {
                'id': 2,
                'question': 'What is the capital of Italy?',
                'answer': 'Rome',
                'bucket': 0
            }
        }]
    }
