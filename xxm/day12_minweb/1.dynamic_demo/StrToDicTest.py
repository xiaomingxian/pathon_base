def main():
    str = '{"aa":"aa","bb":"bb"}'
    dic = eval(str)
    print(dic)
    print('-----------------------------')
    a=A()
    a('jjj')


def que(z, x=1, y=3):
    pass


class A(object):
    def __call__(self, *args, **kwargs):
        print(args)

if __name__ == '__main__':
    main()
