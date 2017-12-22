import unittest


class Node():
    def __init__(self, item) -> None:
        self.item = item
        self.next = None

    def __str__(self) -> str:
        return str(self.item)


class SingleLinkedCycleList():
    def __iter__(self):
        if self.is_empty():
            return None
        cur = self._head
        while cur.next != self._head:
            yield cur.item
            cur = cur.next
        yield cur.item

    def __init__(self, node=None) -> None:
        self._head = node
        if node:
            node.next = node

    def is_empty(self):  # 链表是否为空
        return self._head is None

    def length(self):  # 链表长度
        if self.is_empty():
            return 0
        cur = self._head
        count = 1

        while cur.next != self._head:
            count += 1
            cur = cur.next
        return count

    def travel(self):  # 遍历整个链表
        if self.is_empty():
            return
        cur = self._head
        while cur.next != self._head:
            print(cur.item)
            cur = cur.next
        print(cur)

    def add(self, item):  # 链表头部添加元素
        node = Node(item)

        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node

            temp_node = self._head
            self._head = node
            node.next = temp_node

    def append(self, item):  # 链表尾部添加元素
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            node.next = self._head

    def insert(self, pos, item):  # 指定位置添加元素
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            node = Node(item)
            count = 0
            cur = self._head
            while count != (pos - 1):
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):  # 删除节点
        if self.is_empty():
            return

        cur = self._head

        # 单节点
        if cur.next == self._head:
            if cur.item == item:
                self._head = None
            else:
                return
        else:
            # 多节点
            pre = None
            while cur.next != self._head:
                if cur.item == item:
                    if pre:
                        pre.next = cur.next
                    else:
                        # 多节点第一个
                        temp_node = cur.next
                        while cur.next != self._head:
                            pre = cur
                            cur = cur.next
                        self._head = temp_node
                        cur.next = self._head
                        return
                pre = cur
                cur = cur.next

            # 多节点，最后一个
            if pre and cur.item == item:
                pre.next = self._head
                return

    def search(self, item):  # 查找节点是否存在
        cur = self._head
        count = 0
        while cur and cur.next != self._head:
            if cur.item == item:
                return count
            count += 1
            cur = cur.next

        if cur and cur.next and cur.item == item:
            return count

        return False


class TestLinkedCycleList(unittest.TestCase):
    def test_init(self):
        ll = SingleLinkedCycleList()
        self.assertIsNone(ll._head)

    def test_is_empty(self):
        ll = SingleLinkedCycleList()
        self.assertTrue(ll.is_empty())

    def test_length_0(self):
        ll = SingleLinkedCycleList()
        self.assertEqual(ll.length(), 0)

    def test_length(self):
        ll = SingleLinkedCycleList(Node(1))
        self.assertEqual(ll.length(), 1)

    def test_travel(self):
        ll = SingleLinkedCycleList()
        ll.travel()

    def test_add_1(self):
        ll = SingleLinkedCycleList()
        ll.add(1)
        self.assertEqual(ll.length(), 1)
        self.assertListEqual(list(ll), [1])

    def test_add(self):
        ll = SingleLinkedCycleList()
        ll.add(1)
        ll.add(2)
        ll.add(3)
        self.assertEqual(ll.length(), 3)
        self.assertListEqual(list(ll), [3, 2, 1])

    def test_append_1(self):
        ll = SingleLinkedCycleList()
        ll.append(1)
        ll.append(1)
        self.assertEqual(ll.length(), 2)
        self.assertListEqual(list(ll), [1, 1])

    def test_iter_0(self):
        ll = SingleLinkedCycleList()
        for i in ll:
            print(i)

    def test_iter(self):
        ll = SingleLinkedCycleList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        print(list(ll))

    def test_insert_0(self):
        ll = SingleLinkedCycleList()
        ll.insert(0, 1)
        self.assertListEqual(list(ll), [1])

    def test_insert(self):
        ll = SingleLinkedCycleList()
        ll.insert(0, 1)
        ll.insert(0, 1)
        ll.insert(1, 2)
        ll.insert(100, 3)
        self.assertListEqual(list(ll), [1, 2, 1, 3])

    def test_search(self):
        ll = SingleLinkedCycleList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        self.assertEqual(ll.search(3), 2)

    def test_search_0(self):
        ll = SingleLinkedCycleList()
        self.assertFalse(ll.search(3))

    def test_search_first_last(self):
        ll = SingleLinkedCycleList()
        ll.append(1)
        self.assertEqual(ll.search(1), 0)

    def test_search_first(self):
        ll = SingleLinkedCycleList()
        ll.append(1)
        ll.append(2)
        self.assertEqual(ll.search(1), 0)

    def test_search_last(self):
        ll = SingleLinkedCycleList()
        ll.append(1)
        ll.append(2)
        self.assertEqual(ll.search(2), 1)

    def test_remove_0(self):
        ll = SingleLinkedCycleList()
        ll.append(1)
        ll.remove(1)
        self.assertTrue(ll.is_empty())

    def test_remove(self):
        ll = SingleLinkedCycleList()
        ll.append(1)
        ll.append(2)
        ll.remove(1)
        self.assertListEqual([2], list(ll))

    def test_all(self):
        # TestCase
        ll = SingleLinkedCycleList()
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
