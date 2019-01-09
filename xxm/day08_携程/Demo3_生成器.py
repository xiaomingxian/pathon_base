# 有yield就是生成器---没有就不是
# 生成器是一种特殊的迭代器---通过next执行
# 多个生成器的调用互不影响
# 调用的时候会返回yield后的值
# 保存的生成数据的代码-而不是结果

import datetime
import time


def putong():
    a, b = 0, 1
    cou = 0
    while cou <= 100000:
        # print(a)
        a, b = b, a + b
        cou += 1

    pass


def shengchengQi():
    print('---1---')
    a, b = 0, 1
    cou = 0
    while cou <= 10:
        print('---2---')
        yield a
        a, b = b, a + b
        cou += 1
        print('---3---')
    return "ok..."


def shengchengQi2():
    """send测试"""
    a, b = 0, 1
    cou = 0
    while cou <= 10:
        c = yield a
        print("传入参数:", c)
        a, b = b, a + b
        cou += 1
    return "ok..."


if __name__ == '__main__':
    print('-----------------------------------启动方式一:next()-----------------------------------------')
    s = datetime.datetime.now()
    putong()
    e = datetime.datetime.now()

    print(e - s)
    time.sleep(2)

    s1 = datetime.datetime.now()
    sc = shengchengQi()  # 这一步不是调用函数---而是创建生成器
    # 验证暂停---到yield的时候暂停---直到下一次遍历才继续开始----参考:生成器.jpg
    print("验证暂停：", next(sc))
    print("和上一步验证执行顺序：", next(sc))
    # 取所有值
    # while True:
    #     try:
    #         v = print(next(sc))
    #     except Exception as e:
    #         print("返回值:", e.value)
    #         print("异常：", e)
    #         break
    e1 = datetime.datetime.now()
    print(e1 - s1)

    print('-----------------------------------启动方式二:send()-----------------------------------------')
    # 不传参数报错
    # 得用next(生成器对象)起步否则------TypeError: can't send non-None value to a just-started generator----因为send设置的参数无人接收
    # 传参的作用---可以改变是生成器中的某些元素的值   例如count (改变开始位置--参考以上生成器)
    sc2 = shengchengQi2()
    # next(sc2)
    sc2.send(None)  # 第一次可以传参None----一般用next
    va = sc2.send('l')
    print(va)
    va = sc2.send('hello')
    print(va)

# 耗时对比
# 0: 00:00.137008
# 0: 00:00
