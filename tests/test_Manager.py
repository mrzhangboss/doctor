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
        sys_argv = patch('sys.argv')
        self.argv_mock = sys_argv.start()
        self.man = doctor.Manager()

    def test_manage_begin(self):
        self.assertIsNotNone(self.man)

    @patch('doctor.Managers.Spider')
    def test_manage_use_spider_get_content(self, Spider_mock):
        search_mock = Mock()
        Spider_mock.return_value.search = search_mock

        self.man.search({'keyword': 'hello'})

        Spider_mock.assert_called_once_with(keyword='hello')
        self.assertEqual(search_mock.call_count, 1)

    @patch('doctor.Managers.Spider')
    def test_manage_return_spider_result(self, Spider_mock):
        result = Mock()
        Spider_mock.return_value.result = result

        res = self.man.search({'keyword': 'hello'})

        self.assertEqual(res, result)

    def test_manage_color_print(self):
        self.man.print()

    def test_work_arg_parse_then_search_then_print(self):
        with patch.object(self.man, 'args_parse') as parse_mock, \
                patch.object(self.man, 'search') as search_mock, \
                patch.object(self.man, 'args') as args_mock, \
                patch.object(self.man, 'print') as print_mock:
            def side_effect(mock, num=1):
                def _side_effect(*args, **kwargs):
                    self.assertEqual(mock.call_count, num)
                return _side_effect

            search_mock.side_effect = side_effect(parse_mock)
            print_mock.side_effect = side_effect(search_mock)

            self.man.work()

            search_mock.assert_called_once_with(args_mock)


    @patch('doctor.Managers.DoctorArguments')
    def test_args_parse_take_null_args(self, Argument_Mock):
        self.argv_mock.__len__.return_value = 1
        print_help = Mock()
        Argument_Mock.return_value.print_help = print_help

        with self.assertRaises(SystemExit):
            self.man.args_parse()

        self.assertEqual(print_help.call_count, 1)

    @patch('doctor.Managers.DoctorArguments')
    def test_args_parse_take_one_args(self, Argument_Mock):
        self.argv_mock.__len__.return_value = 2
        print_help = Mock()
        Argument_Mock.return_value.print_help = print_help

        self.man.args_parse()

        self.assertEqual(print_help.call_count, 0)

    @patch('doctor.Managers.DoctorArguments')
    def test_args_parse_return_man_args(self, Argument_Mock):
        self.argv_mock.__len__.return_value = 2

        result = self.man.args_parse()

        self.assertEqual(result, self.man.args)


    @patch('doctor.Managers.PrintManager')
    def test_print_use_PrintManager(self, PrintManager_Mock):
        self.man.print()

        self.assertEqual(PrintManager_Mock.call_count, 1)
        PrintManager_Mock.assert_called_once_with(self.man.data)

    @patch('doctor.Managers.PrintManager')
    def test_print_use_search_data(self, PrintManager_Mock):
        data = self.man.search({'keyword': 'hello'})
        self.man.print()

        PrintManager_Mock.assert_called_once_with(data)





class ArgrumentManageTest(unittest.TestCase):
    def setUp(self):
        from doctor.Managers import DoctorArguments
        self.arg = DoctorArguments()

    def test_args_help(self):
        self.assertIsNone(self.arg.print_help())

    def test_args_can_parse(self):
        a = self.arg.parse_args(['hello'])

        self.assertEqual(a.keyword, 'hello')

    def test_args_can_parse_two_words(self):
        with self.assertRaises(SystemExit):
            a2 = self.arg.parse_args(['hello', 'hello2'])
            self.assertFalse()


if __name__ == '__main__':
    unittest.main()
