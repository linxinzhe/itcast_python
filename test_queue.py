class Queue:
    def __init__(self) -> None:
        self._list = []

    def enqueue(self, item):
        self._list.append(item)

    def dequeue(self):
        self._list.pop(0)

    def is_empty(self):
        return self._list

    def size(self):
        return len(self._list)
