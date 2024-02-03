class Profile:
	def __init__(self, data):
		self.id = data['id']
		self.first_name = data['first_name']
		self.last_name = data['last_name']
		self.can_access_closed = data['can_access_closed']
		self.is_closed = data['is_closed']

	def get_id(self):
		return self.id