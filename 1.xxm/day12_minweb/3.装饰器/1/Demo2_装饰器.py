# 持有原函数的引用  再对它加额外功能  同理与 java中的 装饰者模式
def out(fun):
    def inner():
        print("-----检验1------")
        print("-----检验2------")
        fun()

    return inner


# @out
# def test1():
#     print('-----test1-----')


def test1():
    print('-----test1-----')


def main():
    # @out
    test1()


if __name__ == '__main__':
    # 装饰者模式
    # main()
    # 相当于将函数引用传递给闭包  对它做功能增强后  再赋值给同名的引用
    test1 = out(test1)
    test1()
