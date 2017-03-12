# https://www.hackerrank.com/challenges/list-comprehensions

import unittest


def find_second_lowest_value(students):
    value = []
    for a in students:
        value.append(students[a])

    val = list(set(value))
    val.sort()

    return val[1]


def find_student_name(students):
    # sort values only
    second_lowest_value = find_second_lowest_value(students)
    lowest_student_name = []

    for this_ob in students:
        if students[this_ob] == second_lowest_value:
            lowest_student_name.append(this_ob)

    lowest_student_name.sort()

    return lowest_student_name


if __name__ == '__main__':
    student = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student[name] = score

    for name in find_student_name(student):
        print(name)


class Test(unittest.TestCase):
    def test_find_student_name(self):
        students = {'Akriti': 41, 'Harsh': 39}
        self.assertEqual(['Akriti'], find_student_name(students))

        students = {'Harry': 37.21, 'Berry': 37.21, 'Tina': 37.2, 'Akriti': 41, 'Harsh': 39}
        self.assertEqual(['Berry', 'Harry'], find_student_name(students))

        students = {'Harry': 37.21, 'Tina': 37.2, 'Akriti': 41, 'Harsh': 39}
        self.assertEqual(['Harry'], find_student_name(students))

        students = {'Tina': 52, 'Rina': 25, 'Mahesh': 26,'Hean': 27}
        self.assertEqual(['Mahesh'], find_student_name(students))
