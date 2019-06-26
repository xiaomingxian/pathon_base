from greenlet import greenlet
import time


def g1():
    while True:
        print("-----A-----")
        # 切换携程
        gg2.switch()
        time.sleep(0.5)
        print("....A....")
        pass


def g2():
    while True:
        print("-----B-----")
        gg1.switch()
        time.sleep(0.5)
        print("....B....")
        pass
if __name__ == '__main__':
    gg1 = greenlet(g1)
    gg2 = greenlet(g2)

    # 起步函数？？
    # gg1.switch()
    gg2.switch()

    # 执行顺序类似于   yield
