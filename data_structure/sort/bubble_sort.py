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