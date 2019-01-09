import time
import threading

# method1.使用函数名调用
def dance():
    for i in range(5):
        print("------dance....")
        time.sleep(1)


def sing():
    for i in range(5):
        print("------sing....")
        time.sleep(1)


def main():
    # threading.Thread只是创建了一个对象
    d = threading.Thread(target=dance)
    s = threading.Thread(target=sing)  # target=sing---指定线程去哪里执行
    # print(threading.enumerate().__len__())#线程产生是在start时开始
    d.start()  # 创建了线程
    s.start()
    # while True:
    #     le=len(threading.enumerate())
    #     print("查看线程：%d"%le)
    #     if le==1:
    #         break
    # print(le)
    # for i in threading.enumerate():
    #     print(i)


if __name__ == "__main__":
    main()
