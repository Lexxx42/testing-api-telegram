'''
API tests for deleteMessage method
\nCommand to start deleteMessage tests: pytest . -s -m deletemessage
'''

import pytest
from telegram_api_tests import TEST_USER_ID
from telegram_api_tests.api_requests.base_request_post import BaseRequestPost


@pytest.mark.deletemessage
class TestDeleteMessageMethod():
    @pytest.fixture(scope="class", autouse=True)
    def setup(self):
        global request
        request = BaseRequestPost('sendMessage', chat_id=TEST_USER_ID, text='test message')
        request.send()
        request.should_be_status_ok()
        request.should_be_status_code_200()
        message_id = request.response.json()["result"]["message_id"]
        request = BaseRequestPost('deleteMessage', chat_id=TEST_USER_ID, message_id=message_id)
        request.send()

    def test_delete_message_request_should_return_status_ok(self):
        request.should_be_status_ok()

    def test_delete_message_request_should_return_status_code_200(self):
        request.should_be_status_code_200()

    def test_delete_message_request_should_return_result_of_request(self):
        request.should_be_result_of_request_in_response()
