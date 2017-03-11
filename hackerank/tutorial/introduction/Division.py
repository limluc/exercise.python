# https://www.hackerrank.com/challenges/python-division
# Python 3

import unittest


def divInt(intA, intB):
    return intA // intB


def div(intA, intB):
    return intA / intB

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(divInt(a, b))
    print(div(a, b))


class Test(unittest.TestCase):

    def testDivision(self):
        self.assertEqual(1, div(1, 1))
        self.assertEqual(0.6666666666666666, div(2, 3))
        self.assertEqual(1.3333333333333333, div(4, 3))

    def testDivisionInt(self):
        self.assertEqual(1, divInt(1, 1))
        self.assertEqual(0, divInt(2, 3))
        self.assertEqual(1, divInt(4, 3))
