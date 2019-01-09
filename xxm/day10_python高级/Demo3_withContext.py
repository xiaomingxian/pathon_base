from contextlib import contextmanager


class MyFile(object):
    def __init__(self):
        pass

    def __enter__(self):
        return 'x';

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('有没有异常都一定会-执行')


def main():
    with MyFile() as s:
        print(s)


# zhuangshiqi
@contextmanager
def method2():
    # 相当于 enter
    print('....fore....')
    yield 'return msg'
    # 相当于 exit
    print('....after....')


def main2():
    with method2() as x:
        print(x)


if __name__ == '__main__':
    print('-------------method1-------------')
    main()
    print('-------------method2-------------')
    main2()
