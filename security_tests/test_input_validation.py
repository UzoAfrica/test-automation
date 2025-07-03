import json
import pytest
import requests

BASE_URL = "http://localhost:8000/api/v1/tickets"  # change to relevant form/API endpoint

with open("fixtures/security_test_data.json", "r") as f:
    security_data = json.load(f)

xss_payloads = security_data["xss_test_payloads"]
sql_payloads = security_data["sql_injection_payloads"]

@pytest.mark.parametrize("payload", xss_payloads)
def test_xss_injection_in_description(payload):
    data = {
        "title": "XSS test",
        "description": payload,
        "priority": "low",
        "category": "Security"
    }
    response = requests.post(BASE_URL, json=data)
    assert response.status_code != 500, "Server crashed from XSS"
    assert "<script>" not in response.text.lower(), "Possible XSS vulnerability detected"

@pytest.mark.parametrize("payload", sql_payloads)
def test_sql_injection_in_title(payload):
    data = {
        "title": payload,
        "description": "SQL injection test",
        "priority": "low",
        "category": "Security"
    }
    response = requests.post(BASE_URL, json=data)
    assert response.status_code != 500, "Server crashed from SQL Injection"
    assert "syntax error" not in response.text.lower(), "Possible SQL injection vulnerability"
