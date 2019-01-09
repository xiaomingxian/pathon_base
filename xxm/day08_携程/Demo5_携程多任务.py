import time


def x1():
    while True:
        print("---------1-----------")
        time.sleep(1)
        yield


def x2():
    while True:
        print(".........2............")
        time.sleep(1)
        yield


def main():
    # 产生一个可迭代对象
    xx1 = x1()
    xx2 = x2()
    while True:
        # 执行到yield会阻塞--等待下一次触发----next()需要一个可迭代对象
        next(xx1)
        next(xx2)


if __name__ == '__main__':
    main()
