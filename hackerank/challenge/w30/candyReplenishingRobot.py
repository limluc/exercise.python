# https://www.hackerrank.com/contests/w30/challenges/candy-replenishing-robot

# !/bin/python3

import unittest


def calculate_candy(initial_candy_number_, party_time_, candy_consumed_):
    current_candy_number_ = initial_candy_number_
    sum_candy_added = 0

    if party_time_ == 1:
        return 0

    for i in range(0, party_time_ - 1):
        current_candy_number_ = current_candy_number_ - candy_consumed_[i]

        if current_candy_number_ < 5:
            added_this_round = (initial_candy_number_ - current_candy_number_)
            sum_candy_added = sum_candy_added + added_this_round

            current_candy_number_ = initial_candy_number_

    return sum_candy_added


if __name__ == '__main__':
    initial_candy_number, party_time = input().strip().split(' ')
    initial_candy_number, party_time = [int(initial_candy_number), int(party_time)]

    candy_consumed = list(map(int, input().strip().split(' ')))

    print(
        calculate_candy(initial_candy_number, party_time, candy_consumed)
    )


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(5, calculate_candy(8, 3, [5, 2, 4]))
        self.assertEqual(11, calculate_candy(8, 4, [3, 1, 7, 5]))
        self.assertEqual(0, calculate_candy(5, 1, [3]))
