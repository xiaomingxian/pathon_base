import requests
import json
from pymysql import *



def main():

    con = connect(host='49.234.25.12', port=3306, user='root', passwd='Mysql_root_123456', db='fund', charset='utf8')
    cur = con.cursor()

    total=str(40*260)
    # total=str(3)
    url = 'http://vip.stock.finance.sina.com.cn/fund_center/data/jsonp.php/IO.XSRV2.CallbackList[\'dxJ_DCLDxQnQYM8a\']' \
          '/NetValueReturn_Service.NetValueReturnOpen?page=1&num='+total+'&sort=form_year&asc=0&ccode=&type2=0&type3='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    r = requests.get(url, headers=headers)
    res = (r.text).replace('IO.XSRV2.CallbackList[\'dxJ_DCLDxQnQYM8a\'](', '') \
        .replace(');', '') \
        .replace('/*<script>location.href=\'//sina.com\';</script>*/', '')
    print(res)

    jsonRes = json.loads(res)
    print(jsonRes)
    print('---------------------------------')
    list=jsonRes['data']
    count=0
    sql='insert into fund(symbol,sname,per_nav,total_nav,three_month,'\
                        'six_month,one_year,form_year,form_start,manager,name,zmjgm,'\
                        'clrq,dwjz,ljjz,jzrq,zjzfe,jjglr_code) values '
    val_total=[]
    for i in list:
        val_list=[]
        count+=1
        symbol=i['symbol']
        val_list.append(symbol)
        sname=i['sname']
        val_list.append(sname)
        per_nav=i['per_nav']
        val_list.append(per_nav)
        total_nav=i['total_nav']
        val_list.append(total_nav)
        three_month=i['three_month']
        val_list.append(three_month)
        six_month=i['six_month']
        val_list.append(six_month)
        one_year=i['one_year']
        val_list.append(one_year)
        form_year=i['form_year']
        val_list.append(form_year)
        form_start=i['form_start']
        val_list.append(form_start)
        jjjl=i['jjjl']
        val_list.append(jjjl)
        name=i['name']
        val_list.append(name)
        zmjgm=i['zmjgm']
        val_list.append(zmjgm)
        clrq=i['clrq']
        val_list.append(clrq)
        dwjz=i['dwjz']
        val_list.append(dwjz)
        ljjz=i['ljjz']
        val_list.append(ljjz)
        jzrq=i['jzrq']
        val_list.append(jzrq)
        zjzfe=i['zjzfe']
        val_list.append(zjzfe)
        jjglr_code=i['jjglr_code']
        val_list.append(jjglr_code)

        val_total.append(val_list)

        print(i)
        # 写入mysql

        pass
    vals=sql+' '+str(val_total) \
            .replace('[[','(') \
            .replace('[','(') \
            .replace(']]',')') \
            .replace(']',')')
    # print(vals)
    x=cur.execute(vals)
    con.commit()
    print('num:',x)
    for i in cur.fetchall():
        print(i)


    print('---->>>总数:',count)


if __name__ == '__main__':
    main()
