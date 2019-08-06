# 保存模型
from sklearn.externals import joblib
#
from sklearn.datasets import load_boston
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def main():
    # 获取数据
    lb = load_boston()
    # 分割数据集到训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(lb.data, lb.target, test_size=0.25)

    # 进行数据标准化处理(特征值与目标值都得标准化-目标值根据特征值求出[参考公式]) [两个标准化api:特征值[多列]/目标值[因为只有一列]]
    # 特征是
    std_x = StandardScaler()
    x_train = std_x.fit_transform(x_train)
    x_test = std_x.transform(x_test)
    # 目标值
    std_y = StandardScaler()

    std_y.fit_transform(y_train.reshape(-1, 1))  # 等同于以下写法 n行1列
    # std_y.fit_transform(y_train.reshape(len(y_train),1))
    std_y.transform(y_test.reshape(-1, 1))
    # estimator预测
    # 正规方程求解方式预测结果
    lr = LinearRegression()
    lr.fit(x_train, y_train)

    # 保存训练好的模型--二进制文件
    # save(lr, '../source/lr_test.pkl')

    # 使用保存好的模型进行预测
    y_pre=use('../source/lr_test.pkl',x_test)
    print('预测的结果：\n',std_y.inverse_transform(y_pre))

    pass


def save(mx, loc):
    joblib.dump(mx, loc)

    pass


def use(file,test):
    model=joblib.load(file)
    y_pre=model.predict(test)

    return y_pre


if __name__ == '__main__':
    main()
