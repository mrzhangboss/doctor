# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
import unittest
try:
    from unittest.mock import patch, Mock
except ImportError:
    from mock import patch, Mock

import doctor


class DBManageTest(unittest.TestCase):
    def setUp(self):
        import tempfile
        f = tempfile.mktemp()
        manage = doctor.DBManage(f)
        self.manage = manage

    def test_select(self):
        self.assertEqual(self.manage.select('hello'), None)

    def test_update(self):
        self.assertEqual(self.manage.update('hello'), False)

    def test_insert(self):
        data = {}
        self.assertEqual(self.manage.insert('hello', data), False)

    def test_delete(self):
        self.assertEqual(self.manage.delete('hello'), False)
