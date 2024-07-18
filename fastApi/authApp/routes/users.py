from typing import Annotated
from fastapi import Depends

from authApp.functions.login import login_user
from fastapi import APIRouter

from authApp.database.user import User
from authApp import pydantic


router = APIRouter()

@router.get("/users", response_model=pydantic.User)
def user(user:Annotated[User, Depends(login_user)]):
    
    return {user}
