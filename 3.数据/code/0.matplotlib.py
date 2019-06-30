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
    x = numpy.linspace(-1, 1, 50)
    y1 = x ** 2
    y2 = x ** 3
    # 一个figure是一个窗口对象--按照顺序来[指定序号与长宽]
    plt.figure(num=3, figsize=(8, 10))
    plt.plot(x, y1)
    plt.figure()
    # 同一个figure放入多个图像
    plt.plot(x, y2)
    # --表示虚线
    plt.plot(x, y1, color='red', linewidth=5.0, linestyle='--')
    plt.show()


# xy轴
def xy():
    # -1到5随机50个数字
    x = numpy.linspace(-1, 5, 50)
    y = x ** 2
    # xy取值范围
    plt.xlim(0, 5)
    plt.ylim(0, 30)
    # xy描述
    plt.xlabel('i am x')
    plt.ylabel('i am y')
    # xy轴粒度与描述
    xticks = numpy.linspace(0, 8, 5)  # 0到5分成10段
    plt.xticks(xticks)
    # $xxx$数学字体
    plt.yticks([5, 15, 25], [r'$good$', 'very good', 'pretty good'])
    plt.plot(x, y)
    plt.show()


# xy轴的位置
def xy2():
    plt.xlim(0, 20)
    plt.ylim(0, 20)
    # gca==get current axis#当前的图形
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    # 设置xy轴
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    # 移动-->此处是根据数据移动
    ax.spines['bottom'].set_position(('data', 10))
    ax.spines['left'].set_position(('data', 10))
    plt.show()
    pass


# 图例
def xy3():
    plt.xlim(0, 20)
    plt.ylim(0, 20)
    x = numpy.linspace(0, 5, 10)
    y = x ** 2
    y1 = x

    # 1-->使用默认
    # plt.plot(x,y,label='up')
    # plt.plot(x,y1,label='down')
    #
    # 2-->自定义
    # l1,格式要求得带逗号
    l1, = plt.plot(x, y, label='up')
    l2, = plt.plot(x, y1, label='down')
    # 位置也可以有其他参数
    # plt.legend(handles=[l1,l2,],labels=['AAA','BBB'],loc='best')
    # 显示一条线图例
    plt.legend(handles=[l1, l2, ], labels=['AAA'], loc='best')

    # 添加注释
    x0 = 4
    y0 = x0 ** 2
    # scatter画散点图
    plt.scatter(x0, y0, s=50, color='b')
    # [两个横坐标][两个纵坐标]-->[x0,x0],[y0,0]
    plt.plot([x0,x0],[0,y0],'k--',lw=2.5)
    #annotion 标注点
    # plt.annotate(r'my annotion=%s'%y0,xy=(x0,y0),xycoords='data',xytext=(+5,+16))#相对于(0,0)进行偏移
    plt.annotate(r'my annotion=%s'%y0,xy=(x0,y0),xycoords='data',xytext=(+18,-8),textcoords='offset points'
                 ,fontsize=8,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))#相对于(poit)进行偏移

    # plt.legend()
    plt.show()
    pass




def main():
    # haveData()
    # figure_use()
    xy()
    # xy2()
    # xy3()
    pass


if __name__ == '__main__':
    main()
