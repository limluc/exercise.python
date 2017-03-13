# https://www.hackerrank.com/challenges/ctci-making-anagrams

import unittest


def number_needed(a, b):
    dict_set_a = build_dict(a)
    dict_set_b = build_dict(b)

    count = 0

    for val_a in dict_set_a:
        try:
            num = abs(dict_set_b[val_a] - dict_set_a[val_a])
            count += num
            dict_set_b.pop(val_a)
        except KeyError:
            count += dict_set_a[val_a]

    for val_b in dict_set_b:
        try:
            num = abs(dict_set_b[val_b] != dict_set_a[val_b])
            count += num
        except KeyError:
            count += dict_set_b[val_b]

    return count


def build_dict(_list):
    dict_set = dict.fromkeys(set(_list), 0)
    for _val in _list:
        dict_set[_val] += 1

    return dict_set


if __name__ == '__main__':
    a = input()
    b = input()
    a.split()
    print(number_needed(list(a), list(b)))


class Test(unittest.TestCase):
    def test(self):
        # self.assertEqual(0, number_needed(list('abc'), list('bca')))
        # self.assertEqual(1, number_needed(list('abcd'), list('bca')))
        # self.assertEqual(4, number_needed(list('cde'), list('abc')))
        # self.assertEqual(3, number_needed(list('cdeabc'), list('abc')))
        # self.assertEqual(5, number_needed(list('aaaa'), list('abc')))
        self.assertEqual(5, number_needed(list('aabbczz'), list('cbbban')))
        self.assertEqual(30, number_needed(list('fcrxzwscanmligyxyvym'), list('jxwtrhvujlmrpdoqbisbwhmgpmeoke')))
