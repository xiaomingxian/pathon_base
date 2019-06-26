import json


def main():
    # 对象转json
    s = json.dumps({'s': 'x', 'k': 'v'})
    print(s, type(s))
    # json转对象
    x = json.loads(s)
    print(x, type(x))
    pass


# 读取json文件---直接转换
def read():
    pass
    # 读取json为对象
    with open('file/json_str.json', 'r', encoding='utf8') as f:
        x = json.load(f)
        print(x, type(x))

    # 将对象以json形式写入
    # with open('file/json_str.json', 'w', encoding='utf8') as f:
    #     json.dump({'k1': 'v1', 'k2': 'v2'}, f)


if __name__ == '__main__':
    # main()
    read()
