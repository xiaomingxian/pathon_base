import requests
import json
from pymysql import *
from lxml import etree


#  基金评级
def main():

    url = 'http://landchina.mnr.gov.cn/land/jggg/gpcr1/202006/t20200610_7476600.htm'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    response = requests.get(url, headers=headers)
    response.encoding='utf-8'
    # print(response.encoding)
    # print(response.text)
    tree = etree.HTML(response.text)
    t = tree.xpath('//div[@class="gu-art-con"]/table')
    # t = tree.xpath('//table')
    for i in t:
        print(i.xpath('./tbody'))
    # print(t[0])


    pass


if __name__ == '__main__':
    main()
