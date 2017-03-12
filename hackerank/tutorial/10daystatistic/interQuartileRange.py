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


def calc_interquartile(lis_int):
    return calc_quartile(lis_int, len(lis_int), 3) - calc_quartile(lis_int, len(lis_int), 1)


def construct_freq(lis_int, lis_freq):
    new_lis = []
    for i in range(0, len(lis_int)):
        for _ in range(0, lis_freq[i]):
            new_lis.append(lis_int[i])
    return new_lis


if __name__ == '__main__':
    size = int(input())
    list_int = list(map(int, input().split()))
    list_freq = list(map(int, input().split()))
    new_list = construct_freq(list_int, list_freq)
    print("%.1f" % calc_interquartile(new_list))


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(9.0, calc_interquartile(construct_freq([6, 12, 8, 10, 20, 16], [5, 4, 3, 2, 1, 5])))
        self.assertEqual(8, calc_interquartile(construct_freq([6, 12, 8, 10, 20, 16], [1, 1, 1, 1, 1, 1])))
