# 闭包:运用参数，灵活生成函数的函数
def line(a, b):
    def real_line(x):
        return a * x + b

    return real_line


my_line = line(2, 1)
my_line(2)
