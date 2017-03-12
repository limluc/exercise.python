# https://www.hackerrank.com/challenges/s10-basic-statistics

import unittest


def calc_quartile(lis_int, size_arr, quart):
    lis_int.sort()

    if quart == 1:
        to_value = (size_arr // 2)
        return calc_median(lis_int[0: to_value])
    elif quart == 2:
        return calc_median(lis_int)
    elif quart == 3:
        from_value = (size_arr // 2) + size_arr % 2
        return calc_median(lis_int[from_value: size_arr])
    else:
        return 0


def calc_median(lis_int):
    arr_ = len(lis_int) // 2

    if len(lis_int) % 2 == 1:
        return lis_int[arr_]
    else:
        return (lis_int[arr_] + lis_int[arr_ - 1]) / 2


if __name__ == '__main__':
    size = int(input())
    list_int = list(map(int, input().split()))
    print("%.6g" % calc_quartile(list_int, size, 1))
    print("%.6g" % calc_quartile(list_int, size, 2))
    print("%.6g" % calc_quartile(list_int, size, 3))


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(1.5, calc_quartile([float(5), float(2), float(1), float(4), float(3)], 5, 1))
        self.assertEqual(3, calc_quartile([float(5), float(2), float(1), float(4), float(3)], 5, 2))
        self.assertEqual(4.5, calc_quartile([float(5), float(2), float(1), float(4), float(3)], 5, 3))

        self.assertEqual(4, calc_quartile([4, 17, 7, 14, 18, 12, 3, 16, 10, 4, 4, 12], 12, 1))
        self.assertEqual(11, calc_quartile([4, 17, 7, 14, 18, 12, 3, 16, 10, 4, 4, 12], 12, 2))
        self.assertEqual(15, calc_quartile([4, 17, 7, 14, 18, 12, 3, 16, 10, 4, 4, 12], 12, 3))
