import os
import time
from multiprocessing import Process


def test(num):
    print("pid=%d,ppid=%d,,,,num=%d" % (os.getpid(), os.getppid(), num))


p = Process(target=test, args=(100,))  # 给test传参
p.start()
print("----main--pid=%d--" % os.getpid())


# 另一种创建进程的方法
class MyNewProcess(Process):
    def run(self):
        while True:
            print("---1----")
            time.sleep(1)


p = MyNewProcess()
p.start()

while True:
    print("---main----")
    time.sleep(1)
