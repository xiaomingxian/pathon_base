from pymysql import *


def main():
    con = connect(host='localhost', port=3306, user='root', passwd='abc', db='pythondb', charset='utf8')
    cur = con.cursor()
    cur.execute("select * from goods where id=10")
    print(cur.fetchone())


if __name__ == '__main__':
    main()
