# https://www.hackerrank.com/contests/w30/challenges/candy-replenishing-robot

# !/bin/python3

import unittest


def print_min(string_):
    return "min(int, {})".format(string_)


if __name__ == '__main__':
    n = int(input())
    output = "int"
    for n in range(0, n - 1):
        output = print_min(output)

    print(output)


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual('min(int, min(int, min(int, int)))', print_min(4))
        self.assertEqual('min(int, int)', print_min(2))
