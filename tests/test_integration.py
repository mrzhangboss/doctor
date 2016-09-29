# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
import unittest

try:
    from unittest.mock import patch, Mock
except ImportError:
    from mock import patch, Mock
import sys
import tempfile
import dictman


class IntegationTestCase(unittest.TestCase):
    def setUp(self):
        filename = tempfile.mktemp()
        print(filename)
        self.sys_file = open(filename, 'w+')
        self.sys_stdout = sys.stdout
        self.sys_argv = sys.argv

        sys.stdout = self.sys_file
        sys.argv = ['main.py', 'hello']

    def tearDown(self):
        sys.stdout = self.sys_stdout
        sys.argv = self.sys_argv

    def test_manage_work(self):
        sys.argv = ['main.py', 'hello']

        man = dictman.Manager()

        man.work()

        self.sys_file.seek(0)
        out = self.sys_file.read()
        self.assertEqual(len(out) > 0, True)

