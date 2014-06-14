# -*- coding: utf-8 -*-

from iugu.action import Action
from iugu.exception import RequiredParameters


class Token(Action):

    def create(self, data):
        if not data.get('account_id', None):
            raise RequiredParameters('Token account_id not informed')
        elif not data.get('method', None):
            raise RequiredParameters('Token method not informed')
        elif not data.get('data', None):
            raise RequiredParameters('Token data{} not informed')
        url = self.api.make_url(['payment_token'])
        return super(Token, self).create(url, data)

    def charge(self, data):
        url = self.api.make_url(['charge'])
        return super(Token, self).create(url, data)
