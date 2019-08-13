import tensorflow as tf
import os

# 定义命令行参数
# 1-定义有哪些参数需要在运行时指定
# 2-程序当中获取定义的命令行参数

# 名字，默认值，说明
# 启动 python xxx.py --max_step=500 --model_dir='xxx'
tf.app.flags.DEFINE_integer('max_step', 500, '训练模型的步数')
tf.app.flags.DEFINE_string('model_dir', '../pic/model-test', '模型文件的存储路径')

# 获取值
FLAGS = tf.app.flags.FLAGS


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
    with tf.variable_scope("data_zhunbei"):
        # 1-准备数据
        test_data = tf.random_normal([100, 1], mean=1.75, stddev=0.5, name='x_data')
        # 准备虚假的真实值-----为了有逻辑关系--->[矩阵想成必须是二维]与权重相乘+
        true_val = tf.matmul(test_data, [[0.7]]) + 0.8
    # ***********************************
    with tf.variable_scope("model"):
        # 2-建立线性回归模型
        # 随机给一个权重和偏置值--让他计算损失，然后在当前状态下优化[因为值不固定所以是变量]----,trainable=True默认
        weight = tf.Variable(tf.random.normal([1, 1], mean=1.0, stddev=1.0), name='w')  # 权重得是二维
        bias = tf.Variable(0.0, name='b')
        # 矩阵相乘预测结果
        t_predict = tf.matmul(test_data, weight) + bias
    with tf.variable_scope("youhua"):
        # 3-建立随时函数，均方误差   真实值与预测值做差平方-->平均值
        loss = tf.reduce_mean(tf.square(true_val - t_predict))
        # 4-梯度下降优化损失---学习率不宜太高---太大时会出现Nan值[梯度爆炸--指数爆炸]
        train_op = tf.train.GradientDescentOptimizer(0.2).minimize(loss)  # 指定学习率[0-100],最小化损失

    # 定义全局变量
    init_op = tf.compat.v1.global_variables_initializer()

    # x1.收集tenor-在tensorboard中显示变化
    tf.summary.scalar('loss_back', loss)
    tf.summary.histogram('weight_back', weight)
    # x2.定义合并tensor的op
    merge_op = tf.summary.merge_all()

    # xx0.保存模型的op--[适用与训练次数多,有可能意外中断的情况]
    saver_model = tf.train.Saver()

    with tf.compat.v1.Session() as sess:
        # 初始化变量
        sess.run(init_op)
        print('随机初始化的参数权重 ：%f,偏置为：%f' % (weight.eval(), bias.eval()))
        # x3
        filewriter = tf.summary.FileWriter('../pic/', graph=sess.graph)
        # xx2.加载模型，覆盖模型中随机定义的参数，从上次的参数结果开始
        if os.path.exists('../pic/checkpoint'):  # 可以自定义基准
            saver_model.restore(sess, FLAGS.model_dir)
            # saver_model.restore(sess, '../pic/model-test')
            # 在上一次[文件中的记录]的基准上进行再次训练
            # 上次运行结果：0.700767,偏置为：0.798496

        # 运行一次-进行优化
        for i in range(FLAGS.max_step):
            # for i in range(100):
            # x4.运行合并的tensor- 写入file writer
            summary = sess.run(merge_op)
            filewriter.add_summary(summary, i)  # i第几次
            sess.run(train_op)
            print('运行%d次后的参数权重 ：%f,偏置为：%f' % (i, weight.eval(), bias.eval()))
        # xx1.真实情况可以自定义到训练到某一步的时候进行保存
        saver_model.save(sess, FLAGS.model_dir)  # 位置/自定义名称
        pass
    pass


if __name__ == '__main__':
    # main()
    line_test()
