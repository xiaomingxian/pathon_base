# 豆瓣电影爬取---区分国家 json对象可以动态添加属性
# 36kr爬取

import requests
import re


class DouBanMovie(object):

    def __init__(self):
        self.url = 'https://movie.douban.com/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    def parse_url(self):
        r = requests.get(url=self.url, headers=self.headers)
        return r.content.decode()
        pass

    def save(self):
        content = self.parse_url();
        # c = re.findall(r'<ul class="ui-slide-content".*?>[.*|\s]*<li class="poster">[.*|\s]*<img(.*?)">',
        c = re.findall(
            # r'<li class="poster">[.*|\s]*<.*?>[.*|\s]*<img src=".*?" alt="(.*?)".*?>[.*|\s]*</a>[.*|\s]*</li>[.*|\s]*<li class="title">',
            r'<li class="ui-slide-item s|ui-slide-item".*?data-title="(.*?)" data-release="(.*?)" data-rate="(.*?)" data-star="(.*?)".*?'
            r'data-duration="(.*?)" data-region="(.*?)" data-director="(.*?)" data-actors="(.*?)" data-intro="(.*?)" data-enough="(.*?)" data-rater="(.*?)".*?>'
            r'[.*|\s]*<ul class="">'
            ,
            content,
            re.S)
        for i in c:
            print(i)
        # print(content)
        pass

    pass


def main():
    movie = DouBanMovie()
    content = movie.save()

    pass


if __name__ == '__main__':
    main()
