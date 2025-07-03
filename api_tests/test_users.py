import requests
import pytest

BASE_URL = "http://localhost:8000/api/v1/users"

@pytest.fixture
def user_payload():
    return {
        "first_name": "Test",
        "last_name": "User",
        "email": "test.user@techcorp.com",
        "department": "QA",
        "title": "QA Engineer"
    }

def test_create_user(user_payload):
    response = requests.post(BASE_URL, json=user_payload)
    assert response.status_code == 201
    assert response.json()["email"] == user_payload["email"]

def test_get_user():
    response = requests.get(BASE_URL + "/1")
    assert response.status_code == 200
    assert "email" in response.json()

def test_update_user():
    payload = {"title": "Senior QA"}
    response = requests.put(BASE_URL + "/1", json=payload)
    assert response.status_code == 200
    assert response.json()["title"] == "Senior QA"

def test_delete_user():
    response = requests.delete(BASE_URL + "/1")
    assert response.status_code == 204
