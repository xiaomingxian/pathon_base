from pymysql import *

# MySQLdb  python2中

# 1.建立连接
con = connect(host='localhost', port=3306, user='root', passwd='abc', db='pythondb', charset='utf8')
# 2.创建游标
cur = con.cursor()

# 3.相关操作

sql = 'select * from goods'

# 执行结果保存在游标对象中
res = cur.execute(sql)
print('cursor:', cur)
print('-------逐条查询 fetchone()-------')
# while True:
#     res2 = cur.fetchone()
#     if res2 == None:
#         break
#     print(res2)
print('查询记录数 execute(sql):', res)
print('-----------查询多条 fetchmany(num)--------------')
for i in cur.fetchmany(3):
    print(i)
print('------------查询剩余 fetchall()----------')
for i in cur.fetchall():
    print(i)

print('-----------查询商品分类案例--------------')
cur2=con.cursor()
findsql='select name from goods'
cur2.execute(findsql)
for i in cur2.fetchall():
    print(i[0])

# 4.关闭游标
cur.close()
# 5.关闭连接
con.close()
