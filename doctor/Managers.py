# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
import sys
from argparse import ArgumentParser
from termcolor import colored
from .Spider import Spider

class Manager:
    def __init__(self):
        self.args = {'word': None}
        self.data = {}

    def search(self, args):
        spi = Spider(**args)
        spi.search()
        self.data = spi.result
        return self.data

    def args_parse(self):
        args_parser = DoctorArguments()
        if len(sys.argv) < 2:
            args_parser.print_help()
            sys.exit(0)
        self.args = vars(args_parser.parse_args())
        return self.args

    def print(self):
        pr = PrintManager(self.data)
        pr.print()

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


print_basic = lambda x: {v:colored(k, 'green') for v, k in x.items() if v !='explains'}
print_basic_explains = lambda x: '\n'.join(['{}. {}'.format(i, colored(s, 'blue')) for i,s in enumerate(x, 1)])
print_web = lambda x: '\n'.join(['{i}{key}: {value}'.format(i=i, key=s['key'], value=colored(', '.join(s['value']), 'green')) for i,s in enumerate(x, 1)])
class PrintManager:
    print_module = {
        'query': [lambda x: '词: {}'.format(colored(x, 'green')), 1],
        'translation': [lambda x: '翻译: {}'.format(', '.join([colored(y, 'blue') for y in x])), 2],
        'basic': [lambda x: '英: [{uk-phonetic}] 美: [{us-phonetic}] 英标: [{phonetic}]\n解释:\n{explains}'.format(**(print_basic(x)), explains=print_basic_explains(x['explains'])), 3],
        'web': [lambda x: '其他意思:\n{web}'.format(web=print_web(x)), 4]
    }
    def __init__(self, data):
        self.data = data

    def print(self):
        print_data = []
        for v in self.data:
            if v in self.print_module:
                print_data.append((self.print_module[v][1], self.print_module[v][0](self.data[v])))
        print_data.sort()
        for i, p in print_data:
            print(p)