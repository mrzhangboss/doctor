# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
import unittest

try:
    from unittest.mock import patch, Mock
except ImportError:
    from mock import patch, Mock

import doctor


class IntegationTestCase(unittest.TestCase):
    def test_manage_work(self):
        import sys
        from sys import stdout
        from sys import argv
        import sys
        import tempfile
        filename = tempfile.mktemp()
        f = open(filename, 'w+')
        stdout = f
        sys_argv = sys.argv
        sys.argv = ['main.py', 'hello']

        man = doctor.Manager()

        man.work()

        sys.argv = sys_argv
        f.seek(0)
        out = f.read()
        self.assertEqual(len(out) > 1, True)
