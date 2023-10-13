#!/usr/bin/env python
"""Vocabulary"""

book = {}
FILENAME = 'engbook.txt'

def write():
    with open(FILENAME, 'wt', encoding='utf_8') as f:
        for k, v in book.items():
            f.write(f'{k} {v}\n')


def read():
    try:
        with open(FILENAME, 'rt', encoding='utf_8') as f:
            for line in f.readlines():
                data = line.split()
                book[data[0]] = data[1]
    except FileNotFoundError as e:
        print(e)


if __name__ == '__main__':
    import sys

    read()

    params = sys.argv[1:]

    if params:
        if params[0] == '-a': # add
            book[params[1]] = params[2]
            write()
        elif params[0] == '-r': # remove
            try:
                del book[params[1]]
                write()
            except KeyError:
                pass

    print(book)
