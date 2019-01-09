import imp

print("你好")
print("你好", end="")
print("---------------")


# 函数
def num(x):
    for i in range(1, x + 1):
        for j in range(1, i + 1):
            print("{}x{}={}\t".format(j, i, i * j), end='')
        print('')


# 调用
num(9)

"""
多行注释
。。。。
。。。。
。。。。
# """

# 算数运算符
# print(9 / 2)
# print("取整：", 9 // 2)
# print("取模:", 9 % 2)
# print("幂:", 2 ** 3)
# print("-" * 50)
# print("Hello Python " * 50)
# CPU  内存   硬盘(转数)
# 程序的核心作用处理数据
# 硬盘-->内存-->CPU
# print(type("lll"), end='')
# print(type(1))
# print(type(2 ** 32))
# print(type(2 ** 64))
# 3.0中将long和int整合为int--没有long型
# print(type(2 ** 1000))  # 在其他语言中计算这个数字比较耗时
# print(True - 1)  # True 1 False 0
# print("-键盘录入--")
# 类型全是str
# i=input("writen somthing:")
# print(type(i))
# print(type(int(i)))0
# print(type(float(int(i))))
# print("--------------")
# num=input("苹果的数量:")
# price=input("价格:")
# print(int(num)*float(price))

# print("数量 %f 价格 %f "%(float(input("数量:")),float(input("价格"))))
# print("%d" % 2)
# %s,表示格式化一个对象为字符
# %d,整数
# print("小数后显示几位 %.2f%%" % 1)  # %只能用%转译 不能用
# print("-%.2f%%" % (2 * 2))
# import time
#
# now = time.time()
# print(now)

# 石头剪刀布
# import random
#
# rlist = ['石头', '剪刀', '布']
# winlist = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
# g = True
# while g:
#     uchoice = input("请输入你的选择：")
#     if uchoice not in '012':
#         print("输入错误")
#     else:
#         cnum = random.choice(rlist)
#         print('you:' + rlist[int(uchoice)], "com:" + cnum)
#         if [rlist[int(uchoice)], cnum] in winlist:
#             print("YOU WIN")
#         elif rlist[int(uchoice)] == cnum:
#             print("平局")
#         else:
#             print("YOU LOSE")
#     gg = input("还玩吗Y/N:")
#     if gg == 'N' or gg == 'n':
#         break
# 循环计算:
nu = 1
sum = 0
while nu <= 100:
    sum += nu
    nu += 1

print(sum)
# 循环小星星
for h in range(5):
    for l in range(h):
        print('*  ', end='')
    print('')

for x in range(5):
    for y in range(5):
        if x <= y:
            print("*  ", end='')
        else:
            print('   ', end='')
    print('')


# import hello
# 函数注释---以下
def test(a, b):
    """
    kkkk
    :a: char
    """
    print("test")
    result = "result"
    return result


print(test(1, 2))

print("------变量类型-------")
myList = [1, 2, 3]
print(type(myList[0]))
myList[1] = 'k'
print(myList)
del (myList[1])  # 改
print(myList)  # 删
print('索引', myList.index(1))
# 增加数据
myList.append('aaa')
print(myList)
# 指定位置
myList.insert(1, 'insert')
print(myList)
#
myList.extend(['HELLO', 'WORLD'])
myList.extend('exten')  # 会把参数当做list处理
print(myList)
# 删
# myList.clear()
# print(myList.pop(1))
# print(myList.pop())#不指定参数默认删除最后一个
myList.remove('insert')
print(myList)

print("列表中包含 %d 个元素" % myList.__len__())
# print(len(myList))
print("e 出现了 %d 次" % myList.count('e'))
# myList.sort()
myl = [1, 3, 2, 4, 2]
# myl.sort()
# print(myl)
# myl.reverse()
# print(myl)
# myl.sort(reverse=True)
# print(myl)
for i in myList:
    print(i, end=' ')

print()

ll = [1, '2']
print(ll)
# 元组
to = ()
print(to)
print(type(to))
tt = (3,)
# 没有逗号为int
print(type(tt))
# del(tt[0])
# print(tt)
print(tt.count(3))
print(tt.__len__())

for j in (1, 2, 3):
    print(j, end='  ')
print()

print("%s %d" % ('tom', 10))
# tl = tuple(myList)
# print(type(tl))
# print(type(list(tt)))

# 列表有序  字典无序
dic = {'k1': 'v1', 'k2': 'v2'}
# 类似于并发修改
# for i in dic.keys():
#     del(dic[i])
dic.pop('k1')
print(dic)

# dic.clear()
# 合并
dic2 = {'k3': 'v3', 'k4': 'v4'}
dic.update(dic2)
print(dic)

# 遍历的是key是无序的----有默认的排序方式
for kv in dic:
    print(kv, end="   ")

myList.append(dic)
print(myList)
print("-------string------")
strb = 'hellohellohello'
strs = "hello"
print(strb.count(strs))
print(strb.index(strs))
#
print("aaaa\rm")  # 回车--回到行首
print("mmm\nllll")  # 换行
print(" \t\r\n".isspace())
# 判断字符串是否只包含数字
# 从小到达  都不能判断小数decimal --digit--numeric
print('------')
print("\u00b211".isnumeric())
print('\u00b222'.isdigit())  # 特殊数字字符和中文数字
print('一百'.isnumeric())
print('\u00b2'.isdecimal())  # false
print('----other----')
print('aaa'.replace('a', 'b', 1))  # old new count  ---会返回新值 原来的字符串不会改变
print('aaa'.find('aa'))
print(''.find('ccc'))  # 不存在会返回 -1
# print(''.index('c'))#不存在会报错
print('aaav'.endswith('v'))
# r开头--从右边开始
print('aac'.rindex('c'))
print('abc'.rfind('c'))
print("文本对齐")
print('aaa'.center(10))
poem = ['登鹳雀楼   ', '王之涣   ', '   白日依山尽', '黄河入海流', '欲穷千里目', '更上一层楼']
for i in poem:
    print('|%s|' % i.strip().center(10, " "))

# 去除空白字符---前后的空白字符
print('     n n    '.strip())
x = 'a  c c v c'.split(' ')
print('s'.join(x))  # 将s作为分隔符进行拼接
print('j'.join(dic))  # 只对dic的key进行操作？？？
poemstr = '登鹳雀楼\t 王之涣\n 白日依山尽\t 黄河入海流    欲穷千里目     更上一层楼   '
lpoem = poemstr.strip().split()
print(lpoem)
for i in lpoem:
    print(i.center(10))

print('0123456'[1::2])  # 开始索引，结束索引，步长
print('jkl'[:-1])  # 不包含最后一个
print('123456'[-2:])
print('jkc'[-1::-1])  # 向回切片
print('abc'[::-1])

# print('公共方法---内置函数------')
# len
# del
# max
# min
# cmp  比较  python3已经取消  <  >  可以使用符号
# 字典不能切片 ---- 原因没有索引---字符串  列表  元组 可以切片
# *n 不能对dic使用  dic中的key是唯一的

# append和extend的区别--- append将元素整体追加------extend将元素打撒进行追+
rl = [1, 2]
# rl.extend('kkkk')
rl.append('llll')
print(rl)

for i in range(5):
    if i == 3:
        # break
        pass
    else:
        print(i)
else:
    print("for elseu")


lll=[1,2,3]
for i in lll:
    print(i)