from sklearn.feature_extraction import DictVectorizer


# pip，numpy版本得对应


# 特征抽取----将数据数值化
def main():
    # 实例化
    # 参数指定两种格式
    dict = DictVectorizer()
    # dict = DictVectorizer(sparse=False)
    # 载入数据
    # 内部使用scipy基于numpy
    # 结果展现sparse矩阵  节约内存，方便读取处理
    data = dict.fit_transform([
        {'city': 'beijing', 'template': 20},
        {'city': 'shanghai', 'template': 50},
        {'city': 'shenzhen', 'template': 100}
    ])
    print(data)
    print('特征类型：', dict.get_feature_names())
    # One-Hot编码  1/0 标记有没有  没有优先级
    pass


if __name__ == '__main__':
    main()
