import json
from .base_request import BaseRequest
from .expected_results import ExpectedGetMe as egm


class GetMeRequest(BaseRequest):

    def should_be_correct_id_of_bot(self):
        assert self.response.json()['result']['id'] == egm.BOT_ID, \
            f'id of bot in response shold be {egm.BOT_ID},' \
            f' but got {self.response.json()["result"]["id"]}'

    def should_be_response_from_a_bot(self):
        assert self.response.json()['result']['is_bot'] == egm.RESPONSE_FROM_BOT, \
            f'is_bot in response shold be {egm.RESPONSE_FROM_BOT},' \
            f' but got {self.response.json()["result"]["is_bot"]}'

    def should_be_correct_first_name_of_a_bot(self):
        assert self.response.json()['result']['first_name'] == egm.BOT_FIRST_NAME, \
            f'first_name of bot in response shold be {egm.BOT_FIRST_NAME},' \
            f' but got {self.response.json()["result"]["first_name"]}'

    def should_be_correct_username_of_a_bot(self):
        assert self.response.json()['result']['username'] == egm.BOT_USERNAME, \
            f'username of bot in response shold be {egm.BOT_USERNAME},' \
            f' but got {self.response.json()["result"]["username"]}'

    def should_be_correct_can_join_groups_status(self):
        assert self.response.json()['result']['can_join_groups'] == egm.CAN_JOIN_GROUPS, \
            f'can_join_groups in response shold be {egm.CAN_JOIN_GROUPS},' \
            f' but got {self.response.json()["result"]["can_join_groups"]}'

    def should_be_correct_can_read_all_group_messages_status(self):
        assert self.response.json()['result']['can_read_all_group_messages'] == egm.CAN_READ_ALL_MESSAGES, \
            f'can_read_all_group_messages in response shold be {egm.CAN_READ_ALL_MESSAGES},' \
            f' but got {self.response.json()["result"]["can_read_all_group_messages"]}'

    def should_be_correct_supports_inline_queries_status(self):
        assert self.response.json()['result']['supports_inline_queries'] == egm.IS_SUPPORT_INLINE_QUERIES, \
            f'supports_inline_queries in response shold be {egm.IS_SUPPORT_INLINE_QUERIES},' \
            f' but got {self.response.json()["result"]["supports_inline_queries"]}'
