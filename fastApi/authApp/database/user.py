from .database import Base, get_database
from sqlalchemy.orm import mapped_column, Mapped, Session
from fastapi import Depends
from typing import Annotated
from sqlalchemy.ext.hybrid import hybrid_property


class User(Base):
    __tablename__ = "users"
    
    id:Mapped[int] = mapped_column(primary_key=True, index=True)
    username:Mapped[str] = mapped_column(nullable=False, index=True)
    _password:Mapped[str] = mapped_column("password", nullable=False)
    
   
    
    @classmethod
    def login(cls, username:str, password:str, db:Session):
        
        user:User = db.query(User).filter_by(username=username).first()
        
        if user:
            if cls.verify_password(user.password, password):
                return user
        return None
    
    
    @classmethod
    def verify_password(cls, actual_password, entered_password):
        return actual_password == entered_password
    
    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password
        
        
    