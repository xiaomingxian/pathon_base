# 继承了以下三个方法  还可以  当做字典使用

class Foo(object):
    def __getitem__(self, item):
        print('get %s' % str(item))
        pass


    def __setitem__(self, key, value):
        print('set %s %s' % (str(key), (value)))

    def __delitem__(self, key):
        print('del')


def main():
    obj = Foo()

    print(obj['k1'])
    obj['k2'] = 'v2'
    del obj['k1']


if __name__ == '__main__':
    main()
