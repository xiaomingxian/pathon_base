import requests
import json
from pymysql import *


#  基金评级
def main():
    # http://vip.stock.finance.sina.com.cn/fund_center/data/jsonp.php/IO.XSRV2.CallbackList['AKrTuSoZCv$BMXwB']/FundRank_Service.getMSFundInfo?page=19&num=40&sort=nav&asc=0&ccode=&type=1&type3=&date=

    # con = connect(host='49.234.25.12', port=3306, user='root', passwd='Mysql_root_123456', db='fund', charset='utf8')
    # cur = con.cursor()

    total=str(40*260)
    # 股票型基金
    url = 'http://vip.stock.finance.sina.com.cn/fund_center/data/jsonp.php/IO.XSRV2.' \
          'CallbackList[\'AKrTuSoZCv$BMXwB\']/FundRank_Service.getMSFundInfo?page=1&num='+total+'&sort=nav&asc=0&ccode=&type=1&type3=&date='

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    r = requests.get(url, headers=headers)
    print(r.text)
    res = (r.text).replace('IO.XSRV2.CallbackList[\'AKrTuSoZCv$BMXwB\'](', '') \
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
        count+=1
        val_list=[]

        print(i)
        # 写入mysql

        pass
    vals=sql+' '+str(val_total) \
            .replace('[[','(') \
            .replace('[','(') \
            .replace(']]',')') \
            .replace(']',')')
    # print(vals)
    # x=cur.execute(vals)
    # con.commit()


    print('---->>>总数:',count)


if __name__ == '__main__':
    main()
