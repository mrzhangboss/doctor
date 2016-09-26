# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
import unittest

try:
    from unittest.mock import patch, Mock
except ImportError:
    from mock import patch, Mock

import doctor

class ManageTestCase(unittest.TestCase):
    def test_manage_begin(self):
        man = doctor.Manage()
        self.assertIsNotNone(man)


if __name__ == '__main__':
    unittest.main()
