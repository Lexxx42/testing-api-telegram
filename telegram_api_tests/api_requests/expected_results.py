from .loader import TEST_USER_ID


class ExpectedBaseRequest():
    STATUS_OK = True
    STATUS_CODE = 200
    BOT_ID = 5623238635
    IS_BOT = True
    BOT_FIRST_NAME = 'testing_monkey'
    BOT_USERNAME = 'testing_monke_bot'


class ExpectedGetMe():
    CAN_JOIN_GROUPS = True
    CAN_READ_ALL_MESSAGES = False
    IS_SUPPORT_INLINE_QUERIES = False


class ExpectedSendMessage():
    RECEIVER_ID = int(TEST_USER_ID)
    RECEIVER_FIRST_NAME = 'Alex̷͍͉̤͆̑̌͒͝ander'
    RECEIVER_LAST_NAME = 'Konukђov'
    RECEIVER_USERNAME = 'Lexx_042'
    CHAT_TYPE = 'private'
    MESSAGE_TEXT = 'test message'
