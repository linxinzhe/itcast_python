import unittest
import copy


def shell_sort(alist):
    my_list = copy.deepcopy(alist)
    n = len(my_list)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            for j in range(i, 0, -gap):
                if my_list[j - gap] > my_list[j]:
                    my_list[j], my_list[j - gap] = my_list[j - gap], my_list[j]
        gap = gap // 2

    return my_list


class TestShellSort(unittest.TestCase):
    def test_sort(self):
        a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        self.assertListEqual(sorted(a), shell_sort(a))

    def test_sort_0(self):
        a = []
        self.assertListEqual(sorted(a), shell_sort(a))

    def test_sort_1(self):
        a = [54]
        self.assertListEqual(sorted(a), shell_sort(a))

    def test_sort_2(self):
        a = [11, 22]
        self.assertListEqual(sorted(a), shell_sort(a))
        a = [22, 11]
        self.assertListEqual(sorted(a), shell_sort(a))
        a = [11, 11]
        self.assertListEqual(sorted(a), shell_sort(a))
