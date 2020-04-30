from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from auth.security import authenticate, identity
from auth.user import UserRegister
from items import Item,Items

app = Flask(__name__)
app.secret_key = "Password@123"
jwt = JWT(app, authenticate, identity)
api = Api(app)

api.add_resource(Item, '/item/<string:name>', '/item') 
api.add_resource(Items, '/items')
api.add_resource(UserRegister, '/register')
app.run(debug=True, port=5000)