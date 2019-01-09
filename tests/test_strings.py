import json
import http.client

import pytest

from PySorter import app as test_app

path = '/strings'


@pytest.fixture
def client():
    client = test_app.app.test_client()
    yield client


def test_post_strings_empty(client):
    """
    Verify the app returns a 422 for an empty request.
    """
    response = client.post(path)
    assert response.status_code == http.client.UNPROCESSABLE_ENTITY


def test_post_strings_list(client):
    """
    Verify the app returns a sorted list for a list of strings.
    """
    request_data = {
        'strings': ['The', 'lazy', 'dog', 'jumped']
    }

    expected = ['The', 'dog', 'jumped', 'lazy']
    response = client.post(path, json=request_data)
    assert response.status_code == http.client.OK
    response_data = json.loads(response.data)
    assert response_data == expected


def test_post_non_string(client):
    """
    Verify the app returns a 422 if an element is not a string.
    """
    request_data = {
        'strings': ['1', 2.5, '3']
    }
    response = client.post(path, json=request_data)
    assert response.status_code == http.client.UNPROCESSABLE_ENTITY