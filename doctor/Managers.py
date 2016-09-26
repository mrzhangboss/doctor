# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
from .Spider import Spider


class Manager:
    def search(self, keyword):
        spi = Spider(keyword)
        spi.search()