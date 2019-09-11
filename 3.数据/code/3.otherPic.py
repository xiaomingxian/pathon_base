import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import random

from matplotlib import font_manager

# 实例化一个字体
fontM = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')  # 还可以设置大小等属性


# 散点图--温度散点图
def sandian():
    x6 = range(1, 31)
    x7 = range(31, 31 * 2)

    y6 = [random.randint(26, 40) for i in range(30)]
    y7 = [random.randint(26, 40) for i in range(31)]

    plt.scatter(x6, y6)
    plt.scatter(x7, y7)

    x_tick_labels = ["6月{}日".format(i) for i in x6]
    x_tick_labels += ["7月{}日".format(i - 30) for i in x7]

    y_tick_labels = ["{}度".format(i) for i in y6]
    y_tick_labels += ["{}度".format(i) for i in y7]

    plt.xticks([i for i in range(1, 31 * 2)][::3], x_tick_labels[::3], rotation=45, fontproperties=fontM)
    plt.yticks(y6 + y7, y_tick_labels, fontproperties=fontM)

    plt.xlabel('月份', fontproperties=fontM)
    plt.ylabel('温度', fontproperties=fontM)

    plt.show()


# 竖着的条形图
def tiaoxt_shu():
    x = ['加勒比海盗', '功夫熊猫', '玩具总动员', '钢铁侠', '蜘蛛侠', '变形金刚']
    y = [33, 11, 23, 14, 88, 49]

    plt.bar(range(len(x)), y, width=0.4)

    plt.xticks(range(len(x)), x, fontproperties=fontM)

    plt.show()
    pass


def tiaoxt_heng():
    x = ['加勒比海盗', '功夫熊猫', '玩具总动员', '钢铁侠', '蜘蛛侠', '变形金刚']
    y = [33, 11, 23, 14, 88, 49]
    # 横坐标变成了y轴
    plt.barh(range(len(x)), y, height=0.3)
    plt.yticks(range(len(x)), x, fontproperties=fontM)
    # 网格
    plt.grid(alpha=0.3)
    plt.show()
    pass


def main():
    # sandian()
    # tiaoxt_shu()
    tiaoxt_heng()

    pass


if __name__ == '__main__':
    main()
