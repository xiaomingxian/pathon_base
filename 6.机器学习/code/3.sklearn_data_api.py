# 鸢尾属植物 分类 库  Iris plants dataset
from sklearn.datasets import load_iris, fetch_20newsgroups,load_boston
# 数据测试
from sklearn.model_selection import train_test_split

import ssl

# 取消全局认证
ssl._create_default_https_context = ssl._create_unverified_context

'''
2种类型  load/fetch
'''


def load_iris_demo():
    iris = load_iris()
    # 150行 4列
    # print(iris.data)
    # 分类特征4个类别
    print(iris.target)
    print(iris.target_names)
    # print(iris.DESCR)
    # 特征名称  sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)
    # print(iris.feature_names)
    pass


# https://blog.csdn.net/fxlou/article/details/79189106
def train_test():
    risi = load_iris()
    # 被划分的样本数据集  被划分的样本标签  测试数据集占比
    # 返回值  训练集数据 测试集数据  训练集标签   测试集标签
    d_train, d_test, l_train, l_test = train_test_split(risi.data, risi.target, test_size=0.25)
    print(d_train)
    print(l_train)
    print(d_test)
    print(l_test)
    pass


# 当前python版本是3.7，网上查找说是python高版本需要验证ssl，可以添加--trusted-host domain来解决，于是赶紧尝试一下
# 以下方式不管用
# pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org  --upgrade  baostock
# 使用 取消全局认证 来解决
def fetch_test():
    # 新闻包测试
    # Downloading dataset from https://ndownloader.figshare.com/files/5975967 (14 MB)
    news = fetch_20newsgroups(data_home='/Users/xxm/develop/py_workspace/otherdata_home/news_home')
    print(news.data)
    print(news.target)

    pass


# -------------------------------- 以上都是分类算法测试 [数据是离散类型的] 以下为回归算法测试[数据是连续类型的]

def huigui():
    lb=load_boston()
    print('特征值：\n',lb.data)
    print('目标值：\n',lb.target)
    print(lb.DESCR)
    pass


if __name__ == '__main__':
    # load_iris_demo()
    # train_test()
    fetch_test()
    # huigui()
