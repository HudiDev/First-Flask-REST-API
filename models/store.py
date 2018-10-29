from db import db

class StoreModel(db.Model):

	__tablename__ = 'stores'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))

	#lazy='dynamic' - doesn't create at object-instantiation-time, an ItemModel object.
	#instead, it fetches the raw data from db and we can choose afterwards to change objects.
	#I.E. like in the json method.
	items = db.relationship('ItemModel', lazy='dynamic') 

	def __init__(self, name):
		self.name = name

	def json(self):
		#add self.items.all() if using lazy='dynamic'
		#in order to instantiate data to ItemModels
		return {'name': self.name, 'items': [item.json() for item in self.items]}

	@classmethod
	def find_by_name(cls, name):
		return cls.query.filter_by(name=name).first() 

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()




		 