import re
import datetime


# t = datetime.datetime.now()
# m = re.match('yyyy-dd-MM HH:mm:ss', str(t))
# print(m)
#
# m2 = re.match('[1-9]', '743')
# print(m2.group())  # 匹配到的结果
# print(re.match('lll[1-9]', 'lll3').group())
# # print(re.match('lll[1-9]', 'lll').group())  # 'NoneType' object has no attribute 'group'
#
# # \d数字
# # [1-36-8]
# # 数字字母[1-5Abc][0-9a-zA-Z]
# print(re.match('[0-9a-zA-Z]*', '1W').group())
#
# # \w  数字字母下划线  支持其他语言(eg：中文)
# print(re.match('\w*', 'sas').group())
#
# # \s 空格
# print('空格或tab匹配(没有内容)', re.match('\s', '       tab/space').group())
#
# # 大写与小写相反   \w字符 \W非字符
# print(re.match('\W*', '&*').group())
# print(re.match('\D', 'l').group())
# print(re.match('\S', 'l').group())
#
# print('点:', re.match('.', '.').group())
#
# # 多位限制
# print(re.match('\w{1,4}', 'wwwwwww').group())
# # 固定位数--得连续
# # print(re.match('\d{7}', '11 1111 111 222').group())
#
# # ?前面的东西可有可无   要么有一个   要么没有
# print(re.match('a-?x', 'a-x'))
#
# regx = '[1-9][0-9]{5,10}@qq.com'
# print(re.match(regx, '44512546@qq.com'))
#
# # .不能匹配到  \n  ----加上re.S可以匹配所
# print(re.match(r'.*', 'jjlljl\nasdasd', re.S))
#
# # +至少一个
# print(re.match('9+', ''))
#
# # 变量名匹配
# reg = '[_a-zA-z]+[_a-zA-z0-9]*'
# print('匹配变量名:', re.match(reg, '_asa31sdvds33'))
#
# # 加上结尾判断(正则表达式 后加 $)   ---python中match只判断开头  ---
# # 开头判断^
# print(re.match('assas$', 'ass'))
#
# print(re.match('^ska$','ska'))


def mailTest():
    # ()分组   ----  # 或  (xxx|xxxx|xxx|...)---可以这样取值下标从1开始-->group(1/2/3/...)
    regxmail = '^([a-zA-Z0-9]+)@(qq|163|sina)+\.com+$'
    # regxmail='^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$'
    while True:
        mail = input('mail:')
        if re.match(regxmail, mail):
            print('OK')
            print(re.match(regxmail, mail).group(1) + re.match(regxmail, mail).group(2))

        else:
            print("False")


def getGroupValueInRegx():
    # regxg='<(h[1-7])>.*</\1>'#为啥不管用
    regxg = '^<(?P<p1>h[1-7])>.*</(?P=p1)>$'
    s1 = "<h1>khkjhk</h1>"
    s2 = "<h1>khkjhk</h2>"

    print(re.match(regxg, s1))
    print(re.match(regxg, s2))


def hanshu(x):
    return str(int(x.group()) + 10)


def pythonOnly():
    print(re.search("\d+", 'jkjk1111jkhkj999'))
    print(re.findall("\d+", 'jkjk1111jkhkj999'))
    # sub替换
    print('hhh:', re.sub('\d+', '替换', 'py-845481'))

    print(re.sub('\d+', '替换', 'py-788451 pc=481515'))

    # sub支持函数调用
    # 传过去是字符串  ---- 得到的返回值也是str
    print(re.sub('\d+', hanshu, 'kkk-77'))
    # split
    print(re.split(':| ', 'asa:sas saas kkk'))
    # 字符串的方式
    print('saas :asa:kkk'.split(':'))
    # 数据清晰
    ss = '<div class="">海南房产信息网,海南<font color="#CC0000">东方</font>房产信息,房源,<font color="#CC0000">房价</font>,优惠信息等实时更新.<font color="#CC0000">东方</font>最新<font color="#CC0000">房价</font> 精选房源,动态优惠更新.24小时接送机,全程接送看房<font size="-1" style="margin-left:10px;"></font></div>'
    print(re.sub(r'(<\w*>+|</\w*>+)', ' ', ss))
    print(re.split('^<[a-zA-Z0-9]*\s>$', ss))
    pass


if __name__ == '__main__':
    # mailTest()
    # getGroupValueInRegx()
    pythonOnly()

    pass
