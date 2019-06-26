# 切片测试
def main():
    list = [1, 2, 3, 4, 5]
    # 切片参数传的是索引，包前不包后   -1表示最后一个前一个为-2
    # x = list[1:-1]
    # 第几个及其以后
    x = list[1:]
    print(x)
    pass


if __name__ == '__main__':
    main()
