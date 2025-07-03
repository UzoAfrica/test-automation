import requests
import json

with open("fixtures/test_data.json", "r") as f:
    test_data = json.load(f)["employee_test_data"]["cross_tenant_test"]

def test_user_cannot_access_other_tenant_data():
    tenant_001_user = test_data["tenant_001_employee"]
    headers = {"X-Tenant-ID": tenant_001_user["tenant_id"]}
    url = f"http://localhost:8000/api/v1/employees?tenant_id=tenant_002"
    response = requests.get(url, headers=headers)
    assert response.status_code == 403
