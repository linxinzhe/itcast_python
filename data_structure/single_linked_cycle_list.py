import unittest
from .dual_linked_list import Node


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
