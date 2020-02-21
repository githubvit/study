# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse,HttpResponseRedirect
from hashlib import md5
from models import *
from ch_util import Checkcode
import StringIO,re


# 用户中心 获取用户id
def user(request):
    try:
        # 从浏览器获取用户
        id=request.session['user_id']
        uname=request.session['user_name']

        # 从用户信息表中获取
        user=UserInfo.objects.filter(id=id).first()

        # 获取用户收货信息列表
        ad_list=user.lg.filter(is_Delete=0).order_by('-id')
        # 获取用户默认收货信息
        address=user.lg.filter(is_Delete=0).filter(is_Default=1).last()#is_Default=True也可以

        #获取用户访问ip，这里想做的是，获取用户ip，然后把ip给到第三方，解析出精确到省市区级别的地址，这样一定程度上缓解用户的输入，提升用户体验
        if request.META.has_key('HTTP_X_FORWARDED_FOR'):
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        print address, ip
        context={'title':'用户中心','user':user,'address':address,'ad_list':ad_list}
        return render(request,'ch_user/userinfo-1.html',context)

    #如果没有id，那么会产生错误，处理异常，跳转到首页
    except Exception,e:
        print e
        return redirect('/')
# 添加收货信息 每个用户最多十条记录
def logistics(request):
    ret = {'status': True, 'error': None, 'data': None}
    luser_id=request.session['user_id']
    count=LogisticsInfo.objects.filter(luser_id=luser_id).filter(is_Delete=0).count()
    if count>=10:
        ret['status'] = False
        ret['error'] = '抱歉，最多只能有10条收货信息记录，您可以删除一些记录，然后再添加。'
    else:
        post=request.POST
        lname=post.get('lname',None)
        lphon=post.get('lphon',None)
        larea=post.get('larea',None)
        laddress=post.get('laddress',None)
        is_default=post.get('is_default',0)
        if lname and lphon and larea and laddress:
            lg=LogisticsInfo()
            lg.lname=lname
            lg.lphon=lphon
            lg.larea=larea
            lg.laddress=laddress
            lg.is_Default=is_default
            lg.luser_id=luser_id#对于foreignkey只能用表的字段名，不能用类的属性名，因为属性名是对应对象
            lg.save()
            ret['data']=lg.id
        else:
            ret['status'] = False
            ret['error'] = '不能有空项'
    return JsonResponse(ret)

# 删除收货信息，只是逻辑删除
def lg_del(request,*args,**kwargs):
    ret = {'status': True, 'error': None, 'data': None}
    lg_id=request.GET.get('lg_id')
    lgobj=LogisticsInfo.objects.filter(id=lg_id).first()
    print lg_id,lgobj
    # 如果对象不为空，就删除，否则返回False和error消息
    if lgobj:
        lgobj.is_Delete=1
        lgobj.save()
    else:
        ret['status'] = False
        ret['error'] = '没有该项'
    return JsonResponse(ret)

# 验证码检查
def CheckCode(request):
    mstream = StringIO.StringIO()
    validate_code = Checkcode.create_validate_code()
    img = validate_code[0]
    img.save(mstream, "GIF")
    #将验证码保存到session
    request.session["CheckCode"] = validate_code[1]
    return HttpResponse(mstream.getvalue())

# 检查用户名是否已存在
def register_exist(request):
    uname=request.GET.get('uname')
    print uname
    count=UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})

#注册：要有注册码，防止机器注册
def registerhandle(request):
    # 定义字典
    ret = {'status': True, 'error': None, 'data': None,'idS':None,'unames': None}
    # 接收用户输入
    post=request.POST
    uname=post.get('r_uname',None)
    upwd=post.get("rpwd",None)
    upwd2=post.get('cpwd',None)
    uemail=post.get('remail',None)
    # 接收验用户输入的验证码
    check_code = request.POST.get('checkcode',None)
    # 从session中获取验证码
    session_code = request.session["CheckCode"]

    # 检查用户名合法性
    username=re.match(r'^[a-zA-Z][\w]{4,15}$',uname)
    if not username:
        ret['status'] = False
        ret['error'] = '用户名必须以字母开头，后面是由字母和数字组成，长度在5位到16位之间。'
        return JsonResponse(ret)

    #验证码和密码检查
    if check_code.strip().lower() != session_code.lower():
        ret['status'] = False
        ret['error'] = '验证码错误'
    else:
        print uname,upwd,upwd2,uemail
        #判断两次密码
        if upwd!=upwd2 :
            ret['status']=False
            ret['error']='两次密码不一致'
        else:
            # 密码加密
            s1=md5()
            s1.update(bytes(upwd))
            upwd3=s1.hexdigest()
            # 创建对象
            user=UserInfo()
            user.uname=uname
            user.upwd=upwd3
            user.uemail=uemail
            user.save()
            # 设定session
            request.session['user_id']=user.id
            print user.id
            request.session['user_name']=user.uname
            ret['ids']=user.id
            ret['unames']=user.uname
    return JsonResponse(ret)

# 登录
def login(request):
    ret = {'status': True, 'error': None, 'data': None, 'ids': None, 'unames': None}
    # 接收用户请求信息
    post=request.POST
    uname=post.get('username')
    print uname
    upwd=post.get('upwd')
    jizhu=post.get('jizhu',0)
    # 根据用户名查询对象，因为输入的用户名有可能不存在，所以不能用get，要用filter。
    users=UserInfo.objects.filter(uname=uname)
    print users
    # 判断用户是否存在
    if len(users)==1:
        # 对输入的密码加密
        m1=md5()
        m1.update(bytes(upwd))
        # 判断用户密码是否正确
        if m1.hexdigest()==users[0].upwd:
            # 设定session
            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            ret['ids'] = users[0].id
            ret['unames'] = uname
            red=JsonResponse(ret)
            #记住用户名
            if jizhu!=0:
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uname','',max_age=-1) #置为空并立即过期
            return red
        else:
            ret['status'] = False
            ret['error'] = '密码错误'
            return JsonResponse(ret)
    else:
        ret['status'] = False
        ret['error'] = '用户名错误'
        return JsonResponse(ret)


# 修改密码
def change_upwd(request):
    ret = {'status': True, 'error': None, 'data': None}
    # 获取用户ID和用户密码
    uid=request.session['user_id']
    upwd=request.POST.get('old-pwd')
    npwd=request.POST.get('new-pwd')
    print uid
    print upwd
    print npwd
    # 根据id获取用户对象
    user= UserInfo.objects.filter(id=uid).first()
    # 对输入的旧密码加密
    m1 = md5()
    m1.update(bytes(upwd))
    # 判断输入的密码是否正确
    if m1.hexdigest()==user.upwd:
        # 对新密码加密，并升级该用户密码为新密码
        m2=md5()
        m2.update(bytes(npwd))
        user.upwd=m2.hexdigest()
        user.save()
        print '密码正确'
    else:
        print '密码错误'
        ret['status'] = False
        ret['error'] = '原密码错误'
    return JsonResponse(ret)

# 微信扫码登录
from wxlogin import wxlogin
wxl=wxlogin()
def login_wx(request):
    if request.path=='/user/login_wx/':
        return wxl.login_wx(request)
    elif request.path == '/user/polling_wx/':
        print request.path
        return wxl.polling_wx(request)

#退出
def logout(request):
    #清除session
    # request.session.flush()#所有session全清
    del request.session['user_name']#个别session清除
    del request.session['user_id']#个别session清除
    # 微信有个bug，就是结束轮询后，再一次轮询，依然可以用前一次的二维码字符串和票据再登录一次
    # 重新初始化微信对象,应对微信bug，不然退出后，再点击微信扫码登录，不用手机扫码，就会自动登录，影响安全
    # 因此要重新初始化该微信实例对象。*****这一步很重要*****
    wxl.__init__()
    return redirect('/')


'''
#第三方微信登录
#chrome分析微信网页版，network-all，找到二维码图片出二维码之前，应该生成二维码字符串，找到如下
#Request URL:https://login.wx.qq.com/jslogin?
# appid=wx782c26e4c19acffb&
# redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&
# fun=new&lang=zh_CN&
# _=1525003112434
# 上面的请求返回的Response:window.QRLogin.code = 200; window.QRLogin.uuid = "YfyEQeipPA==";
# 我们需要的二维码随机字符串就是YfyEQeipPA==
# 通过上面多次请求，可以看到请求的_=1525003112434是变化的，就是时间戳生成的，因此可以用time.time()搞定
# 定义全局变量：
import time,requests,re,json,os
WCODE=None #二维码字符串
WCTIME=None  #时间戳字符串
WTIP=0 #轮询相关
REQ_COOKIE_DICT={} #全局长轮询请求cookie字典
TICK_COOKIE_DICT={} #初始化之前所需get请求获取票据的cookies
TICK_DICT={} #初始化所需票据字典
#1， 获取微信登录的图片二维码
def login_wx(request):
    WEB_URL='https://login.wx.qq.com/jslogin?' \
                       'appid=wx782c26e4c19acffb&' \
                       'redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&' \
                       'lang=zh_CN&_={0}'#{0}占位符
    CHECK_LOGIN_URL=''
    ERDIRECT_URL_SUFFIX='&fun=new&version=v2&lang=zh_CN'
    global WCTIME
    WCTIME=str(time.time())#生成时间戳字符串
    # 构造请求url
    web_url=WEB_URL.format(WCTIME)#占位符替换format
    # 向该url发起请求，获得结果

    response=requests.get(web_url)#注意是requests 不是 request，要引入requests
    # 这个结果是个response对象，有text属性，是字符串
    print response.text
    # 结果'window.QRLogin.code = 200; window.QRLogin.uuid = "YbNze-tO0g==";'
    # 其中YbNze-tO0g==就是我们想要的二维码随机字符串

    # 从结果中获得二维码随机字符串，使用正则
     #使用正则匹配
    code=re.findall('uuid = "(.*)";',response.text)
    print code
    # code的结果[u'4f03N-am_Q==']是个列表，该列表中只有1个元素
    context={'code':code[0]}
    # 将获得的二维码字符串给全局变量WCODE
    global WCODE
    WCODE=code[0]

    return render(request,'ch_user/login_wx.html',context)

# 2，在模板上实现长轮询polling，等待手机扫描，根据手机扫描的操作，返回状态码，根据状态码进行操作
# 未扫描：window.code=408;
# 已扫描未在手机确认登录：window.code=201;
# 在手机确认登录：window.code=200;
# 初始化用户，获取用户数据
# 轮询函数
def polling_wx(request):
    #定义一个字典，用来返回ajax请求的长轮询结果
    ret={'status':408,'src':None}
    # 获取手机扫描的结果
    # 等待手机扫描的url返回的response
    # https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?
    # loginicon=true&
    # uuid=IaLXstaSvQ==&该参数就是手机二维码的随机字符串
    # tip=0& 该参数用来避免客户端不断轮询，如果无该参数，则手机端每秒轮询一次，不是每分钟轮询。如果服务器效率低，则造成服务器报错。
    # r=-373054253& 该参数不清楚，好像不影响
    # _=1525064306978 该参数为时间戳字符串
    # 手机未扫描的时候，状态码一直为pending，1分钟后，该地址状态码变为200，并返回response：window.code=408;

    phone_url='https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?' \
              'loginicon=true&' \
              'uuid={0}&' \
              'tip={1}&' \
              'r=-373054253&' \
              '_={2}'
    #用format替换占位符生成新的url，向新的url发起请求，并获得结果
    new_url=phone_url.format(WCODE,WTIP,WCTIME)
    response=requests.get(new_url)
    print response.text
    # 结果：window.code=408;
    # 当手机扫描后：window.code=201;window.userAvatar = 'data:img/jpg;base64,/9j/4AA......QhCAP/Z';
    # 状态码变为201，并且回传了window.userAvatar=,这个是64位加密的图像，这个图像就是用户头像，
    # 如果字符串window.code=201在返回的结果列表里，获取用户头像，给到前端;
    if 'window.code=201' in response.text:
        #用正则获取头像
        tx=re.findall("userAvatar = '(.*)';",response.text)[0]
        ret['status']=201
        ret['src']=tx
        # 这时当在手机上点确认登录后，response.text 返回如下结果：跳转地址和200状态码
        # window.redirect_uri="https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage?ticket=ARokbQGY-KTjkAF2dBPyk3Vh@qrticket_0&uuid=wb7w2dJ_jQ==&lang=zh_CN&scan=1525096971";
        # window.code=200;
        # 现象，在客户端不停的发出轮询，这时应将轮询参数设为1


    elif 'window.code=200' in response.text:
        global WTIP
        WTIP=1
        # 因为这时要跳转到另一个url，那么势必要验证cookie，那么我们在跳转之前，获取当前cookie
        # 获取new_url的cookie，并加入到全局请求的cookie字典中
        REQ_COOKIE_DICT.update(response.cookies.get_dict())
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
        #在初始化之前，对上面url发起了get请求，该请求获得的结果在Response中果如下
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
        get_url=re.findall('redirect_uri="(.*)";',response.text)[0]
        # 再用获取该跳转地址的变量，因为在跳转的时候，有些变量在构造初始化url时要用
        wxinit_url_start=re.findall('https://(.*)/cgi',get_url)[0]
        print wxinit_url_start
        get_url+='&fun=new&version=v2&lang=zh_CN'
        get_response=requests.get(get_url)
        print get_response.text
        # 获得的结果同初始化前一步获得的结果相同是个xml文件有初始化需要的参数，ok

        #获取初始化票据请求的cookie
        TICK_COOKIE_DICT.update(get_response.cookies.get_dict())

        # 对请求的结果，也就是获取的xml票据字典化，用beautifulsoup将xml转成字典
        from bs4 import BeautifulSoup
        soup=BeautifulSoup(get_response.text,'html.parser')
        for tag in soup.find():
            TICK_DICT[tag.name]=tag.string

        # 初始化用户，发送post请求，获取response,注意有个form表单选项，要提交
        post_url='https://{0}/cgi-bin/mmwebwx-bin/webwxinit?' \
                 'r=-389991253&' \
                 'lang=zh_CN&' \
                 'pass_ticket={1}'
        #提交的form表单选项
        form_data={
            'BaseRequest':{
               'DeviceID':"e921814936107411",#DeviceID为随机数，可以随意贴写，并不是设备的id
                'Sid':TICK_DICT['wxsid'],
                'Skey':TICK_DICT['skey'],
                'Uin':TICK_DICT['wxuin']  #这个才是识别用户的唯一标识，******
               }
            }
        #所有cookie放到一个dict中
        all_cookie={}
        all_cookie.update(REQ_COOKIE_DICT)
        all_cookie.update(TICK_COOKIE_DICT)
        # 构建初始化url
        post_url=post_url.format(wxinit_url_start,TICK_DICT['pass_ticket'])
        # 向初始化url发起post请求，携带cookie，和提交form，将结果交给wxinit_resopse
        wxinit_respose=requests.post(post_url,json=form_data,cookies=all_cookie )
        wxinit_respose.encoding='utf-8'#转码
        print wxinit_respose.text

        # 将状态码置为200，让网页跳转
        ret['status']=200
    return HttpResponse(json.dumps(ret))
'''