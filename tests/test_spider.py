# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
import unittest
try:
    from unittest.mock import patch, Mock
except ImportError:
    from mock import patch, Mock

import doctor



class SpiderTestCase(unittest.TestCase):
    def setUp(self):
        self.spider = doctor.Spider('hello')

    def test_spider_get_result_is_not_null(self):
        self.assertEqual(self.spider.result!=None, True)

    def test_spider_search_database_before_scrapy(self):
        with patch.object(self.spider, 'find') as find_mock,\
                patch.object(self.spider, 'search') as search_mock:
            res = self.spider.result
            self.assertEqual(find_mock.call_count, 1)
            self.assertEqual(search_mock.call_count, 1)

    def test_spider_find_before_search(self):
        with patch.object(self.spider, 'find') as find_mock,\
                patch.object(self.spider, 'search') as search_mock:
            def find_before_search():
                self.assertEqual(find_mock.call_count, 1)
            search_mock.side_effect = find_before_search
            res = self.spider.result

    def test_find_use_db_manage(self):
        with patch.object(self.spider, 'db') as db_mock:
            db_mock.select = Mock()
            select_mock = db_mock.select
            self.spider.find()
            self.assertEqual(select_mock.call_count, 1)

    def test_find_db_call_with_key(self):
        with patch.object(self.spider, 'db') as db_mock:
            db_mock.select = Mock()
            select_mock = db_mock.select
            self.spider.find()
            select_mock.assert_called_once_with(self.spider.keyword)

    def test_search_json_data(self):
        import json
        self.spider.search()
        self.assertEqual(self.spider.result.content_type, json)

    @patch('doctor.requests.get')
    def test_search_call_get_with_youdao_api(self, mock_requests):
        self.spider.search()
        mock_requests.assert_called_once_with(self.spider.youdao_api.format(key=self.spider.key,
                                                                            keyfrom=self.spider.keyfrom,
                                                                            keyword=self.spider.keyword))

    @patch('doctor.requests.get')
    def test_search_result_is_from_requests_get(self, get_mock):
        get = Mock()
        get_mock.return_value.json = get
        json_data = Mock
        get.return_value = json_data

        self.spider.search()

        self.assertEqual(self.spider.result.content, json_data)
