import time
# 数据库数据
from pymysql import *
import re

urlDic = dict()


def getCursor():
    con = connect(host='localhost', port=3306, user='root', passwd='abc', db='pythondb', charset='utf8')
    cur = con.cursor()
    return cur


def route(url):
    def out(fun):
        # 将页面资源的引用 添加到字典
        urlDic[url] = fun

        def inner(*args, **kwargs):
            return fun()

        return inner

    return out


@route('index.py')
def index():
    try:
        with open('index.html', 'r') as  f:
            con = f.read()
            cur = getCursor()
            cur.execute('select * from goods')

            title = """<tr>
                <td>id</td>  
                <td>name</td>  
                <td>cate_id</td>  
                <td>brad_id</td>  
                <td>price</td>  
                <td>is_show</td>  
                <td>is_saleoff</td>  
                <td>do</td>  
            </tr>"""

            temp = """<tr>
                <td>%s</td>  
                <td>%s</td>  
                <td>%s</td>  
                <td>%s</td>  
                <td>%s</td>  
                <td>%s</td>  
                <td>%s</td>  
                <td>
                    <button id='b' type='button' onclick="add()">add</button>
                </td>
            </tr>"""

            body = title
            for i in cur.fetchall():
                body += temp % (i[0], i[1], i[2], i[3], i[4], i[5], i[6])

            return re.sub(r'content',
                          """<table border="0" cellspacing="2" width="800px" height="190px">""" + body + "</table>",
                          con)
    except Exception as e:
        print('e:', e)
        pass
    finally:
        cur.close()


@route('login.py')
def login():
    print('-----login----')
    with open('login.html', 'r') as  f:
        return f.read()


def application(env, method):
    # env放服务端传过来的东西eg:url
    # 服务端定义 method 用来接收传过去的东西  eg:heads
    url = env['PATH-INF']
    # 也可以用 re.match(url,遍历urlDic取出key) 匹配上就有返回值 否则没有
    if url in urlDic:
        method('HTTP/1.1 200 OK', [('Content-Type', 'text/html;charset=gbk')])
        return urlDic[url]()
    else:
        print("--------------")
        method('HTTP/1.1 404 NOT FOUND', [('Content-Type', 'text/html;charset=gbk')])
        return '您访问的资源不存在...  %s' % str(time.ctime())
