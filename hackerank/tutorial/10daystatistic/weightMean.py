# https://www.hackerrank.com/challenges/s10-basic-statistics

import unittest


def calc_weighted_mean(siz, float_values, weight_values):
    sum_num = 0
    for i in range(0, siz):
        sum_num += float_values[i] * weight_values[i]

    return sum_num / sum(weight_values)


if __name__ == '__main__':
    size = int(input())
    list_float_values = list(map(float, input().split()))
    list_weight_values = list(map(int, input().split()))
    print("%.1f" % calc_weighted_mean(size, list_float_values, list_weight_values))


class Test(unittest.TestCase):
    def testMeanCalculator(self):
        self.assertEqual(3,
                         calc_weighted_mean(5, [float(1), float(2), float(3), float(4), float(5)],
                                            [1, 1, 1, 1, 1]))
        self.assertEqual(32.0,
                         calc_weighted_mean(5, [float(10), float(40), float(30), float(50), float(20)],
                                            [1, 2, 3, 4, 5]))
        self.assertEqual(3.7,
                         calc_weighted_mean(5, [float(1), float(2), float(3), float(4), float(5)],
                                            [1, 2, 6, 4, 7]))
