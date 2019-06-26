import requests
from lxml import etree


class TieBa(object):
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f/index/forumpark?cn=%E7%BE%8E%E5%89%A7&ci=0&pcn=%E7%94%B5%E8%A7%86%E5%89%A7&pci=0&ct=1&rn=20&pn={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }

    def parse_url(self):
        i = 1
        url = self.url.format(i)
        r = requests.get(url=url, headers=self.headers)
        html = etree.HTML(r.content)
        # 最后一页
        t = html.xpath('//div[@class="square_pager"]/div[@class="pagination"]/a[@class="last"]/@href')[0].split('&')[
            -1].split('=')[-1]
        while i <= int(t):
            itim = {}
            url = self.url.format(i)
            r = requests.get(url=url, headers=self.headers)
            htm = etree.HTML(r.content.decode())
            # print(etree.tostring(htm))
            hh = htm.xpath(
                '//div[@class="ba_post "]/a[@rel="noopener"]/text()')
            for j in hh:
                print(j)
            # print(etree.tostring(hh[0]))
            # 解析结果
            itim['pic'] = self.find_pic()
            itim['message'] = self.getMessage()
            i += 1

    def getMessage(self):
        return
        pass

    def find_pic(self):
        return
        pass

    pass


def main():
    t = TieBa()
    t.parse_url()
    pass


if __name__ == '__main__':
    main()
