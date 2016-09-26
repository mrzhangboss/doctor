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

    def test_manage_color_print(self):
        self.man.print()

    def test_work_arg_parse_then_search_then_print(self):
        with patch.object(self.man, 'args_parse') as parse_mock, \
                patch.object(self.man, 'search') as search_mock, \
                patch.object(self.man, 'print') as print_mock:
            def side_effect(mock, num=1):
                def _side_effect():
                    self.assertEqual(mock.call_count, num)
                return _side_effect

            search_mock.side_effect = side_effect(parse_mock)
            print_function.side_effect = side_effect(search_mock)

            self.man.work()


class ArgrumentTestCase(unittest.TestCase):
    def test_args_help(self):
        import sys
        import tempfile
        fname = tempfile.mktemp()
        f = open(fname, mode='w+')
        from doctor.Managers import DoctorArguments
        arg = DoctorArguments()

        arg.print_help(file=f)
        f.seek(0)

        self.assertIsNotNone(f.read())

if __name__ == '__main__':
    unittest.main()
