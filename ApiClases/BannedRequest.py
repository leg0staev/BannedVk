import requests


class BannedRequest:
	def __init__(self, token, group_id, offset=0):
		self.url = 'https://api.vk.com/method/groups.getBanned'
		self.token = token
		self.offset = offset
		self.headers = {
				'Authorization': f'Bearer {token}',
		}
		self.params = {
				'group_id': group_id,
				'v': '5.199',
				'offset': self.offset,
				'count': 200
		}

	def send(self):
		return requests.post(url=self.url, headers=self.headers, params=self.params)
