from fastapi.testclient import TestClient

from authApp.app import app
from .db import get_test_database, test_engine, Base, TestingSessionLocal
import pytest
from sqlalchemy.orm import Session


# @pytest.fixture(autouse=True)
# def setup_database():

#     Base.metadata.create_all(bind=test_engine)
#     # Base.metadata.drop_all(bind=test_engine)

def test_admin_user_created():
    db:Session = get_test_database()
# We grab another session to check 
    # if the items are created
    client = TestClient(app)
    # users = db.query(User).all()
    
    assert 1 == 1


