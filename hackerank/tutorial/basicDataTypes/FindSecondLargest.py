# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list

import unittest


def find_second_largest(arr_int):
    l = list(set(arr_int))
    l.sort()
    return l[-2]


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(find_second_largest(list(arr)))


class Test(unittest.TestCase):
    def test_find_second_largest(self):
        input_str = [2, 3, 4, 5, 6, 5]
        self.assertEqual(5, find_second_largest(list(map(int, input_str))))
        input_str = [1, 2, 4, 6, 9]
        self.assertEqual(6, find_second_largest(list(map(int, input_str))))
