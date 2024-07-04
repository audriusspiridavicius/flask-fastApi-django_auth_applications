import base64
from flask import json
import pytest
from flask_auth_app import create_app

@pytest.fixture
def test_app():
    app = create_app("sqlite:///test_db.db")

    with app.app_context():
        yield app

@pytest.fixture
def test_client(test_app):
    yield test_app.test_client()
    
    
@pytest.fixture
def valid_credentials():
    return base64.b64encode(b"admin0:admin0").decode("utf-8")

@pytest.fixture
def invalid_credentials():
    return base64.b64encode(b"test:12345").decode("utf-8")

def test_login_valid_details(test_client, valid_credentials):

    
    response = test_client.post(
        "/login-token",
        headers={"Authorization": "Basic " + valid_credentials}
    )
    assert response.status_code == 200
    tokens = response.get_json()
    assert tokens["token"] != None
    assert tokens["refresh_token"] != None
    
def test_login_in_valid_details(test_client, invalid_credentials):
    
    response = test_client.post(
        "/login-token",
        headers={"Authorization": "Basic " + invalid_credentials}
    )

    assert response.status_code == 401
