import secrets
from flask import Flask, redirect, request, url_for
from .models import db, fill_database_test_data, create_database
from flask_migrate import Migrate
from flask_restful import Api
from flask_dance.contrib.github import github, make_github_blueprint
import os
from werkzeug.middleware.proxy_fix import ProxyFix


def init_auth_api(app):
    auth_api = Api(app)
    
    auth_api.add_resource(Login, '/login')
    auth_api.add_resource(Users, '/users')
    auth_api.add_resource(LoginToken, '/login-token')
    auth_api.add_resource(RefreshToken, '/refresh-token')

    
def create_app(db_name = "sqlite:///users.db")->Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = db_name
    app.secret_key = os.environ.get("APP_SECRET_KEY", secrets.token_hex(16))
    os.environ['AUTHLIB_INSECURE_TRANSPORT'] = '1'
    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
    with app.app_context():
        db.init_app(app)
    create_database(app)
    init_auth_api(app)
    fill_database_test_data(app)
    
    migrations = Migrate(app)
    
    
    @app.route("/resultpage")
    @app.route("/")
    
    def resultpage():
         return f" authorized = { github.authorized}. You are successfully authorized using GitHub"
    
      
    blueprint = make_github_blueprint(
    client_id=os.environ.get("GITHUB_CLIENT_ID"),
    client_secret=os.environ.get("GITHUB_CLIENT_SECRET"),
    redirect_url="https://127.0.0.1:5000/"
)
    app.register_blueprint(blueprint)
    
    @app.route("/index")
    def index():    
        if not github.authorized:
            return redirect(url_for("github.login"))
    return app
from .resources import Login, Users, LoginToken, RefreshToken