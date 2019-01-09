import re
import time
# 数据库数据
from pymysql import *
import logging
from urllib import request
from urllib import parse

# urlDic
urlDic = dict()


# 路由
def route(url):
    def out(fun):
        # 将页面资源的引用 添加到字典
        urlDic[url] = fun

        def inner(*args, **kwargs):
            return fun()

        return inner

    return out


# 修改信息
@route('show/ok/(\d+)/(.*)\.py')
def ok(ret):
    print('--------------------g : ', ret.group(1), parse.unquote(ret.group(2), 'utf8'))
    # 修改描述信息
    try:
        con = connect(host='localhost', port=3306, user='root', passwd='abc', db='pythondb', charset='utf8')
        cur = con.cursor()
        cur.execute('update my_love_goods set name=%s where good_id=%s',
                    (parse.unquote(ret.group(2), 'utf8'), ret.group(1)))

        con.commit()
        cur.close()
        con.close()

        return 'change success'
    except Exception as e:
        print('异常:', e)
        return 'change fail'

        pass
    pass


# 显示详情
@route('show/(\d+)\.py')
def show(ret):
    # ret为匹配到的结果 re.match(字典中的key,实际截取到的url)
    # 查询信息
    con = connect(host='localhost', port=3306, user='root', passwd='abc', db='pythondb', charset='utf8')
    cur = con.cursor()
    cur.execute("""
    select
    g.id, g.name, g.price, m.name
    good_desc
    from goods g, my_love_goods
    m
    where
    g.id=m.good_id and
    m.good_id = %s
    """ % ret.group(1))

    result = cur.fetchone()
    print('----->result : ', ret.group(1), result)

    with open('detil.html', 'r') as f:
        con = f.read()
    print('llll:', result[3])
    temp = """
        <tr>
            <td>id</td>
            <td>name</td>
            <td>price</td>
            <td>desc</td>
            <td>Ok</td>
        </tr>
        """
    body = """
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td><input id='desc' value='%s'></td>
            <td><button onclick='ok(%s,"%s")'>ok</button></td>
        </tr>
        """ % (result[0], result[1], result[2], result[3], result[0], result[3])

    content = re.sub('content',
                     """<table border="0" cellspacing="1" width="700px" height="100px">""" + temp + body + "</table>",
                     con)

    return content


@route(r"add/(\d+)\.py")
def add(ret):
    # 先检查有没有关注
    con = connect(host='localhost', port=3306, user='root', passwd='abc', db='pythondb', charset='utf8')
    cur = con.cursor()
    cur.execute('select * from my_love_goods where good_id=%s', ret.group(1))
    if cur.fetchone():
        cur.close()
        con.close()
        return 'you have focused...'
    else:
        # 查找 id 是否有对应的数据
        cur.execute('select name from goods where id=%s', ret.group(1))
        name = cur.fetchone()
        if name:
            cur.execute('insert into my_love_goods (name,good_id) select name,id from goods where id=%s', ret.group(1))
            con.commit()
            cur.close()
            con.close()
            return 'focus success...'
        else:
            return "have no source..."


@route('index.py')
def index(ret):
    try:
        with open('index.html', 'r') as  f:
            con = f.read()
            conn = connect(host='localhost', port=3306, user='root', passwd='abc', db='pythondb', charset='utf8')
            cur = conn.cursor()
            cur.execute(
                'SELECT g.id,g.name,g.cate_id,g.brand_id,g.price,g.is_show,g.is_saleoff,m.name good_desc FROM goods g left JOIN my_love_goods m on g.id=m.good_id')

            title = """<tr>
                <td>id</td>  
                <td>name</td>  
                <td>cate_id</td>  
                <td>brad_id</td>  
                <td>price</td>  
                <td>is_show</td>  
                <td>is_saleoff</td>  
                <td>desc</td>  
                <td>do</td>  
                <td>change</td>  
            </tr>"""

            temp = """<tr>
                <td id='mid'>%s</td>  
                <td>%s</td>  
                <td>%s</td>  
                <td>%s</td>  
                <td>%s</td>  
                <td>%s</td>  
                <td>%s</td>
                <td>%s</td>
                  
                <td>
                    <button  type='button' onclick="add(%s)">add</button>
                </td>
                <td>
                    <button  type='button' onclick="show(%s)">change</button>
                </td>
            </tr>"""

            body = title
            for i in cur.fetchall():
                body += temp % (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[0], i[0])

            return re.sub(r'content',
                          """<table border="0" cellspacing="2" width="800px" height="190px">""" + body + "</table>",
                          con)
    except Exception as e:
        print('e:', e)
        pass
    finally:
        cur.close()
        conn.close()


@route('login.py')
def login(ret):
    print('-----login----')
    with open('login.html', 'r') as  f:
        return f.read()


def application(env, method):
    # env放服务端传过来的东西eg:url
    # 服务端定义 method 用来接收传过去的东西  eg:heads
    url = env['PATH-INF']
    # 也可以用 re.match(url,遍历urlDic取出key) 匹配上就有返回值 否则没有
    # print("urlDic:", urlDic)
    logging.basicConfig(level=logging.INFO, filename='./log.txt', filemode='a',
                        format='%(asctime)s-%(filename)s [line:%(lineno)d]-%(levelname)s : %(message)s')
    logging.info('访问的 url 是:%s' % url)

    for urlkey, urlvalue in urlDic.items():
        ret = re.match(urlkey, url)
        if ret:
            method('HTTP/1.1 200 OK', [('Content-Type', 'text/html;charset=utf8')])
            return urlDic[urlkey](ret)

    else:
        logging.warning('未发现资源...')
        method('HTTP/1.1 404 NOT FOUND', [('Content-Type', 'text/html;charset=utf8')])
        return ('no source')
    # method2
    # if url in urlDic:
    #     method('HTTP/1.1 200 OK', [('Content-Type', 'text/html;charset=utf8')])
    #     return urlDic[url]()
    # else:
    #     print("--------------")
    #     method('HTTP/1.1 404 NOT FOUND', [('Content-Type', 'text/html;charset=utf8')])
    #     return '您访问的资源不存在...  %s' % str(time.ctime())
