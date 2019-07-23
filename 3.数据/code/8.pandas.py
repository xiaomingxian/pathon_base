import pandas as pd
import string


# pandas与numpy的区别

# pandas常用数据类型
# Series一维，带标签数组
# DataFrame 二维,Series容器

def base():
    # 默认索引
    ser = pd.Series([12, 23, 34, 45, 56])
    print(ser)  # 索引/标签  数据
    # 指定索引(索引数量得与数据数量相同)
    se2 = pd.Series([11, 22, 33, 44, 55], index=list('abcde'))
    print(se2)
    # 字典类型-key是索引,val是值
    dict_data = {'name': 'tom', 'age': 20, 'Home': 'America'}
    se3 = pd.Series(dict_data)
    print(se3)

    print('**' * 20, "切片和索引")
    print('第一行：\n', se3[0])
    print('前三行：\n', se3[:3])
    print('后几行：\n', se3[2:])
    print('某几行：\n', se3[[0, 2]])
    print('根据key取：\n', se3[['name', 'age']])
    print('boolean索引：\n', ser[ser > 10])
    print('取出索引：', se3.index)  # 可使用len() list()进行转换
    print('取出值：', se3.values)
    # where 略
    print('*' * 50, '读取外部数据很多')
    ukdata = pd.read_csv('../result/uk.csv')
    print(ukdata)
    # 从剪切板读取内容
    cldata = pd.read_clipboard()
    print(cldata)
    # 也可以读 mysql,json等mongodb等
    pass


def other():
    # for i in range(26):
    # A-Z 下标 0-25
    #     print(string.ascii_uppercase[i])
    code = {string.ascii_uppercase[i]: i for i in range(26)}
    codearr = pd.Series(code)
    print(codearr)

    # key:abcdefghij val:0123456789
    code_little = {string.ascii_uppercase[i]: i for i in range(10)}
    # 此处的key f-0 与code_little只有部分重叠 没有重叠的部分val为nan
    havenan = pd.Series(code_little, index=list(string.ascii_uppercase[5:15]))
    print(havenan)
    pass


if __name__ == '__main__':
    base()
    # other()
