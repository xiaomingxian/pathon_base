class ZS(object):
    def __init__(self, fun):
        print('init:', fun)
        self.fun = fun
        pass

    def __call__(self, *args, **kwargs):
        print("args:", args)
        print('--callback--')
        return self.fun()


@ZS
def test():
    print('test')
    return "xxx"


def test2():
    print('test2')
    return "xxx2"


if __name__ == '__main__':
    # 函数的引用指向了类
    print(test())

    print('----------...--------------')
    # 相当于--test上不加@ZS
    zs = ZS(test2)
    test2 = zs
    test2()
    # 类实例(xxx)只为__call__传参
