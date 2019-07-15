import numpy as np


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


if __name__ == '__main__':
    shap_test()
