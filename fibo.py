#!/usr/bin/env python
'''Fibonacci numbers module'''


def fib(n):
    '''Write Fibonacci series up to `n`.'''

    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


def fib2(n):
    '''Return Fibonacci series up to `n`.'''

    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2:
        try:
            fib(int(sys.argv[1]))
        except ValueError:
            print(f'`{sys.argv[1]}` is not a *integer* number!')
