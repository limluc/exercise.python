# https://www.hackerrank.com/challenges/python-tuples

import unittest


def hash_func(tuple_input):
    return hash(tuple(tuple_input))

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash_func(integer_list))


class Test(unittest.TestCase):
    def test_tuple_func(self):
        self.assertEqual(3713082714465905806, hash_func(map(int, [2, 1])))
        self.assertEqual(3713081631934410656, hash_func(map(int, [1, 2])))
