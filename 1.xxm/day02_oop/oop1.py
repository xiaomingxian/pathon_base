class Animal:
    def __init__(self):
        self.name = 'tom'
        self.age = 10  # 必须得给值？？
        print("静态方法")

    def eat(self):
        print("cat eat ...", self)


Animal().eat()
# print('地址： %x' % id(Animal()))
# print('地址： %d' % id(Animal()))
# print('地址： %s' % id(Animal()))

o1 = Animal()
# o1.name = 'tom'
# o1.eat()
# print(o1.__init__())  # 分配空间  --设置初始值---相当于java中的静态--创建对象时自动调用

# print(o1)
print(o1.name)

print("------可赋值属性-------")


class o2:
    def __init__(self, name):
        self.name = name

    def test(self):
        print(self.name)

    def __del__(self):
        print("del")

    def __str__(self):
        return "str..."


print(o2('tom').name)
print(o2('2'))



