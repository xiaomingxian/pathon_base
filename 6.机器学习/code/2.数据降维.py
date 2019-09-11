# 过滤器[方差过滤]   特征选择包中
from sklearn.feature_selection import VarianceThreshold
# PCA
from sklearn.decomposition import PCA

import pandas as pd


# 方差过滤[过滤掉雷同的数据]
def variance():
    # 删除低方差特征   threshold默认参数为0.0[过滤方差为0的数据]    threshold的值根据数据而定
    var = VarianceThreshold(threshold=1)

    data = var.fit_transform([[1, 2, 3, 4, 5], [1, 3, 4, 9, 6], [1, 4, 100, 6, 7]])

    print(data)
    pass


# PCA:主成分分析 简化数据集
# 数据维数压缩，尽可能降低原始数据的维数(复杂度),损失少量信息
# 场景：特征达到数百
# 存在的问题：特征可能相关联 eg:
def pca_demo():
    '''
    主成分分析 进行特征降维
    :return:
    '''
    # 保留90% 怎么验证
    pca = PCA(n_components=0.9)
    data = pca.fit_transform([
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 77],
        [1, 2, 3, 4, 5, 44],
        [6, 7, 8, 9, 0, 22]])
    print(data)
    pass


# 商品-订单-类型 合表(多表关联查询)
def pac_demo2():
    product = pd.read_csv('../source/product.csv')
    order = pd.read_csv('../source/order.csv')
    type = pd.read_csv('../source/type.csv')
    pro_type = pd.read_csv('../source/pro_type.csv')
    # 合并
    pro_order = pd.merge(product, order, on=['product_id', 'product_id'])
    type_pro = pd.merge(type, pro_type, on=['type_id', 'type_id'])

    data = pd.merge(type_pro, pro_order, on=['product_id', 'product_id'])

    # print(data)

    # 交叉表---指定行/列
    data = pd.crosstab(data['user_id'], data['type_id'])

    print(data.shape)
    # 主成分分析
    pca = PCA(n_components=0.9)
    data = pca.fit_transform(data)
    print(data)
    print(data.shape)
    pass


if __name__ == '__main__':
    # variance()
    # pca_demo()
    pac_demo2()
