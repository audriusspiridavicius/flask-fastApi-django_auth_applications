from flask import Flask
from .models import db, fill_database_test_data, create_database
from flask_migrate import Migrate
from flask_restful import Api





def init_auth_api(app):
    auth_api = Api(app)
    
    auth_api.add_resource(Login, '/login','/')
    auth_api.add_resource(Users, '/users')
    auth_api.add_resource(LoginToken, '/login-token')
    auth_api.add_resource(RefreshToken, '/refresh-token')
    
def create_app(db_name = "sqlite:///users.db")->Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = db_name
    with app.app_context():
        db.init_app(app)
    create_database(app)
    init_auth_api(app)
    fill_database_test_data(app)
    
    migrations = Migrate(app)
    
    return app
from .resources import Login, Users, LoginToken, RefreshToken