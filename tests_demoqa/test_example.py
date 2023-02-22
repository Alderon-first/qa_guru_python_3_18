import requests
from pytest_voluptuous import S
from qa_guru_python_3_14.model.schemas.user import create_user_schema


def test_post_users_create_status_code():
    response = requests.post(url="https://reqres.in/api/users")
    assert response.status_code == 201


def test_post_users_create_data():
    payload = {
            "name": "имя",
            "job": "император земли"
        }
    response = requests.post(url="https://reqres.in/api/users", data=payload)
    assert response.status_code == 201
    assert response.json().get("name", "имя")
    assert response.json().get("job", "императьор земли")


def test_post_user_create_schema():
    payload = {
            "name": "имя",
            "job": "император земли"
        }
    response = requests.post(url="https://reqres.in/api/users", data=payload)
    assert response.status_code == 201
    assert S(create_user_schema) == response.json()


def test_login_user():
    payload = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
    response = requests.post(url="https://reqres.in/api/login", data=payload)
    assert response.status_code == 200
    assert response.json()["token"] is not None


def test_login_user_error():
    payload = {
            "email": "eve.holt@reqres.in"
        }
    response = requests.post(url="https://reqres.in/api/login", data=payload)
    assert response.status_code == 400
    assert response.json()["error"] is not None
    assert response.json()["error"] == "Missing password"
