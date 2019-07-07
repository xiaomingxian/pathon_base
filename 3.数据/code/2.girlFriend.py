import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import random
from matplotlib import font_manager

# 字体实例
fontM = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')  # 还可以设置大小等属性


def main():
    # 横轴，年龄
    x = range(15, 25)
    xx = range(15, 25)
    # 纵轴，女朋友数量
    y = [random.randint(0, 10) for i in range(10)]
    yy = [random.randint(0, 10) for i in range(10)]

    # 设置画布大小
    plt.figure(figsize=(10, 20), dpi=80)
    # 绘制网格  alpha透明度 粒度根据横轴纵轴粒度而定
    plt.grid(alpha=0.4)
    # 填充数据
    plt.plot(x, y, color='cyan', label='汤姆',linewidth=0.7)
    plt.plot(xx, yy, color='blue', label='杰瑞',linewidth=0.7)

    # 显示
    plt.legend(prop=fontM, loc='best')

    _xtick_labels = ["{}岁".format(i) for i in range(15, 25)]
    # 展示粒度与自定义显示，字体
    plt.xticks(x[::2], _xtick_labels, rotation=45, fontproperties=fontM)

    plt.xlabel('年龄', fontproperties=fontM)
    plt.ylabel('女朋友数量', fontproperties=fontM)
    plt.title('女朋友数量统计图', fontproperties=fontM)

    plt.show()
    pass


if __name__ == '__main__':
    main()
