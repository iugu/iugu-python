# -*- coding: utf-8 -*-

import os
import re
import json
import requests
from iugu import exception
from iugu.version import __version__
from requests.auth import HTTPBasicAuth

class IuguApi(object):

    def __init__(self, **kwargs):
        self.token = kwargs.get("token")

    def headers(self):
        return {
            "User-Agent": "Iugu Python Api %s" % __version__,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def base_request(self, url, method, data={}):
        try:
            response = requests.request(method, url,
                                        auth=HTTPBasicAuth(self.token, ''),
                                        data=json.dumps(data),
                                        headers=self.headers())
            return json.loads(response.content.decode('utf-8'))
        #TODO: Create especifics exceptions
        except Exception as error:
            raise

    def get(self, url, data={}):
        return self.base_request(url, 'GET', data=data)

    def post(self, url, data={}):
        return self.base_request(url, 'POST', data=data)

    def put(self, url, data={}):
        return self.base_request(url, 'PUT', data=data)

    def delete(self, url):
        return self.base_request(url, 'DELETE')

    def make_url(self, paths):
        url = 'https://api.iugu.com/v1/'
        for path in paths:
            url = re.sub(r'/?$', re.sub(r'^/?', '/', str(path)), url)
        return url

__default_api__ = None


def default_api():

    global __default_api__
    if __default_api__ is None:
        try:
            token = os.environ["IUGU_API_TOKEN"]
        except KeyError:
            raise exception.ConfigError("Required IUGU_API_TOKEN")
        __default_api__ = IuguApi(token=token)
    return __default_api__


def config(**kwargs):

    global __default_api__
    __default_api__ = IuguApi(**kwargs)
    return __default_api__
