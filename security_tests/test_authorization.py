import requests
import json
import pytest

with open("fixtures/security_test_data.json", "r") as f:
    data = json.load(f)

test_cases = data["authorization_test_cases"]

@pytest.mark.parametrize("case", test_cases)
def test_authorization_enforcement(case):
    url = f"http://localhost:8000{case['attempted_access']}"
    headers = {}

    if case.get("token_status") == "expired":
        headers["Authorization"] = "Bearer expired.jwt.token"
    elif case.get("user_role") == "employee":
        headers["Authorization"] = "Bearer employee.jwt.token"
    else:
        headers["X-Tenant-ID"] = case.get("user_tenant")

    response = requests.get(url, headers=headers)
    assert str(response.status_code) == case["expected_result"].split("_")[0], f"{case['description']} failed"
