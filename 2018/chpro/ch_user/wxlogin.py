# -*- coding: utf-8 -*-
'''
微信类的封装
'''
import time, requests, re, json, random
from hashlib import md5
from django.shortcuts import render,HttpResponse
from models import UserInfo,wxuserinfo
# 第三方微信登录
    # 破解过程，chrome分析微信网页版，network-all，找到二维码图片出二维码之前，应该生成二维码字符串，找到如下
    # Request URL:https://login.wx.qq.com/jslogin?
    # appid=wx782c26e4c19acffb&
    # redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&
    # fun=new&lang=zh_CN&
    # _=1525003112434
    # 上面的请求返回的Response:window.QRLogin.code = 200; window.QRLogin.uuid = "YfyEQeipPA==";
    # 我们需要的二维码随机字符串就是YfyEQeipPA==
    # 通过上面多次请求，可以看到请求的_=1525003112434是变化的，就是时间戳生成的，因此可以用time.time()搞定
    # 定义全局变量：
class wxlogin(object):
    def __init__(self):
        self.wcode=None # 二维码字符串
        self.wctime=None # 时间戳字符串
        self.wtip=0 # 轮询相关
        self.req_cookie_dict={} # 全局长轮询请求cookie字典
        self.tick_cookie_dict={} # 初始化之前所需get请求获取票据的cookies
        self.tick_dict={} # 初始化所需票据字典


    # 1， 获取微信登录的图片二维码
    def login_wx(self,request):
        WEB_URL = 'https://login.wx.qq.com/jslogin?' \
                  'appid=wx782c26e4c19acffb&' \
                  'redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&' \
                  'lang=zh_CN&_={0}'  # {0}占位符

        self.wctime = str(time.time())  # 生成时间戳字符串
        # 构造请求url
        web_url = WEB_URL.format(self.wctime)  # 占位符替换format
        # 向该url发起请求，获得结果

        response = requests.get(web_url)  # 注意是requests 不是 request，要引入requests,是浏览器模拟对象，爬虫大量使用该对象
        # 这个结果是个response对象，有text属性，是字符串
        print response.text
        # 结果'window.QRLogin.code = 200; window.QRLogin.uuid = "YbNze-tO0g==";'
        # 其中YbNze-tO0g==就是我们想要的二维码随机字符串

        # 从结果中获得二维码随机字符串，使用正则
        # 使用正则匹配
        code = re.findall('uuid = "(.*)";', response.text)
        print code
        # code的结果[u'4f03N-am_Q==']是个列表，该列表中只有1个元素
        context = {'code': code[0]}
        # 将获得的二维码字符串给自身私例变量self.wcode

        self.wcode = code[0]

        # return render(request, 'ch_user/login_wx.html', context)
        return HttpResponse(json.dumps(context))

    # 2，在模板上实现长轮询polling，等待手机扫描，前端根据手机扫描的操作，返回状态码，根据状态码进行操作
    # 未扫描：window.code=408;
    # 已扫描未在手机确认登录：window.code=201;
    # 在手机确认登录：window.code=200;
    # 初始化用户，获取用户数据
    # 轮询函数

    def polling_wx(self,request):

        # tip为0表示还未扫码
        self.wtip = 0
        # 定义一个字典，用来返回ajax请求的长轮询结果
        ret = {'status': 408, 'src': None}
        # 获取手机扫描的结果
        # 等待手机扫描的url返回的response
        # https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?
        # loginicon=true&
        # uuid=IaLXstaSvQ==&该参数就是手机二维码的随机字符串
        # tip=0& 轮询参数，为0表示未扫描，tip=1，表示已扫描。
        # r=-373054253& 该参数不清楚，好像不影响
        # _=1525064306978 该参数为时间戳字符串
        # 手机未扫描的时候，状态码一直为pending，1分钟后，该地址状态码变为200，并返回response：window.code=408;

        phone_url = 'https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?' \
                    'loginicon=true&' \
                    'uuid={0}&' \
                    'tip={1}&' \
                    'r=-373054253&' \
                    '_={2}'
        # 用format替换占位符生成新的url，向新的url发起请求，并获得结果
        new_url = phone_url.format(self.wcode,self.wtip, self.wctime)
        response = requests.get(new_url)
        print response.text
        # 结果：window.code=408;
        # 当手机扫描后：window.code=201;window.userAvatar = 'data:img/jpg;base64,/9j/4AA......QhCAP/Z';
        # 状态码变为201，并且回传了window.userAvatar=,这个是64位加密的图像，这个图像就是用户头像，
        # 如果字符串window.code=201在返回的结果列表里，获取用户头像，给到前端;
        if 'window.code=201' in response.text:
            #tip为1表示已经扫了码
            self.wtip = 1
            # 用正则获取头像
            tx = re.findall("userAvatar = '(.*)';", response.text)[0]
            ret['status'] = 201
            ret['src'] = tx



        # 这时当在手机上点确认登录后，response.text 返回如下结果：跳转地址和200状态码
        # window.redirect_uri="https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage?ticket=ARokbQGY-KTjkAF2dBPyk3Vh@qrticket_0&uuid=wb7w2dJ_jQ==&lang=zh_CN&scan=1525096971";
        # window.code=200;
        # 现象，在客户端不停的发出轮询，这时应将轮询参数设为1

        elif 'window.code=200' in response.text:

            self.wtip = 1
            # 因为这时要跳转到另一个url，那么势必要验证cookie，那么我们在跳转之前，获取当前cookie
            # 获取new_url的cookie，并加入到全局请求的cookie字典中
            self.req_cookie_dict.update(response.cookies.get_dict())
            # 分析当前跳转的url
            # window.redirect_uri="https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage?
            # ticket=AX6ILPwVZU4XqDS1IbhD_R1e@qrticket_0& 票据
            # uuid=oY-I8yasmA==& 二维码字符串
            # lang=zh_CN&
            # scan=1525099842";
            # 对该url访问(直接用浏览器)_，报初始化失败，要求退出重新登录，只能确定，
            #
            # 那么提示了要初始化，chrome中看到data：img 200后有webwxinit?r=...之类的，猜测是初始化，点击后在Headers查看到
            # Request URL:https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxinit?
            # r=-389991253& 这个参数
            # lang=zh_CN&
            # pass_ticket=DFuNYreWjXQ32P19WYCzsD0rpD1CAJIyuRFM7r2P0lVuWEFQPav6Z6MauvE%252By7zz
            # Request Method:POST
            #  看到是post请求，需要pass_ticket参数
            # 看到初始化之前还有一步：webwxnewloginpage?r=...,点击后，在Headers看到请求的url
            # https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage?
            # ticket=AcLgmk_bwvCk0TcK8WzBAWrl@qrticket_0&uuid=oY-LSj1eJA==&
            # lang=zh_CN&
            # scan=1525103462&
            # fun=new&version=v2&
            # lang=zh_CN
            # Request Method:GET
            # 在初始化之前，对上面url发起了get请求，该请求获得的结果在Response中果如下
            # <error>
            # <ret>0</ret>
            # <message></message>
            # <skey>@crypt_c5957d04_a5a8f371172238039dc15dad01a1bae2</skey>
            # <wxsid>AsQN5PWbtNzblYmK</wxsid>
            # <wxuin>969499281</wxuin> #这个才是识别用户的唯一标识，******
            # <pass_ticket>DFuNYreWjXQ32P19WYCzsD0rpD1CAJIyuRFM7r2P0lVuWEFQPav6Z6MauvE%2By7zz</pass_ticket>
            # <isgrayscale>1</isgrayscale>
            # </error>
            # 这个xml结果就包含初始化需要的pass_ticket参数，
            # 并且该get请求的网址就是在我们获取的网址后加上不变的参数
            # &fun=new&version=v2&lang=zh_CN

            # 因此我们只要把不变的参数拼接后，用get访问，取得结果就可以拿到pass_ticket，然后发送post请求给初始化url
            # 先用正则获取跳转url
            get_url = re.findall('redirect_uri="(.*)";', response.text)[0]
            # 再用获取该跳转地址的变量，因为在跳转的时候，有些变量在构造初始化url时要用
            wxinit_url_start = re.findall('https://(.*)/cgi', get_url)[0]
            print wxinit_url_start
            get_url += '&fun=new&version=v2&lang=zh_CN'
            get_response = requests.get(get_url)
            # print get_response.text
            # 获得的结果同初始化前一步获得的结果相同是个xml文件有初始化需要的参数，ok

            # 获取初始化票据请求的cookie
            self.tick_cookie_dict.update(get_response.cookies.get_dict())

            # 对请求的结果，也就是获取的xml票据字典化，用beautifulsoup将xml转成字典
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(get_response.text, 'html.parser')
            for tag in soup.find():
                self.tick_dict[tag.name] = tag.string

            # 初始化用户，发送post请求，获取response,注意有个form表单选项，要提交
            post_url = 'https://{0}/cgi-bin/mmwebwx-bin/webwxinit?' \
                       'r=-389991253&' \
                       'lang=zh_CN&' \
                       'pass_ticket={1}'
            # 提交的form表单选项
            form_data = {
                'BaseRequest': {
                    'DeviceID': "e921814936107411",  # DeviceID为随机数，可以随意贴写，并不是设备的id
                    'Sid': self.tick_dict['wxsid'],
                    'Skey': self.tick_dict['skey'],
                    'Uin': self.tick_dict['wxuin']  # 这个才是识别用户的唯一标识，******
                }
            }
            # 所有cookie放到一个dict中
            all_cookie = {}
            all_cookie.update(self.req_cookie_dict)
            all_cookie.update(self.tick_cookie_dict)
            # 构建初始化url
            post_url = post_url.format(wxinit_url_start, self.tick_dict['pass_ticket'])
            # 向初始化url发起post请求，携带cookie，和提交form，将结果交给wxinit_resopse
            wxinit_respose = requests.post(post_url, json=form_data, cookies=all_cookie)
            wxinit_respose.encoding = 'utf-8'  # 转码
            # print wxinit_respose.text
            #将返回的结果转成字典
            wxinit_respose_dict=json.loads(wxinit_respose.text)
            # 利用上面的字典打印该用户的微信网页版唯一标识符
            print wxinit_respose_dict['User']['Uin']
            print wxinit_respose_dict['User']['NickName']

            #检查uin用户是否已存在 ，
                #UserInfo用户表中，用户名构成 前缀'__wx__'+uin
            uname='-wx-'+str(wxinit_respose_dict['User']['Uin'])
            user=UserInfo.objects.filter(uname=uname)


            # 如果存在，则返回用户数据,给浏览器设定session
            if len(user)==1:
                user=user[0]
                # 设定session
                request.session['user_id'] = user.id
                wxuser=wxuserinfo.objects.filter(wxuser_id=user.id).first()
                request.session['user_name'] =wxuser.wxnickname


            # 否则，创建用户
                # UserInfo用户表中， 用户名构成 前缀'__wx__'+uin
            else:
                #设置6位随机密码
                upwd=''
                # 实现6位随机字母数字码
                for i in range(6):
                    # 生成一个随机数字，范围与上面相同
                    current = random.randrange(6)
                    # 字母-->猜中了，就使用字母
                    if i == current:
                        # 生成大写字母对应ascii码的随机整数
                        tmp = random.randint(97, 122)
                        # 把整数转成字母
                        tmp = chr(tmp)
                    # 数字-->没猜中，就使用数字
                    else:
                        tmp = random.randint(0, 9)
                        upwd += str(tmp)
                #对密码加密
                m=md5()
                m.update(bytes(upwd))
                upwd3 = m.hexdigest()

                # 创建用户信息表对象
                user = UserInfo()
                user.uname = uname
                user.upwd = upwd3
                user.uemail = uname+'@chw.com'
                user.save()


                # 创建微信用户信息对象
                wxuser = wxuserinfo()
                wxuser.wxuin = str(wxinit_respose_dict['User']['Uin'])
                wxuser.wxnickname = wxinit_respose_dict['User']['NickName']
                wxuser.wxinfo = wxinit_respose_dict['User']
                wxuser.wxuser_id=user.id
                wxuser.save()
                # 把手工输入的账号和密码在前端弹出，用户点确定后再跳转
                ret['username'] = user.uname
                ret['upwd'] = upwd

            # 设定session
            request.session['user_id'] = user.id
            print user.id
            request.session['user_name'] = wxuser.wxnickname
            # 记录替换的id和用户名和密码，
            ret['ids'] = user.id
            ret['unames'] = wxuser.wxnickname

            # 退出微信url
            # quit_url='https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxlogout?' \
            #          'redirect=1&' \
            #          'type=1&' \
            #          'skey=%40crypt_c5957d04_75c6d023fc30a7edf029932e934987eb'
            # Request Method:POST
            # form data:
            # sid:7Sz6ALrFrbNwprQS
            # uin:969499281
            quit_url='https://{0}/cgi-bin/mmwebwx-bin/webwxlogout?' \
                     'redirect=1&' \
                     'type=1&' \
                     'skey={1}'
            # 拼接url
            q_url=quit_url.format(wxinit_url_start,self.tick_dict['skey'])
            quit_form={
                'sid':self.tick_dict['wxsid'],
                'uin':self.tick_dict['wxuin'],
            }
            # 退出，该退出没有返回,如果没有该动作，则手机上会有‘网页微信已登录，手机通知已关闭'.
            requests.post(q_url,json=quit_form,cookies=all_cookie)


            # 清空二维码和票据，因为微信有个bug，就是结束轮询后，再一次轮询，依然可以用前一次的二维码字符串和票据再登录一次
            # 调用类的构建函数，重新初始化，这样会使微信服务器退出网页登录，释放掉。
            wxlogin.__init__(self) #这一步在退出的时候也很重要

            # 将状态码置为True，让网页更新
            ret['status'] = True

        return HttpResponse(json.dumps(ret))