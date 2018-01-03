import unittest

from .binary_search import binary_search
from .binary_search import binary_search_2


class TestBinarySearch(unittest.TestCase):
    def test_binary_search_recursion_0(self):
        testlist = []

        self.assertFalse(binary_search(testlist, 1))
        self.assertFalse(binary_search(testlist, 2))

    def test_binary_search_recursion_1(self):
        testlist = [1]

        self.assertTrue(binary_search(testlist, 1))
        self.assertFalse(binary_search(testlist, 2))

    def test_binary_search_recursion_even(self):
        testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, 60]

        self.assertTrue(binary_search(testlist, 13))
        self.assertFalse(binary_search(testlist, 3))

    def test_binary_search_recursion_odd(self):
        testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]

        self.assertTrue(binary_search(testlist, 13))
        self.assertFalse(binary_search(testlist, 3))

    def test_binary_search_loop_0(self):
        testlist = []

        self.assertFalse(binary_search_2(testlist, 1))
        self.assertFalse(binary_search_2(testlist, 2))

    def test_binary_search_loop_1(self):
        testlist = [1]

        self.assertTrue(binary_search_2(testlist, 1))
        self.assertFalse(binary_search_2(testlist, 2))

    def test_binary_search_loop_even(self):
        testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, 60]

        self.assertTrue(binary_search_2(testlist, 13))
        self.assertFalse(binary_search_2(testlist, 3))

    def test_binary_search_loop_odd(self):
        testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]

        self.assertTrue(binary_search_2(testlist, 13))
        self.assertFalse(binary_search_2(testlist, 3))
