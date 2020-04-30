from flask import Flask,request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from auth.security import authenticate, identity

app = Flask(__name__)

app.secret_key = 'xyz123'

api = Api(app)

jwt = JWT(app,authenticate, identity)

items = [
    {
        'name':'milk',
        'price':'10$'
    },
    {
        'name':'book',
        'price':'15$'
    },
    {
        'name':'pencil',
        'price':'2$'
    }
]

class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items),None)
        return item, 200 if item is not None else 404

    def post(self):
        # data = request.get_json()
        parser = reqparse.RequestParser()
        parser.add_argument('name',
            type=str,
            required=True,
            help="Name field can not empty"
        )
        parser.add_argument('price',
            type=float,
            required=True,
            help="Price field can not empty"
        )
        data = parser.parse_args()
        item = {'name':data['name'], 'price':data['price']}
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return items

api.add_resource(Item, '/item/<string:name>', '/item')
api.add_resource(ItemList, '/items')
app.run(port=5000, debug=True)

