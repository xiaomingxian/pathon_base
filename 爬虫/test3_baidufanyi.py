import requests


def main():
    msg = input()
    param = {'query': msg, 'from': 'zh',
             'to': 'en'}

    headars = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    # url = 'https://fanyi.baidu.com/translate?aldtype=16047&query=%E4%BD%A0%E5%A5%BD%0D%0A&keyfrom=baidu&smartresult=dict&lang=auto2zh#zh/en/%E4%BD%A0%E5%A5%BD'
    url = 'http://fanyi.baidu.com/basetrans'
    res = requests.get(url, headers=headars, data=param)

    print(res.status_code, res.content.decode('utf-8'))


if __name__ == '__main__':
    main()
