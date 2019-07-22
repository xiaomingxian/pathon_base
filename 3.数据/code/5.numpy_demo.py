import numpy as np


# 在数组后拼接一列0-一列1
def append0_1():
    a1 = np.arange(12, 24).reshape(3, 4)
    a2 = np.arange(24, 36).reshape(3, 4)

    # 构造一列0-行数与数组相同
    zeros = np.zeros((a1.shape[0], 1)).astype(int)  # 行，列#shape[0]表示行[1]表示列 -- a1.shape[0]表示构造的数组形状行与a1的行相同
    ones = np.ones((a2.shape[0], 1)).astype(int)
    # 构造一列1
    zeros_data = np.hstack((a1, zeros))
    ones_data = np.hstack((a2, ones))
    print(zeros_data)
    print(ones_data)
    pass


def othertest():
    print(np.zeros((3, 4)))
    print(np.ones((3, 4)))
    print('**' * 50, '>方阵')
    print(np.eye(4))  # n行n列--对角线为1

    ar1 = np.eye(5)
    res1 = np.argmax(ar1, axis=0)  # 横轴 最大值所在位置
    print(res1)

    # 替换等于1位置的值
    ar1[ar1 == 1] = -1
    print(ar1)

    # 取每行的最小值的位置
    res1_min = np.argmin(ar1, axis=0)
    print(res1_min)

    # 取列的极值
    res2_max = np.argmax(ar1, axis=1)
    res2_min = np.argmin(ar1, axis=1)
    print(res2_max)
    print(res2_min)

    print('**' * 50, '随机数测试')
    # numpy生成随机数
    print(np.random.rand(3, 4))  # N~Nn维度的随机数-范围0-1
    print('*' * 50)
    print(np.random.randn(3, 4))  # N~Nn维度的正态分布随机数-范围0-1  平均数0 标准差1
    print('*' * 50)
    print(np.random.randint(3, 7, (3, 4)))  # (start,end,(shape)) 不包含end
    print('*' * 50)
    print(np.random.uniform(1, 10, (3, 5)))  # 产生均匀分布的数组  (start,end,(shape))
    print('*' * 50)
    print(np.random.normal(5, 1, (2, 5)))  # (分布中心,标准差,(shape))
    print('*' * 50)
    # 设置种子后-一个随机数函数多次运行的结果一致
    # np.random.seed(3)
    print(np.random.randint(1, 10))

    pass


if __name__ == '__main__':
    # append0_1()
    othertest()
