import tensorflow as tf


# 队列同步模拟
def tongbu():
    '''
    从队列中获取数据改变数据再加入队列/处理数据[简单的获取最后的值]
    :return:
    '''
    Q = tf.queue.FIFOQueue(3, tf.float32)

    # 1.放入一些数据
    queue_op = Q.enqueue_many([[1.0, 2.0, 3.0], ])

    # 2.取数据/操作数据/
    out_q = Q.dequeue()
    data = out_q + 1  # 类型转换(op与int)[这里叫重载/java叫装箱]
    en_q = Q.enqueue(data)

    with tf.compat.v1.Session() as sess:
        # 初始化队列
        sess.run(queue_op)
        # 处理数据[依赖传递 en_q依赖于data-->data依赖于out_q 会先运行out_q]
        for i in range(100):
            sess.run(en_q)

        # 处理数据[简单的获取数据]-----必须等待上一步
        for i in range(Q.size().eval()):
            print(sess.run(Q.dequeue()))


# 模拟异步子线程 存入样本 ，主线程 读取样本
def anscy():
    # 1-定义一个队列
    Q = tf.queue.FIFOQueue(1000, tf.float32)
    # 2-定义要做的事情 循环自增，放入队列中
    var = tf.Variable(0.0)  # 定义变量-自己可变
    # 自增
    data = tf.assign_add(var, tf.constant(1.0))
    # 放入队列
    en_q = Q.enqueue(data)

    # 3-定义队列管理器，指定多少个线程，子线程该做什么事
    qr = tf.train.QueueRunner(Q, enqueue_ops=[en_q] * 2)  # 要操作的队列,[行为]*线程数

    # 初始化变量
    init_op = tf.global_variables_initializer()

    print(qr)
    with tf.compat.v1.Session() as sess:  # 会话掌握着各种资源
        # 初始化变量
        sess.run(init_op)

        # 开启线程管理器
        coord = tf.train.Coordinator()

        # 真正开启开启子线程
        threads = qr.create_threads(sess, coord=coord, start=True)  # coord=coord：指定由谁来回收
        # 主线程从队列中拿数据...训练数据
        for i in range(300):
            print(sess.run(Q.dequeue()))

        # 没有线程回收期 主线程结束，意味着session关闭,意味着资源释放---但是子线程还没有结束 所以报错
        # 停止子线程
        coord.request_stop()
        # 回收线程资源
        coord.join(threads)
        pass

    pass


if __name__ == '__main__':
    # tongbu()
    anscy()
