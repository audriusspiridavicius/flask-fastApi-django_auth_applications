import datetime
import jwt
from flask_httpauth import HTTPTokenAuth

token_auth = HTTPTokenAuth()

_key = "123456789_abc!"

def generate_token(user, expires_in_seconds = 60):
    
    payload = {"user":user.to_dict(),"exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(seconds=expires_in_seconds)}
    
    refresh = {"user":str(user.id),"exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(seconds=expires_in_seconds * 2)}
    
    token = jwt.encode(payload,_key, algorithm="HS256")
    refresh_token = jwt.encode(refresh, _key, algorithm="HS256")
    
    return {"token":token, "refresh_token": refresh_token}


@token_auth.verify_token
def verify_token(token):
    
    try:
        decoded = jwt.decode(token,_key, algorithms=["HS256"])
    except Exception as e:
        return None
    
    return decoded["user"]