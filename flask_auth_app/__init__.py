from flask import Flask, g
from .models import db, fill_database_test_data, create_database
from flask_migrate import Migrate
from flask_restful import Api
from .resources import Login

def init_auth_api(app):
    auth_api = Api(app)
    
    auth_api.add_resource(Login, '/login','/')
    
def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
    
    db.init_app(app)
    create_database(app)
    init_auth_api(app)
    fill_database_test_data(app)
    
    migrations = Migrate(app)
    
    return app
