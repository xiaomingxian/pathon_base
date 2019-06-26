import requests
from pip._vendor.retrying import retry


# 有异常出现就重新尝试 --直到最大次数为止
@retry(stop_max_attempt_number=3)
def main():
    print('*' * 20)
    pass
    # 将cookie转为字典
    r = requests.get('http://www.baidu.com')
    cook_dic = requests.utils.dict_from_cookiejar(r.cookies)
    print(cook_dic)
    #     url 编码解码
    res = requests.utils.quote('http://www.baidu.com?kw=奥特曼')
    print(res)
    un = requests.utils.unquote('http%3A//www.baidu.com%3Fkw%3D%E5%A5%A5%E7%89%B9%E6%9B%BC')
    print(un)
    # ssl证书验证 12306demo 认证方式不同
    # verify=False忽略安全认证 默认是true
    resp = requests.get('https://www.12306.cn/mormhweb/', verify=False)
    print(resp)

    # 1 / 0 #retry test
    pass


if __name__ == '__main__':
    try:
        main()
    except:
        print('----')
