import tensorflow as tf


def main():
    '''
    1.将图结构序列化成文件 events[事件文件]
    2.tensorboard进行可视化显示
    3.name参数 tensorboard显示/区分相同类型op
    '''
    var = tf.Variable(tf.random_normal(shape=[2, 3], mean=3), name='var1')
    # 实例话
    init = tf.global_variables_initializer()

    a = tf.constant(2.0)
    b = tf.constant(3.0)
    sum = tf.add(a, b)
    with tf.compat.v1.Session() as sess:
        sess.run([init, sum])
        tf.summary.FileWriter('../pic/', graph=var.graph)
        pass
    # python -m tensorboard.main --logdir="/Users/xxm/develop/py_workspace/python_base/7.深度学习/pic"
    pass


# 线性测试
def line_test():
    '''
    :return:
    '''
    # 准备数据
    x = tf.random_normal([100, 1], mean=1.75, stddev=0.5, name='x_data')
    # [矩阵想成必须是二维]与权重相乘+
    tf.matmul(x, [[0.7]]) + 0.8
    pass


if __name__ == '__main__':
    main()
