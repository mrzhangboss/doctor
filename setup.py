# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
from setuptools import setup, find_packages

setup(
    name='dictman',
    version='0.1.0',
    description='a English word shell finder',
    author='zhanglun',
    author_email='zhanglun.me@gmail.com',
    packages=['doctor'],
    install_requires=['termcolor'],
    entry_points={
        'console_scripts':[
            'dictman = doctor.main:main'
        ]
    }

)