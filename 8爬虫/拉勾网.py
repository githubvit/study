# 拉勾网帐户
# REQUEST_ID: 0e636c49-85ff-4713-ae92-09a6881712b2
#username 18611453110
#pwd alex3714
import requests
import re
s=requests.session()

# 第一步 获取登录页面 及 动态授权码
    # url:https://passport.lagou.com/login/login.html
    # 方法：get
    # 请求头：
        # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
r1=s.get('https://passport.lagou.com/login/login.html',headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
})  
X_Anti_Forge_Token=re.findall("X_Anti_Forge_Token.*?'(.*?)'",r1.text,re.S)[0]
X_Anti_Forge_Code=re.findall("X_Anti_Forge_Code.*?'(.*?)'",r1.text,re.S)[0]
print(X_Anti_Forge_Token,'---',X_Anti_Forge_Code)

# 第二步 登录
    # url:https://passport.lagou.com/login/login.json
    # 方法：POST
    # 请求头：
        # 'Referer':'https://passport.lagou.com/login/login.html'
        # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        # 下面的Token从Referer带过来的
        # X-Anit-Forge-Code: 63084141
        # X-Anit-Forge-Token: e5c05022-63b8-49e2-8795-88da1f0d3bd4
        # X-Requested-With: XMLHttpRequest

    # 请求体：    
        # sValidate: true
        # username: 18611453110
        # password: 70621c64832c4d4d66a47be6150b4a8e
        # request_form_verifyCode: 
        # submit: 
        # challenge: ebf18b5faeb5507fcf6a39af668c4916

# 第三步 滑动验证码 难点
    # Request URL: https://api.geetest.com/gt_judgement?pt=0&gt=66442f2f720bfc86799932d8ad2eb6c7
    # Request Method: POST
    # Status Code: 200 OK

    # 请求头：
        # Referer: https://passport.lagou.com/login/login.html
        # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'

    # 请求体：
        # jL7zDsWAYqcCJkXnvPbwQCwH2ZBrbFSlX3SCO7c8ApiMA27Ccpfy1uJ00iGDwPjy90GWdR58PQy9cavBYDdNrdgv27vTWA8pSWb0sCETx2jfAKsSiJir0WDN90GZ6hBEELF
        # n7WnkH2)G3ddf2iKlrXWytGq52bAvfSPn1ArLcavcCQymYjjTeGQ5dTaT6SU(4rwhQ6nBEE2ypiOLeibSDQQ)jm9TmbkATtx95z9S8IINmPIstXpW0vp4QZR9Vtmxev(Gfn
        # E7EdV1VWEA4PrFrdeJ83muiqd9FdWpUsOkuILKkBchnopuV6lgl()tVTIG4ZRyZC0H1E7Sfzjm)7Fda6C5GHHoGJvCqieisBoI0yE74u7zHby3LT(w0JbB1gjIlG73Iw8m)
        # kvHDd10nHRHo4HorPhlj0Wg)UtJE8asp2mQGMdXKkOUvkIGwJO7q6gkU23QRlyBdFYh)uj52v5V5M1cPwGnrEUgWBqrPqVg8ugWaUWaBFzeF0Musw)...

# 第四步 授权
    # url:https://passport.lagou.com/grantServiceTicket/grant.html
    # 方法：get
    # 状态码：Status Code: 302 Found #重定向
    # 请求头：
        # Referer: https://passport.lagou.com/login/login.html
        # User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36
    # 响应头：
        # 重定向到登录后的页面 requests 会自动重定向 因此到此就完成了
        # Location: http://www.lagou.com?action=grantST&ticket=ST-7cbfe8df4eea4504b8478ac26963c188


# 第五步 验证
    # 找一个登录成功后才能登录的网址，get即可。