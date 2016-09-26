# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
import json
import requests


class Spider:
    youdao_api = 'http://fanyi.youdao.com/openapi.do?keyfrom={keyfrom}&key={key}&type=data&doctype=json&version=1.1&q={keyword}'
    keyfrom = 'EnglishSearcher'
    key = '1098649915'
    def __init__(self, keyword, filename=''):
        self.keyword = keyword
        self.content = None
        self.content_type = json
        self.db = DBManage(filename)

    def search(self):
        url = self.youdao_api.format(keyfrom=self.keyfrom, key=self.key, keyword=self.keyword)
        response = requests.get(url)
        self.content = response.json()

    def find(self):
        self.db.select(self.keyword)
        self.content = 'find'


    @property
    def result(self):
        self.find()
        self.search()
        return self

class DBManage:
    def __init__(self, filename):
        pass

    def select(self, keyword):
        pass

    def update(self, keyword):
        return False

    def insert(self, keyword, data):
        return False

    def delete(self, keyword):
        return False