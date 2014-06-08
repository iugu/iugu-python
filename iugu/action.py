# -*- coding: utf-8 -*-

from iugu.iuguapi import default_api


class Action(object):

    def __init__(self):
        self.api = default_api()

    def create(self, url, data):
        return self.api.post(url, data)

    def search(self, url):
        return self.api.get(url)

    def change(self, url, data):
        return self.api.put(url, data)

    def remove(self, url):
        return self.api.delete(url)

    def list(self, url, data={}):
        return self.api.get(url, data)
