# https://www.hackerrank.com/challenges/py-if-else
import unittest


def add(intA, intB):
    return intA + intB


def minus(intA, intB):
    return intA - intB


def multiply(intA, intB):
    return intA * intB


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(add(a, b))
    print(minus(a, b))
    print(multiply(a, b))


class Test(unittest.TestCase):

    def testAdd(self):
        self.assertEqual(2, add(1, 1))
        self.assertEqual(5, add(2, 3))
        self.assertEqual(7, add(4, 3))

    def testMinus(self):
        self.assertEqual(0, minus(1, 1))
        self.assertEqual(0, minus(2, 2))
        self.assertEqual(1, minus(4, 3))

    def testMultiple(self):
        self.assertEqual(1, multiply(1, 1))
        self.assertEqual(4, multiply(2, 2))
        self.assertEqual(12, multiply(4, 3))
