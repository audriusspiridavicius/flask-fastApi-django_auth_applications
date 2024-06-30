from flask_restful import Api, Resource
from flask_auth_app.models.user import User


class Login(Resource):
    def post(self):
        
        return {"test":"test value"}
        