from src.app import app

def test_health_integration():
    cleint = app.test_client()
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"

def test_patients_integration_list():
    client = app.test_client()
    r = client.get("/patients")
    assert r.status_code == 200
    assert isinstance(r.get_json(), list)
