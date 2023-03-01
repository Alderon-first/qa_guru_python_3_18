from pytest_voluptuous import S

from schemas.user import create_user_schema


def test_post_users_create_status_code(example_api):
    response = example_api.post("/users")
    assert response.status_code == 201


def test_post_users_create_data(example_api):
    payload = {
        "name": "имя",
        "job": "император земли"
    }
    response = example_api.post("/users", data=payload)
    assert response.status_code == 201
    assert "имя" == response.json().get("name")
    assert "император земли" == response.json().get("job")


def test_post_user_create_schema(example_api):
    payload = {
        "name": "имя",
        "job": "император земли"
    }
    response = example_api.post("/users", data=payload)
    assert response.status_code == 201
    assert S(create_user_schema) == response.json()


def test_login_user(example_api):
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = example_api.post("/login", data=payload)
    assert response.status_code == 200
    assert response.json()["token"].isalnum()
    assert len(response.json()["token"]) > 8


def test_login_user_error(example_api):
    payload = {
        "email": "eve.holt@reqres.in"
    }
    response = example_api.post("/login", data=payload)
    assert response.status_code == 400
    assert response.json()["error"] == "Missing password"
