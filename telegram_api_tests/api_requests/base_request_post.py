import json
import requests
from .base_request import BaseRequest
from .expected_results import ExpectedBaseRequest as ebr


class BaseRequestPost(BaseRequest):
    def send(self):
        self.response = requests.post(self.url + self.token + '/' + self.method_api,
                                      data=self.params)
        return self.response

    def should_be_correct_id_of_bot(self):
        assert self.response.json()['result']['from']['id'] == ebr.BOT_ID, \
            f'id of bot in response should be {ebr.BOT_ID},' \
            f' but got {self.response.json()["result"]["from"]["id"]}'

    def should_be_response_from_a_bot(self):
        assert self.response.json()['result']['from']['is_bot'] == ebr.IS_BOT, \
            f'is_bot in response should be {ebr.IS_BOT},' \
            f' but got {self.response.json()["result"]["from"]["is_bot"]}'

    def should_be_correct_first_name_of_a_bot(self):
        assert self.response.json()['result']['from']['first_name'] == ebr.BOT_FIRST_NAME, \
            f'first_name of bot in response should be {ebr.BOT_FIRST_NAME},' \
            f' but got {self.response.json()["result"]["from"]["first_name"]}'

    def should_be_correct_username_of_a_bot(self):
        assert self.response.json()['result']['from']['username'] == ebr.BOT_USERNAME, \
            f'username of bot in response should be {ebr.BOT_USERNAME},' \
            f' but got {self.response.json()["result"]["from"]["username"]}'
