# range(10)   --python2保存的是生成的值 --->python3中已经相当于 xrange() ---->减少对内存的消耗
# xrange(10)  --保存的是生成方式
#
class FieBoNaCi(object):

    def __init__(self):
        self.a = 0
        self.b = 1
        self.cou = 0
        pass

    def __iter__(self):
        return self

    def __next__(self):
        if self.cou <= 10:
            self.a, self.b = self.b, self.a + self.b
            self.cou += 1
            return self.a

        else:
            raise StopIteration


for i in FieBoNaCi():
    print(i)

print("---------------------------------other:类型转换(定义空列表，迭代取值填入)------------------------")
print("---------------------------------other------------------------")
import datetime

s = datetime.datetime.now()
# 输出x*2在10000000以内-----得到值
nums = [x * 2 for x in range(10000000)]
e = datetime.datetime.now()
print(e - s)  # 0:00:01.053060
# print(nums)
s2 = datetime.datetime.now()
# 生成器
nums2 = (x * 2 for x in range(10000000))
e2 = datetime.datetime.now()  # 0:00:00
print(nums2)
print(e2 - s2)
