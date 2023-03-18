from telegram_api_tests.api_requests.base_request import BaseRequest


def test_good():
    request = BaseRequest('getMe')
    res = request.send()
    print(res.status_code)
    print(res.text)
