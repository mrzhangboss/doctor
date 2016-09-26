# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
import json
import requests
from .DBManagers import DBManage


class Spider:
    youdao_api = 'http://fanyi.youdao.com/openapi.do?keyfrom={keyfrom}&key={key}&type=data&doctype=json&version=1.1&q={keyword}'

    def __init__(self, keyword, filename='', keyfrom='EnglishSearcher', key='1098649915'):
        self.keyword = keyword
        self.content = None
        self.db = DBManage(filename)
        self.keyfrom = keyfrom
        self.key = key

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
        return self.content
