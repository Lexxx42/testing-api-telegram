import requests
from .token_loader import BOT_TOKEN


class BaseRequest():
    def __init__(self, method_api, method_req='get', url='https://api.telegram.org/bot', **kwargs):
        self.method_req = method_req
        self.method_api = method_api
        self.url = url
        self.response = None
        self.token = BOT_TOKEN
        self.params = {key: value for key, value in kwargs.items()}

    def send(self):
        if self.method_req == 'get':
            self.response = requests.get(self.url + self.token + '/' + self.method_api)
            return self.response
        if self.method_req == 'post':
            self.response = requests.post(self.url + self.token + '/' + self.method_api,
                                          data=self.params)
            return self.response
