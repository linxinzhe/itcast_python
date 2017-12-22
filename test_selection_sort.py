import unittest
import copy


def selection_sort(alist):
    my_list = copy.deepcopy(alist)
    n = len(my_list)

    for j in range(0, n - 1):
        min_i = j
        for i in range(j, n):
            if my_list[min_i] > my_list[i]:
                min_i = i
        my_list[j], my_list[min_i] = my_list[min_i], my_list[j]

    return my_list


class TestSelectionSort(unittest.TestCase):
    def test_sort(self):
        a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        self.assertListEqual(sorted(a), selection_sort(a))

    def test_sort_0(self):
        a = []
        self.assertListEqual(sorted(a), selection_sort(a))

    def test_sort_1(self):
        a = [54]
        self.assertListEqual(sorted(a), selection_sort(a))

    def test_sort_2(self):
        a = [11, 22]
        self.assertListEqual(sorted(a), selection_sort(a))
        a = [22, 11]
        self.assertListEqual(sorted(a), selection_sort(a))
        a = [11, 11]
        self.assertListEqual(sorted(a), selection_sort(a))
