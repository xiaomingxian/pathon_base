import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import random

font = {
    "family": "Microsoft YaHei",  # 也可简写为M
    "weight": "10",
    "size": "10"
}
# windows/linux解决方式
# matplotlib.rc("font", **font)  # 对以上font的使用

# or
# matplotlib.rc("font",family="Microsoft YaHei",weight='blod',size='larger')

# Windows/mac/linux
from matplotlib import font_manager

#
# # 实例化一个字体
fontM = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')  # 还可以设置大小等属性


# 天气
def main():
    x = range(0, 120)
    # 产生120个[20-35]范围的随机数,并放到列表
    y = [random.randint(20, 35) for i in range(120)]
    plt.figure(figsize=(14, 9), dpi=80)
    plt.plot(x, y)
    # xy轴的粒度--中文显示
    _x = list(x)[::3]  # 步长为3 从开始到结束
    _xtick_labels = ["10点{}分".format(i) for i in range(60)]
    _xtick_labels += ["11点{}分".format(i - 60) for i in range(60, 120)]
    # plt.xticks(x[::3], _xtick_labels[::3], rotation=45)  # rotation旋转角度
    plt.xticks(x[::3], _xtick_labels[::3], rotation=45, fontproperties=fontM)  # rotation旋转角度
    plt.xlabel("时间", fontproperties=fontM)
    plt.ylabel("温度", fontproperties=fontM)
    plt.title("温度统计图", fontproperties=fontM)

    plt.show()
    pass


def test():
    x = [1, 2, 3, 4, 5, 6]
    print(list(x))
    print(list(x)[::3])


if __name__ == '__main__':
    # test()
    main()
