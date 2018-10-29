from werkzeug.security import safe_str_cmp
from models.user import UserModel


# username_mapping = {u.username: u for u in users}
# userid_mapping = {u.id: u for u in users}

#method to send jwt (token) back to user
def authenticate(username, password):
	user = UserModel.find_by_username(username)
	if user and safe_str_cmp(user.password, password):
		 return user


#checks token for method whom require authorization
def identity(payload):
	user_id = payload['identity']
	return UserModel.find_by_id(user_id)






