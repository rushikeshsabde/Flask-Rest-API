from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3

class Item(Resource):
    
    # @jwt_required()
    def get(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM items WHERE name= ?'
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
        item = {
            'name':row[0],
            'price':row[1]
        }

        return item, 200 if item is not None else 404

    # @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name',type=str,required=True,help='Name field is mandetory')
        parser.add_argument('price',type=float, required=True,help='Value field is mandetory')
        data = parser.parse_args()
        item = {'name':data['name'], 'price':data['price']}
        
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'INSERT INTO items VALUES (?,?)'
        cursor.execute(query, (item['name'], item['price']))
        connection.commit()
        connection.close()
        return item, 201

class Items(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM items'
        result =  cursor.execute(query)
        items = []
        for row in result:
            items.append({
                'name':row[0],
                'price':row[1]
            })
        return items, 200