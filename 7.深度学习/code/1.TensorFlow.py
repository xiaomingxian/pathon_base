import tensorflow as tf
import os

# 设置最低log level
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


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

    with tf.compat.v1.Session(graph=g1,config=tf.ConfigProto(log_device_placement=True)) as se:
        # 图只能运行自己的资源
        # print(se.run(sum))
        print('---->启动图')
        run=se.run()
        aa=tf.constant(10.0)
        bb=tf.constant(5.0)
        summ=tf.add(aa,bb)
        print(run.run(summ))
    pass


# 会话 只能运行一个图结构
# 1-运行图结构欧
# 2-分配计算资源
# 3-掌握资源(变量的资源,队列,线程)
# with run()完会自定关闭  否则要用以下写法
# session.run()启动整个图
# session.close() 释放资源
def session():
    pass


if __name__ == '__main__':
    main()
