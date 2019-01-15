import requests
import json
import sys


def main():
    msg = input()
    # msg=sys.argv[1]#[0是文件名]
    param = {'query': msg, 'from': 'zh',
             'to': 'en'}

    # headars = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    # }

    # 曲线救国----手机端方式
    headars = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36',

    }

    # url = 'https://fanyi.baidu.com/translate?aldtype=16047&query=%E4%BD%A0%E5%A5%BD%0D%0A&keyfrom=baidu&smartresult=dict&lang=auto2zh#zh/en/%E4%BD%A0%E5%A5%BD'
    url = 'http://fanyi.baidu.com/basetrans'
    res = requests.get(url, headers=headars, params=param)

    # print(res.status_code, res.content.decode('utf-8'))
    print(json.loads(res.content.decode('utf-8'))['trans'][0]['dst'])

def sys_test():
    import sys
    print(sys.argv)
    # sys.argv[1]


if __name__ == '__main__':
    main()
    # sys_test()