from fastapi.testclient import TestClient
from sqlmodel import Session, select

from app.models import UsersTable


def test_check_api(client: TestClient):
    response = client.get("api/development/check-api")
    assert response.status_code == 200


def test_create_user_dev(client: TestClient) -> None:
    r = client.post(
        "api/development/create-user-dev/",
        json={
            "email": "test@test.com",
            "username": "testtest",
            "password": "password",
        },
    )

    assert r.status_code == 200
