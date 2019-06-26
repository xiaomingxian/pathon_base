from lxml import etree
import requests


def main():
    url = "http://whois.chinaz.com/suffix"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }

    while 1:
        context = requests.get(url=url, headers=headers)

        print(context.content.decode('utf-8'))
    pass


if __name__ == '__main__':
    main()
