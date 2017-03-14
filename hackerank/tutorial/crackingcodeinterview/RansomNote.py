import unittest


# Option 1 - Slower
# def ransom_note(magazine_, ransom_):
#     result_ = True
#     for string in ransom_:
#         found_ = find_local_array(magazine_, string)
#         if found_ == -1:
#             result_ = result_ and False
#         else:
#             result_ = result_ and True
#             magazine_.pop(found_)
#     return result_
#
#
# def find_local_array(array_, string):
#     for i in range(0, len(array_)):
#         if array_[i] == string:
#             return i
#     return -1


# Option 2 - Using dictionary
def ransom_note(reference_, ransom_):
    dict_set = dict.fromkeys(set(reference_), 0)
    for word in reference_:
        dict_set[word] += 1

    for word in ransom_:
        try:
            if dict_set[word] == 0:
                return False
        except KeyError:
            return False
        dict_set[word] -= 1
    return True


if __name__ == '__main__':
    m, n = map(int, input().split(' '))
    magazine = input().strip().split(' ')
    ransom = input().strip().split(' ')
    answer = ransom_note(magazine, ransom)
    if answer:
        print("Yes")
    else:
        print("No")


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(True, ransom_note(['give', 'me', 'one', 'grand', 'today', 'night'],
                                           ['give', 'one', 'grand', 'today']))
        self.assertEqual(False, ransom_note(['give', 'me', 'One', 'grand', 'today', 'night'],
                                            ['give', 'one', 'grand', 'today']))
        # should deal with duplicated
        self.assertEqual(False, ransom_note(['give', 'me', 'one', 'grand', 'today', 'night'],
                                            ['give', 'one', 'one', 'grand', 'today']))
