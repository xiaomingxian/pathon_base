class Parent(object):
    def __init__(self):
        print('Parent...')
        super().__init__()

    pass


class Son1(Parent):
    def __init__(self):
        print("Son1...")
        super().__init__()

    pass


class Son2(Parent):
    def __init__(self):
        print("Son2...")
        super().__init__()

    pass


class GrandSon(Son1, Son2):
    def __init__(self):
        print("GrandSon...")
        # 不指定
        # super().__init__()
        # 指定
        super(Son2, self).__init__()

    pass


def main():
    print(GrandSon.__mro__)
    GrandSon()


if __name__ == '__main__':
    main()
