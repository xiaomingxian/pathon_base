def out(fun):
    print('...装饰器1')

    # 有参数
    def inner(*args, **kwargs):
        print('------增强1------')
        # 有返回值
        return fun(*args, **kwargs)

    return inner


def out2(fun):
    print('...装饰器2')

    # 有参数
    def inner(*args, **kwargs):
        print('------增强2------')

        # 有返回值
        return fun(*args, **kwargs)

    return inner


def out3(fun):
    print('...装饰器3')

    # 有参数
    def inner(*args, **kwargs):
        print('------增强3------')

        # 有返回值
        return fun(*args, **kwargs)

    return inner


# 装饰器执行 标有@XXX装饰器就执行  @out发现下面还有装饰器 就先执行下面的
# 闭包内部函数  @out3  test-->out3inner[fun-->test1原]
#             @out2  test-->out2inner[fun-->【test-->out3inner[fun-->test1原]】]
# 最终         @out   test-->outinner[fun-->【test-->out2inner[fun-->【test-->out3inner[fun-->test1原]】] 】]
# 执行顺序:   outinner --> out2inner --> out3inner
# 从下到上  层层指向  改变


# eg:董事长-->总经理--->员工

#
@out
@out2
@out3
def test(num):
    print("====>test %s" % str(num))
    return num


# @out
# def test2():
#     print('lllll')


def main():
    print(test(10))
    # print(test2())


if __name__ == '__main__':
    main()
