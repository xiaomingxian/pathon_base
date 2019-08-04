# ensemble集成学习
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
# GridSearchCV 交叉验证
from sklearn.model_selection import train_test_split, GridSearchCV


def main():
    data = pd.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt")
    # print(data)
    # 提取特征 特征值与目标值
    tz = data[['pclass', 'age', 'sex']]
    res = data['survived']

    # 替换缺失值--用平均值替换
    tz['age'].fillna(tz['age'].mean(), inplace=True)

    # 分割数据集-->训练集与测试集
    x_train, x_test, y_train, y_test = train_test_split(tz, res, test_size=0.25)

    # 将数据特征化 (特征工程 one-hot编码)
    dic = DictVectorizer(sparse=False)

    # print(x_train)

    # 进行特征工程 pd转字典 特征抽取  one-hot编码
    x_train = dic.fit_transform(x_train.to_dict(orient='records'))  # orient='records') 一行对应一条记录
    x_test = dic.fit_transform(x_test.to_dict(orient='records'))  # orient='records') 一行对应一条记录

    # print(dic.get_feature_names())

    # 随机森林进行预测(超参数调优)
    rf = RandomForestClassifier()

    # 决策树数量  树深度  6*5=30次的组合
    param = {'n_estimators': [120, 200, 300, 500, 800, 1200], 'max_depth': [5, 8, 15, 25, 30]}

    # 此处 cv=2 每个参数有两次交叉验证
    gc = GridSearchCV(rf, param_grid=param, cv=2)
    gc.fit(x_train, y_train)

    print('准确率', gc.score(x_test, y_test))
    print('best:', gc.best_params_)
    pass


if __name__ == '__main__':
    main()
