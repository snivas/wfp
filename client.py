import json
import os
from urllib.parse import urlparse  
from urllib.request import urlopen


class Connection(object):

    def __init__(self, url, **kwargs):
        self.url = urlparse(url)
        

    def request(self, path, **extras):
        url = u'{}://{}{}'.format(self.url.scheme, self.url.netloc, path)
        self.response = urlopen(url)

        if 400 <= self.response.getcode() < 500:
            raise Exception(None, self.response)

        if not 200 <= self.response.getcode() < 400:
            raise Exception(None, self.response)

        return self.response

    def get(self, path, **extras):
        return self.request(path, **extras)


class ONAClient(object):

    def __init__(self, api_addr, **kwargs):
        self.api_addr = api_addr
        self.conn = Connection(self.api_addr, **kwargs)
        self.formurl = self.getCatalogue('forms')

    def getValue(self, jsonstream, key):
        return ijson.items(f, key)        

    def getCatalogue(self, key):
        self.urllist = json.loads(self.conn.get(self.conn.url.path).read())
        return urlparse(self.urllist.get(key)).path

    def getFORM(self, formid):
        return self.conn.get(u'{}/{}'.format(self.formurl, formid))

