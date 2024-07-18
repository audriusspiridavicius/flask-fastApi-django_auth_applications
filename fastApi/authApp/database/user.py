from .database import Base, get_database
from sqlalchemy.orm import mapped_column, Mapped, Session
from fastapi import Depends
from typing import Annotated
from sqlalchemy.ext.hybrid import hybrid_property
from passlib.hash import sha512_crypt

class User(Base):
    __tablename__ = "users"
    
    id:Mapped[int] = mapped_column(primary_key=True, index=True)
    username:Mapped[str] = mapped_column(nullable=False, index=True)
    _password:Mapped[str] = mapped_column("password", nullable=False)
    
   
    
