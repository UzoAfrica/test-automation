import requests
import json

BASE_URL = "http://localhost:8000/api/v1/tickets"

with open("fixtures/security_test_data.json", "r") as f:
    data = json.load(f)

expired_token = data["authorization_test_cases"][2]["token_status"]
invalid_token = "invalid.jwt.token"

def test_access_with_expired_token():
    headers = {"Authorization": f"Bearer {expired_token}"}
    response = requests.get(BASE_URL, headers=headers)
    assert response.status_code == 401

def test_access_with_invalid_token():
    headers = {"Authorization": f"Bearer {invalid_token}"}
    response = requests.get(BASE_URL, headers=headers)
    assert response.status_code in [401, 403]
