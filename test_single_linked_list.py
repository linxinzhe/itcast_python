import unittest


class Node():
    def __init__(self, item) -> None:
        self.item = item
        self.next = None

    def __str__(self) -> str:
        return str(self.item)


class SingleLinkedList():

    def __init__(self, node=None) -> None:
        self._head = node

    def __iter__(self):
        if self.is_empty():
            return None
        cur = self._head
        while cur:
            yield cur.item
            cur = cur.next

    def is_empty(self):  # 链表是否为空
        return self._head is None

    def length(self):  # 链表长度
        cur = self._head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def travel(self):  # 遍历整个链表
        cur = self._head
        while cur:
            print(cur.item)
            cur = cur.next

    def add(self, item):  # 链表头部添加元素
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            temp_node = self._head
            self._head = node
            node.next = temp_node

    def append(self, item):  # 链表尾部添加元素
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next:
                cur = cur.next

            cur.next = node

    def insert(self, pos, item):  # 指定位置添加元素
        if pos == 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            count = 0
            cur = self._head
            while count != (pos - 1):
                count += 1
                cur = cur.next
            temp_node = cur.next
            node = Node(item)
            node.next = temp_node
            cur.next = node

    def remove(self, item):  # 删除节点
        cur = self._head
        pre = None
        count = 0
        while cur:
            if cur.item == item:
                if count == 0:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                    break
            count += 1
            pre = cur
            cur = cur.next

    def search(self, item):  # 查找节点是否存在
        cur = self._head
        count = 0
        while cur:
            if cur.item == item:
                return count
            count += 1
            cur = cur.next
        else:
            return False


class TestSingleLinkedList(unittest.TestCase):
    def test_init(self):
        ll = SingleLinkedList()
        self.assertIsNone(ll._head)

    def test_is_empty(self):
        ll = SingleLinkedList()
        self.assertTrue(ll.is_empty())

    def test_length_0(self):
        ll = SingleLinkedList()
        self.assertEqual(ll.length(), 0)

    def test_length(self):
        ll = SingleLinkedList(Node(1))
        self.assertEqual(ll.length(), 1)

    def test_travel(self):
        ll = SingleLinkedList()
        ll.travel()

    def test_add_1(self):
        ll = SingleLinkedList()
        ll.add(1)
        self.assertEqual(ll.length(), 1)
        self.assertListEqual(list(ll), [1])

    def test_add(self):
        ll = SingleLinkedList()
        ll.add(1)
        ll.add(2)
        ll.add(3)
        self.assertEqual(ll.length(), 3)
        self.assertListEqual(list(ll), [3, 2, 1])

    def test_append_1(self):
        ll = SingleLinkedList()
        ll.append(1)
        ll.append(1)
        self.assertEqual(ll.length(), 2)
        self.assertListEqual(list(ll), [1, 1])

    def test_iter_0(self):
        ll = SingleLinkedList()
        for i in ll:
            print(i)

    def test_iter(self):
        ll = SingleLinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        print(list(ll))

    def test_insert_0(self):
        ll = SingleLinkedList()
        ll.insert(0, 1)
        self.assertListEqual(list(ll), [1])

    def test_insert(self):
        ll = SingleLinkedList()
        ll.insert(0, 1)
        ll.insert(0, 1)
        ll.insert(1, 2)
        ll.insert(100, 3)
        self.assertListEqual(list(ll), [1, 2, 1, 3])

    def test_search(self):
        ll = SingleLinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        self.assertEqual(ll.search(3), 2)

    def test_search_0(self):
        ll = SingleLinkedList()
        self.assertFalse(ll.search(3))

    def test_search_first_last(self):
        ll = SingleLinkedList()
        ll.append(1)
        self.assertEqual(ll.search(1), 0)

    def test_search_first(self):
        ll = SingleLinkedList()
        ll.append(1)
        ll.append(2)
        self.assertEqual(ll.search(1), 0)

    def test_search_last(self):
        ll = SingleLinkedList()
        ll.append(1)
        ll.append(2)
        self.assertEqual(ll.search(2), 1)

    def test_remove_0(self):
        ll = SingleLinkedList()
        ll.append(1)
        ll.remove(1)
        self.assertTrue(ll.is_empty())

    def test_remove(self):
        ll = SingleLinkedList()
        ll.append(1)
        ll.append(2)
        ll.remove(1)
        self.assertListEqual([2], list(ll))

    def test_all(self):
        # TestCase
        ll = SingleLinkedList()
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
