import os


def main():
    print(os.path.join('aa', 'bb', 'cc'))
    # 从最后一个/开头的开始拼接,前面 的全部舍弃
    print(os.path.join('/aa', '/bb', '/cc'))
    # ./从他的前一个开始拼接
    print(os.path.join('aa', './bb', 'cc'))
    # 同时存在/优先
    print(os.path.join('aa', './bb', '/cc'))



class A():
    name=1
    age=1

    def __str__(self):
        return self.__dict__


if __name__ == '__main__':
    main()
    # print(A())
