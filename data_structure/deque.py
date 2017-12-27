class Deque():
    def __init__(self):
        self._list = []

    def add_front(self, item):
        # 从队头加入一个item元素
        self._list.insert(0, item)

    def add_rear(self, item):
        # 从队尾加入一个item元素
        self._list.append(item)

    def remove_front(self):
        # 从队头删除一个item元素
        self._list.pop(0)

    def remove_rear(self):
        # 从队尾删除一个item元素
        self._list.pop()

    def is_empty(self):
        # 判断双端队列是否为空
        return self._list

    def size(self):
        # 返回队列的大小
        return len(self._list)
