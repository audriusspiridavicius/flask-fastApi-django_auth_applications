from flask_httpauth import HTTPBasicAuth
from flask_auth_app import create_app
from flask_bcrypt import Bcrypt
from flask_auth_app.models.user import User



basic_auth = HTTPBasicAuth()

@basic_auth.verify_password
def check_password(username, password):

    app = create_app()
    
    bcr = Bcrypt(app)
    with app.app_context():
        user:User = User.query.filter_by(username=username).first()
        
        if user and bcr.check_password_hash(user.password, password):
            return user
    
    return None
