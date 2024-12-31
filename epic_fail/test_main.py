from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_healthz():
    response = client.get("/healthz")
    assert response.status_code == 200


def test_evil_healthz():
    response = client.get("/unhealthz")
    assert response.status_code == 500

def test_fibonacci():
    response = client.post("/api/fibonacci", json={"length": 5})
    assert response.status_code == 200
    assert response.json() == {"sequences": [[0, 1, 1, 2, 3]]}
    # A second request should return the previous sequence plus the new one.
    response = client.post("/api/fibonacci", json={"length": 5})
    assert response.status_code == 200
    assert response.json() == {"sequences": [[0, 1, 1, 2, 3], [0, 1, 1, 2, 3]]}
