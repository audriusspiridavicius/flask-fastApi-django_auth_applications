from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_bcrypt import Bcrypt

class BaseModel(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=BaseModel)



def _fill_users_table(app):
    from .user import User
    
    bcr = Bcrypt(app)
    
    with app.app_context():
        
        users = User.query.first()
        if not users:
            dummy_users = [User(username = f"admin{index}", password=bcr.generate_password_hash(f"admin{index}"), email=f"admin_email{index}@email.com") for index in range(10)]
            db.session.add_all(dummy_users)
            db.session.commit()
        
    


def fill_database_test_data(app):
    _fill_users_table(app)


def create_database(app):
    
    with app.app_context():
        db.create_all()

    
    
    