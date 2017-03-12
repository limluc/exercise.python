# https://www.hackerrank.com/challenges/s10-standard-deviation

import unittest
import math


def calc_mean(lis_float):
    return sum(lis_float) / len(lis_float)


def cal_sd(lis_float):
    mean = calc_mean(lis_float)
    sum = 0
    for _float in lis_float:
        sum += math.pow(_float - mean, 2)

    return math.sqrt(sum / len(lis_float))


if __name__ == '__main__':
    size = int(input())
    list_float = list(map(float, input().split()))
    list_float.sort()
    print("%.1f" % cal_sd(list_float))


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(0.8, cal_sd([float(3), float(3), float(3), float(4), float(5)]))
        self.assertEqual(14.142135623730951, cal_sd([10, 40, 30, 50, 20]))
