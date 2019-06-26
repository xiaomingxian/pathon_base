import matplotlib

# 独立窗口
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy

# 基础
def haveData():
    # -1~1生成50个随机数
    xx = numpy.linspace(-1, 1, 50)
    # 斜线公式
    yy = 2 * xx + 1
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
    # 解决方式1：调整顺序
    # 解决方式2：画图的时候获取当前图像（这一点非常类似于Matlab的句柄的概念）：
    # # gcf: Get Current Figure
    # fig = plt.gcf()
    # plt.show()
    # fig.savefig('tessstttyyy.png', dpi=100)

# 图像区域
def figure_use():
    x=numpy.linspace(-1,1,50)
    y1=x**2
    y2=x**3
    # 一个figure是一个窗口对象--按照顺序来[指定序号与长宽]
    plt.figure(num=3,figsize=(8,10))
    plt.plot(x,y1)
    plt.figure()
    # 同一个figure放入多个图像
    plt.plot(x,y2)
    # --表示虚线
    plt.plot(x,y1,color='red',linewidth=5.0,linestyle='--')
    plt.show()

# xy轴
def xy():
    # -1到5随机50个数字
    x=numpy.linspace(-1,5,50)
    y=x**2
    # xy取值范围
    plt.xlim(0,5)
    plt.ylim(0,30)
    # xy描述
    plt.xlabel('i am x')
    plt.ylabel('i am y')
    # xy轴粒度与描述
    xticks= numpy.linspace(0,8,5)#0到5分成10段
    plt.xticks(xticks)
    # $xxx$数学字体
    plt.yticks([5,15,25],[r'$good$','very good','pretty good'])
    plt.plot(x,y)
    plt.show()




def main():
    # haveData()
    # figure_use()
    xy()
    pass


if __name__ == '__main__':
    main()
