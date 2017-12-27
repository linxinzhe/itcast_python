import unittest
from .dual_linked_list import Node


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
