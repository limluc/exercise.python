# https://www.hackerrank.com/challenges/s10-basic-statistics

import unittest


def calc_mean(lis_float, size_arr):
    return sum(lis_float) / size_arr


def calc_median(lis_float, size_arr):
    arr_ = size_arr // 2

    if size_arr % 2 == 1:
        return lis_float[arr_]
    else:
        return (lis_float[arr_] + lis_float[arr_ - 1]) / 2


def calc_mode(lis_float):
    dict_set = dict.fromkeys(set(lis_float), 0)
    for this_float in lis_float:
        dict_set[this_float] += 1

    max_count = 1
    max_value = lis_float[0]

    for entry_key in dict_set:
        if dict_set[entry_key] > max_count:
            max_count = dict_set[entry_key]
            max_value = entry_key
        elif dict_set[entry_key] == max_count and entry_key < max_value:
            max_count = dict_set[entry_key]
            max_value = entry_key

    return max_value


if __name__ == '__main__':
    size = int(input())
    list_float = list(map(float, input().split()))
    list_float.sort()
    print("%.6g" % calc_mean(list_float, size))
    print("%.6g" % calc_median(list_float, size))
    print("%.6g" % calc_mode(list_float))


class Test(unittest.TestCase):
    def testMeanCalculator(self):
        self.assertEqual(3, calc_mean([float(1.0), float(2), float(3), float(4), float(5)], 5))
        self.assertEqual(2.5, calc_mean([float(1), float(4)], 2))

    def testMedianCalculator(self):
        self.assertEqual(3, calc_median([float(2), float(3), float(4)], 3))
        self.assertEqual(3.5, calc_median([float(2), float(3), float(4), float(5)], 4))

    def testModeCalculator(self):
        self.assertEqual(2, calc_mode([float(2), float(2), float(3), float(6), float(5)]))
        self.assertEqual(2, calc_mode([float(10), float(2), float(3), float(6), float(5), float(10), float(2)]))
        self.assertEqual(2, calc_mode([float(2), float(9), float(3), float(6), float(5)]))
