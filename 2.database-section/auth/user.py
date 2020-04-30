import sqlite3
from flask_restful import Resource, reqparse

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.passeword = password

    @classmethod
    def find_user_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM users WHERE username=?'
        result = cursor.execute(query, (username,) )
        row = result.fetchone()
        if row:
            # user = cls(row[0], row[1], row[2])
            user = cls(*row) #Passing as set of arguments
        else:
            user = None
        
        connection.close()
        return user

    @classmethod
    def find_user_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM users WHERE id=?'
        result = cursor.execute(query, (_id,) )
        row = result.fetchone()
        if row:
            # user = cls(row[0], row[1], row[2])
            user = cls(*row) #Passing as set of arguments
        else:
            user = None
        
        connection.close()
        return user

class UserRegister(Resource):
    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help='Username is mandetory')
        parser.add_argument('password', type=str, required=True, help='Password is mandetory')
        data = parser.parse_args()

        if User.find_user_username(data['username']):
            return {'message':'User with that username already exists'}, 400

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'INSERT INTO users VALUES (NULL, ?, ?)'
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {'message':'User has been successfully created'}, 201