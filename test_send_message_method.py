'''
API tests for sendMessage method
\nCommand to start SendMessage tests: pytest . -s -m sendmessage
'''

import pytest
from telegram_api_tests import TEST_USER_ID
from telegram_api_tests.api_requests.send_message import SendMessageRequest


@pytest.mark.sendmessage
class TestSendMessageMethod():
    @pytest.fixture(scope="class", autouse=True)
    def setup(self):
        global request
        request = SendMessageRequest('sendMessage', chat_id=TEST_USER_ID, text='test message')
        request.send()

    def test_send_message_request_should_return_status_ok(self):
        request.should_be_status_ok()

    def test_send_message_request_should_return_status_code_200(self):
        request.should_be_status_code_200()

    def test_get_me_request_should_return_result_of_request(self):
        request.should_be_result_of_request_in_response()

    def test_send_message_request_should_return_correct_bot_id(self):
        request.should_be_correct_id_of_bot()

    def test_send_message_request_should_return_correct_is_bot_status(self):
        request.should_be_response_from_a_bot()

    def test_send_message_request_should_return_correct_first_name_of_a_bot(self):
        request.should_be_correct_first_name_of_a_bot()

    def test_send_message_request_should_return_correct_username_of_a_bot(self):
        request.should_be_correct_username_of_a_bot()

    def test_send_message_request_should_return_correct_receiver_id(self):
        request.should_be_correct_receiver_id()

    def test_send_message_request_should_return_correct_receiver_first_name(self):
        request.should_be_correct_receiver_first_name()

    def test_send_message_request_should_return_correct_receiver_last_name(self):
        request.should_be_correct_receiver_last_name()

    def test_send_message_request_should_return_correct_receiver_username(self):
        request.should_be_correct_receiver_username()

    def test_send_message_request_should_return_correct_chat_type(self):
        request.should_be_correct_chat_type()

    def test_send_message_request_should_return_correct_message_text(self):
        request.should_be_correct_message_text()
