# https://www.hackerrank.com/challenges/python-lists

import unittest

result_list = []


def list_func(command):
    command_input = command.split(' ')
    if command_input[0] == 'insert':
        result_list.insert(int(command_input[1]), int(command_input[2]))
    elif command_input[0] == 'print':
        print(result_list)
    elif command_input[0] == 'remove':
        result_list.remove(int(command_input[1]))
    elif command_input[0] == 'append':
        result_list.append(int(command_input[1]))
    elif command_input[0] == 'sort':
        result_list.sort()
    elif command_input[0] == 'pop':
        result_list.pop()
    elif command_input[0] == 'reverse':
        result_list.reverse()


if __name__ == '__main__':
    a = int(input())
    for i in range(0, a):
        list_func(input())


class Test(unittest.TestCase):
    def test_list_function(self):
        input_test = 'insert 0 5'
        list_func(input_test)
        input_test = 'insert 1 10'
        list_func(input_test)
        input_test = 'insert 0 6'
        list_func(input_test)

        self.assertEqual([6, 5, 10], result_list)

        input_test = 'remove 6'
        list_func(input_test)
        input_test = 'append 9'
        list_func(input_test)
        input_test = 'append 1'
        list_func(input_test)
        input_test = 'sort'
        list_func(input_test)

        self.assertEqual([1, 5, 9, 10], result_list)

        input_test = 'pop'
        list_func(input_test)
        input_test = 'reverse'
        list_func(input_test)

        self.assertEqual([9, 5, 1], result_list)
