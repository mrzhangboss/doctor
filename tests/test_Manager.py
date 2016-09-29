# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
import unittest

try:
    from unittest.mock import patch, Mock
except ImportError:
    from mock import patch, Mock

import dictman


class ManagerTestCase(unittest.TestCase):
    def setUp(self):
        sys_argv = patch('sys.argv')
        self.argv_mock = sys_argv.start()
        self.man = dictman.Manager()

    def test_manage_begin(self):
        self.assertIsNotNone(self.man)

    @patch('dictman.Managers.Spider')
    def test_manage_use_spider_get_content(self, Spider_mock):
        search_mock = Mock()
        Spider_mock.return_value.search = search_mock

        self.man.search({'keyword': 'hello'})

        Spider_mock.assert_called_once_with(keyword='hello')
        self.assertEqual(search_mock.call_count, 1)

    @patch('dictman.Managers.Spider')
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


    @patch('dictman.Managers.DoctorArguments')
    def test_args_parse_take_null_args(self, Argument_Mock):
        self.argv_mock.__len__.return_value = 1
        print_help = Mock()
        Argument_Mock.return_value.print_help = print_help

        with self.assertRaises(SystemExit):
            self.man.args_parse()

        self.assertEqual(print_help.call_count, 1)

    @patch('dictman.Managers.DoctorArguments')
    def test_args_parse_take_one_args(self, Argument_Mock):
        self.argv_mock.__len__.return_value = 2
        print_help = Mock()
        Argument_Mock.return_value.print_help = print_help

        self.man.args_parse()

        self.assertEqual(print_help.call_count, 0)

    @patch('dictman.Managers.DoctorArguments')
    def test_args_parse_return_man_args(self, Argument_Mock):
        self.argv_mock.__len__.return_value = 2

        result = self.man.args_parse()

        self.assertEqual(result, self.man.args)


    @patch('dictman.Managers.PrintManager')
    def test_print_use_PrintManager(self, PrintManager_Mock):
        self.man.print()

        self.assertEqual(PrintManager_Mock.call_count, 1)
        PrintManager_Mock.assert_called_once_with(self.man.data)

    @patch('dictman.Managers.PrintManager')
    def test_print_use_search_data_and_print(self, PrintManager_Mock):
        print_mock = Mock()
        PrintManager_Mock.return_value.print = print_mock

        data = self.man.search({'keyword': 'hello'})
        self.man.print()

        PrintManager_Mock.assert_called_once_with(data)
        self.assertEqual(print_mock.call_count, 1)


class PrintManagerTest(unittest.TestCase):
    def setUp(self):
        import sys
        import tempfile
        filename = tempfile.mktemp()  #use filename will not read anything
        print(filename)
        self.sys_stdout = sys.stdout
        class_file = open(filename, mode='w+')
        sys.stdout = class_file
        self.sys_file = class_file
        from dictman.Managers import PrintManager
        self.Print = PrintManager

    def tearDown(self):
        import sys
        self.sys_file.close()
        sys.stdout = self.sys_stdout

    def line_assert_equal(self, sys_file, num):
        real_n = 0
        content = []
        sys_file.seek(0)
        while True:
            line = sys_file.readline()
            if line == '':
                break
            else:
                real_n += 1
                content.append(line.decode('utf-8'))
        assert num == real_n
        return '\n'.join(content)

    def test_print_query(self):
        p = self.Print({'query': 'hello'})
        p.print()

        out = self.line_assert_equal(self.sys_file, 1)

        self.assertIn('hello', out)

    def test_print_translation(self):
        p = self.Print({'translation': ['你好'], 'query': 'hello'})
        p.print()

        out = self.line_assert_equal(self.sys_file, 2)

        self.assertIn('你好', out)

    def test_print_translation_and_query_order(self):
        p = self.Print({'translation': ['你好'], 'query': 'hello'})
        p.print()

        out = self.line_assert_equal(self.sys_file, 2)

        lines = out.split('\n')
        self.assertIn('hello', lines[0])
        self.assertIn('你好', lines[2])

    # @unittest.skip
    def test_print_hello(self):

        data = {"translation":["你好"],"basic":{"us-phonetic":"hɛˈlo, hə-","phonetic":"hə\'ləʊ; he-","uk-phonetic":"hə\'ləʊ; he-","explains":["n. 表示问候， 惊奇或唤起注意时的用语","int. 喂；哈罗","n. (Hello)人名；(法)埃洛"]},"query":"hello","errorCode":0,"web":[{"value":["你好","您好","Hello"],"key":"Hello"},{"value":["凯蒂猫","昵称","匿称"],"key":"Hello Kitty"},{"value":["哈乐哈乐","乐扣乐扣"],"key":"Hello Bebe"}]}
        p = self.Print(data)
        p.print()

        self.assertEqual(True, True)




class ArgrumentManageTest(unittest.TestCase):
    def setUp(self):
        from dictman.Managers import DoctorArguments
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
