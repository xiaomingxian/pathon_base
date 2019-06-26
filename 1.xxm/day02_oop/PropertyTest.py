# 调用函数像获取值调用属性一样  可读性更强



class test(object):

    def __init__(self):
        self.num2 = 1

    @property
    def num(self):
        return self.num2
        pass

    @num.setter
    def num(self, value):
        print('setter方法...')
        self.num2 = value
        pass

    @num.deleter
    def num(self):
        print('deleter方法...')
        del self.num2
        pass


# 类形式
class LeiTest(object):

    def __init__(self):
        self.num = None

    def getNum(self):
        print('属性值获取...')
        return self.num

    def setNum(self, value):
        print('属性赋值')
        self.num = value

    def delNum(self):
        print("删除属性执行")

    def desc(self):
        print("属性描述...")

    BAR = property(getNum, setNum, delNum, desc)

    # | property(fget=None, fset=None, fdel=None, doc=None) -> property
    pass


def main():
    # 加括号-- 定义-时多写参数都是错误的(只能写self)
    t = test()
    t.num = 10
    print(t.num)

    del t.num
    # 直接删除对象属性
    # print(t.num)


def leiTest():
    lei = LeiTest()
    # setter
    lei.BAR = 20
    # get
    print('获取：', lei.BAR)
    # desc
    LeiTest.BAR.__doc__
    # 删除---删除不掉？？
    del lei.BAR
    print(lei.BAR)


if __name__ == '__main__':
    print('-----------------method1 对象属性(函数)装时器 ------------- ')
    main()
    print('-----------------method2 类属性 ------------- ')
    leiTest()
