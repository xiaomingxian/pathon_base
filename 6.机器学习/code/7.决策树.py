import pandas as pd
# 导入字典
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
# 决策树
from sklearn.tree import DecisionTreeClassifier, export_graphviz  # 可视化
import graphviz


def main():
    '''
    泰坦尼克号预测生死
    :return:
    '''
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

    print(dic.get_feature_names())
    # print(x_train)
    # print(x_test)

    # 使用决策树[估计器]
    dec = DecisionTreeClassifier(max_depth=5)
    dec.fit(x_train, y_train)

    print('预测结果-准确率：', dec.score(x_test, y_test))

    # 导出决策树的结构
    export_graphviz(dec, out_file='../pic/shu.dot', feature_names=['年龄', '一层', '二层', '三层', '女性', '男性'])

    pass


def read_dot():
    # 环境未配置
    # pip3 install graphviz
    with open('../pic/shu.dot') as f:
        fr = f.read()
    dot = graphviz.Source(fr)
    dot.view()

    pass


if __name__ == '__main__':
    main()
    # read_dot()
