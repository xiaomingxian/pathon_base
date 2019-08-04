import numpy as np
# 波士顿房价数据
from sklearn.datasets import load_boston
# 正规方程/梯度下降
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def main():
    # 矩阵运算[必须得是2维]
    a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    b = [[2], [1], [3], [4]]
    res = np.dot(a, b)
    print(res)
    pass


# 线性回归
def line_test():
    # 获取数据
    lb = load_boston()
    # 分割数据集到训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(lb.data, lb.target, test_size=0.25)
    print(y_train,'\n',y_test)

    # 进行数据标准化处理(特征值与目标值都得标准化-目标值根据特征值求出[参考公式]) [两个标准化api:特征值[多列]/目标值[因为只有一列]]
    # 特征是
    std_x=StandardScaler()
    std_x.fit_transform(x_train)
    std_x.transform(x_test)
    # 目标值
    std_y=StandardScaler()

    std_y.fit_transform(y_train.reshape(-1,1))#等同于以下写法 n行1列
    # std_y.fit_transform(y_train.reshape(len(y_train),1))
    std_y.transform(y_test.reshape(-1,1))
    # estimator预测
    print('*'*100)
    # 正规方程求解方式预测结果
    lr=LinearRegression()
    lr.fit(x_train,y_train)

    print(lr.coef_)

    # 进行预测结果
    res=lr.predict(x_test)
    print('结果：\n',res)
    # 将标准化结果转为真实结果
    print('真实结果：\n',std_y.inverse_transform(res))
    pass


if __name__ == '__main__':
    # main()
    line_test()
