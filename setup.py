# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
from setuptools import setup, find_packages

setup(
    name='dictman',
    version='0.1.3',
    description='a English word shell finder',
    author='zhanglun',
    author_email='zhanglun.me@gmail.com',
    packages=['dictman'],
    install_requires=['termcolor'],
    entry_points={
        'console_scripts':[
            'dictman = dictman.main:main'
        ]
    }

)