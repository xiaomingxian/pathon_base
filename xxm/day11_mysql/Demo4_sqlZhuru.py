from pymysql import *


def main():
    con = connect(host='localhost', port=3306, user='root', passwd='abc', db='pythondb', charset='utf8')
    cur = con.cursor()
    # x=cur.execute('select * from brand where name="" or 1=1')
    x=cur.execute('select * from brand where name=%s','"" or 1=1')
    print('num:',x)
    for i in cur.fetchall():
        print(i)


if __name__ == '__main__':
    main()
