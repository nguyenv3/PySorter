import json
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
    assert response.status_code == http.client.UNPROCESSABLE_ENTITY


def test_post_numbers_non_numbers(client):
    """
    Verify the app returns a 422 for lists containing non numbers.
    """
    request_data = {
        'numbers': ['a', '1', '2']
    }

    response = client.post(path, data=request_data)
    assert response.status_code == http.client.UNPROCESSABLE_ENTITY


def test_post_numbers_string_numbers(client):
    """
    Verify the app returns a sorted list for string numbers.
    """
    request_data = {
        'numbers': ['1', '5', '4', '2', '3']
    }
    expected = [1, 2, 3, 4, 5]
    response = client.post(path, json=request_data)
    assert response.status_code == http.client.OK
    response_data = json.loads(response.data)
    assert response_data == expected


def test_post_numbers_numbers(client):
    """
    Verify the app returns a sorted list for numbers.
    """
    request_data = {
        'numbers': [1, 5, 4, 2, 3]
    }
    expected = [1, 2, 3, 4, 5]
    response = client.post(path, json=request_data)
    assert response.status_code == http.client.OK
    response_data = json.loads(response.data)
    assert response_data == expected