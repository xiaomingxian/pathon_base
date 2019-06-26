import time


def index():
    f = open('index.html', 'r')
    return f.read()


def login():
    with  open('login.html', 'r') as f:
        con = f.read()
    print('kkk:', con)
    return con


def application(env, method):
    # 状态 和 heads
    method('200 OK', [('Content-Type', 'text/html;charset=gbk')])
    # body
    rec = env['PATH-INFO']
    if rec == 'login.py':
        return login()
    if rec == 'index.py':
        return index()
    else:
        return '资源不存在...  %s' % str(time.ctime())
