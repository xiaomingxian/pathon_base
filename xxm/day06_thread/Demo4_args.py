import threading
import time


# 传参数...


def thread1(args):
    print("1...%s" % str(args))


def thread2(args):
    print("2...%s" % str(args))


num = [1, 2]


def main():
    t1 = threading.Thread(target=thread1, args=(num,))
    t2 = threading.Thread(target=thread2, args=(num,))
    t1.start()
    t2.start()


def test():
    n=10
    print(n+1)


if __name__ == "__main__":
    # main()
    test()