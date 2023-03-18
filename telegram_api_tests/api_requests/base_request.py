import requests
from .env_loader import BOT_TOKEN, TEST_USER_ID


class BaseRequest():
    def __init__(self, method_api, method_req='get', url='https://api.telegram.org/bot', **kwargs):
        self.method_req = method_req
        self.method_api = method_api
        self.url = url
        self.response = None
        self.token = BOT_TOKEN
        self.user_id = TEST_USER_ID

    def send(self):
        if self.method_req == 'get':
            self.response = requests.get(self.url + self.token + '/' + self.method_api)
            return self.response
