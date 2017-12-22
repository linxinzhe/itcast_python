import unittest
import copy


def bubble_sort(alist):
    my_list = copy.deepcopy(alist)
    n = len(my_list)

    for j in range(0, n - 1):
        for i in range(0, n - 1 - j):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    return my_list


class TestBubbleSort(unittest.TestCase):
    def test_sort(self):
        a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        self.assertListEqual(sorted(a), bubble_sort(a))

    def test_sort_0(self):
        a = []
        self.assertListEqual(sorted(a), bubble_sort(a))

    def test_sort_1(self):
        a = [54]
        self.assertListEqual(sorted(a), bubble_sort(a))

    def test_sort_2(self):
        a = [11, 22]
        self.assertListEqual(sorted(a), bubble_sort(a))
        a = [22, 11]
        self.assertListEqual(sorted(a), bubble_sort(a))
        a = [11, 11]
        self.assertListEqual(sorted(a), bubble_sort(a))
