# 继承不是复制    而是本类中找不到就去父类中找

class P():
    x = 1


class S1(P):
    pass


class S2(P):
    pass


def main():
    S1.x = 2
    P.x = 3
    print(P.x, S1.x, S2.x)


if __name__ == '__main__':
    main()
