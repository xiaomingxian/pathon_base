import redis
import time

redis_pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)


def base():
    # 连接redis
    # 加上decode_responses=True，写入的键值对中的value为str类型，不加这个参数写入的则为字节类型。
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    r.set('skey', '字符串值')
    print(r['skey'])
    print(type(r['skey']))
    print(r.get('skey'))


def pool():
    # 创建连接池
    pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
    # 使用连接池
    r = redis.Redis(connection_pool=pool)
    r.set('key2_pool', 'value_pool')
    print(r.get('key2_pool'))


def expire():
    pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    # 过期时间设置 -- ex秒    还有很多类似操作 见笔记
    # r.set('k3', '设置过期时间', ex=10)
    print(r.get('k3'))
    time.sleep(10)
    print(r.get('k3'))

    pass


def time_test():
    print('xxxxxxxx')
    # 单位  秒
    time.sleep(1)
    print('lllllllll')


#     自增  ---   计算点击量

def incr():
    pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    r.set('incr_key', 10)
    for i in range(5):
        r.incr('incr_key', amount=2)  # 整数
        # r.incrbyfloat('incr_key', amount=1.1)
        # r.decr('incr_key', amount=1)
        # r.decr('incr_key', amount=0.1)  #redis.exceptions.ResponseError: value is not an integer or out of range
    print(r.get('incr_key'))


def append():
    pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    # r.set('append_test', 'tom')
    # r.append('append_test', '-Jerry')

    print(r.get('append_test'))

    pass


def hash():
    r = redis.Redis(connection_pool=redis_pool)
    # keys = r.keys()  #测试出现乱码
    # print(keys)
    # r.hset('big_key', 'sk1', 'v1')
    # r.hset('big_key', 'sk2', 'v2')
    # r.hset('big_key', 'sk3', 'v3')
    # r.hset('big_key', 'sk4', 'v4')
    # print(r.hkeys('big_key'))
    # print('获取单个值:', r.hget('big_key', 'sk2'))
    # print('获取多个值:', r.hmget('big_key', 'sk2', 'sk3'))
    # print('新建[只能新建]:', r.hsetnx('big_key', 'sk_nx', 'v_nx'))  # 添加成功返回 1  否则 0

    # print('------------批量增加/获取--------------')
    # r.hmset('lot_set/get', {'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 'k5': 'v5'})
    # print(r.hmget('lot_set/get', ['k1', 'k2']))
    # print(r.hmget('lot_set/get', 'k4', 'k5'))

    # print('------------获取所有键值对---------------')
    # print(r.hgetall('lot_set/get'))
    #
    # print('-----------获取键值对的数量---------------')
    # print(r.hlen('lot_set/get'))

    # print('-----------获取所有的小key----------------')
    # print(r.hkeys('lot_set/get'))

    # print('获取所有的values : ', r.hvals('lot_set/get'))

    # print('判断是否存在 : ', r.hexists('lot_set/get', 'k1'), r.hexists('lot_set/get', 'k33'))

    # print('----------------- 删除测试 -------------------')
    # r.hmset('lot_set/get', {
    #     'kd1': 'dv1',
    #     'kd2': 'dv2',
    #     'kd3': 'dv3',
    #     'kd4': 'dv4',
    #     'kd5': 'dv5'
    # })
    #
    # print(r.hmget('lot_set/get', [
    #     'kd1',
    #     'kd2',
    #     'kd3',
    #     'kd4',
    #     'kd5',
    # ]))
    #
    # print(r.hdel('lot_set/get', 'kd1'))
    # print(r.hdel('lot_set/get', 'kd2', 'kd3'))
    # # print(r.hdel('lot_set/get', ['kd4', 'kd5']))  #删除格式错误
    # print(r.hgetall('lot_set/get'))

    # print('-----------------自增测试-------------------')
    # r.hset('incr_test', 'num', 10)
    # r.hincrby('incr_test', 'num', amount=2)
    # r.hincrby('incr_test', 'num2', amount=2)  # 不存在  值就是 amount值
    # print(r.hgetall('incr_test'))



    print(r.hget('incr_test','nu?'))

if __name__ == '__main__':
    pass
    # time_test()
    # base()u
    # pool()
    # expire()
    # incr()
    # append()
    hash()
