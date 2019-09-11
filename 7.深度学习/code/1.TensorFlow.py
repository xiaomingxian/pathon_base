import tensorflow as tf
import os

# 设置最低log level
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# 会话 只能运行一个图结构
# 1-运行图结构欧
# 2-分配计算资源
# 3-掌握资源(变量的资源,队列,线程)
# with run()完会自定关闭  否则要用以下写法
# session.run()启动整个图
# session.close() 释放资源
# 交互式 无需开启session tf.InteractiveSession()  a.eval()
# 只要有上下文环境都可以使用eval()
# 张量：数组 tensor类型 名字/形状/数据类型 #tensorflow的基本格式
# API位置--[算数运算符,基本数学运算符,矩阵运算,减少维度的运算(求平均值),序列运算]
# https://www.tensorflow.org/version/r1.0/api_guides/python/math_ops
def main():
    # 图
    a = tf.constant(5.0, )
    b = tf.constant(6.0, )
    sum = tf.add(a, b, )

    with tf.compat.v1.Session() as sess:
        print(sess.run(sum, ))
        # 图信息---都是一个地址
        print(sess.graph)
        print(sum.graph)
        print(a.graph)

    # 获取默认的图：相当于给程序分配的一个内存
    graph = tf.compat.v1.get_default_graph()
    print(graph)
    print('*' * 50, '定义图', '*' * 50)
    # **************************  创建一张图  ************************
    g1 = tf.Graph()
    # 使用上下文 with
    with g1.as_default():
        c = tf.constant(12.0)
        print(c.graph)
        aa = tf.constant(10.0)
        bb = tf.constant(5.0)
        sum2 = tf.add(aa, bb)
        # 重载机制--op类型与其他类型运算会转成 op类型
        v1 = tf.constant(4.0)
        v2 = 5
        s1 = v1 + v2
        print('~~~~~~~~~~~~>', s1)
        # 占位符-实时填充数据

        plt = tf.compat.v1.placeholder(tf.float32, shape=[2, 3])
        # 不固定形状
        plt2 = tf.compat.v1.placeholder(tf.float32, [None, 3])
        pass
    # session
    with tf.compat.v1.Session(graph=g1, config=tf.ConfigProto(log_device_placement=True)) as se:
        # 图只能运行自己的资源
        # print(se.run(sum))
        # print('--------->启动图 run()')
        # print(se.run([aa, bb, sum2, s1]))
        # print(se.run(plt, feed_dict={plt: [[1, 2, 3], [4, 5, 6]]}))
        print(se.run(plt2, feed_dict={plt2: [[1, 2, 3], [2, 2, 2], [4, 5, 6]]}))
        print(sum2.eval())

        # 张量
        print('*' * 50, '-->张量')
        print('张量图：', sum2.graph)
        # 形状：静态/动态
        print('张量形状：', plt2.shape)  # 0() 一维(n) (x,y) (?,x) (x,?) 。。。
        plt3 = tf.compat.v1.placeholder(tf.float32, [None, 2])
        print(plt3)
        plt3.set_shape([4, 2])  # 对于静态：已经固定的部分不可改变--维度不可变
        print(plt3)
        # 动态--创建一个新的张量
        plt4 = tf.reshape(plt3, [2, 4])  # 变化前后数据总量不可变-否则报错
        plt5 = tf.reshape(plt3, [2, 2, 2])  #
        print('形状改变：', plt4, '变换维度：', plt5)
        # 运算API
        print('*' * 50, '-->运算API')
        # 固定值张量
        zes = tf.compat.v1.zeros([2, 3], dtype=tf.float32)  # ones
        print(zes)
        # 随机值张量
        rand = tf.random_normal([3, 4], mean=3, stddev=3, dtype=tf.float32, seed=None, name='test')
        print('随机张量-->', rand.eval())
        # 类型转换
        cast_val = tf.cast([[2, 3], [4, 3], [5, 6]], tf.float32)
        print(cast_val.eval())
        # 数据合并--行/列
        a = [[1, 1], [2, 2], [3, 3]]
        b = [[4, 5], [6, 7], [8, 9]]
        lie = tf.concat([a, b], axis=1)
        print(lie.eval())
        hang = tf.concat([a, b], axis=0)
        print(hang.eval())

        pass
    pass


# 变量--是一种op,是一种特殊的张量，能够进行持久化存储，他的值就是张量，默认被训练
def variables():
    # var = tf.Variable(initial_value=1, name='variable_test', trainable=True)
    var = tf.Variable(tf.compat.v1.random_normal(shape=[2, 3], mean=3, stddev=2))

    # 必须显示化的初始化
    init_op = tf.compat.v1.global_variables_initializer()
    with tf.compat.v1.Session() as sess:
        sess.run(init_op)
        print(sess.run(var))
    pass


if __name__ == '__main__':
    # main()
    variables()
