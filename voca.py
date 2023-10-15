#!/usr/bin/env python
"""Vocabulary"""

import json

FILENAME = 'engbook.txt'

def write(book):
    with open(FILENAME, 'wt', encoding='utf_8') as f:
        json.dump(book, f, ensure_ascii=False, separators=(',', ':'),
                  sort_keys=True)


def read():
    try:
        with open(FILENAME, 'rt', encoding='utf_8') as f:
            return json.load(f)
    except FileNotFoundError as e:
        print(e)
    return None


def show_vocas(book):
    print('='*30)
    print(f'단어장 ({len(book)}) ver 2023.10.15')
    print('='*30)
    for k, v in book.items():
        print(f'{k}\n{v}\n')


def main(params):
    book = read()

    if params:
        if params[0] == '-a': # add
            book[params[1]] = params[2]
            write(book)
        elif params[0] == '-r': # remove
            try:
                del book[params[1]]
                write(book)
            except KeyError as e:
                print(f'{e} not found!')

    show_vocas(book)


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
