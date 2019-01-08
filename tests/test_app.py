import http.client

import pytest
from PySorter import app as test_app

@pytest.fixture
def client():
    client = test_app.app.test_client()
    yield client


def test_get_app(client):
    """
    Verify the app returns a 200 for an empty request.
    """
    response = client.get('/')
    assert response.status_code == http.client.OK