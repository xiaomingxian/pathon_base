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


def main():
    s = '<a href="http://www.baidu.com"></a>'
    html = etree.HTML(s)
    r = html.xpath('//a[@*]')
    print(r)

    pass


if __name__ == '__main__':
    main()
