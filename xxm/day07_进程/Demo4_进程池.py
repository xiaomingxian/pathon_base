from multiprocessing import Pool
import os, time


def pro(i):
    print("参数:%d---进程号:%d" % (i, os.getpid()))
    time.sleep(1)
    # print("子进程....", i)


def main():
    # 必须写在里边？？？
    po = Pool(3)
    for i in range(10):
        po.apply_async(func=pro, args=(i,))

    po.close()
    po.join()  # 等待线程池关闭后  主进程才结束


if __name__ == '__main__':
    main()

# from multiprocessing import Pool  # 导入进程池模块pool
# import time, os

#
# def foo(i):
#     time.sleep(2)
#     print("in process", os.getpid())  # 打印进程号
#
#
# if __name__ == "__main__":
#     pool = Pool(processes=5)  # 设置进程池个数为5，也可以写成pool = Pool(5)，允许进程池同时放入5个进程，并且这5个进程交给cpu去运行
#     for i in range(10):
#         pool.apply(func=foo, args=(i,))  # 同步执行挂起进程
#     print('end')
#     pool.close()
#     pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。

# def foo(i):
#     time.sleep(2)
#     print("in process", os.getpid())  # 打印进程号
#
#
# if __name__ == "__main__":
#     pool = Pool(processes=5)  # 设置进程池个数为5，也可以写成pool = Pool(5)，允许进程池同时放入5个进程，并且这5个进程交给cpu去运行
#     for i in range(10):
#         pool.apply_async(func=foo, args=(i,))  # 采用异步方式执行foo函数
#     print('end')
#     pool.close()
#     pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。
