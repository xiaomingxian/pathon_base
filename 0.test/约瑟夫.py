def main():
    nums = 41
    call = 3

    # 参数定义：
    peoples = []
    for _ in range(nums):
        # True定义状态为活
        peoples.append(True)

    result = []
    num = 1
    # 主逻辑
    while (any(peoples)):  # peoples中存在任何True元素
        # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
        for index, people in enumerate(peoples):
            if people:#如果人存活True
                if num == call:
                    peoples[index] = False
                    result.append(index + 1)  # index是从0开始 但是值是从1开始
                    #                print(index+1)#每轮的出局者
                    #                print(peoples)#每次的队列状态
                    num = 1  # 找到后就计数归为初始值 接着从上次循环的位置开始计数
                else:
                    num += 1
    print('-' * 25)
    print('\n总数为%d,报数为%d' % (nums, call))
    print('约瑟夫序列为：\n%s\n' % result)
    print('-' * 25)

    print(any([False]))

    pass


if __name__ == '__main__':
    main()
