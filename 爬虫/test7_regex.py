import re


def main():
    # .匹配任意符号除 \n
    # re.DOTALL == rs.S
    # r = re.match('.', '\n', re.DOTALL)
    r = re.match('.', '\n', re.S)
    print(r)
    # []或-->取[]中的一个  +可一次或多次
    r2 = re.findall('a[bcd]+c', 'acbc')
    print(r2)
    r3 = re.findall('aa|bc|ss', 'bc')
    print(r3)
    # \s空白字符  空行空格换行...   \S非空白字符
    print(re.findall('\s', '\n  \t'))
    print(re.findall('\S', '\n kjk \t'))
    # \d数字 \D非数字
    print(re.findall('\d', '1515ssds5496'))
    print(re.findall('\D', '1515ssds5496'))
    # \w单词字符   \W非单词字符
    print(re.findall('\w', 'as\n55'))
    print(re.findall('\W', 'as\n55'))
    # re.sub('正则','替换内容','愿字符串')
    print(re.sub('\d', '_', 'HHH12H4'))

    pass


def test():
    a = '<div class="pull-right login-wrap unlogin">   \n         <ul class="btns">            <li class="toolbar-tracking csdn-tracking-statistics tracking-click" data-mod="popu_369"><a href="#" style="padding:0" target="_blank"></a></li>              <li>                <div class="search_bar csdn-tracking-statistics tracking-click" data-mod="popu_366">                  <input type="text" class="input_search" name="" id="toolber-keyword" placeholder="搜博主文章" autocomplete="off">                  <a href="//so.csdn.net/so/" target="_blank" class="btn-nobg-noborder btn-search"><svg class="toolbar-icon" aria-hidden="true"><use xlink:href="#sousuo"></use></svg></a>                </div>              </li>              <li class="write-bolg-btn csdn-tracking-statistics tracking-click gitChat" data-mod="popu_370"><a class="" href="//mp.csdn.net/postedit" target="_blank"><img src="https://csdnimg.cn/public/common/toolbar/images/spring/xieboke.png" alt="" class="money"><span>写博客</span></a></li>              <li class="gitChat"><a class="" href="//gitbook.cn/new/gitchat/activity?utm_source=csdnblog1" target="_blank"><img src="https://csdnimg.cn/public/common/toolbar/images/spring/money.png" alt="" class="money"><span>赚零钱</span></a></li>              <li class="gitChat upload"><a target="_blank" class="" href="//i.csdn.net/#/msg/index"><img src="https://csdnimg.cn/public/common/toolbar/images/spring/message-icon.png" alt="" class="message"><span>消息</span><div class="toolbar-circle" id="msg-circle"></div></a></li>              <li class="userinfo"><a href="https://passport.csdn.net/account/login" target="_blank">登录</a><span></span><a href="https://passport.csdn.net/account/login" target="_blank">注册</a></li>              <li class="userLogin">                <div class="loginCenter"><a href="//i.csdn.net" target="_blank"><img class="login_img" src="//csdnimg.cn/public/common/toolbar/images/100x100.jpg"></a></div>                <div class="userControl">                <div class="bord">                <div><i class="pull_icon pull_icon1"></i><a href="https://www.csdn.net/nav/watchers" target="_blank">我的关注</a></div>                <div><i class="pull_icon pull_icon2"></i><a href="https://i.csdn.net/#/uc/favorite-list" target="_blank">我的收藏</a></div>                <div><i class="pull_icon pull_icon4"></i><a href="https://i.csdn.net/#/uc/profile" target="_blank">个人中心</a></div>                <div><i class="pull_icon pull_icon7"></i><a href="https://i.csdn.net/#/account/index" target="_blank">帐号设置</a></div>                </div>                  <div class="bord">                  <div><i class="pull_icon pull_icon5"></i><a href="https://blog.csdn.net/" target="_blank">我的博客</a></div>                  <div><i class="pull_icon pull_icon6"></i><a href="https://mp.csdn.net/" target="_blank">管理博客</a></div>                  <div><i class="pull_icon pull_icon12"></i><a href="https://edu.csdn.net/mycollege" target="_blank">我的学院</a></div>                  <div><i class="pull_icon pull_icon13"></i><a href="https://download.csdn.net/my/downloads" target="_blank">我的下载</a></div>                  </div>                  <div class="bord">                  <div><i class="pull_icon pull_icon8"></i><a href="https://my.csdn.net/my/score" target="_blank">我的C币</a></div>                  <div><i class="pull_icon pull_icon9"></i><a href="https://order.csdn.net/myorder" target="_blank">订单中心</a></div>                  </div>                  <div class="bord">                  <div><i class="pull_icon pull_icon10"></i><a href="https://blog.csdn.net/home/help.html" target="_blank">帮助</a></div>                  <div><i class="pull_icon pull_icon11"></i><a href="javascript:void(0);" class="logout">退出</a></div>                  </div>                </div>                <div class="guo_tip_box" style="display: none;">关注和收藏在这里</div>              </li>            </ul>          </div>'
    # ？尽可能少的匹配  .匹配不到\n
    r = re.findall('<.+>', a)
    # r = re.findall('<.+?>', a)
    print(r.__len__())
    for i in r:
        print(i)
    pass


def my_compile():
    # 预先编译正则
    p = re.compile('\d')
    print(p.findall('saas2142'))
    print(p.sub('_', 'saas2142ww'))
    # 相关配置需要写在compile中  否则不管用
    p2 = re.compile('.', re.S)
    print(p2.findall('\n'))
    # 得到指定内容
    print(re.findall('ab(.*)c','ab87758ccc'))
    pass


def r_test():
    print(r'\n' == '\\n')
    # r...完全匹配？？？
    print(re.findall(r'\n', '\\n'))
    # windows路径  r'E:\xxx'

    pass


if __name__ == '__main__':
    # main()
    # test()
    my_compile()
    # r_test()
    pass
