# 朴素贝叶斯
from sklearn.naive_bayes import MultinomialNB
from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
# 准确率-召回率
from sklearn.metrics import classification_report


def main():
    '''
    读取文章
    对文章进行重要性分类(过滤掉共性的不重要的词语)
    使用贝叶斯算法进行预测(参数：关键词数据化[个人理解-->基于算法模型理解])
    :return:
    '''

    # 获取所有的新闻数据
    news = fetch_20newsgroups(subset='all', data_home='/Users/xxm/develop/py_workspace/otherdata_home/news_home')

    # 数据分割
    tz_train, tz_test, mb_train, mb_test = train_test_split(news.data, news.target, test_size=0.25)

    # 对数据集进行特征抽取[重要性词语]
    tf = TfidfVectorizer()
    # 对训练集进行训练---抽取重要性词语特征
    tz_train = tf.fit_transform(tz_train)
    # 数据分词后 及其每个词对应的数据重要性指标
    print(tz_train.toarray())
    # print(tf.get_feature_names())
    tz_test = tf.transform(tz_test)

    # 进行朴素贝叶斯算法预测
    # 实例化朴素贝叶斯算法
    mul = MultinomialNB(alpha=1)
    # 朴素贝叶斯算法 输入参数 要求是分词后的特征值？？？？[应该是这样]
    mul.fit(tz_train, mb_train)
    # 进行预测
    article_type = mul.predict(tz_test)
    print(len(article_type), article_type)

    score = mul.score(tz_test, mb_test)
    print('预测准确率：', score)

    # -------------------精确率与召回率[类型检测-不适合此处案例]
    print('精确率：', classification_report(mb_test, article_type, target_names=news.target_names))  # 预测值，目标值  文章类别字符串
    # precision精确率  recall召回率  f1-score得分  support样本数量
    pass


if __name__ == '__main__':
    main()
