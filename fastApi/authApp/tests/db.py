
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from sqlalchemy.orm import declarative_base

from authApp.database.database import get_database
from authApp.app import app

SQLALCHEMY_DATABASE_URL_TEST = "sqlite:///test_db.db"

test_engine = create_engine(
    SQLALCHEMY_DATABASE_URL_TEST,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

Base = declarative_base()



def get_test_database():
    from authApp.database.user import User 
    Base.metadata.create_all(bind=test_engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()



app.dependency_overrides[get_database] = get_test_database

# test_client = TestClient(app)

