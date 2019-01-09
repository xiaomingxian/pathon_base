ai = "sss"
# 查看地制值
print(id(ai))

dic = {'k1': 'v1'}
print(id(dic['k1']))
print(id(dic))
dic['k1'] = 'bb'
print(id(dic['k1']))
print(id(dic))

# hash值只能记录不可变类型
print("元组hash值:", hash(()))


# print(hash([]))

def a():
    # 对全局变量的修改---再碰到同名的就不要创建 局部变量了
    global ai
    ai = 'kkk'
    aa = 1;
    aa = 2
    print(aa)


a()
print(ai)

g1, g2 = (1, 2)
print(g1, g2)
print('----交换数值----')
a = 1;
b = 2
# method1
a = a + b
b = a - b
a = a - b
print(a, b)
# method2
a, b = (b, a)
print(a, b)
# 当函数返回元组时()可以省略
c, d = 3, 4
print(c, d)
# --------------------
# 不可变类型  不会发生改变--可变类型会发生改变(根据地制值改变)
num = 10
list = [1, 2]
list2=[]


def ch():
    num = 100
    list[0] = 3
    print(list)


ch()
print(num)
print(list)


def ch2(mlist):
    mlist=[1,2]

ch2(list2)
print(list2)