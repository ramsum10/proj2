import sqlite3

import sqlite3he
from flask_restful import Resource, reqparse

class User:
    table_name = 'users'

    def __init__(self,_id,username,password):
        self._id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls,username):
        query = 'SELECT * FROM {table} WHERE username = ?'.format(table =cls.table_name)
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        result = cursor.execute(query,(username,))
        row = result.fetchone()
        user = cls(*row)
        connection.commit()
        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        query = 'SELECT * FROM {table} WHERE _id = ?'.format(table=cls.table_name)
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        user = cls(*row)
        connection.commit()
        connection.close()
        return user

class UserRegister(Resource):
    table_name = 'users'
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='cannot leave blank')
    parser.add_argument('password', type=str, required=True, help='cannot leave blank')
    def post(self):
        table_name = 'users'
        data = UserRegister.parser.parse_args()
        if User.find_by_username():
            return {"message":"already exists"}
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'INSERT INTO {table} VALUES(NULL,?,?)'.format(table = self.table_name)
        cursor.execute(query,data['username'],data['password'])

        connection.commit()
        connection.close()

        return {"message": "User created successfully."}, 201

