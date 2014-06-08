# -*- coding: utf-8 -*-

from iugu.action import Action
from iugu.exception import RequiredParameters


class Plan(Action):

    def create(self, data):
        if not data.get('name', None):
            raise RequiredParameters('Plan name not informed')
        elif not data.get('identifier', None):
            raise RequiredParameters('Plan identifier not informed')
        elif not data.get('interval', None):
            raise RequiredParameters('Plan interval not informed')
        elif not data.get('interval_type', None):
            raise RequiredParameters('Plan interval_type not informed')
        elif not data.get('currency', None):
            raise RequiredParameters('Plan currency not informed')
        elif not data.get('value_cents', None):
            raise RequiredParameters('Plan value_cents not informed')
        url = self.api.make_url(['plans'])
        return super(Plan, self).create(url, data)

    def search(self, id=None, identifier=None):
        if not id and not identifier:
            raise RequiredParameters('Please, inform the id or identifier of the plan')
        if id:
            url = self.api.make_url(['plans', id])
        else:
            url = self.api.make_url(['plans', 'identifier', identifier])
        return super(Plan, self).search(url)

    def change(self, id, data):
        url = self.api.make_url(['plans', id])
        return super(Plan, self).change(url, data)

    def remove(self, id):
        url = self.api.make_url(['plans', id])
        return super(Plan, self).remove(url)

    def list(self, data={}):
        url = self.api.make_url(['plans'])
        return super(Plan, self).list(url, data)
