class yuan(type):
    pass

    def __new__(cls, lname, funs, params):
        # 将函数的参数的key变为大写
        new_params = {}
        for key, value in params.items():
            if not key.startswith("__"):
                new_params[key.upper()] = value

        return type(lname, funs, new_params)

        pass


# metaclass=yuan---这一步相当于type(...)  这里是 yuan(...) 创建type对象会调用 __new__
class A(object, metaclass=yuan):
    num = 10


def main():
    help(A)


if __name__ == '__main__':
    main()
