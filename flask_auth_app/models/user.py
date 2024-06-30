from sqlalchemy.orm import Mapped, mapped_column
from .db import db
from sqlalchemy_serializer import SerializerMixin

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    id = mapped_column(db.Integer, primary_key=True)
    email = mapped_column(db.String(255), unique=True, nullable=False)
    password = mapped_column(db.String(255), nullable=False)
    username:Mapped[str]
    
