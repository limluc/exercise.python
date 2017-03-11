# https://www.hackerrank.com/challenges/write-a-function

import sys


def print_func(v):
    for i in range(1, v + 1):
        sys.stdout.write('%d' % i)


if __name__ == '__main__':
    v = int(input())
    print_func(v)