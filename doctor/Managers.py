# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
import sys
from argparse import ArgumentParser
from .Spider import Spider

class Manager:
    def __init__(self):
        self.args = {'word': None}

    def search(self, args):
        spi = Spider(**args)
        return spi.search()

    def args_parse(self):
        args_parser = DoctorArguments()
        if len(sys.argv) < 2:
            args_parser.print_help()
            sys.exit(0)
        self.args = vars(args_parser.parse_args())
        return self.args

    def print(self):
        pass

    def work(self):
        self.args_parse()
        self.search(self.args)
        self.print()

class DoctorArguments(ArgumentParser):
    def __init__(self):
        super().__init__()
        self.add_argument('keyword', metavar='Words', type=str)
        self.description = 'Doctor: help you a better English'
        self.prog = 'Doctor'
