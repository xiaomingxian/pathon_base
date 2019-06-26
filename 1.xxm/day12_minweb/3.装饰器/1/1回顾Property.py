class Lei(object):
    def __init__(self):
        pass

    def getNum(self):
        print('...get...')

    def setNum(self, num):
        print('...set...')

    def delNum(self):
        print('...del...')

    def desc(self):
        print('...desc...')

    pro = property(getNum, setNum, delNum, desc)


class sx(object):
    def __init__(self):
        self.num2 = 1
        pass

    @property
    def num(self):
        print('---------get')
        return self.num2
        pass

    @num.setter
    def num(self, val):
        print('---------set')
        self.num2 = val

    @num.deleter
    def num(self):
        print('---------del')
        self.num2


class dic(object):
    def __init__(self):
        pass

    def __setitem__(self, key, value):
        pass

    def __getitem__(self, item):
        pass

    def __delitem__(self, key):
        pass


def LeiTest():
    lei = Lei()
    lei.pro
    lei.pro = 'xxx'
    del (lei.pro)
    Lei().pro.__doc__


def shuxing():
    # t = test()
    # t.num = 10
    # print(t.num)
    #
    # del t.num
    # 函数名和 变量名不能一样？？？
    s = sx()
    s.num = 10
    print(s.num)
    pass


def main():
    print('-----类测试-----')
    LeiTest()
    print('-----属性测试-----')
    shuxing()
    pass


if __name__ == '__main__':
    main()
