import numpy as np

import random


# numpy-api
# https://www.runoob.com/numpy/numpy-tutorial.html


# 数组测试
def shap_test():
    # 一维(x,)
    # 二维(x,x)
    # 三维(x,x,x)
    # ----------- shap==>(行,列) ----------
    array1 = np.arange(12)
    print(array1)
    print(array1.shape)  # 数组的形状：一维数组元素12个(12,)
    array2 = np.array([[1, 2, 3], [4, 3, 5, 3]])
    print(array2)
    print(array2.shape)  # 二维数组 每个里面有三个元素==>(2, 3)，如果每个里面的元素不同那么就只显示二维数组中一维数组的数量==>(2,)

    # ----------- reshap((行,列)) -------------
    # 行列相成得==数组元素数量 否则报错
    array3 = np.arange(12).reshape((3, 4))
    print(array3)
    # 变为一维数组
    # array3=array3.reshape((12,))  # 方式1
    a = array3.flatten()  # 方式2
    # print(array3)
    print(a)

    # --------- 数组与数字计算(会作用到数组的每一个元素上) -----------
    array4 = np.arange(12)
    a4res = array4 + 3
    print(a4res)
    # --------- 数组与数组计算(某一维度[大维度]得对上[行,列]否则报错) ------------
    # shap(3,3,3) 与 shap(3,2)  不能计算
    # shap(3,3,2) 与 shap(3,2)  可以计算
    pass


# numpy 一个在python中做科学计算的基础库,重在数值计算,也是大部分python科学计算的基础库
# 多用在大型 多维数组上执行数值运算
def numpyTest():
    # 创建数组--三种方式
    array1 = np.array([1, 2, 3, 4])
    array2 = np.array(range(1, 6))
    array3 = np.arange(1, 10, 2)  # start,end,步长
    print("类型：", type(array1), " 元素类型：", array1.dtype, array1)
    print(type(array2), array1.dtype, array2)
    print(type(array3), array1.dtype, array3)

    # 创建数组--指定dtype
    array4 = np.array(range(1, 8), dtype=float)
    print(array4.dtype, array4)

    # 调整数据类型
    array5 = np.array([1, 0, 1, 0, 1, 0], dtype=bool)
    print("调整前：", array5.dtype, array5)
    array5_1 = array5.astype('int')
    print("调整后：", array5_1.dtype, array5_1)

    # 随机数  round(random.random(),3)保留3位小数，不指定默认没有小数
    x = [round(random.random(), 3) for i in range(1, 5)]
    print(x)
    pass


# 多维数组的轴
# eg:二维数组 (shape(1,2)) 0,1轴；；三维数组(shape(2,2,3))0,1,2轴
def axis_test():
    # 数组转制
    a1 = np.arange(0, 10).reshape((2, 5))
    # 1-T属性(表示转制)
    # ta1=a1.T
    # 2-指定轴反转 eg:二维数组的0/1轴反转
    # ta1=a1.swapaxes(1,0)
    # 3-转制方法
    ta1 = a1.transpose()
    print(ta1)
    pass


uk = '../result/uk.csv'
us = '../result/us.csv'


# 本地文件读取
def local_file():
    # skiprows跳过某一行从1开始    unpack行列旋转true为列展示
    ukdata = np.loadtxt(uk, delimiter=',', dtype='int', skiprows=1)
    usdata = np.loadtxt(us, delimiter=',', dtype='int', skiprows=1)
    usdata2 = np.loadtxt(us, delimiter=',', dtype='int', skiprows=1, unpack=True)

    print(ukdata)
    print(usdata)
    print('*' * 100)
    print(usdata2)
    pass


# 索引和切片
def index_slice():
    # 4行5列
    array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]).reshape((4, 5))
    # 取行
    print('*' * 30, '取某一行', '*' * 30)
    print(array1[0])  # 取第一行
    print('*' * 30, '取连续的行', '*' * 30)
    print(array1[2:])  # 不包含2-取2,3索引(即3，4行数据)
    print('*' * 30, '取不连续的行', '*' * 30)
    print(array1[[2, 3]])  # 取不连续的行
    print('*' * 30, '取列', '*' * 30)
    print(array1[:, 3])  # 第4列
    print('*' * 30, '取连续的列', '*' * 30)
    print(array1[:, 3:])  # 从第四列往后
    print('*' * 30, '取不连续的列', '*' * 30)
    print(array1[:, [1, 2, 4]])  # 每一行的3列
    print('*' * 30, '行列-定位到一个元素', '*' * 30)
    print(array1[3, 2])
    print('*' * 30, '取多行多列', '*' * 30)
    print(array1[[1, 2, 3], [2, 3, 4]])  # 2,3,4行-3,4,5列
    print(array1[2:4, 3:5])  # 连续列取值

    # print(array1[2:4, 3:5:2])  # 也可以加步长 行列都适用


def ohter():
    array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]).reshape((4, 5))
    array1[:, 2:4] = 0  # 将2-4索引列赋值为0
    print(array1)

    print(array1 < 10)  # ture false
    print(array1[array1 < 10])  # 取数组中小于10的部分
    array1[array1 < 10] = 3  # 将小于10的赋值3
    print(array1)

    # 三元运算符 格式
    x = np.where(array1 < 10, 5, 11)
    print(x)

    # 裁剪---小于等于4的替换为4；大于等于10的替换为10
    xx = array1.clip(4, 10)
    print(xx)

    xxx = array1.astype(float)
    xxx[3, 4] = np.nan
    print(xxx)
    pass


# 数组拼接--行列交换
def arrayConcat():
    ukdata = np.loadtxt(uk, delimiter=',', dtype='int', skiprows=1)
    usdata = np.loadtxt(us, delimiter=',', dtype='int', skiprows=1)
    # 竖直拼(上下)
    vstack = np.vstack((ukdata, usdata))
    print(vstack)
    print('--' * 50)
    hstack = np.hstack((ukdata, usdata))
    print(hstack)
    # ---------行列交换
    print('--' * 50)
    array = np.arange(0, 12).reshape(3, 4)
    # 交换行-[1,2行交换]
    array[[0, 1], :] = array[[1, 0], :]
    print('-' * 50, '->交换行')
    print(array)
    print('-' * 50, '->交换列')
    array[:, [2, 3]] = array[:, [3, 2]]
    print(array)

    pass


if __name__ == '__main__':
    # shap_test()
    # numpyTest()
    # local_file()
    # axis_test()
    # index_slice()
    # ohter()
    arrayConcat()
