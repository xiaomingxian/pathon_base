from pymysql import *


class JD(object):
    def __init__(self):
        # 成员变量
        self.con = connect(host='localhost', port=3306, user='root', passwd='abc', db='pythondb', charset='utf8')
        self.cur = self.con.cursor()

    def find(self, sql):
        self.cur.execute(sql)

    def show_all(self):
        sql = 'select * from goods'
        self.find(sql)

    def show_cate(self):
        sql = 'select name from cate'
        self.find(sql)

    def show_brand(self):
        sql = 'select name from brand'
        self.find(sql)

    @staticmethod
    def show_JD():
        print('-----------JD-------------')
        print('----1.show all------')
        print('----2.show cate-----')
        print('----3.show brand----')

    def __del__(self):
        # 释放资源
        self.cur.close()
        self.con.close()
        pass

    def run(self):
        self.show_JD()
        while True:
            i = input('请输入你的选择')
            if i == '1':
                self.show_all()
                for i in self.cur.fetchall():
                    print(i)
            elif i == '2':
                self.show_cate()
                for i in self.cur.fetchall():
                    print(i[0])
            elif i == '3':
                self.show_brand()
                for i in self.cur.fetchall():
                    print(i[0])
            else:
                print('您输入的不合法，请重新输入。')


def main():
    jd = JD()
    jd.run()


if __name__ == '__main__':
    main()
