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
        
        