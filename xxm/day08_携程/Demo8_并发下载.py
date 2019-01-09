import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()


def download(name, url):
    # print('拷贝', url)
    yuan = urllib.request.urlopen(url)
    r = yuan.read()
    with open(name, 'wb') as f:
        f.write(r)


def main():
    gevent.joinall([

        gevent.spawn(download, '1.jpg',
                     'https://gss1.bdstatic.com/9vo3dSag_xI4khGkpoWK1HF6hhy/baike/whfpf%3D135%2C180%2C50/sign=150575eb80b1cb133e3c6f53bb69677d/5ab5c9ea15ce36d3f4949d3437f33a87e950b125.jpg'),

        gevent.spawn(download, '2.jpg',
                     'https://gss1.bdstatic.com/9vo3dSag_xI4khGkpoWK1HF6hhy/baike/s%3D220/ sign=a988a813740e0cf3a4f749f93a47f23d / a044ad345982b2b7e9783cc537adcbef77099bcf.jpg'),

        gevent.spawn(download, '3.jpg',
                     'https://gss0.bdstatic.com/-4o3dSag_xI4khGkpoWK1HF6hhy/baike/s%3D220/sign=f849178558df8db1b82e7b663923dddb/c2cec3fdfc03924572a1f7128194a4c27d1e2592.jpg')

    ])

    # download('1.jpg',
    #          'https://gss1.bdstatic.com/9vo3dSag_xI4khGkpoWK1HF6hhy/baike/s%3D220/ sign=a988a813740e0cf3a4f749f93a47f23d / a044ad345982b2b7e9783cc537adcbef77099bcf.jpg')


if __name__ == '__main__':
    main()
