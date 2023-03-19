import requests
from .token_loader import BOT_TOKEN
from .expected_results import ExpectedBaseRequest as ebr


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

    def should_be_status_ok(self):
        assert self.response.json()['ok'] == ebr.STATUS_OK, \
            f'Response status ok with method {self.method_api} shold be {ebr.STATUS_OK},' \
            f' but got {self.response.json()["ok"]}'

    def should_be_status_code_200(self):
        assert self.response.status_code == ebr.STATUS_CODE, \
            f'Response status code ok with method {self.method_api} shold be {ebr.STATUS_CODE},' \
            f' but got {self.response.status_code}'

    def should_be_correct_id_of_bot(self):
        assert self.response.json()['result']['id'] == ebr.BOT_ID, \
            f'id of bot in response shold be {ebr.BOT_ID},' \
            f' but got {self.response.json()["result"]["id"]}'

    def should_be_response_from_a_bot(self):
        assert self.response.json()['result']['is_bot'] == ebr.IS_BOT, \
            f'is_bot in response shold be {ebr.IS_BOT},' \
            f' but got {self.response.json()["result"]["is_bot"]}'

    def should_be_correct_first_name_of_a_bot(self):
        assert self.response.json()['result']['first_name'] == ebr.BOT_FIRST_NAME, \
            f'first_name of bot in response shold be {ebr.BOT_FIRST_NAME},' \
            f' but got {self.response.json()["result"]["first_name"]}'

    def should_be_correct_username_of_a_bot(self):
        assert self.response.json()['result']['username'] == ebr.BOT_USERNAME, \
            f'username of bot in response shold be {ebr.BOT_USERNAME},' \
            f' but got {self.response.json()["result"]["username"]}'
