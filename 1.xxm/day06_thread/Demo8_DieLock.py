import threading
import time

# 死锁---枷锁的顺序相反--出现存在概率问题(数据量大时)
# 优化:1.银行家算法--约定锁的解锁时间   2.合理的设计程序  3.设计超时时间

# 定义锁
l1 = threading.Lock()
l2 = threading.Lock()


def t1():
    for i in range(30):
        l1.acquire()
        l2.acquire()
        print("111---------")
        l2.release()
        l1.release()


def t2():
    for i in range(30):
        l2.acquire()
        l1.acquire()
        print("222--")
        l1.release()
        l2.release()


if __name__ == "__main__":
    tt1 = threading.Thread(target=t1)
    tt2 = threading.Thread(target=t2)

    tt1.start()
    tt2.start()
