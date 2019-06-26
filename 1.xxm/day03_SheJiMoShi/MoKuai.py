import random

# import xxm.day03_SheJiMoShi.Single as single
#
print("查看位置:%s" % random.__file__)
x = random.randint(0, 10)
print(x)
#
# print(single.Music.chushi)

# 局部导入:
# from xxm.day02_oop.JiCheng import T2
# T2().say()


print("--------------------")
# 全部导入:

# print(title)
# print(Dog())
# method1()

# 开发原则：所有模块都应该被导入
# 没有任何缩进的部分都会被执行一遍
# __name__  测试代码
