# https://www.hackerrank.com/challenges/python-loops

import unittest


def calc(int_a):
    return int_a * int_a

if __name__ == '__main__':
    a = int(input())

    for i in range(0, a):
        print(calc(i))


class Test(unittest.TestCase):

    def testDivision(self):
        self.assertEqual(4, calc(2))
        self.assertEqual(25, calc(5))
        self.assertEqual(100, calc(10))
