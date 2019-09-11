import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np


def data_show():
    ukdata = np.loadtxt('../result/uk.csv', delimiter=',', dtype=int, skiprows=1)
    print(ukdata)

    ukdata = ukdata[ukdata[:, -2] <= 2000]
    ukdata = ukdata[ukdata[:, 0] <= 3000]

    # 观看量 与 点赞量的关系
    nzan = ukdata[:, -1]  # 最后一列
    # print(nzan)

    zan = ukdata[:, -2]
    look = ukdata[:, 0]
    # print(zan)
    # print(look)

    # 图形设置
    plt.figure(figsize=(20, 10), dpi=80)

    plt.scatter(look, zan)

    plt.show()

    pass


if __name__ == '__main__':
    data_show()
