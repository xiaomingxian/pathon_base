import threading
import time

# 资源竞争
num = 0

lock=threading.Lock()



def t1(n):
    global num
    lock.acquire()
    for i in range(n):
        num += 1
        # print('111111')
    lock.release()


def t2(n):
    global num
    lock.acquire()
    for i in range(n):
        num += 1
        # print('22222')
    lock.release()


def main():
    tt1 = threading.Thread(target=t1, args=(100000000,))
    tt2 = threading.Thread(target=t2, args=(100000000,))
    tt1.start()
    time.sleep(1)
    print("test:%d"%num)
    tt2.start()


if __name__ == "__main__":
    main()
    # 执行时间过长？？？过早的拿到了num???
    time.sleep(20)
    print(num)
