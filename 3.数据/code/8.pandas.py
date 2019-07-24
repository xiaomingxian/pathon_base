import pandas as pd
import string
import numpy as np


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


# 二维
def erwei():
    # 第一列：行索引  第一行：column
    data = pd.DataFrame(np.arange(12).reshape(3, 4))
    print(data)
    # 指定索引
    data2 = pd.DataFrame(np.arange(12, 24).reshape(3, 4), index=list('abc'), columns=list('ABCD'))
    print(data2)
    print('*' * 30, '字典作为数据')
    # 一条数据是一行  数据量得对上否则报错(eg:name2个,age3个会报错)
    zd = {'name': ['jerry', 'tom'], 'age': [10, 11]}
    zds = pd.DataFrame(zd)
    print(zds)
    #  数组形式  对不上的数据为Nan
    d = [{'name': 'tom', 'age': 20, 'address': 'america'}, {'name': 'jerry', 'age': 20},
         {'address': 'China', 'name': 'JackChen'}]
    ds = pd.DataFrame(d)
    print(ds)

    print('行索引：', ds.index)
    print('列索引：', ds.columns)
    print('数据类型：', ds.dtypes)
    print('数据形状：', ds.shape)
    print('数据维度：', ds.ndim)
    print('数据的前1行', ds.head(1))
    print('数据的后一行：', ds.tail(1))
    print('相关信息概览：', ds.info())
    print('快速综合统计结果：\n', ds.describe())

    pass


# 索引和切片
def indexAndSlice():
    # []里是数字取的是行，里是数字取的是列
    datas = pd.DataFrame(np.arange(0, 100).reshape(50, 2), columns=['c1', 'c2'])
    print('取前10行的第一列:\n', datas[:10]['c1'])
    print('一列的数据类型是Serices:', type(datas[:10]['c1']))

    # loc['行'，'列']
    print('loc:', datas.loc[1, 'c1'])
    print('loc多列：\n', datas.loc[:, :'c2'].head(5))  # datas.loc[:, 'c1','c2']
    print('loc多行：\n', datas.loc[:3, :])  # datas.loc[:3] 列可以省略
    # iloc[行索引,列索引]
    print('iloc', datas.iloc[1, 1])
    print('iloc', datas.iloc[:5, :1])
    # 赋值 可以直接赋值Nan
    datas.iloc[[1, 2], :2] = np.NaN
    print('赋值后的结果：\n', datas.iloc[:5])
    print('boolean索引：\n', datas[datas['c1'] > 90])
    a = 11
    print('python-boolean连写：', 10 < a < 20)
    print('padans-boolean没有连写得用&连接：\n', datas[(datas['c1'] > 80) & (datas['c2'] < 90)])
    # pandas字符串api-略
    #
    print(pd.isnull(datas[1:5]))
    print(pd.notnull(datas[1:5]))
    print(datas[pd.notnull(datas['c1'])].head(5))
    print('*' * 100)
    # 删除nan相关
    # datas=datas.dropna(axis=0)
    # how默认为all(全部为nan的才删)
    # inplace是否原地替换 eg:a=a.xxx(..) inplcae=True时a操作后自己直接改变不需要再用变量接受
    # datas = datas.dropna(axis=0, how='any', inplace=False)

    # 填充nan---也可以针对某一列进行操作 a['c1'].fillna(xxx)
    datas = datas.fillna(datas.mean())  # 填充均值
    print(datas[:5])
    # pandas计算时会自动跳过nan
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

    print('*' * 50, 'dogName排序', '*' * 50)
    dogs = pd.read_csv('../result/dogName.csv')
    dos = pd.DataFrame(dogs)
    dos = dos.sort_values(by='count', ascending=False)
    print('按大到小排序取前5：\n', dos.head(5))
    pass


if __name__ == '__main__':
    # base()
    # other()
    # erwei()
    indexAndSlice()
