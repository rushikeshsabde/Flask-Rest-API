# users = [
#     {
#         'id': 1,
#         'username': 'John',
#         'password':'Password@123',
#     }
# ]

# username_mapping = {
#     'bob' : {
#         'id': 1,
#         'username': 'John',
#         'password':'Password@123',
#     }
# }

# userid_mapping = {
#     1: {
#         'id': 1,
#         'username': 'John',
#         'password':'Password@123',
#     }
# }
from werkzeug.security import safe_str_cmp
from .user import User

users = [
    User(1, 'John', 'Password')
]

username_mapping = {u.username: u for u in users}

userid_mapping = {u.id: u for u in users}

def authenticate(username, password): 
    user = username_mapping.get(username, None)
    if user is not None and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
