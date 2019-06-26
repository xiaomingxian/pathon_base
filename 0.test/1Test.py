import re

a = 'abc'
b = 'dfe'

x = re.sub('\w', a, b)


def main():
    print(x)
    print(re.match('\d+', "45515"))
    print("sasaa"[1:2])
    print('-----------dicTest------------')
    dic = {'a': 1, 'b': 2, 'c': 3}
    list = [1, 2, 3, 4, 5, 6]
    # dic.pop('a')
    # print(dic)
    print('---------并发修改测试---------')
    for i in list:
        if i == 4:
            list.__delitem__(i)
    print(list)

    # dic有并发修改异常
    # for k,v in dic.items():
    #     if k=='c':
    #         dic.pop(k)
    # print(dic)
    print('------------------ 字符串拼接数组测试 -------------------')
    # 列表的元素必须是字符串格式
    print(list)
    # int 类型 list 转 str
    print([str(i) for i in list])
    print(",".join(['1', '2', '3']))
    [print(i) for i in 'sasa']


class B(RuntimeError):

    def __init__(self, *args):
        self.name = 10
        print("异常测试...")
        pass

    def __str__(self):
        return str(self.__dict__)


if __name__ == '__main__':
    main()
    a = 10.43
    print(B())

    if a > 1:
        raise B("你好")
