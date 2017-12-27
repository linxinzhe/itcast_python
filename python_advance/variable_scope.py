# locals
# enclosing   外部嵌套函数的命名空间，闭包上面的变量
# globals
# buitins
# legb 按顺序查找

# num = 100  global
def test1():
    # num = 200  enclosing
    def test2():
        num = 300  # locals
        print(num)

    return test2


ret = test1()
ret()
