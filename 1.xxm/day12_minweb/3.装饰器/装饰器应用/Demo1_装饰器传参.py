# 传参  级别认定(自定义删选)
def parm(parm):
    # 传被增强函数引用
    def out(fun):
        # 实际执行(接收函数的参数...)
        def inner(*args, **kwargs):
            if parm == 1:
                print('----权限验证1----')
            elif parm == 2:
                print('----权限验证2----')
            return fun()

        return inner

    return out


# 传参得到 返回的函数引用就是  装饰的函数 out 对test进行装饰
@parm(1)
def test():
    print('------test------')


@parm(2)
def test2():
    print('------test------')


def main():
    test()
    print('-------分割线-------')
    test2()


if __name__ == '__main__':
    main()
