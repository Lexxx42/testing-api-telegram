import json
from .base_request_post import BaseRequestPost
from .expected_results import ExpectedSendMessage as esm


class SendMessageRequest(BaseRequestPost):
    def should_be_correct_receiver_id(self):
        assert self.response.json()['result']['chat']['id'] == esm.RECEIVER_ID, \
            f'id of bot in response should be {esm.RECEIVER_ID},' \
            f' but got {self.response.json()["result"]["chat"]["id"]}'

    def should_be_correct_receiver_first_name(self):
        assert self.response.json()['result']['chat']['first_name'] == esm.RECEIVER_FIRST_NAME, \
            f'id of bot in response should be {esm.RECEIVER_FIRST_NAME},' \
            f' but got {self.response.json()["result"]["chat"]["first_name"]}'

    def should_be_correct_receiver_last_name(self):
        assert self.response.json()['result']['chat']['last_name'] == esm.RECEIVER_LAST_NAME, \
            f'id of bot in response should be {esm.RECEIVER_LAST_NAME},' \
            f' but got {self.response.json()["result"]["chat"]["last_name"]}'

    def should_be_correct_receiver_username(self):
        assert self.response.json()['result']['chat']['username'] == esm.RECEIVER_USERNAME, \
            f'id of bot in response should be {esm.RECEIVER_USERNAME},' \
            f' but got {self.response.json()["result"]["chat"]["username"]}'

    def should_be_correct_chat_type(self):
        assert self.response.json()['result']['chat']['type'] == esm.CHAT_TYPE, \
            f'id of bot in response should be {esm.CHAT_TYPE},' \
            f' but got {self.response.json()["result"]["chat"]["type"]}'

    def should_be_correct_message_text(self):
        assert self.response.json()['result']['text'] == esm.MESSAGE_TEXT, \
            f'id of bot in response should be {esm.MESSAGE_TEXT},' \
            f' but got {self.response.json()["result"]["text"]}'
