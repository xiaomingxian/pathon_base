# /跟目录
# //li  选取li元素不考虑它的位置
# @href
# //ul[@id='xxx']
# xxx/test()  获取文本
# xpath helper
# /a[1]  选择第几个  /a[last]  /a[last-1]
# a/[position<3] 某几个
# 06-04 lxml
from lxml import etree
import requests


def main():
    #
    list = ['//li[@class="ui-slide-item" and @data-title="%s"]/@%s',
            '//li[@class="ui-slide-item s" and @data-title="%s"]/@%s']
    list2 = ['data-release', 'data-rate', 'data-star', 'data-trailer', 'data-ticket', 'data-duration',
             'data-region', 'data-director', 'data-actors', 'data-intro', 'data-enough', 'data-rater']
    list3 = []
    r = requests.get('https://movie.douban.com/')

    html = etree.HTML(r.content)
    # 先获取所有的title---再根据title去限定
    x = html.xpath('//li[@class="ui-slide-item"]/@data-title| //li[@class="ui-slide-item s"]/@data-title')
    for i in x:
        x = {}
        x['title'] = i
        list3.append(x)
    # 根据title取查询其他字段

    for l in list:
        for j in list2:
            for i in list3:
                title = i['title']
                parse_str = l % (title, j)
                # print(parse_str)
                con = html.xpath(parse_str)
                # print('====>', len(con))
                if len(con):
                    i[j] = con[0]
    # print(r.content.decode())

    for i in list3:
        with open('file/DouBanMovie.txt', 'a', encoding='utf8') as f:
            yu = '有' if i['data-enough'] == 'true' else '无'
            jian = '无' if i['data-intro'] == '' else i['data-intro']
            f.write('%s' * 10 % (
                '【电影】：' + i['title'] + '\t\n',
                '\t年份：' + i['data-release'] + '\n',
                '\t评分：' + i['data-rate'] + '\n',
                '\t星星：' + i['data-star'] + '\n',
                '\t时长：' + i['data-duration'] + '\n',
                '\t国家：' + i['data-region'] + '\n',
                '\t导演：' + i['data-director'] + '\n',
                '\t主演：' + i['data-actors'] + '\n',
                '\t简介：' + jian + '\n',
                '\t余票：' + yu + '\n'
            ))
            f.write('\n')
    print('-------->OK')


def test():
    l = [1, 2, 3]
    print(l[0])


if __name__ == '__main__':
    main()
    # test()
