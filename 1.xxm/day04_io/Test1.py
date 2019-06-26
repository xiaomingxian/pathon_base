# 读取的是同目录下的文件
file = open("__init__.py", 'a')
# x = file.read()
file.write("zhuijia")
# print(x)
file.close()

# 文件指针
# open("文件","打开方式")#默认只读
# w覆盖,a追加
# w+,r+,a+.....都有写入操作
f = open("writeTest.py", 'a')
f.write("#aaa\n")

# readLine
ff=open("writeTest.py",'r')
while True:

    txt=ff.readline()
    if not txt:
        break
    print(txt)

ff.close()
# 文件的复制

open(f,'r')

import os
fi=file("writeTest")
os.remove(fi)

