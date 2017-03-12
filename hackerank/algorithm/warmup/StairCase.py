# !/bin/python3

# https://www.hackerrank.com/challenges/staircase

if __name__ == '__main__':
    v = int(input())
    for i in range(1, v + 1):
        _string = (' ' * (v - i)) + ('#' * (i))
        print(_string)
