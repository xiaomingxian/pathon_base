class A(object):
    def __init__(self,a):
        print('init...')

    def __new__(cls, *args, **kwargs):
        print('new ...')
        return super().__new__(cls)


def main():
    a = A(1)


if __name__ == '__main__':
    main()
