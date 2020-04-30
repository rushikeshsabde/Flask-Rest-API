from .user import User
from werkzeug.security import safe_str_cmp

def authenticate(username, password):
    user = User.find_user_username(username)
    if user and safe_str_cmp(user.passeword, password):
        return user

def identity(payload):
    user_id = payload['identity']
    user = User.find_user_id(user_id)
    return user
