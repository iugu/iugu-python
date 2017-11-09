# -*- coding: utf-8 -*-

from iugu.action import Action
from iugu.exception import RequiredParameters


class MarketPlace(Action):

    def create(self, data):
        if not data.get('name', None):
            raise RequiredParameters('MarketPlace name not informed')
        url = self.api.make_url(['marketplace', 'create_account'])
        return super(MarketPlace, self).create(url, data)

    def request_verification(self, id, data):
        if not data.get('data', None):
            raise RequiredParameters('MarketPlace data not informed')
        url = self.api.make_url(['accounts', id, 'request_verification'])
        return self.api.post(url, data)

    def sub_account(self, id):
        url = self.api.make_url(['accounts', id])
        return super(MarketPlace, self).list(url)
