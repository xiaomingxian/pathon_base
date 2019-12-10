from pymysql import *

con = connect(host='10.1.15.201', port=3306, user='root', passwd='root', db='aioa_test', charset='utf8')
cur = con.cursor()

def insert(haveProBool):


    sql = 'insert into oa_button_set (PROC_DEF_KEY_,TASK_DEF_KEY_,i_proc_button_id,i_button_id,i_order,i_permit_type,i_is_creater,' \
          'i_is_reader,i_is_lastsender,i_is_transactors) values %s'
    # 按钮一个业务一套
    ids = None
    val = None

    # 按钮ids
    bunids = [33, 34, 35, 36, 37, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58]
    # taskDefKey
    taskDefKeys = ['usertask1', 'usertask2', 'countersign_leaderVerify', 'leaderApprove',
                   'countersign_receiveDepts', 'countersign_receivePersons', 'usertask6', 'recordFile']
    # prokey
    prokey = None

    # 有流程
    real_val = ''
    # 无流程

    if haveProBool:
        ids = [1, 2, 26, 41]
        val = "('%s','%s',%d,%d,%d,%d,%d,%d,%d,%d),"
        prokey = 'receiveFile'
        real_val = havePro(ids, taskDefKeys, bunids, val, real_val, prokey)

    else:
        ids = [49, 33, 2]
        val = "(%s,%s,%d,%d,%d,%d,%d,%d,%d,%d),"
        real_val = haveNoPro(ids, bunids, val, real_val)

    real_sql = sql % real_val
    # 截掉最后一个，
    final_sql = real_sql[0: -1]
    print(final_sql)
    cur.execute(final_sql)
    con.commit()

    # cur.execute("select * from goods where id=10")
    # print(cur.fetchone())


def havePro(ids, taskDefKeys, bunids, val, real_val, prokey):
    for i in ids:
        for tk in taskDefKeys:
            for index, btnId in enumerate(bunids, 1):
                val_real = val % (prokey, tk, i, btnId, index, 0, 1, 1, 1, 1)
                print(val_real)
                real_val += val_real
                # print(val_real)

    return real_val


def haveNoPro(ids, bunids, val, real_val):
    for i in ids:
        for index, btnId in enumerate(bunids, 1):
            val_real = val % (NULL, NULL, i, btnId, index, 0, 1, 1, 1, 1)
            real_val += val_real
            print(val_real)

    return real_val


if __name__ == '__main__':
    # insert(True)
    insert(False)
