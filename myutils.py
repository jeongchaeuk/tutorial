"""myutils.py
My custom utility module
"""

#pylint: disable=w0611

# from __future__ import *

__all__ = ['cls', 'ls', 'cat', 'cidir']
__version__ = '0.1'
__author__ = 'Chaeuk Jeong'
# datetime.now().strftime('%Y-%m-%d-%a %H:%M:%S')
__date__ = '2023-09-14-Thu 15:19:17'

import os
from pprint import pprint as pp
import sys


def cls():
    """clear screen"""
    os.system('cls')


def ls(top='.'):
    """show list of files and directories which in the top directory"""
    os.system(f'dir /o {top}')


def cat(filename):
    """show file's content"""
    os.system(f'type {filename}')


def cidir(o=None):
    """show case-insensitive sorted python's dir()"""
    if o:
        return sorted(dir(o), key=lambda x: x.upper())
    return sorted(dir(sys.modules['__main__']), key=lambda x: x.upper())


def filematch(filename, substr):
    """Find lines that have substr from file."""
    with open(filename, encoding='utf-8') as f:
        for line in f:
            if substr in line:
                yield line

if __name__ == '__main__':
    import logging
    logging.basicConfig(filename='app.log',
                        filemode='wt',
                        encoding='utf-8',
                        level=logging.WARNING)
