import json
from .base_request import BaseRequest


class GetMeRequest(BaseRequest):

    def should_be_status_ok(self):
        assert self.response.json()['ok'] == True, \
            f'Response status ok with method {self.method_api} shold be true, but got {self.response.json()["ok"]}'

    def should_be_status_code_200(self):
        assert self.response.status_code == 200, \
            f'Response status code ok with method {self.method_api} shold be 200, but got {self.response.status_code}'

    def should_be_correct_id_of_bot(self):
        assert self.response.json()['result']['id'] == 5623238635, \
            f'id of bot in response shold be 5623238635, but got {self.response.json()["result"]["id"]}'

    def should_be_response_from_a_bot(self):
        assert self.response.json()['result']['is_bot'] == True, \
            f'is_bot in response shold be true, but got {self.response.json()["result"]["is_bot"]}'

    def should_be_correct_first_name_of_a_bot(self):
        assert self.response.json()['result']['first_name'] == 'testing_monkey', \
            f'first_name of bot in response shold be "testing_monkey", but got {self.response.json()["result"]["first_name"]}'

    def should_be_correct_username_of_a_bot(self):
        assert self.response.json()['result']['username'] == 'testing_monke_bot', \
            f'username of bot in response shold be "testing_monke_bot", but got {self.response.json()["result"]["username"]}'

    def should_be_correct_can_join_groups_status(self):
        assert self.response.json()['result']['can_join_groups'] == True, \
            f'can_join_groups in response shold be true, but got {self.response.json()["result"]["can_join_groups"]}'

    def should_be_correct_can_read_all_group_messages_status(self):
        assert self.response.json()['result']['can_read_all_group_messages'] == False, \
            f'can_read_all_group_messages in response shold be false, but got {self.response.json()["result"]["can_read_all_group_messages"]}'

    def should_be_correct_supports_inline_queries_status(self):
        assert self.response.json()['result']['supports_inline_queries'] == False, \
            f'supports_inline_queries in response shold be false, but got {self.response.json()["result"]["supports_inline_queries"]}'
