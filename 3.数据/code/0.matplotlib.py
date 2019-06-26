import matplotlib
# 独立窗口
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy

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

def haveData():
    # -1~1生成50个随机数
    xx=numpy.linspace(-1,1,50)
    # 斜线公式
    yy=2*xx+1
    # 设置图片大小[尺寸，清晰度]  figure就是窗口对象
    plt.figure(figsize=(20, 10), dpi=80)
    # 绘图
    # plt.plot(x, y, color='green', linewidth=2.0)
    plt.plot(xx, yy)
    # 保存图片
    plt.savefig('../result/0.matplotlib1.png')
    # 展示图片
    plt.show()

    # 保存放在后面显示保存空白图片的原因
    # 其实产生这个现象的原因很简单：在plt.show()
    # 后调用了plt.savefig() ，在plt.show()
    # 后实际上已经创建了一个新的空白的图片（坐标轴），这时候你再plt.savefig()
    # 就会保存这个新生成的空白图片。

    # 解决方式2：画图的时候获取当前图像（这一点非常类似于Matlab的句柄的概念）：
    #
    # # gcf: Get Current Figure
    # fig = plt.gcf()
    # plt.show()
    # fig.savefig('tessstttyyy.png', dpi=100)

    pass


def main():
    # base()
    haveData()
    pass


if __name__ == '__main__':
    main()
