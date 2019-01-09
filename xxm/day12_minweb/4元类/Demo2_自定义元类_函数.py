# coding=utf-8

# 自定义元类---函数
def MyType(lname, fus, params):
    # 还可以进行其他 操作  例如python3的类 都继承object 可以遍历 fus 判断元组内有没有object 没有就添加
    new_params = {}
    for name, value in params.items():
        # 过滤魔法/私有属性
        if not name.startswith('__'):
            new_params[name.upper()] = value
    return type(lname, fus, new_params)


# 使用自定义 元类 (将属性key变成大写)
class A(object, metaclass=MyType):
    num = 10





def main():
    print('------------元类应用------------')
    print('---------------------------')
    # 源于 type
    print(A().__class__)
    print(A().__class__.__class__)
    # 自定义元类
    print(help(A))


if __name__ == '__main__':
    main()
