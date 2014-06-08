# -*- coding: utf-8 -*-

from iugu.action import Action
from iugu.exception import RequiredParameters


class Subscription(Action):

    def create(self, data):
        if not data.get('customer_id', None):
            raise RequiredParameters('Subscription customer_id not informed')
        url = self.api.make_url(['subscriptions'])
        return super(Subscription, self).create(url, data)

    def search(self, id):
        url = self.api.make_url(['subscriptions', id])
        return super(Subscription, self).search(url)

    def change(self, id, data):
        url = self.api.make_url(['subscriptions', id])
        return super(Subscription, self).change(url, data)

    def remove(self, id):
        url = self.api.make_url(['subscriptions', id])
        return super(Subscription, self).remove(url)

    def suspend(self, id):
        url = self.api.make_url(['subscriptions', id, 'suspend'])
        return self.api.post(url)

    def active(self, id):
        url = self.api.make_url(['subscriptions', id, 'activate'])
        return self.api.post(url)

    def change_plan(self, id, plan_identifier):
        url = self.api.make_url(['subscriptions', id,
                                 'change_plan', plan_identifier])
        return self.api.post(url)

    def add_credits(self, id, quantity):
        data = {'quantity': quantity}
        url = self.api.make_url(['subscriptions', id, 'add_credits'])
        return self.api.post(url, data)

    def remove_credits(self, id, quantity):
        data = {'quantity': quantity}
        url = self.api.make_url(['subscriptions', id, 'remove_credits'])
        return self.api.post(url, data)

    def list(self, data={}):
        url = self.api.make_url(['subscriptions'])
        return super(Subscription, self).list(url, data)
