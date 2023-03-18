import os
from dotenv import load_dotenv
from telegram_api_tests.api_requests.base_request import BaseRequest

TEST_USER_ID = os.getenv('TEST_USER_ID')


def test_get_me():
    request = BaseRequest('getMe')
    res = request.send()
    print(res.status_code)
    print(res.text)


def test_send_message():
    request = BaseRequest('sendMessage', 'post', chat_id=TEST_USER_ID, text='test')
    res = request.send()
    print(res.status_code)
    print(res.text)
