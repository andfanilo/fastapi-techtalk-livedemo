from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_get_status():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_post_user():
    response = client.post(
        "/users",
        json={
            "id": 4,
            "name": "Mary",
            "joined": "2018-11-30",
        },
    )
    assert response.status_code == 200
    assert response.json() == "Mary"
