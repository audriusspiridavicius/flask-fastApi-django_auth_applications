from fastapi import FastAPI
from fastapi.security import HTTPBasic
from .database import database, user


database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

auth = HTTPBasic()

from .routes import users
app.include_router(users.router)