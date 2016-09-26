# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
import unittest

try:
    from unittest.mock import patch, Mock
except ImportError:
    from mock import patch, Mock

import doctor

class ManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.man = doctor.Manager()

    def test_manage_begin(self):
        self.assertIsNotNone(self.man)

    @patch('doctor.Managers.Spider')
    def test_manage_use_spider_get_content(self, Spider_mock):
        search_mock = Mock()
        Spider_mock.return_value.search = search_mock

        self.man.search('hello')

        Spider_mock.assert_called_once_with('hello')
        self.assertEqual(search_mock.call_count, 1)

    @patch('doctor.Managers.Spider')
    def test_manage_return_spider_result(self, Spider_mock):
        result = Mock()
        Spider_mock.return_value.search.return_value = result

        res = self.man.search('hello')

        self.assertEqual(res, result)


if __name__ == '__main__':
    unittest.main()
