# https://www.hackerrank.com/challenges/write-a-function

import unittest


def is_leap(year):
    leap = False
    # Write your logic here
    if year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0):
        leap = True

    return leap


if __name__ == '__main__':
    year = int(input())
    print(is_leap(year))


class Test(unittest.TestCase):
    def testDivision(self):
        self.assertEqual(True, is_leap(2000))
        self.assertEqual(False, is_leap(2100))
        self.assertEqual(False, is_leap(1990))
        self.assertEqual(False, is_leap(2010))
        self.assertEqual(True, is_leap(2012))
