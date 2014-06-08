# -*- coding: utf-8 -*-

from action import Action
from exception import RequiredParameters


class Transfer(Action):

    def create(self, data):
        if not data.get('receiver_id', None):
            raise RequiredParameters('Transfer receiver_id not informed')
        if not data.get('amount_cents', None):
            raise RequiredParameters('Transfer amount_cents not informed')
        url = self.api.make_url(['transfers'])
        return super(Transfer, self).create(url, data)

    def list(self, data={}):
        url = self.api.make_url(['subscriptions'])
        return super(Transfer, self).list(url, data)
