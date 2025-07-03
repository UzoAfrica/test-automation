import requests
import pytest
import json

with open("fixtures/test_data.json", "r") as f:
    test_data = json.load(f)["auth_test_data"]

BASE_URL = "http://localhost:8000/api/v1/auth"

def test_login_with_valid_credentials():
    payload = test_data["valid_credentials"]
    response = requests.post(BASE_URL + "/login", json=payload)
    assert response.status_code == 200
    assert "token" in response.json()

@pytest.mark.parametrize("creds", test_data["invalid_credentials"])
def test_login_with_invalid_credentials(creds):
    response = requests.post(BASE_URL + "/login", json=creds)
    assert response.status_code == 401
    assert creds["expected_error"] in response.text
