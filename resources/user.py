import sqlite3
from flask_restful import Resource, reqparse
from flask import request
from models.user import UserModel

class UserRegister(Resource): 

	parser = reqparse.RequestParser()
	parser.add_argument('username',
		type=str,
		required=True,
		help="This field cannot be blank")

	parser.add_argument('password', 
		type=str,
		required=True,
		help="This field cannot be blank")

	def post(self):
		data = UserRegister.parser.parse_args()
		if UserModel.find_by_username(data['username']) :
			return {"message": "sorry, but this user name already exists."}, 400

		new_user = UserModel(**data)
		new_user.save_to_db()
		
		# connection = sqlite3.connect('data.db')
		# cursor = connection.cursor()
		# insert_table = "INSERT INTO users VALUES (NULL, ?, ?)"
		# cursor.execute(insert_table, (data['username'], data['password']))

		# connection.commit()
		# connection.close()

		return {"message": "User created successfully"}, 201  

















