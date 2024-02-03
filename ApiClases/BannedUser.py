from ApiClases.BanInfo import BanInfo
from ApiClases.Profile import Profile


class BannedUser:
	def __init__(self, ban_info, profile):
		self.ban_info = BanInfo(ban_info)
		self.profile = Profile(profile)

	def get_id(self):
		return self.profile.get_id()
