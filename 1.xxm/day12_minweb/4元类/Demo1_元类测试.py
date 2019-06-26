@staticmethod
def static_method():
    print('静态方法...')


@classmethod
def class_method(cls):
    print('类方法...')


# 实例方法
def sl_m(self):
    print('实例方法...')


A = type('A', (), {'num': 10, 'cl_m': class_method, 'st_m': static_method, 'sl_m': sl_m})


def main():
    # print(help(A))
    print("--------------------")
    a = A()
    A.cl_m()
    a.st_m()
    a.sl_m()


if __name__ == '__main__':
    main()
