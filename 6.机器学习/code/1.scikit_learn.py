from sklearn.feature_extraction import DictVectorizer
# 文本次数统计
from sklearn.feature_extraction.text import CountVectorizer
# tf-idf
from sklearn.feature_extraction.text import TfidfVectorizer
# 归一化(预处理中的包)
from sklearn.preprocessing import MinMaxScaler
# 标准化
from sklearn.preprocessing import StandardScaler
# 中文分词库
import jieba


# pip，numpy版本得对应


# 特征抽取----将数据数值化[进行计算]

# 字典特征抽取
def main():
    # 实例化
    # 参数指定两种格式 (是否立即替换)
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


# 文本特征抽取  次数
def textTz():
    # 实例化
    cv = CountVectorizer()

    # sparse矩阵
    data = cv.fit_transform(['人生苦短 我用python', 'life is short i choice python', 'life is long i choice java'])

    # print(data)

    # 7 个单词 --->单个字母不统计 因为单个字母没有情感倾向，没有分类依据
    # 中文 空格分开会更详细的分词语   单个汉字没有情感倾向  jieba分词
    print(cv.get_feature_names())
    # 对单词出现次数的统计
    print(data.toarray())

    pass


# 中文文本特征抽取
def parse_chines():
    t1, t2, t3 = chinese()
    # 实例化
    cv = CountVectorizer()
    # sparse矩阵
    data = cv.fit_transform([t1, t2, t3])
    # 查看特征
    print(cv.get_feature_names())
    print(data.toarray())
    pass


# 重要性分析
def tf_idf():
    t1, t2, t3 = chinese()
    # 实例化
    tf = TfidfVectorizer()
    #
    data = tf.fit_transform([t1, t2, t3])
    # 重要性分析
    print(tf.get_feature_names())
    print(data.toarray())

    pass


# 归一化
# 归一化demo 相亲对象约会数据 (对一个人多个维度的特征进行打分)[多个维度的特征同等重要]
def guiyi():
    # 实例化--参数可不指定，默认是0-1
    mm = MinMaxScaler(feature_range=(1, 2))
    #  参数得是二维数组 因为是针对列的操作
    data = mm.fit_transform([[90, 2, 10, 40], [60, 4, 15, 45], [75, 3, 13, 46]])
    # 得到的值形状于数组形状相同 不过 每个位置是原数值 计算的结果
    print(data)
    pass


# 标准化
def stander():
    # 实例化
    st = StandardScaler()
    #
    # data = st.fit_transform([[1, -1, 3], [2, 4, 2], [4, 6, -1]])
    data = st.fit_transform([[1, 2, 3], [2, 4, 2], [4, 6, 1]])
    print(data)
    pass


# 对中文进行分词 拼接
def chinese():
    y1 = '可迭代对象都具有__iter__函数，并且可迭代对象通过iter()函数会返回一个迭代器，迭代器内部具有一个状态，该状态用于记录当前迭代所在的位置方便下一次迭代';
    y2 = '迭代器是一种带状态的对象，它能在你调用next()方法的时候返回容器中的下一个值，任何实现了__iter__和__next__方法的对象都是迭代器，__iter__返回迭代器本身，__next__返回容器中的下一个值，当遍历到最后一个值，没有元素的时候会抛出StopIteration异常'
    y3 = '尽管绝大多数容器都提供了某种方式来获取其中的每一个元素，但这并不是容器本身提供的能力，而是**可迭代对象**赋予了容器这种能力，当然并不是所有的容器都是可迭代的，比如：[Bloom filter]，虽然Bloom filter可以用来检测某个元素是否包含在容器中，但是并不能从容器中获取其中的每一个值，因为Bloom filter压根就没把元素存储在容器中，而是通过一个散列函数映射成一个值保存在数组中'

    # 分词--生成的是迭代器[生成器]
    r1 = jieba.cut(y1)
    r2 = jieba.cut(y2)
    r3 = jieba.cut(y3)
    # 生成器可以直接用list转换成列表
    print(type(r1))  # 生成器： <class 'generator'>
    l1 = list(r1)
    l2 = list(r2)
    l3 = list(r3)
    # print(l1)
    # print(l2)
    # print(l3)

    t1 = ' '.join(l1)
    t2 = ' '.join(l2)
    t3 = ' '.join(l3)

    # 把列表转换为字符串 用 ' ' 拼接，为了便于特征工程分析
    return t1, t2, t3


if __name__ == '__main__':
    # main()
    # textTz()
    # chinese()
    # parse_chines()
    # tf_idf()
    # guiyi()
    stander()
