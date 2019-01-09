from urllib import parse


def main():
    qu = parse.quote('哈哈哈')
    print(qu)
    unqu = parse.unquote(qu)
    print(unqu)


if __name__ == '__main__':
    main()
