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


# 多列条形图
def moreLie():
    # 电影数据
    films = ['玩具总动员', '钢铁侠', '蜘蛛侠', '变形金刚']
    # 评分数据--每一组表示一个指标
    values_1 = [100, 200, 234, 120]
    values_2 = [180, 130, 432, 360]
    values_3 = [202, 120, 204, 220]

    # 间隔
    barwidth = 0.2
    # 横坐标粒度---递增偏移
    h1 = list(range(len(films)))
    h2 = [i + barwidth for i in h1]
    h3 = [i + barwidth * 2 for i in h1]

    # 条形图显示--宽度是间隔宽度--label图例
    plt.bar(h1, values_1, width=barwidth, label='15日')
    plt.bar(h2, values_2, width=barwidth, label='16日')
    plt.bar(h3, values_3, width=barwidth, label='17日')

    # 显示图例
    plt.legend(prop=fontM, loc='best')

    # 横坐标-中文显示-选h2逻辑居中
    plt.xticks(h2, films, fontproperties=fontM)

    plt.show()


def main():
    # sandian()
    # tiaoxt_shu()
    # tiaoxt_heng()
    moreLie()
    pass


if __name__ == '__main__':
    main()
