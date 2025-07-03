import requests

def test_regular_user_cannot_access_admin_route():
    headers = {"Authorization": "Bearer regular_user_token"}
    response = requests.get("http://localhost:8000/api/v1/admin/system-config", headers=headers)
    assert response.status_code == 403

def test_admin_can_access_admin_route():
    headers = {"Authorization": "Bearer admin_user_token"}
    response = requests.get("http://localhost:8000/api/v1/admin/system-config", headers=headers)
    assert response.status_code == 200
