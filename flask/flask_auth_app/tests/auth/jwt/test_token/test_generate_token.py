from flask import Flask
from flask_auth_app import create_app, db
from flask_auth_app.models.user import User
from flask_auth_app.auth.jwt_token import generate_token, verify_token
import pytest
import time

@pytest.fixture
def app():
    app = create_app("sqlite:///test_db.db")
    yield app
    with app.app_context():
        db.drop_all()

@pytest.fixture
def usr():
    user:User = User(username="new user", email = 'newuser@email.com', password="testpass")

    return user

def test_user_created(usr, app:Flask):
    
    with app.app_context():
        db.session.add(usr)
        db.session.commit()
        assert len(User.query.all()) == 11
        
def test_token_generated(usr):
    
    token = generate_token(usr)

    assert len(token) > 0
    
    
def test_token_decode(usr):
    
    token = generate_token(usr)
    decoded_user = verify_token(token["token"])
    
    assert decoded_user["username"] == usr.username

def test_expired_token(usr):
    token = generate_token(usr, 2)
    time.sleep(3)
    
    decoded_user = verify_token(token)
    
    assert decoded_user == None

def test_token_still_valid(usr):
    token = generate_token(usr, 10)
    time.sleep(5)
    
    decoded_user = verify_token(token["token"])
    
    assert decoded_user != None

def test_invalid_token(usr):
    token = generate_token(usr, 10)
    
    decoded_user = verify_token(token["token"] + "123")
    
    assert decoded_user == None
    
def test_token_refresh_token(usr):
    token = generate_token(usr, 5)
    
    assert token["token"] != token["refresh_token"]

def test_refresh_token_decode(usr):
    
    token = generate_token(usr, 2)
    time.sleep(2) 
    
    assert verify_token(token["token"]) == None
    assert verify_token(token["refresh_token"]) != None
    
    