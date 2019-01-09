class A(object):
    pass

print(A().__class__)
# 代码是不变的  数据在变化   代码是公用的  使用__class__来找到公用的代码