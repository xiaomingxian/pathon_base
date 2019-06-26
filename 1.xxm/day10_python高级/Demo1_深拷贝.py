# c是深拷贝
a = ['aaa']
b = a
print(id(a))
print(id(b))

import copy

# 对只读类型不管用----
c = copy.deepcopy(a)
d = copy.copy(a)
print(id(c))
print(id(d))
print('a is b?', a is b)
print('a is c?', a is c)
print('a is d?', a is d)

print('----------------- copy and deepcopy --------------------')
list1 = [1, 2]
list2 = [2, 3]
list3 = [list1, list2]
co = copy.copy(list3)
dc = copy.deepcopy(list3)
print('copy()内部元素是否深拷贝', '\t不是' if (co[0] is list1) else '\t是')  # 内部元素还是浅拷贝----类似于java的clone接口
print('deepcopy()内部元素是否深拷贝', '\t不是' if (dc[0] is list1) else '\t是')
list3.append(['o', 't'])
print(list3)
print(co)  # copy实现的是表面深拷贝


def change(list):
    # list[0]=9
    list = [4, 4, 4, ]
    pass


change(list1)
print(list1)

print("------------------- 元组测试  --------------")
l1 = [1, 2]
y1 = (2, 3, l1)
cy = copy.copy(y1)
print(id(y1), id(cy))
print(y1 == cy)

dcy = copy.deepcopy(y1)

print(id(y1), id(dcy))

print('-------------------- other ---------------')
x = [1, 2]
yz = [x, 2]
cc = yz[:]
print(cc)
print(id(cc), id(yz))
# 切片是浅拷贝
print(id(yz[0]), id(cc[0]))
# 切片
# https://blog.csdn.net/xpresslink/article/details/77727507

print('------------字典（与java中的map相同 元素的位置也是key的哈希）  同样适用于以上拷贝结论 -----------')

dic = {'a': x, 'b': 2}
dic2 = copy.copy(dic)
#
print('copy:', id(dic), id(dic2), '   内部元素：', id(dic['a']), id(dic2['a']))
dic3 = copy.deepcopy(dic)
print('deepcopy:', id(dic), id(dic3), '   内部元素：', id(dic['a']), id(dic3['a']))
