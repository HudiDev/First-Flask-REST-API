from flask_restful import Resource, reqparse 
from models.store import StoreModel

class Store(Resource):

	def get(self, name):
		store = StoreModel.find_by_name(name)
		if store:
			return store.json()
		else:
			return {'message': 'No such store in the DB'}, 404
		
	def post(self, name):
		if StoreModel.find_by_name(name):
			return {'message': 'There is a store like this in the DB'}, 400
		new_store = StoreModel(name)
		new_store.save_to_db()
		return new_store.json()

	def delete(self, name):
		store = StoreModel.find_by_name(name)
		if store:
			store.delete_from_db()
		return {'message': 'store deleted successfully'}



class StoreList(Resource):

	def get(self):
		return {'stores': [store.json() for store in StoreModel.query.all()]}

