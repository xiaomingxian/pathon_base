import multiprocessing


def p1(q):
    # 模拟传输数据
    data = ['mv', 'music', 'book']
    # 将数据存放到队列中去
    for i in data:
        q.put(i)
    print("存储数据完毕")
    pass


def p2(q):
    while True:

        if q.empty():
            print("...数据读取完毕")
            break
        else:
            x = q.get()
            print(x)

    pass


def main():
    # 定义队列--用于通信
    q = multiprocessing.Queue()
    pp1 = multiprocessing.Process(target=p1, args=(q,))
    pp2 = multiprocessing.Process(target=p2, args=(q,))

    pp1.start()
    pp2.start()


if __name__ == '__main__':
    main()
