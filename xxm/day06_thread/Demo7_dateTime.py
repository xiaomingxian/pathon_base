import datetime

t = datetime.datetime.now()
print(t)

for i in range(200000000):
    i += 1;

e = datetime.datetime.now()
print(e)
print((e - t).seconds)
# 测试--执行22秒
