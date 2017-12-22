class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        # 添加一个新的元素item到栈顶
        self.items.append(item)

    def pop(self):
        # 弹出栈顶元素
        return self.items.pop()

    def peek(self):
        # 返回栈顶元素
        return self.items[-1]

    def is_empty(self):
        # 判断栈是否为空
        return self.items

    def size(self):
        # 返回栈的元素个数
        return len(self.items)
