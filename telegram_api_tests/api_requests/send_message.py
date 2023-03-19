import json
from .base_request_post import BaseRequestPost
from .expected_results import ExpectedSendMessage as esm


class SendMessageRequest(BaseRequestPost):
    def should_be_correct_receiver_id(self):
        assert self.response.json()['result']['chat']['id'] == esm.RECEIVER_ID, \
            f'id of bot in response shold be {esm.RECEIVER_ID},' \
            f' but got {self.response.json()["result"]["chat"]["id"]}'
