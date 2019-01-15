import requests


def main():
    pass
    proxies={'http':'http://113.103.142.160:52895'}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    r=requests.get('http://www.baidu.com',proxies=proxies,headers=headers)
    print(r.status_code)
if __name__ == '__main__':
    main()
