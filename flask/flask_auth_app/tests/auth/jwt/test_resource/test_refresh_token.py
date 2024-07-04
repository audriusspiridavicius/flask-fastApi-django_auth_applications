import base64
from pytest import fixture

from flask_auth_app import create_app, db
from flask_auth_app.models.user import User


@fixture
def user(app):
    
    with app.app_context():
        user = User.query.filter_by(id=1).first()
    return user


@fixture
def app():
    app = create_app("sqlite:///test_db.db")
    yield app
    
    with app.app_context():
        db.drop_all()


@fixture
def client(app):
    return app.test_client()


def test_refresh_token_not_expired(client, user):
    
    auth_str = f"{user.username}:{user.username}"
    encoded_auth = base64.b64encode(auth_str.encode('utf-8')).decode('utf-8')

    tokens = client.post("/login-token", headers={"Authorization": "Basic " + encoded_auth})
    
    assert tokens.status_code == 200
    
    tokens_data = tokens.get_json()
    refresh_token = tokens_data["refresh_token"]
    
    refreshed_tokens = client.post("/refresh-token", headers={"Authorization": f"Bearer {refresh_token}"})
    
    assert refreshed_tokens.status_code == 200
    

def test_refresh_invalid_token(user, client):
    
    auth_str = f"{user.username}:{user.username}"
    encoded_auth = base64.b64encode(auth_str.encode('utf-8')).decode('utf-8')

    tokens = client.post("/login-token", headers={"Authorization": "Basic " + encoded_auth})
    
    
    tokens_data = tokens.get_json()
    refresh_token = tokens_data["refresh_token"]
    
    refreshed_tokens = client.post("/refresh-token", headers={"Authorization": f"Bearer {refresh_token + "0"}"})
    
    assert refreshed_tokens.status_code == 401


def test_refresh_invalid_token_pass_auth_token(user, client):
    
    auth_str = f"{user.username}:{user.username}"
    encoded_auth = base64.b64encode(auth_str.encode('utf-8')).decode('utf-8')

    tokens = client.post("/login-token", headers={"Authorization": "Basic " + encoded_auth})
    
    
    tokens_data = tokens.get_json()
    refresh_token = tokens_data["token"]
    
    refreshed_tokens = client.post("/refresh-token", headers={"Authorization": f"Bearer {refresh_token}"})
    
    assert refreshed_tokens.status_code == 401

