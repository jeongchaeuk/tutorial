#!/usr/bin/env python
"""Vocabulary"""

book = {}
FILENAME = 'engbook.txt'
SPLIT = '::'

def write():
    with open(FILENAME, 'wt', encoding='utf_8') as f:
        for k, v in book.items():
            f.write(f'{k}{SPLIT}{v}\n')


def read():
    try:
        with open(FILENAME, 'rt', encoding='utf_8') as f:
            for line in f.readlines():
                line = line.strip()
                data = line.split(SPLIT)
                book[data[0]] = data[1]
    except FileNotFoundError as e:
        print(e)


def show_vocas():
    print('='*30)
    print(f'단어장 ({len(book)}) ver 2023.10.15')
    print('='*30)
    for k, v in book.items():
        print(f'{k}\n{v}\n')


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

    show_vocas()
