import requests


class serach():
    def __init__(self):
        self.url = url = 'https://tieba.baidu.com/p/2501933226?pn={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

        pass

    def search(self):
        for i in range(31, 201):
            print('第 ', i, ' 页')
            url = self.url.format(i)
            res = requests.get(url=url, headers=self.headers)
            # print(i, res.status_code, res.content.decode('utf8'))
            self.save('贴吧内容', res.content, i)
        pass

    def save(self, filename, contetx, num):
        try:
            path = 'd:/pachong/{}第{}页.html'
            with open(path.format(filename, num), 'wb') as f:
                f.write(contetx)
        except Exception as e:
            print('页码：', num, '  异常: ', e)
            pass

        pass


def main():
    search = serach()
    search.search()
    pass


if __name__ == '__main__':
    main()
