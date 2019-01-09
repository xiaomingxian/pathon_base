import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}


def main():
    url = 'https://www.baidu.com/s'
    # 身份标识
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    # 参数
    param = {'wd': '北京'}
    res = requests.get(url=url, headers=headers, params=param)

    print('状态：', res.status_code)
    print('url: ', res.request.url)
    con = res.content.decode('utf8')
    print(con)


def test():
    url = 'https://www.baidu.com/s?wd={}'.format("北京")
    res = requests.get(url)
    print(res.request.url)


def format_test():
    s = "哈{}哈{}哈{}".format(1, {'key': 'value'}, [5, 6])
    print(s)


# 保存爬虫内容到本地
def save():
    pass


if __name__ == '__main__':
    pass
    # main()
    # test()
    # format_test()
