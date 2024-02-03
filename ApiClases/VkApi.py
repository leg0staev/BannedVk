import requests
import json
import time
from ApiClases.BannedRequest import BannedRequest
from ApiClases.BannedUser import BannedUser


class VkApi:
	def __init__(self, token: str, group_id: int):
		self.__token = token
		self.__group_id = group_id
		self.__api_version = '5.199'

	def get_banned(self):

		banned_request = BannedRequest(self.__token, self.__group_id)
		response = banned_request.send()

		users = []
		grou_cnt = 0

		if response.status_code != 200:
			return f'Error: status code - {response.status_code}, {response.content.decode("utf8")}'

		response_json = json.loads(response.content.decode("utf8"))
		count = response_json['response']['count']
		items = response_json['response']['items']
		for item in items:
			if item['type'] == 'group':
				continue
			user = BannedUser(item['ban_info'], item['profile'])
			users.append(user)

		if count <= 200:
			return users

		for i in range(1, count // 200 + 1):
			offset = i * 200
			banned_request = BannedRequest(self.__token, self.__group_id, offset=offset)
			response = banned_request.send()
			response_json = json.loads(response.content.decode("utf8"))
			items = response_json['response']['items']
			for item in items:
				if item['type'] == 'group':
					grou_cnt += 1
					continue
				user = BannedUser(item['ban_info'], item['profile'])
				users.append(user)
			time.sleep(0.3)

		return users
