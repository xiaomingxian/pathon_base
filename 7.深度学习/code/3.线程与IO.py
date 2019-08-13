import tensorflow as tf


# 队列同步模拟
def tongbu():
    '''
    从队列中获取数据改变数据再加入队列/处理数据[简单的获取最后的值]
    :return:
    '''
    Q = tf.queue.FIFOQueue(3, tf.float32)

    # 1.放入一些数据
    queue_op=Q.enqueue_many([[1.0, 2.0, 3.0],])

    # 2.取数据/操作数据/
    out_q = Q.dequeue()
    data = out_q + 1  # 类型转换(op与int)[这里叫重载/java叫装箱]
    en_q=Q.enqueue_many(data)

    with tf.compat.v1.Session() as sess:
        # 初始化队列
        sess.run(queue_op)
        # 处理数据[依赖传递 en_q依赖于data-->data依赖于out_q 会先运行out_q]
        for i in range(11):
            sess.run(en_q)
        # 处理数据[简单的获取数据]
        for i in range(Q.size().eval()):
            print(sess.run(Q.dequeue()))



        pass
    pass


if __name__ == '__main__':
    tongbu()
