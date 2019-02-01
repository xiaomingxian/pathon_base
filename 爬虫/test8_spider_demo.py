import requests
import re


class MySpider(object):
    def __init__(self):
        self.page = 0
        self.url = 'http://www.budejie.com/text/%i'
        self.heads = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36'}
        pass

    def parse_url(self):
        r = requests.get(url=self.url % (self.page + 1), headers=self.heads)
        self.page += 1
        return r.content.decode()

    def getMessage(self, content):
        message = re.findall(
            r'<div class="j-r-list-c">.*?<div class="j-r-list-c-desc">[.*?\s?]*<a href="/detail-.*?>(.*?)</a>.*?</div>',
            content, re.S)
        return message
        pass

    def save(self, message):
        for i in message:
            with open('file/duanzi.txt', 'a', encoding='utf8') as f:
                f.write(i)
                f.write('\r\n')
                pass

    def run(self):
        for i in range(0, 2):
            # while True:
            content = self.parse_url()
            message = self.getMessage(content)
            self.save(message)
            print('-----page: ', self.page)


def mian():
    sp = MySpider()
    try:
        sp.run()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    mian()
