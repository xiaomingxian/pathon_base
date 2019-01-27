import requests


# 解码  python3:
# response.decode()  utf-8
# response.decode('gbk')
# response.content()  获取到的是二进制数据
# response.text()  获取到的是字符串
# 模拟登陆的三种方式----
def main():
    # 模拟一个登陆后才能访问的页面
    # requests  的session模块在内部处理了cookie
    pass
    session = requests.session()
    # url = 'https://github.com/session'
    # data = {'login': 'xiaomingxian', 'password': 'XIan_934792834'}
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    #
    # session.post(url,data=data,headers=headers)
    r = session.get('https://github.com/xiaomingxian')
    print(r.content)
    with open('download/a.html', 'w', encoding='utf8') as f:
        f.write(r.content.decode())


def cookie_method():
    pass
    url = 'https://github.com/session'
    data = {'login': 'xiaomingxian', 'password': 'XIan_934792834'}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Cookie': 's'
    }

    requests.get('url', headers=headers)


def cookie_m2():
    pass
    url = 'https://github.com/session'
    data = {'login': 'xiaomingxian', 'password': 'XIan_934792834'}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

    }
    cs = {i.split('=')[0]: i.split('=')[1] for i in '模拟cookie'.split(';')}

    requests.get('url', headers=headers, cookies=cs)


if __name__ == '__main__':
    main()
