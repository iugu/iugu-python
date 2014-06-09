# -*- coding: utf-8 -*-

from iugu.action import Action
from iugu.exception import RequiredParameters


class Customer(Action):

    def create(self, data):
        if not data.get('email', None):
            raise RequiredParameters('Customer email not informed')
        url = self.api.make_url(['customers'])
        return super(Customer, self).create(url, data)

    def search(self, id):
        url = self.api.make_url(['customers', id])
        return super(Customer, self).search(url)

    def change(self, id, data):
        url = self.api.make_url(['customers', id])
        return super(Customer, self).change(url, data)

    def remove(self, id):
        url = self.api.make_url(['customers', id])
        return super(Customer, self).remove(url)

    def list(self, data={}):
        url = self.api.make_url(['customers'])
        return super(Customer, self).list(url, data)


class PaymentMethod(Action):

    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.base_url_paths = ['customers', self.customer_id,
                               'payment_methods']
        super(PaymentMethod, self).__init__()

    def create(self, data):
        if not data.get('token', None) and not data.get('data', {}):
            raise RequiredParameters('Please, inform token or card data{} to create a Payment Method')
        elif not data.get('description', None):
            raise RequiredParameters('Payment Method description not informed')
        url = self.api.make_url(self.base_url_paths)
        return super(PaymentMethod, self).create(url, data)

    def search(self, id):
        url = self.api.make_url(self.base_url_paths + [id])
        return super(PaymentMethod, self).search(url)

    def change(self, id, description):
        data = {'description': description}
        url = self.api.make_url(self.base_url_paths + [id])
        return super(PaymentMethod, self).change(url, data)

    def remove(self, id):
        url = self.api.make_url(self.base_url_paths + [id])
        return super(PaymentMethod, self).remove(url)

    def list(self):
        url = self.api.make_url(self.base_url_paths)
        return super(PaymentMethod, self).list(url)
