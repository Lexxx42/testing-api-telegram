import json
from .base_request_post import BaseRequestPost
from .expected_results import ExpectedSendMessage as esm
from .expected_results import ExpectedBaseRequest as ebr


class SendMessageRequest(BaseRequestPost):
    def should_be_correct_receiver_id(self):
        assert self.response.json()['result']['from']['id'] == ebr.BOT_ID, \
            f'id of bot in response should be {ebr.BOT_ID},' \
            f' but got {self.response.json()["result"]["from"]["id"]}'
