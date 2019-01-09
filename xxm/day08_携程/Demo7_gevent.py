# 遇到延时就切换--没有就不切换
# 网络异步并发库
# 延迟阻塞都需要换成gevent的
import gevent
from gevent import monkey
import time

monkey.patch_all()  # 将所有耗时操作替换为gevent模块的内容


def g(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # gevent.sleep(1)
        time.sleep(1)


def gg(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # gevent.sleep(1)
        time.sleep(1)


def ggg(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # gevent.sleep(1)
        time.sleep(1)


def main():
    # g1 = gevent.spawn(g, 5)
    # g2 = gevent.spawn(gg, 5)
    # g3 = gevent.spawn(ggg, 5)
    # join的作用是啥(耗时？g1 = gevent.spawn(g, 5)创建对象不走里面的print) ，为啥必须有它
    # g1.join()
    # g2.join()
    # g3.join()
    gevent.joinall([
        gevent.spawn(g, 5),
        gevent.spawn(gg, 5),
        gevent.spawn(ggg, 5)
    ])


if __name__ == '__main__':
    main()
