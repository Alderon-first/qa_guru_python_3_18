from pytest_voluptuous import S
from utils.base_session import regres
from schemas.user import create_user_schema


def test_post_users_create_status_code():
    response = regres.post("users")
    assert response.status_code == 201


def test_post_users_create_data():
    payload = {
            "name": "имя",
            "job": "император земли"
        }
    response = regres.post("users", data=payload)
    assert response.status_code == 201
    assert response.json().get("name", "имя")
    assert response.json().get("job", "императьор земли")


def test_post_user_create_schema():
    payload = {
            "name": "имя",
            "job": "император земли"
        }
    response = regres.post("users", data=payload)
    assert response.status_code == 201
    assert S(create_user_schema) == response.json()


def test_login_user():
    payload = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
    response = regres.post("login", data=payload)
    assert response.status_code == 200
    assert response.json()["token"] is not None


def test_login_user_error():
    payload = {
            "email": "eve.holt@reqres.in"
        }
    response = regres.post("login", data=payload)
    assert response.status_code == 400
    assert response.json()["error"] is not None
    assert response.json()["error"] == "Missing password"
