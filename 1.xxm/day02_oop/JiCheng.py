# class Parent:
#     def __init__(self):
#         self.__name = "tom"
#
#     def say(self):
#         print("parent..." + self.__name)
#
#
# class Son(Parent):
#     def say(self):
#         super().say()
#         # 调用父类方法2
#         Parent.say(self)
#
#
# # 子类不能访问父类的私有属性
# Son().say()
# print(Parent()._Parent__name)

class Tool:
    count = 0

    def __init__(self):
        pass


tool = Tool()


# 多继承
class Dad:
    def __init__(self):
        tool.count += 1
        print("dad:", tool.count)

    def say(self):
        print("dad say ...")


class Mon:
    def __init__(self):
        tool.count += 1
        print("mom:", tool.count)

    def say(self):
        print("Mom say ...")


class Son2(Dad, Mon):
    def __init__(self):
        super().__init__()
        tool.count += 1
        print("son:", tool.count)

    pass


class Son3:
    def __init__(self):
        tool.count += 1


# 尽量避免同名方法---
Son2().say()
# print(dir(Son2()))
print(Son2.__mro__)
# print(tool.count)
print(Tool.count)


class T2:
    c = 0

    def __init__(self):
        T2.c += 1

    def say(self):
        print("模块测试")


t1 = T2()
t2 = T2()
t3 = T2()
# print(T2.c)
tool.count = 99
print(t1.c)
print("对象属性:%d" % tool.count)
print("类属性:%d" % Tool.count)
# 对象名.类属性--->不会对类属性作改变只会对对象的属性作改变----而使用类名会
