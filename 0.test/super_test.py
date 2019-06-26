class Fu():
    @classmethod
    def m1(cls):
        super(Fu, cls).sout('---fu[第一个继承的父类]')

    pass


class Fu2():

    def sout(x):
        print('--- 输出测试 ---', x)


class Son1(Fu, Fu2):
    @classmethod
    def mm1(cls):
        super(Son1, cls).sout('xx')
        super(Son1, cls).m1()

    pass


def main():
    s1 = Son1()
    s1.mm1()
    print(Son1.__mro__)


if __name__ == '__main__':
    main()
