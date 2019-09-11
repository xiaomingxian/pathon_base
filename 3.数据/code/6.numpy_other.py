import numpy as np


# 不是数字nan,nif正无穷,-nif负无穷  常用统计方法
def nan_nif():
    # nan不等
    print(np.nan == np.nan)
    print(np.nan != np.nan)

    a1 = np.arange(1, 10).astype(float)
    a1[2] = np.nan

    print(a1)
    # 统计数组中nan的个数
    # method 1
    print(a1[a1 != a1])
    print('个数：', np.count_nonzero(a1 != a1))
    # method 2
    print(a1[np.isnan(a1)])
    print('个数：', np.count_nonzero(np.isnan(a1)))

    # nan和任何值计算都为nan
    a2 = np.arange(0, 12).astype(float).reshape(3, 4)
    print(np.sum(a2))
    print(np.sum(a2, axis=0))
    print(np.sum(a2, axis=1))

    a2[0, 0] = np.nan
    print(np.sum(a2))
    print(np.sum(a2, axis=0))
    print(np.sum(a2, axis=1))

    # 均值
    # 和
    print(a2.sum())
    print(a2.sum(axis=0))
    print(a2.sum(axis=1))
    # 中值
    print(a2.mean())
    print(a2.mean(axis=0))
    print(a2.mean(axis=1))
    # max min 略
    print(np.ptp(a2, axis=0))
    print(np.ptp(a2, axis=1))
    # 标准差[每个值距离均值的距离]
    print(a2.std())
    print(a2.std(axis=0))
    print(a2.std(axis=1))

    pass


# 将列中的nan 替换为中值
def nan_test():
    a = np.arange(12).reshape((3, 4)).astype(float)
    print(a)
    # 2索引行  2索引列 以后赋值为nan
    a[1, 2:] = np.nan
    print(a)
    print('*' * 20, '均值替换', '*' * 20)
    # 将nan替换为列的均值
    for i in range(a.shape[1]):  # a.shape[1]==4列数字 range(a.shape[1]) ==>列元素数组组成的数组
        # 取当前列 数组[]
        lie = a[:, i]
        nan_num = np.count_nonzero(lie != lie)
        if nan_num:  # 说明存在nan值
            # 去出不为nan的值 求平均值
            not_nan_num = lie[lie == lie]
            mean_val = not_nan_num.mean()
            # 将nan值替换为中值
            # lie[lie != lie] = mean_val
            # 或者
            lie[np.isnan(lie)] = mean_val

            pass
    print(a)
    pass


# numpy小结
def numpy_sumary():
    arr = np.arange(12, 24).reshape(3, 4)
    # ====================== 索引和且切片[n:]格式
    # 选择行列
    print('*' * 20, '行')
    print(arr[1, :])
    # 多行
    print(arr[1:, :])
    # 不连续
    print(arr[[1, 2], :])
    print('*' * 20, '列')
    print(arr[:, 1])
    # 多列
    print(arr[:, 1:])
    print(arr[:, [1, 2]])
    print('*' * 20, '行列')
    # 索引
    print(arr[1, 1])
    # 不连续
    print(arr[[1, 2], 1:])
    # 多行多列 连续
    print(arr[1:, 1:])
    # ========================= boolean索引
    print(arr[arr > 10])
    # ========================= 三元运算
    # 大于20的替换为30 其他的替换为20
    arr2 = np.where(arr > 20, 30, 20)
    print(arr2)

    # ========================= 裁剪
    # 15 与 20两端分别替换为这两个数字
    arr3 = arr.clip(15, 20)
    print(arr3)

    # ========================= 转置[横纵坐标交换]
    arr4=arr.T
    print(arr4)

    arr5=arr.swapaxes(1,0)
    print(arr5)
    arr6=arr.transpose()
    print(arr6)


    # 赋值 以上索引/切片 后跟=即可

    pass


if __name__ == '__main__':
    # nan_nif()
    # nan_test()
    numpy_sumary()
