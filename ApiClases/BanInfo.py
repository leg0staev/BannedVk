class BanInfo:
	def __init__(self, data):
		self.admin_id = data['admin_id']
		self.comment = data['comment']
		self.comment_visible = data['comment_visible']
		self.date = data['date']
		self.reason = data['reason']
