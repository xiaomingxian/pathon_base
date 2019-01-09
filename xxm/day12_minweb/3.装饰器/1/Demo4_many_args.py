def out(fun):
    def inner(*args, **kwargs):
        print('----装饰器增强1----')
        print('----装饰器增强2----')
        # 参数是 元组和字典
        # fun(args,kwargs)
        # 自动拆包----  将参数保持原状态  而不是  元组/字典
        print('参数：', args, kwargs)
        fun(*args, **kwargs)
        pass

    return inner


# 不传参数也可以
@out
def test(*args, **kwargs):
    print('----test----')


def main():
    test(1, 2, m=3)


if __name__ == '__main__':
    main()
