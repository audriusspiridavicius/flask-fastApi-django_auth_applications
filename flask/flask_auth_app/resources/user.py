from flask_restful import Resource
from flask_auth_app.auth import basic_auth, token_auth, generate_token
from flask_auth_app.models.user import User




class Users(Resource):
    
    @token_auth.login_required
    def get(self):
        return {'users get': [{'name': 'John', 'age': 30}]}
    
    @token_auth.login_required
    def post(self):
        return {'users post': [{'name': 'John', 'age': 30}]}
    
    
class LoginToken(Resource):
    
    @basic_auth.login_required
    def post(self):
        
        usr = basic_auth.current_user()
        token = generate_token(usr)
        
        return token

class RefreshToken(Resource):
    
    @token_auth.login_required
    def post(self):
        usr_id = basic_auth.current_user()
       
        
        if usr_id and type(usr_id) == int:
            user = User.query.filter_by(id=usr_id).first()
            if user:   
                token = generate_token(user)
                return token
            else:
                return {'error': 'User not found'}, 404
        else:
            return {'error': 'Invalid Token! or Token is Expired'}, 401
        
        