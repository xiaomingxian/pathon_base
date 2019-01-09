# 函数名是引用指向函数    引用发生变化  原函数会被覆盖(指向发生了改变)

def fun():
    print('----')


# 匿名函数
fun = lambda x: x + 1;


def main():
    x = fun(1)
    print(x)


if __name__ == '__main__':
    main()
