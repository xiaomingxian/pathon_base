# 别名
from matplotlib import pyplot as plt
import random

x = [range(0, 20,2)]
y = [range(10,30,2)]


def base():
    # 参数说明
    # help(plt.plot)
    # 设置图片大小[尺寸，清晰度]  figure就是窗口对象
    plt.figure(figsize=(20,8),dpi=80)
    # 绘图
    plt.plot(x,y,color='green',linewidth=2.0)
    # 展示图片
    plt.show()
    # 保存图片
    plt.savefig('../result/0.matplotlib1.png')
    pass


def main():
    base()
    pass


if __name__ == '__main__':
    main()
