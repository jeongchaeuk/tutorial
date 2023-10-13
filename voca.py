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


def add(eng, kor):
    book[eng] = kor


def find(eng):
    return book[eng]


def main():
    read()
    print(book)


if __name__ == '__main__':
    main()
