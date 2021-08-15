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
    rv = client.get('/api/cards')
    assert rv.data == b'cards'
    os.close(db_fd)
    os.unlink(db_path)
