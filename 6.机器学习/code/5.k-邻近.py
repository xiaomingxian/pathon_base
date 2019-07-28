from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import random
import time


def get_loc():
    li = []
    for i in range(500):
        place_id = random.randint(100000000, 9999999999)
        li.append(place_id)
        pass
    return li


# 造数据
def create_data():
    first = 'row_id,x,y,accuracy,time,place_id\n'

    li = get_loc()
    with open('../source/loc.csv', 'a') as f:
        f.write(first)
        for i in range(0, 100000):
            row_id = i
            x = round(random.uniform(0, 10), 4)
            y = round(random.uniform(0, 10), 4)
            accuracy = random.randint(0, 100)
            r_time = get_time()
            place_id = random.sample(li, 1)[0]
            oneLine = ','.join([str(row_id), str(x), str(y), str(accuracy), str(r_time), str(place_id)]) + '\n'

            f.write(oneLine)
        pass


def main():
    # 读取与构造数据
    data = read_data()
    # print(data)

    # 把签到少于n个的数据删除-----按place_id分组后 行索引就变成了place_id
    plac_count = data.groupby('place_id').count()
    # 数据删选后 索引归位
    plac_count = plac_count[plac_count['x'] > 200].reset_index()
    # print(plac_count)

    # 取出特征值和目标值
    mb = data['place_id']
    tz = data.drop(['place_id'], axis=1)
    # 进行数据训练测试
    # 参数  特征值  目标值 占比
    # 返回值 训练集特征值 测试集特征值  训练集目标值  测试集目标值
    tz_train, tz_test, mb_train, mb_test = train_test_split(tz, mb, test_size=0.25)

    # ------------------- 对训练集和测试集的特征进行标准化
    sta = StandardScaler()
    tz_train = sta.fit_transform(tz_train)
    tz_test = sta.transform(tz_test)
    # kjl实例化------调参 调k值  #超参数(算法实例化时的参数)
    kn = KNeighborsClassifier(n_neighbors=5)
    #
    kn.fit(tz_train, mb_train)
    # 得出预测结果
    res = kn.predict(tz_test)
    print('结果：\n', res, '\n数量：', len(res))
    # 得出准确率
    score = kn.score(tz_test, mb_test)  # 输入 训练集特征 为了得到预测值 与 目标测试集进行比对
    print('得分：', score)
    pass


def read_data():
    # 读取数据
    data = pd.read_csv('../source/loc.csv')
    # 处理数据
    # 1.缩小数据范围
    # data = data.query('x<10 & x>5')
    # print(data)
    # 处理时间戳数据
    time_val = pd.to_datetime(data['time'], unit='s')  # 单位秒
    # print(time_val)
    # 日期格式转换为字典
    time_val = pd.DatetimeIndex(time_val)
    # 构造数据
    data['month'] = time_val.month
    data['day'] = time_val.day
    data['hour'] = time_val.hour
    # 删除原来的时间特征
    data = data.drop(['time'], axis=1)
    data = data.drop(['row_id'], axis=1)

    # print(data)

    return data


def get_time():
    # 随机时间戳
    d1 = (2019, 1, 1, 0, 0, 0, -1, -1, -1)
    d2 = (2019, 8, 1, 0, 0, 0, -1, -1, -1)
    t1 = time.mktime(d1)
    t2 = time.mktime(d2)
    r_time = random.uniform(t1, t2)
    return r_time


def test():
    # 指定位数的浮点数
    x = random.uniform(0, 10)
    # print(round(x, 4))

    # 随机时间戳
    d1 = (2019, 1, 1, 0, 0, 0, -1, -1, -1)
    d2 = (2019, 8, 1, 0, 0, 0, -1, -1, -1)
    t1 = time.mktime(d1)
    t2 = time.mktime(d2)
    r_time = random.uniform(t1, t2)
    print(r_time)
    # 本地时间验证
    # print(time.asctime(time.localtime(t)))

    res = ','.join([str(1), str(2), str(3), str(4), str(r_time), str(33)]) + '\n'
    print(res, res)

    li = []
    for i in range(10):
        accuracy = random.randint(0, 100)
        li.append(accuracy)

    print(li)
    print(random.sample(li, 1)[0])
    pass


if __name__ == '__main__':
    main()
    # test()
    # create_data()
