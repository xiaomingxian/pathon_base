# 匿名函数
fun = lambda x: x + 1;


class A():
    pass


def main():
    print(A.__dict__)
    fun(1)


if __name__ == '__main__':
    main()
    x = 1
    print(fun(1))
