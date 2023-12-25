import pytest
import requests


@pytest.fixture(scope="session")
def authorization_user_token():
    url = "localhost/api/auth/user_token/"
    data = {
        "username": "username",
        "password": "password",
        "grant_type": "grant_type",
        "client_id": "client_id",
        "client_secret": "client_secret"
    }
    response = requests.post(url, data=data)
    yield response.json().get("access_token")


@pytest.fixture(scope="session")
def authorization_admin_token():
    url = 'localhost/api/kazi_admin/token/'
    data = {
        "username": "username",
        "password": "password",
        "grant_type": "grant_type",
        "client_id": "client_id",
        "client_secret": "client_secret"
    }
    response = requests.post(url, data=data)
    yield response.json().get("access_token")
