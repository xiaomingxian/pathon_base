# *args, **kwargs   放在形参会自动装包
# *args, **kwargs   放在实参会自动拆包


def test2(a, b, *args, **kwargs):
    print('--------test2-------')
    print(a)
    print(b)
    print(args)
    print(kwargs)
    pass


# 形参
def test(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    # 实参
    test2(a, b, *args, **kwargs)
    pass


def main():
    # 换顺序会报错
    test(1, 2, 'aaa', name='tom', age=18)


if __name__ == '__main__':
    main()
