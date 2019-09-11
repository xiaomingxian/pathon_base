import pandas as pd
import ssl
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
# 逻辑回归
from sklearn.linear_model import LogisticRegression
# 召回率
from sklearn.metrics import classification_report

ssl._create_default_https_context = ssl._create_unverified_context


def main():
    '''
    逻辑回归做二分类
    :return:
    '''
    # 默认会将第一行作为特征名
    # colums = ['c' + str(i) for i in range(1, 12)]
    colums = ['id', '块厚度', '细胞大小的一致性', '电池形状的均匀性', '边缘着附力', '单个上皮细胞大小'
                                                            '裸核', '平淡的染色质', '正常核', '有丝分裂', '分类(2良性,4恶性)']
    # print(colums)
    data = pd.read_csv(
        'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data'
        , names=colums)

    # 替换缺失值
    data.replace(to_replace='?', value=np.nan, inplace=True)
    # 删除nan
    data = data.dropna()
    # print(data)

    # 数据分割
    x_train, x_test, y_train, y_test = train_test_split(data[colums[1:10]],
                                                        data[colums[9]],
                                                        test_size=0.25)

    # 进行标准化处理--此处是分类问题-目标值不用标准化
    std = StandardScaler()
    x_train = std.fit_transform(x_train)
    x_test = std.transform(x_test)

    # 逻辑回归预测 可调参
    logic = LogisticRegression(C=1.0)

    logic.fit(x_train, y_train)

    pre = logic.predict(x_test)
    # 回归系数
    print(logic.coef_)

    # 准确率
    score = logic.score(x_test, y_test)
    print(score)

    # 召回率
    print('召回率：', classification_report(y_test, pre, labels=[2, 4], target_names=['良性', '恶性']))

    pass


if __name__ == '__main__':
    main()
