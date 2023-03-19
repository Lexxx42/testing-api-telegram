import json
from .base_request import BaseRequest
from .expected_results import ExpectedGetMe as egm


class GetMeRequest(BaseRequest):
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
