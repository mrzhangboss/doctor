# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
from argparse import ArgumentParser
from .Spider import Spider


class Manager:
    def search(self, keyword):
        spi = Spider(keyword)
        return spi.search()

    def args_parse(self):
        pass

    def print(self):
        pass

    def work(self):
        self.args_parse()
        self.search()
        self.print()

class DoctorArguments(ArgumentParser):
    pass