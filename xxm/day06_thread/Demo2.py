import threading
import time


# method2.实用类

class MyThread(threading.Thread):

    def run(self):
        for i in range(5):
            print('线程一')
            time.sleep(1)


class MyThread2(threading.Thread):

    def run(self):
        for i in range(5):
            print("线程2")
            time.sleep(1)


def main():
    t1 = MyThread()
    t2 = MyThread2()

    t1.start()
    t2.start()
    print(threading.enumerate())


if __name__ == "__main__":
    main()
