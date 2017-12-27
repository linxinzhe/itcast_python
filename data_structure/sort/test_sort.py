import unittest
from .bubble_sort import bubble_sort
from .select_sort import select_sort
from .insert_sort import insert_sort
from .shell_sort import shell_sort


class TestBubbleSort(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.sort = bubble_sort

    def test_sort(self):
        a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        self.assertListEqual(sorted(a), self.sort(a))

    def test_sort_0(self):
        a = []
        self.assertListEqual(sorted(a), self.sort(a))

    def test_sort_1(self):
        a = [54]
        self.assertListEqual(sorted(a), self.sort(a))

    def test_sort_2(self):
        a = [11, 22]
        self.assertListEqual(sorted(a), self.sort(a))
        a = [22, 11]
        self.assertListEqual(sorted(a), self.sort(a))
        a = [11, 11]
        self.assertListEqual(sorted(a), self.sort(a))


class TestSelectionSort(TestBubbleSort):
    def setUp(self):
        super().setUp()
        self.list = select_sort


class TestInsertSort(TestBubbleSort):
    def setUp(self):
        super().setUp()
        self.list = insert_sort


class TestShellSort(TestBubbleSort):
    def setUp(self):
        super().setUp()
        self.list = shell_sort
