from collections import Iterable
from collections import Iterator
import time

# 如果一个对象是迭代器，他一定可以迭代
# 如果可以迭代不一定是迭代器（迭代器和类[持有迭代器的引用]分离）

# a = 10
# print(isinstance(a, Iterable))
#
#
# # 自定义迭代器
# class ite(object):
#     def __iter__(self):
# #         pass
#
#     def __next__(self):
#         return 22
#         # pass
#
#
# class Obj:
#     def __iter__(self):
#         return ite()
#
#
# # 必须继承 __iter__(self):
# # 必须返回  一个对象的引用(_iter__(self),__next__(self):)
# print(isinstance(Obj(), Iterable))
# # iter(Obj())--会自动调用Obj类的 __iter__(self)函数--返回的是ite类实例的引用
# ii = iter(Obj())
# print(ii)
# # 验证迭代器
# print("是否是迭代器:", isinstance(ii, Iterator))
# # 迭代器返回值-----自动调用next函数得到返回值
# print(next(ii))
#

# ----------------------------------------案例----------------------------------
print("----------------------------------------method1:迭代器与类分离----------------------------------")


class MyIteror(object):
    def __init__(self, obj):
        self.obj = obj
        self.index = 0

    def __iter__(self):
        pass

    def __next__(self):

        if self.index < len(self.obj.names):
            value = self.obj.names[self.index]
            self.index += 1
        else:
            raise StopIteration

        return value


class Person(object):
    def __init__(self):
        self.names = list()

    def __iter__(self):
        return MyIteror(self)

    def add(self, per):
        self.names.append(per)


p = Person()
p.add("张三")
p.add("李四")
p.add("王五")
# print(p.names)

for name in p:
    print(name)
    # time.sleep(1)

#
print(" ------------------------------------- method2：类综合迭代器 -------------------------------------------")


class Student(object):
    def __init__(self):
        self.names = list()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= self.names.__len__() - 1:
            v = self.names[self.index]

            self.index += 1
        else:
            raise StopIteration

        return v

    def add(self, name):
        self.names.append(name)


stu = Student()
stu.add("张三")
stu.add("李四")
stu.add("王五")

for i in stu:
    print(i)
