# -*- coding: utf-8 -*-

from iugu.action import Action
from iugu.exception import RequiredParameters


class Invoice(Action):

    def create(self, data):
        if not data.get('email', None):
            raise RequiredParameters('Invoice email not informed')
        elif not data.get('due_date', None):
            raise RequiredParameters('Invoice due_date not informed')
        elif not data.get('items', None):
            raise RequiredParameters('Invoice items not informed')
        url = self.api.make_url(['invoices'])
        return super(Invoice, self).create(url, data)

    def search(self, id):
        url = self.api.make_url(['invoices', id])
        return super(Invoice, self).search(url)

    def change(self, id, data):
        if not data.get('email', None):
            raise RequiredParameters('Invoice email not informed')
        elif not data.get('due_date', None):
            raise RequiredParameters('Invoice due_date not informed')
        elif not data.get('items', None):
            raise RequiredParameters('Invoice items not informed')
        url = self.api.make_url(['invoices', id])
        return super(Invoice, self).change(url, data)

    def remove(self, id):
        url = self.api.make_url(['invoices', id])
        return super(Invoice, self).remove(url)

    def cancel(self, id):
        url = self.api.make_url(['invoices', id, 'cancel'])
        return self.api.put(url)

    def refund(self, id):
        url = self.api.make_url(['invoices', id, 'refund'])
        return self.api.post(url)

    def list(self, data={}):
        url = self.api.make_url(['invoices'])
        return super(Invoice, self).list(url, data)
