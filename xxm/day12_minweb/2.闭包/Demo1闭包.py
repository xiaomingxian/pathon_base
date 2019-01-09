class Outu(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, *args, **kwargs):
        print(self.a * self.b + args[0])


def out(x, y):
    def iner(z):
        print(x * y + z)
        pass

    return iner


def main():
    print('----数学中的函数计算 耗费资源少的情况下 改变参数:bibao-----')
    print('--------类------------')
    # out = Outu(2, 3)
    # out(3)
    print('-------bibao----------')
    o = out(2, 3)
    o(2)


if __name__ == '__main__':
    main()
