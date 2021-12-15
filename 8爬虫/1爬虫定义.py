爬虫的定义：

    向网站发起请求，获取资源后分析并提取有用数据的程序 

爬取的过程：

    发送请求 ———> 获取响应 ———> 解析内容 ———> 保存数据

    #1、发起请求
        使用http库向目标站点发起请求，即发送一个Request
        Request包含：请求头、请求体等

    #2、获取响应内容
        如果服务器能正常响应，则会得到一个Response
        Response包含：响应头、响应体（html，json，图片，视频）等

    #3、解析内容
        解析html数据：正则表达式，第三方解析库如Beautifulsoup，pyquery等
        解析json数据：json模块
        解析二进制数据:以b的方式写入文件

    #4、保存数据
        数据库
        文件

因此，学习爬虫就是学习三大类库

1. 请求库

2. 解析库

3. 存储库

# 抓包分析 

    1. 填入地址
    2. 用浏览器的右击检查或F12打开 调式分析窗口 
    3. 选择Network 选择 preserve log 保存以前的日志，因为，有可能在抓包过程中，地址跳转了，以前的结果都没了。
    4. 在地址栏回车发送请求
        看到页面内容拿下，排在第一位的就是第一个请求，后面的请求都是由这个请求引发的。
        先说http请求Request需要关注的东西：
            请求的url: url及其中文编码编码
                参数字典 pdict={
                    "user":'adsf',
                    "pwd":"xfaf"
                }
                参数：parmes=pdict
            请求方法：
            请求体：data=字节码  
                Post请求才有请求体，因为get请求把参数放入地址中，post请求把参数要放入请求体中。
                所以get请求参数有大小限制1kb，而post请求参数就没有限制。

                如果是post方式，请求体是format data

                ps：
                1、登录窗口，文件上传等，信息都会被附加到请求体内
                2、登录，输入错误的用户名密码，然后提交，就可以看到post，正确登录后页面通常会跳转，无法捕捉到post

                常见的格式：urlencoded\json\xml
                xml='''
                    <?xml=...>
                '''
                    消息体参数：data =xml.encode('utf-8') 要转为字节码
                urlencoded={
                    "ads":asd,
                }    
                   消息体参数： data=urlencoded 用字典定义的，就不用转为字节码 和get的参数方式一样
                json1= {
                    "a":"sdf",
                    "b":1
                }   
                     消息体参数: 不用data 用json=json1
            请求头：headers={}
                cookie、
                user-agent（浏览器）、
                Referer（从哪个网站跳过来的，比如拉勾网，对于不是从本网跳转过来的求职信息一律封杀，并且给的提示是当前访问太频繁，请稍后访问，你还以为没被禁止。）

        再说http响应Response要关注的：

            状态行：
                200：代表成功
                301：代表跳转
                404：文件不存在
                403：权限
                502：服务器错误

                注意：一般网站为了迷惑爬虫，没成功也会报200，因此200意义不大。
                而301要注意，这就是为什么在抓包过程要选preserve log的原因，这种事请非常多，比如登录，登录成功就会跳转。要注意跳转的地址即location.
                看到301就要知道，这个页面已经被重定向了，重定向的url就是location。
                如果请求库没有重定向功能，就要自己用requests向location发请求，模拟重定向。
            响应头：
                set_cookie,
                location    重定向

            响应体：
                html(静态页面) ：用正则匹配想要的内容。response.text
                json（ajax后台请求的动态数据）：用json模块反序列化获取想要的数据。response.json
                二进制b（图片、视频等）：以wb方式打开一个文件，把该二进制写入该文件，即可。response.content


# 白月黑羽讲requests和http协议

# requests模块 http://www.python3.vip/doc/tutorial/apitest/03/#requests库简介

    requests是 代替浏览器客户端 用http协议向服务器发送请求和获取响应的模块。
    
    selenium是 用程序控制浏览器 用http协议向服务器发送请求和获取响应的模块。

    requests不需要浏览器。只能模拟浏览器发送http请求，不能模拟人操作浏览器的动作点击、拖拽等等，
    selenium必须要有浏览器，模拟人操作浏览器就用selenium模块。

# http协议 http://www.python3.vip/doc/tutorial/apitest/01/#http协议简介
    由客户端和服务器组成，特点是只能由客户端先开始发消息。
    规定了客户端和服务器发消息的格式。
    请求格式：
        1 请求行 请求方法 路径 协议版本
            常见的HTTP 请求方法包括：

                GET

                    从服务器 获取 资源信息，这是一种最常见的请求。

                    比如 要 从服务器 获取 网页资源、获取图片资源、获取用户信息数据等等。

                POST

                    添加 资源信息 到 服务器进行处理（例如提交表单或者上传文件）。

                    比如 要 添加用户信息、上传图片数据 到服务器 等等

                    具体的数据信息，通常在 HTTP消息体中， 后面会讲到

                PUT

                    请求服务器 更新 资源信息 。

                    比如 要 更新 用户姓名、地址 等等

                    具体的更新数据信息，通常在 HTTP消息体中， 后面会讲到

                DELETE

                    请求服务器 删除 资源信息 。

                    比如 要 删除 某个用户、某个药品 等等

                HTTP还有许多其他方法，比如 PATCH、HEAD 等，不是特别常用，暂且不讲

        2 请求头 key:value 每个消息头一行
        3 空行
        4 请求体 
            增(POST)、改(PUT)、删(DELETE)有消息体，
            查(GET)没有消息体(查询的内容在url中)，
            
            请求消息体 通常是某种格式的文本，常见的有
                Json
                Xml
                www-form-urlencoded (示例2就是urlencoded格式)
        示例1：
            GET /mgr/login.html HTTP/1.1
            Host: www.baiyueheiyu.com
            User-Agent: Mozilla/6.0 (compatible; MSIE5.01; Windows NT)
            Accept-Language: zh-cn
            Accept-Encoding: gzip, deflate

        示例2：
            POST /api/medicine HTTP/1.1
            Host: www.baiyueheiyu.com
            User-Agent: Mozilla/6.0 (compatible; MSIE5.01; Windows NT)
            Content-Type: application/x-www-form-urlencoded
            Content-Length: 51
            Accept-Language: zh-cn
            Accept-Encoding: gzip, deflate

            name=qingmeisu&sn=099877883837&desc=qingmeisuyaopin

    响应格式：
        1 状态行
        2 响应头
        3 空行
        4 响应体 常见格式和请求体一样，示例中的响应体为json格式。

        示例：
            HTTP/1.1 200 OK
            Date: Thu, 19 Sep 2019 08:08:27 GMT
            Server: WSGIServer/0.2 CPython/3.7.3
            Content-Type: application/json
            Content-Length: 37
            X-Frame-Options: SAMEORIGIN
            Vary: Cookie

            {"ret": 0, "retlist": [], "total": 0}

# 抓包工具 fiddler http://www.python3.vip/doc/tutorial/apitest/03/#抓包工具-fiddler
    
    1 fiddler 设置好过滤 即抓取某某请求的请求和返回包。
    2 浏览器不用抓包工具，因为其调式窗口自带。
    3 使用requests 模块 如何使用抓包工具代理：proxies参数
        示例
            # fiddler 启动后 默认 127.0.0.1:8888
            import requests

            proxies = {
              'http': 'http://127.0.0.1:8888',
              'https': 'http://127.0.0.1:8888',
           }

            response = requests.get('http://mirrors.sohu.com/', proxies=proxies)
            print(response.text)

