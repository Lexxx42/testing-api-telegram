import json
from .send_message import SendMessageRequest
from .expected_results import ExpectedEditMessageText as eemt


class EditMessageTextRequest(SendMessageRequest):
    def should_be_correct_message_text(self):
        assert self.response.json()['result']['text'] == eemt.EDITED_MESSAGE_TEXT, \
            f'id of bot in response should be {eemt.EDITED_MESSAGE_TEXT},' \
            f' but got {self.response.json()["result"]["text"]}'
