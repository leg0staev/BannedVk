from settings import *
from ApiClases.VkApi import VkApi

vk_api = VkApi(TOKEN, GR_ID)

banned_users_list = vk_api.get_banned()

with open('banned_users_list.txt', 'w') as f:
    for item in banned_users_list:
        id = item.get_id()
        f.write("%s\n" % id)