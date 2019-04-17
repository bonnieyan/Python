import threading
import time
import random


def test(someinfo):
    time.sleep(random.randint(1, 10))
    print("执行：" + someinfo)


if __name__ == "__main__":
    t1 = threading.Thread(target=test, args=("线程1",))
    t2 = threading.Thread(target=test, args=("线程2",))
    t3 = threading.Thread(target=test, args=("线程3",))
    t4 = threading.Thread(target=test, args=("线程4",))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    print("主线程运行")