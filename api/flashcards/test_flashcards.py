import os
import tempfile

import pytest

from api import create_app


@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app({
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'
    })
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


def test_create_flashcards_with_default_bucket(client):
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

    # Get by bucket
    resp = client.get('/api/flashcards/buckets/0')
    assert len(resp.json) == 2


def test_attempt_flashcard_not_exists(client):
    # arrange
    # act
    resp = client.post('/api/flashcards/1/attempt', json={
        'answer': 'Brussels'
    })

    # assert
    assert resp.status_code == 404


def test_attempt_flashcard_correctly(client):
    # arrange
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

    # act
    resp = client.post('/api/flashcards/1/attempt', json={
        'answer': 'Brussels'
    })

    # assert
    assert resp.status_code == 200
    assert resp.json['is_correct']
    resp = client.get('/api/flashcards/1')
    assert resp.status_code == 200
    assert resp.json['bucket'] == 1


def test_attempt_flashcard_incorrectly(client):
    # arrange
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

    # act
    resp = client.post('/api/flashcards/1/attempt', json={
        'answer': 'Rome'
    })

    # assert
    assert resp.status_code == 200
    assert not resp.json['is_correct']
    resp = client.get('/api/flashcards/1')
    assert resp.status_code == 200
    assert resp.json['bucket'] == 0


def test_get_flashcard_by_id(client):
    # arrange
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

    # act
    resp = client.get('/api/flashcards/1')

    # assert
    assert resp.status_code == 200
    assert resp.json['question'] == 'What is the capital of Belgium?'
    assert resp.json['answer'] == 'Brussels'


def test_get_flashcard_by_id_not_exists(client):
    # arrange
    # act
    resp = client.get('/api/flashcards/1')

    # assert
    assert resp.status_code == 404


def test_create_session(client):
    # arrange
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

    # act
    resp = client.post('/api/flashcards/sessions')

    # assert
    assert resp.status_code == 201
    assert resp.json['id'] == 1
    assert resp.json['current_flashcard']['id'] == 1


def test_get_session(client):
    # arrange
    resp = client.get('/api/flashcards/sessions')
    # act
    # assert
    pass
