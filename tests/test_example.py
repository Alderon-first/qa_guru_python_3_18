from pytest_voluptuous import S
from schemas.user import create_user_schema


def test_post_users_create_status_code(examp_api):
    response = examp_api.post("users")
    assert response.status_code == 201


def test_post_users_create_data(examp_api):
    payload = {
            "name": "имя",
            "job": "император земли"
        }
    response = examp_api.post("users", data=payload)
    assert response.status_code == 201
    assert response.json().get("name", "имя")
    assert response.json().get("job", "императьор земли")


def test_post_user_create_schema(examp_api):
    payload = {
            "name": "имя",
            "job": "император земли"
        }
    response = examp_api.post("users", data=payload)
    assert response.status_code == 201
    assert S(create_user_schema) == response.json()


def test_login_user(examp_api):
    payload = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
    response = examp_api.post("login", data=payload)
    assert response.status_code == 200
    assert response.json()["token"] is not None


def test_login_user_error(examp_api):
    payload = {
            "email": "eve.holt@reqres.in"
        }
    response = examp_api.post("login", data=payload)
    assert response.status_code == 400
    assert response.json()["error"] is not None
    assert response.json()["error"] == "Missing password"
