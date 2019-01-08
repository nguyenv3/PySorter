import http.client

import pytest

from PySorter import app as test_app

path = '/numbers'


@pytest.fixture
def client():
    client = test_app.app.test_client()
    yield client


def test_post_numbers_empty(client):
    """
    Verify the app returns a 422 for an empty request.
    """
    response = client.post(path)
    print(response.data)
    assert response.status_code == http.client.UNPROCESSABLE_ENTITY


def test_post_numbers_string_numbers(client):
    """
    Verify the app returns a 200 for an empty request.
    """
    request_data = {
        'numbers': ['1', '2', '3', '4', '5']
    }
    response = client.post(path, json=request_data)
    assert response.status_code == http.client.OK