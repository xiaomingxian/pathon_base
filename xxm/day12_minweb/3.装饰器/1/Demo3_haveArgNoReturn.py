def out(fun):
    print('-----装饰器开始执行-----')

    def inner(a):
        print("---------校验1----------")
        print("---------校验2----------")
        fun(a)

    return inner


@out
def test1(num):
    print('------test1-----------%s' % str(num))


def main():
    test1(10)


if __name__ == '__main__':
    # main()
    # 装时器执行时机  @out
    pass
