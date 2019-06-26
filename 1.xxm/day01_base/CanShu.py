# 数字和字符串的+=是赋值操作
# list之类的时extend操作
list1 = [1, 2, 3]


def test1(c):
    # list+=实际上是extend
    c += [4, 5]


test1(list1)
print(list1)

list2 = [1, 1]


def test2():
    global list2
    list2 += [2, 2]


test2()
print(list2)

print("")


def moren(sex, name='k', age=True):
    """

    缺省参数：有缺省值的参数必须在最后面
    :param name:
    :param age:
    :return:
    """
    print(name, age)


moren('nv')
print('----------------------')


# 多值参数
# *变量-->可接收元组   *args
# **变量-->可接收字典  **kwargs

def demo(arg, *args, **kwargs):
    """

    :param args:
    :param kwargs:
    :return:
    """
    print(arg)
    print(args)
    print(kwargs)


demo(1, 2, 3, 4, name='tom', age=18)


def sum_num(*args):
    num = 0
    for i in args:
        num += i
    return num


print(sum_num(1, 2, 3, 4))


# 递归
def digui(num):
    if num == 1:
        return 1
    else:
        return num + digui(num - 1)


print(digui(3))

# dir查看对象属性或方法
print(dir(len))
