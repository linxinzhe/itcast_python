import unittest, pytest
from .dual_linked_list import Node, DualLinkedList
from .single_linked_list import SingleLinkedList
from .single_linked_cycle_list import SingleLinkedCycleList


class TestDualLinkedList(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.list = DualLinkedList

    def test_init(self):
        ll = self.list()
        self.assertIsNone(ll._head)

    def test_is_empty(self):
        ll = self.list()
        self.assertTrue(ll.is_empty())

    def test_length_0(self):
        ll = self.list()
        self.assertEqual(ll.length(), 0)

    def test_length(self):
        ll = self.list(Node(1))
        self.assertEqual(1, ll.length())

    def test_travel(self):
        ll = self.list()
        ll.travel()

    def test_add_1(self):
        ll = self.list()
        ll.add(1)
        self.assertEqual(ll.length(), 1)
        self.assertListEqual(list(ll), [1])

    def test_add(self):
        ll = self.list()
        ll.add(1)
        ll.add(2)
        ll.add(3)
        self.assertEqual(ll.length(), 3)
        self.assertListEqual(list(ll), [3, 2, 1])

    def test_append_1(self):
        ll = self.list()
        ll.append(1)
        ll.append(1)
        self.assertEqual(ll.length(), 2)
        self.assertListEqual(list(ll), [1, 1])

    def test_iter_0(self):
        ll = self.list()
        for i in ll:
            print(i)

    def test_iter(self):
        ll = self.list()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        print(list(ll))

    def test_insert_0(self):
        ll = self.list()
        ll.insert(0, 1)
        self.assertListEqual(list(ll), [1])

    def test_insert(self):
        ll = self.list()
        ll.insert(0, 1)
        ll.insert(0, 1)
        ll.insert(1, 2)
        ll.insert(100, 3)
        self.assertListEqual(list(ll), [1, 2, 1, 3])

    def test_search(self):
        ll = self.list()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        self.assertEqual(ll.search(3), 2)

    def test_search_0(self):
        ll = self.list()
        self.assertFalse(ll.search(3))

    def test_search_first_last(self):
        ll = self.list()
        ll.append(1)
        self.assertEqual(ll.search(1), 0)

    def test_search_first(self):
        ll = self.list()
        ll.append(1)
        ll.append(2)
        self.assertEqual(ll.search(1), 0)

    def test_search_last(self):
        ll = self.list()
        ll.append(1)
        ll.append(2)
        self.assertEqual(ll.search(2), 1)

    def test_remove_0(self):
        ll = self.list()
        ll.append(1)
        ll.remove(1)
        self.assertTrue(ll.is_empty())

    def test_remove(self):
        ll = self.list()
        ll.append(1)
        ll.append(2)
        ll.remove(1)
        self.assertListEqual([2], list(ll))

    def test_remove_last(self):
        ll = self.list()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.remove(3)
        self.assertListEqual([1, 2], list(ll))

    def test_all(self):
        # TestCase
        ll = self.list()
        ll.add(1)
        self.assertListEqual([1], list(ll))
        ll.add(2)
        self.assertListEqual([2, 1], list(ll))
        ll.append(3)
        self.assertListEqual([2, 1, 3], list(ll))
        ll.insert(2, 4)
        self.assertListEqual([2, 1, 4, 3], list(ll))

        self.assertEqual(4, ll.length())
        print("--begin travel----")
        ll.travel()
        print("--end travel----")
        self.assertEqual(3, ll.search(3))

        self.assertFalse(ll.search(5))

        ll.remove(1)
        self.assertEqual(3, ll.length())
        print("--begin travel----")
        ll.travel()
        print("--end travel----")


class TestSingleLinkedList(TestDualLinkedList):
    def setUp(self):
        super().setUp()
        self.list = SingleLinkedList


#
class TestSingleLinkedCycleList(TestDualLinkedList):
    def setUp(self):
        super().setUp()
        self.list = SingleLinkedCycleList
