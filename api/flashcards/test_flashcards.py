import os
import tempfile

import pytest

from api import create_app
from api.flashcards.services import FlashcardService, Flashcard


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
    assert resp.json == [{
        'id': 1,
        'question': 'What is the capital of Belgium?',
        'answer': 'Brussels'
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
                'answer': 'Brussels'
            }
        }, {
            'flashcard': {
                'id': 2,
                'question': 'What is the capital of Italy?',
                'answer': 'Rome'}
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
                'answer': 'Brussels'
            }
        }, {
            'flashcard': {
                'id': 2,
                'question': 'What is the capital of Italy?',
                'answer': 'Rome'}
        }]
    }


def test_foo():
    cards = [
        Flashcard(key=1, question='What is the capital of Italy?', answer='Rome'),
        Flashcard(key=2, question='What is the capital of Germany?', answer='Berlin')
    ]
    fc = FlashcardService(flashcards=cards)
    bucket = fc.get_bucket(0)
    assert len(bucket) == 2
    print()
    print([c.updated for c in cards])
    fc.answer(cards[0])
    print([c.updated for c in cards])
