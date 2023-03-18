'''
API tests
\nCommand to start all tests: pytest .
\nCommand to start getMe tests: pytest . -m getme
'''

import os
import pytest
from dotenv import load_dotenv
from telegram_api_tests.api_requests.get_me import GetMeRequest

TEST_USER_ID = os.getenv('TEST_USER_ID')


@pytest.mark.getme
class TestGetMeMethod():
    @pytest.fixture(scope="class", autouse=True)
    def setup(self):
        global request
        request = GetMeRequest('getMe')
        request.send()

    def test_get_me_request_should_return_status_ok(self):
        request.should_be_status_ok()

    def test_get_me_request_should_return_status_code_200(self):
        request.should_be_status_code_200()

    def test_get_me_request_should_return_correct_bot_id(self):
        request.should_be_correct_id_of_bot()

    def test_get_me_request_should_return_correct_is_bot_status(self):
        request.should_be_response_from_a_bot()

    def test_get_me_request_should_return_correct_first_name_of_a_bot(self):
        request.should_be_correct_first_name_of_a_bot()

    def test_get_me_request_should_return_correct_username_of_a_bot(self):
        request.should_be_correct_username_of_a_bot()

    def test_get_me_request_should_return_correct_can_join_groups_status(self):
        request.should_be_correct_can_join_groups_status()

    def test_get_me_request_should_return_correct_can_read_all_group_messages_status(self):
        request.should_be_correct_can_read_all_group_messages_status()

    def should_be_correct_supports_inline_queries_status(self):
        request.should_be_correct_can_read_all_group_messages_status()

# def test_send_message():
#     request = BaseRequest('sendMessage', 'post', chat_id=TEST_USER_ID, text='test')
#     res = request.send()
#     print(res.status_code)
#     print(res.text)
