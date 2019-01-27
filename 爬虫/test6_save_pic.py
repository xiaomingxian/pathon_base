import requests


def main():
    r = requests.get('https://www.baidu.com/img/bd_logo1.png')
    # 二进制形式写入
    with open('download/a.png', 'wb') as f:
        f.write(r.content)


def response_text():
    r = requests.get('https://www.sina.com.cn')

    r.encoding = 'utf8'
    print(r.text)


def response_content():
    r = requests.get('https://www.sina.com.cn')

    print(r.content.decode())


if __name__ == '__main__':
    pass
    # main()
    response_text()
