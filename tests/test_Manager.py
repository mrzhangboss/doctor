# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
import unittest

try:
    from unittest.mock import patch, Mock
except ImportError:
    from mock import patch, Mock

import doctor

class ManagerTestCase(unittest.TestCase):
    def test_manage_begin(self):
        man = doctor.Manager()
        self.assertIsNotNone(man)

    @patch('doctor.Managers.Spider')
    def test_manage_use_spider_get_content(self, Spider_mock):
        search_mock = Mock()
        Spider_mock.return_value.search = search_mock

        man = doctor.Manager()
        man.search('hello')

        Spider_mock.assert_called_once_with('hello')
        self.assertEqual(search_mock.call_count, 1)


if __name__ == '__main__':
    unittest.main()
