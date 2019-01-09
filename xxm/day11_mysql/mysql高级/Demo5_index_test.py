from pymysql import *


def main():
    con = connect(host='localhost', port=3306, user='root', passwd='abc', db='pythondb', charset='utf8')
    cur = con.cursor()
    for i in range(100000000):
        # 防止注入漏洞
        cur.execute('insert into index_test values (null,"哈%s")', i)
        con.commit()



if __name__ == '__main__':
    main()
