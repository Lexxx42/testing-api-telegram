import requests
from .loader import BOT_TOKEN
from .expected_results import ExpectedBaseRequest as ebr


class BaseRequest():
    def __init__(self, method_api, url='https://api.telegram.org/bot', **kwargs):
        self.method_api = method_api
        self.url = url
        self.response = None
        self.token = BOT_TOKEN
        self.params = {key: value for key, value in kwargs.items()}

    def should_be_status_ok(self):
        assert self.response.json()['ok'] == ebr.STATUS_OK, \
            f'Response status ok with method {self.method_api} should be {ebr.STATUS_OK},' \
            f' but got {self.response.json()["ok"]}'

    def should_be_status_code_200(self):
        assert self.response.status_code == ebr.STATUS_CODE, \
            f'Response status code ok with method {self.method_api} should be {ebr.STATUS_CODE},' \
            f' but got {self.response.status_code}'
