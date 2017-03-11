# https://www.hackerrank.com/challenges/py-if-else
import unittest


def main(input):
    prefix = ''

    if input % 2 == 0:
        if (2 <= input <= 5) or (input > 20):
            prefix = 'Not '

    return prefix + 'Weird'


if __name__ == '__main__':
    print(main(int(input())))


class Test(unittest.TestCase):
    nw = 'Not Weird'
    w = 'Weird'

    def test(self):
        self.assertEqual(self.w, main(1))
        self.assertEqual(self.nw, main(2))
        self.assertEqual(self.nw, main(4))
        self.assertEqual(self.w, main(5))
        self.assertEqual(self.w, main(6))
        self.assertEqual(self.w, main(7))
        self.assertEqual(self.w, main(20))
        self.assertEqual(self.w, main(21))
        self.assertEqual(self.nw, main(22))
