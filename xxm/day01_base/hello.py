# # encoding:utf-8
# python2.0项目
# print"你好"
# print"------"
#
# # 素数:1和本事
# su = 2
# while su <= 100:
#     ch = 2
#     # 当除数小于商时
#     while ch <= su / ch:
#         if not (su % ch): break  # 被整除的情况
#         ch += 1
#     if ch > su / ch:  # 直到  还没有一个被整除
#         print su, "是素数"
#     su += 1
# #     4 1(1<4) 2(2<=2) 3(3>1) 4(4>1)
# #     5 1(1<5) 2(2<=2) 3(3>1) 4(4>1) 5(5>1)
#
# print "------------------MyMethod----------------------"
# ss = 2
# while ss <= 100:
#     cc = 2
#     while cc < ss:
#         if ss % cc == 0: break  # 整除，不是被本身
#         cc += 1
#     if cc == ss:
#         print ss, "是素数"
#     ss += 1
#
# print "---------------format---------------"
# str = "jjjkkkku"
# print str[2:5]
#
# # 更改字符串
# print str[:4] + "-python"
# # 原始字符串r开头
# print r"//\""  # 转义符也会输出原始的内容
# print "//\""
# # 格式化  各种格式化：查表
# # 传统
# print "my name is %s and wight is %f kg" % ("tom", 60.5)
# #
# print "my name is{} age{}".format("Tom", 20)
# print "my name is{0} age{0},{1}".format("Tom", 20)
# li = ['Jerry', 22]
# print "my name is {} age {}".format(*li)
# print "my name is {} age {}".format(li[0], li[1])
# # 字典传值---属性得对上
# dic = {'name': "Bluce", 'age': '23'}
# print "myname is {name} age is {age}".format(**dic)
# # '''复制
# s = '''copy content'''
# print "--------内建函数--------"
# print s.capitalize()
# print s.center(20)
#
# # 字符串依然是只读
# str2 = "teeeest"
# print str2.capitalize()
# print str2
# #
# print str2.count("e", 0, len(str))
# # 解码
# print str2.decode('gbk', 'strict')
# # 编码
# str2.encode('UTF-8', 'strict')
# print str2.endswith("est", 0, len(str2))
# # 扩展命令---默认的扩展值是8
# str3 = "iPho\tn\te"
# print str3
# str4 = str3.expandtabs(8)
# print str4
# # 检验是否存在:存在返回1 否则是-1
# # print (str2.find("ee", 0, len(str2),"")
# # 与find不同的地方:找不到会报异常
# print str2.index("e", 0, len(str2))
# # 数字和字母返回true
# str5 = "你好sth4jjj"
# print str2.isalnum()
# print str5.isalnum()
# # 全是字母
# print str2.isalpha()
# print str5.isalpha()
# # 十进制数字
# str6 = u"11111"
# # print str2.isdecimal()
# print"只适用于unicode字符串：", str6.isdecimal()
# # 只包含数字 unicode和普通字符串都适用
# str7 = "11111"
# print str6.isdigit()
# print str7.isdigit()
# print str2.isdigit()
# print"是否是小写：", str2.islower()
# print"是否只包含数字(unicode使用):", u"111".isnumeric()
# print"是否全部为空格:", " ".isspace()
# print"是否为标题（每个单词首字母大写）：", "This Is Title".istitle()
# print"是否为标题：", "this Is title".istitle()
# print"是否全部为大写:", "HHHH".isupper()
# print"合并", "My name is".join("k-l-")
#
# print "---------------------"
# # 99乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print"{}x{}={}\t".format(i, j, i * j),
#     print''
# print "------函数-------"
#
#
# def table(k):
#     for i in range(1, k + 1):
#         for j in range(1, i + 1):
#             print"{}x{}={}\t".format(i, j, i * j),
#         print''
#
#
# table(5)
