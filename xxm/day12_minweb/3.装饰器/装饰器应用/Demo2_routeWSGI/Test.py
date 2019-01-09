import re
from urllib import parse


def main():
    a = re.match('a', 'a')
    print(a)
    print('show/js/jquery-1.11.3.min.js'.__contains__('js/jquery-1.11.3.min.js'))
    qu=parse.quote('哈哈哈')
    print(qu)
    print(parse.unquote(qu))

if __name__ == '__main__':
    main()
