import os
import requests
import pytest

@pytest.mark.e2e
def test_health_e2e():
    base = os.getenv("BASE_URL", "http://localhost:8000")
    r = requests.get(f"{base}/health", timeout=5)
    assert r.status_code == 200
    assert r.json()["status"] == "ok"
