# https://www.hackerrank.com/challenges/list-comprehensions

import unittest


def cube_permutation(x, y, z):
    results = []
    for x_value in range(0, x + 1):
        for y_value in range(0, y + 1):
            for z_value in range(0, z + 1):
                # option to add logic here, but not for more reusable code
                results.append([x_value, y_value, z_value])
    return results


def sum_value(list):
    sum_i = 0
    for i in list:
        sum_i = sum_i + i
    return sum_i


def remove_sum(lists, n):
    new_values = []
    for list_i in lists:
        if sum_value(list_i) != n:
            new_values.append(list_i)
    return new_values


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    cube_iter = cube_permutation(x, y, z)
    print(remove_sum(cube_iter, n))


class Test(unittest.TestCase):
    sample = [[0, 0, 0], [0, 0, 1], [1, 0, 0], [1, 0, 1]]

    def test_cube_permutation(self):
        self.assertEqual(self.sample, cube_permutation(1, 0, 1))

    def test_remove_sum(self):
        self.assertEqual([[0, 0, 0], [0, 0, 1], [1, 0, 0]], remove_sum(self.sample, 2))
        self.assertEqual([[0, 0, 0], [1, 0, 1]], remove_sum(self.sample, 1))
