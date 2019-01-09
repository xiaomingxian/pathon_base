from pymysql import *


def main():
    con = connect(host='localhost', port=3306, user='root', passwd='abc', db='pythondb', charset='utf8')
    cur = con.cursor()
    # cur.execute('insert into brand values (null ,"test")')
    # con.commit()

    try:
        for i in range(10):
            if i == 5:
                pass
                # 1 / 0
            cur.execute('insert into brand values (null,"test%d")'%i)

        con.commit()
    except Exception as e:
        print("出现异常回滚",e)
        con.rollback()
        pass


if __name__ == '__main__':
    main()
