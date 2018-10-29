import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):

	parser = reqparse.RequestParser()
	parser.add_argument('price',
		type=float,
		required=True,
		help='This field cannot be blank!'
	)
	parser.add_argument('store_id',
		type=str,
		required=True,
		help='Store id field is required')

	@jwt_required()
	def get(self, name): 
		item = ItemModel.find_by_name(name)
		if item:
			return item.json()
		return {'message': 'item not found'}, 404

	@jwt_required()
	def post(self, name):
		print(f'name issss: {name}')
		#try:
		if ItemModel.find_by_name(name):
			 return {'message': f'{name} item, already exists in the db'}, 400
		#except:
			#return {'message': 'Internal error occured'}, 500
		data = Item.parser.parse_args()

		item = ItemModel(name, **data)
		print(f'ITEM IS: {item}')
		# try:
		item.save_to_db()
		# except:
		# 	return {'message': 'Internal error occured while attempting to save'}, 500

		return item.json(), 201			
		

	@jwt_required()
	def put(self, name):
		
		data = Item.parser.parse_args()
		
		item = ItemModel.find_by_name(name)
		if item is None:
			try:
				item = ItemModel(name, **data)
			except:
				return {'message': 'Internal error occured while attempting to save'}, 500
		else:
			try:
				item.price = data['price']
			except:
				return {'message': 'Internal error occured while attempting to update'}, 500
		item.save_to_db()
		return item.json()

	@jwt_required()
	def delete(self, name):
		if ItemModel.find_by_name(name):
			ItemModel.delete_from_db()
		return {'mesage': 'Item deleted successfully'}


class ItemList(Resource):

	def get(self):
		# list(map(lambda x: x.json(), ItemModel.query.all()))
		return {'items': [x.json() for x in ItemModel.query.all()]}

