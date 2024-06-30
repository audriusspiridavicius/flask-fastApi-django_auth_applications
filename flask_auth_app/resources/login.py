from flask_restful import Resource
from flask_auth_app.auth import basic_auth



class Login(Resource):
    
    @basic_auth.login_required
    def post(self):
        
        return basic_auth.current_user().to_dict()
        