from lxml import etree
import requests


class JapaneseDir(object):
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f/index/forumpark?cn=%E7%BE%8E%E5%89%A7&ci=0&pcn=%E7%94%B5%E8%A7%86%E5%89%A7&pci=0&ct=1&rn=20&pn={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }

    def send(self):
        content = requests.get(url=self.url, headers=self.headers)
        # 解析结果


def main():
    pass


if __name__ == '__main__':
    main()
