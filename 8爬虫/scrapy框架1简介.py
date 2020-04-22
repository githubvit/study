# 爬虫框架：scrapy - linhaifeng - 博客园
# https://www.cnblogs.com/linhaifeng/articles/7811861.html
# 视频 https://www.bilibili.com/video/BV1CE411i73L?p=37

# 1 scrapy是什么
        Scrapy一个开源和协作的框架，其最初是为了页面抓取 (更确切来说, 网络抓取 )所设计的，
    使用它可以以快速、简单、可扩展的方式从网站中提取所需的数据。
        但目前Scrapy的用途十分广泛，可用于如数据挖掘、监测和自动化测试等领域，
    也可以应用在获取API所返回的数据(例如 Amazon Associates Web Services ) 或者通用的网络爬虫。

        Scrapy 是基于twisted框架开发而来，twisted是一个流行的事件驱动的python网络框架（Python Twisted介绍 https://blog.csdn.net/hanhuili/article/details/9389433）。
    因此Scrapy使用了一种非阻塞（又名异步）的代码来实现并发。整体架构大致如下：
        https://images2017.cnblogs.com/blog/1036857/201711/1036857-20171109221422778-1731419400.png


# 2 安装
    # 1 安装 twisted
    # 2 安装 scrapy
        # 翻墙 pip3 install scrapy
        
# 3 组成：
    #  1. 引擎(EGINE)
    # 引擎负责控制系统所有组件之间的数据流，并在某些动作发生时触发事件。有关详细信息，请参见上面的数据流部分。
    # 
    #  2. 调度器(SCHEDULER)
    # 用来接受引擎发过来的请求, 压入队列中, 并在引擎再次请求的时候返回. 可以想像成一个URL的优先级队列, 由它来决定下一个要抓取的网址是什么, 同时去除重复的网址
    # 
    #  3. 下载器(DOWLOADER)
    # 用于下载网页内容, 并将网页内容返回给EGINE，下载器是建立在twisted这个高效的异步模型上的
    # 
    #  4. 爬虫(SPIDERS)
    # PIDERS是开发人员自定义的类，发送初始请求，用来解析responses，并且提取items，或者发送新的请求
    # 
    #  5. 项目管道(ITEM PIPLINES)
    # 在items被提取后负责处理它们，主要包括清理、验证、持久化（比如存到数据库）和发送新的请求等操作
    # 
    #  6. 下载器中间件(Downloader Middlewares)
    # 位于Scrapy引擎和下载器之间，主要用来处理从EGINE传到DOWLOADER的请求request，已经从DOWNLOADER传到EGINE的响应response，你可用该中间件做以下几件事
    #    1 process a request just before it is sent to the Downloader (i.e. right before Scrapy sends the request to the website);
    #    2 change received response before passing it to a spider;
    #    3 send a new Request instead of passing received response to a spider;
    #    4 pass response to a spider without fetching a web page;
    #    5 silently drop some requests.
    # 
    #  7. 爬虫中间件(Spider Middlewares)
    # 位于EGINE和SPIDERS之间，主要工作是处理SPIDERS的输入（即responses）和输出（即requests）

# 4 使用命令行：

    #1 查看帮助 命令
        scrapy -h
        scrapy <command> -h

    #2 有两种命令：全局命令Global commands，项目命令Project-only commands。
        # 其中Project-only必须切到项目文件夹下才能执行，而Global的命令则不需要
        Global commands:
            startproject #在当前目录下创建项目
            genspider    #创建爬虫程序
            
            settings     #如果是在项目目录下，则得到的是该项目的配置
                # 在 项目目录下 执行 <scrapy settings --get 配置项> 命令 得到 settings.py配置文件中该配置项相应的值。
           
            runspider    #运行一个独立的python文件，不必创建项目
                # 执行<scrapy runspider 爬虫路径> 命令 运行爬虫
                
            shell   #scrapy shell url地址  在交互式调试，如选择器规则正确与否
                scrapy shell --nolog https://www.baidu.com
                    # 进入命令行的交互式调试
                    # 支持 table补全
                    C:\Users\69598>scrapy shell --nolog https://www.baidu.com
                    [s] Available Scrapy objects:
                    [s]   scrapy     scrapy module (contains scrapy.Request, scrapy.Selector, etc)
                    [s]   crawler    <scrapy.crawler.Crawler object at 0x0000023BB0B10748>
                    [s]   item       {}
                    [s]   request    <GET https://www.baidu.com>
                    [s]   response   <200 https://www.baidu.com>
                    [s]   settings   <scrapy.settings.Settings object at 0x0000023BB0CDBAC8>
                    [s]   spider     <DefaultSpider 'default' at 0x23bb113b0c8>
                    [s] Useful shortcuts:
                    [s]   fetch(url[, redirect=True]) Fetch URL and update local objects (by default, redirects are followed)
                    [s]   fetch(req)                  Fetch a scrapy.Request and update local objects
                    [s]   shelp()           Shell help (print this help)
                    [s]   view(response)    View response in a browser
                    In [1]: 

                    In [1]: response.status #获取状态码
                    Out[1]: 200

                    In [2]: response.headers # 获取响应头
                    Out[2]:
                    {b'Cache-Control': b'private, no-cache, no-store, proxy-revalidate, no-transform',
                     b'Content-Type': b'text/html',
                     b'Date': b'Fri, 17 Apr 2020 15:23:47 GMT',
                     b'Last-Modified': b'Mon, 23 Jan 2017 13:24:17 GMT',
                     b'Pragma': b'no-cache',
                     b'Server': b'bfe/1.0.8.18',
                     b'Set-Cookie': b'BDORZ=27315; max-age=86400; domain=.baidu.com; path=/'}

                    In [3]:   
                    In [3]: request.headers # 获取请求头
                    Out[3]:
                    {b'Accept': b'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                     b'Accept-Language': b'en',
                     b'User-Agent': b'Scrapy/2.0.1 (+https://scrapy.org)',
                     b'Accept-Encoding': b'gzip, deflate'}

                    In [4]: 
                    In [4]: response.xpath('//a') # 查找元素
                    Out[4]:
                    [<Selector xpath='//a' data='<a href="http://news.baidu.com" name=...'>,
                     <Selector xpath='//a' data='<a href="https://www.hao123.com" name...'>,
                     <Selector xpath='//a' data='<a href="http://map.baidu.com" name="...'>,
                     <Selector xpath='//a' data='<a href="http://v.baidu.com" name="tj...'>,
                     <Selector xpath='//a' data='<a href="http://tieba.baidu.com" name...'>,
                     <Selector xpath='//a' data='<a href="http://www.baidu.com/bdorz/l...'>,
                     <Selector xpath='//a' data='<a href="//www.baidu.com/more/" name=...'>,
                     <Selector xpath='//a' data='<a href="http://home.baidu.com">关于百度</a>'>,
                     <Selector xpath='//a' data='<a href="http://ir.baidu.com">About B...'>,
                     <Selector xpath='//a' data='<a href="http://www.baidu.com/duty/">...'>,
                     <Selector xpath='//a' data='<a href="http://jianyi.baidu.com/" cl...'>]

                    In [5]:   
                    In [5]: exit #退出调试器


                    C:\Users\69598>

            fetch   #独立于程单纯地爬取一个页面，可以拿到请求头
                scrapy fetch --nolog --headers https://www.baidu.com
                    # --nolog 不输出日志信息 --headers 输出请求头和响应头信息 如不写 会输出整个页面
                    C:\Users\69598>scrapy fetch --nolog --headers https://www.baidu.com
                    > Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
                    > Accept-Language: en
                    > User-Agent: Scrapy/2.0.1 (+https://scrapy.org)
                    > Accept-Encoding: gzip, deflate
                    >
                    < Cache-Control: private, no-cache, no-store, proxy-revalidate, no-transform
                    < Content-Type: text/html
                    < Date: Fri, 17 Apr 2020 15:18:25 GMT
                    < Last-Modified: Mon, 23 Jan 2017 13:24:18 GMT
                    < Pragma: no-cache
                    < Server: bfe/1.0.8.18
                    < Set-Cookie: BDORZ=27315; max-age=86400; domain=.baidu.com; path=/
                    C:\Users\69598>

            view   #下载完毕后直接弹出浏览器，以此可以分辨出哪些数据是ajax请求
                # scrapy view https://www.baidu.com #在浏览器打开百度，有点像selenium

            version      #scrapy version 查看scrapy的版本，
                # scrapy version -v 查看scrapy所有依赖库的版本
        
        Project-only commands:
            crawl        #运行爬虫，必须创建项目才行，确保配置文件中ROBOTSTXT_OBEY = False
                # 在项目目录下 执行<scrapy crawl 爬虫名> 命令 运行爬虫
            
            check        #检测项目中有无语法错误 在项目目录下执行 scrapy check

            list         #列出项目中所包含的爬虫名

            edit         #编辑器，一般不用

            parse        #scrapy parse url地址 --callback 回调函数  #以此可以验证我们的回调函数是否正确
            
            bench        #scrapy bench压力测试  测试 爬虫程序可以爬取的 速度 
            在项目目录下执行 scrapy bench  可以测试 爬虫程序可以爬取的 速度 情况

                D:\pyj\st\study\8爬虫\AMAZON>scrapy bench
                2020-04-18 07:38:18 [scrapy.utils.log] INFO: Scrapy 2.0.1 started (bot: AMAZON)
                2020-04-18 07:38:18 [scrapy.utils.log] INFO: Versions: lxml 4.4.1.0, libxml2 2.9.9, cssselect 1.1.0, parsel 1.5.2, w3lib 1.21.0, Twisted 20.3.0, Python 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 
                64 bit (AMD64)], pyOpenSSL 19.0.0 (OpenSSL 1.1.1d  10 Sep 2019), cryptography 2.7, Platform Windows-10-10.0.18362-SP0
                2020-04-18 07:38:19 [scrapy.crawler] INFO: Overridden settings:
                {'BOT_NAME': 'AMAZON',
                 'CLOSESPIDER_TIMEOUT': 10,
                 'LOGSTATS_INTERVAL': 1,
                 'LOG_LEVEL': 'INFO',
                 'NEWSPIDER_MODULE': 'AMAZON.spiders',
                 'ROBOTSTXT_OBEY': True,
                 'SPIDER_MODULES': ['AMAZON.spiders']}
                2020-04-18 07:38:19 [scrapy.extensions.telnet] INFO: Telnet Password: 9baec76c23a79f31
                2020-04-18 07:38:19 [scrapy.middleware] INFO: Enabled extensions:
                ['scrapy.extensions.corestats.CoreStats',
                 'scrapy.extensions.telnet.TelnetConsole',
                 'scrapy.extensions.closespider.CloseSpider',
                 'scrapy.extensions.logstats.LogStats']
                2020-04-18 07:38:19 [scrapy.middleware] INFO: Enabled downloader middlewares:
                ['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
                 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
                 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
                 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
                 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
                 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
                 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
                 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
                 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
                 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
                 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
                 'scrapy.downloadermiddlewares.stats.DownloaderStats']
                2020-04-18 07:38:19 [scrapy.middleware] INFO: Enabled spider middlewares:
                ['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
                 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
                 'scrapy.spidermiddlewares.referer.RefererMiddleware',
                 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
                 'scrapy.spidermiddlewares.depth.DepthMiddleware']
                2020-04-18 07:38:19 [scrapy.middleware] INFO: Enabled item pipelines:
                []
                2020-04-18 07:38:19 [scrapy.core.engine] INFO: Spider opened
                2020-04-18 07:38:19 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
                2020-04-18 07:38:19 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
                
                #开始压力测试  页面数/分钟
                2020-04-18 07:38:20 [scrapy.extensions.logstats] INFO: Crawled 71 pages (at 4260 pages/min), scraped 0 items (at 0 items/min)
                2020-04-18 07:38:21 [scrapy.extensions.logstats] INFO: Crawled 127 pages (at 3360 pages/min), scraped 0 items (at 0 items/min)
                2020-04-18 07:38:22 [scrapy.extensions.logstats] INFO: Crawled 184 pages (at 3420 pages/min), scraped 0 items (at 0 items/min)
                2020-04-18 07:38:23 [scrapy.extensions.logstats] INFO: Crawled 239 pages (at 3300 pages/min), scraped 0 items (at 0 items/min)
                2020-04-18 07:38:24 [scrapy.extensions.logstats] INFO: Crawled 288 pages (at 2940 pages/min), scraped 0 items (at 0 items/min)
                2020-04-18 07:38:25 [scrapy.extensions.logstats] INFO: Crawled 336 pages (at 2880 pages/min), scraped 0 items (at 0 items/min)
                2020-04-18 07:38:26 [scrapy.extensions.logstats] INFO: Crawled 383 pages (at 2820 pages/min), scraped 0 items (at 0 items/min)
                2020-04-18 07:38:27 [scrapy.extensions.logstats] INFO: Crawled 424 pages (at 2460 pages/min), scraped 0 items (at 0 items/min)
                2020-04-18 07:38:28 [scrapy.extensions.logstats] INFO: Crawled 472 pages (at 2880 pages/min), scraped 0 items (at 0 items/min)
                2020-04-18 07:38:29 [scrapy.core.engine] INFO: Closing spider (closespider_timeout)
                # 结论 爬取速度： 2400 pages/min
                2020-04-18 07:38:29 [scrapy.extensions.logstats] INFO: Crawled 512 pages (at 2400 pages/min), scraped 0 items (at 0 items/min)
                2020-04-18 07:38:30 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
                {'downloader/request_bytes': 229977,
                 'downloader/request_count': 527,
                 'downloader/request_method_count/GET': 527,
                 'downloader/response_bytes': 1564747,
                 'downloader/response_count': 527,
                 'downloader/response_status_count/200': 527,
                 'elapsed_time_seconds': 10.741979,
                 'finish_reason': 'closespider_timeout',
                 'finish_time': datetime.datetime(2020, 4, 17, 23, 38, 30, 241484),
                 'log_count/INFO': 20,
                 'request_depth_max': 19,
                 'response_received_count': 527,
                 'robotstxt/request_count': 1,
                 'robotstxt/response_count': 1,
                 'robotstxt/response_status_count/200': 1,
                 'scheduler/dequeued': 526,
                 'scheduler/dequeued/memory': 526,
                 'scheduler/enqueued': 10518,
                 'scheduler/enqueued/memory': 10518,
                 'start_time': datetime.datetime(2020, 4, 17, 23, 38, 19, 499505)}
                2020-04-18 07:38:30 [scrapy.core.engine] INFO: Spider closed (closespider_timeout)

                D:\pyj\st\study\8爬虫\AMAZON>

# 5 创建项目和项目配置：
    # 执行 scrapy startproject 项目名称 命令在当前目录下创建项目
        (venv) D:\pyj\st\study\8爬虫>scrapy startproject AMAZON
        New Scrapy project 'AMAZON', using template directory 'd:\anaconda3\lib\site-packages\scrapy\templates\project', created in:        
            D:\pyj\st\study\8爬虫\AMAZON

        You can start your first spider with:
            cd AMAZON
            scrapy genspider example example.com
    # 该命令在该目录下建立了 项目目录结构：
        project_name/
            scrapy.cfg
            project_name/
                __init__.py
                items.py
                pipelines.py
                settings.py
                spiders/
                    __init__.py
                    爬虫1.py
                    爬虫2.py
                    爬虫3.py
        # 文件说明
            scrapy.cfg      项目的主配置信息，用来部署scrapy时使用，爬虫相关的配置信息在settings.py文件中。
            items.py        设置数据存储模板，用于结构化数据，如：Django的Model
            pipelines       数据处理行为，如：一般结构化的数据持久化
            settings.py     配置文件，如：递归的层数、并发数，延迟下载等。强调:配置文件的选项必须大写否则视为无效，正确写法USER_AGENT='xxxx'
            spiders         爬虫目录，如：创建文件，编写爬虫规则
        # 注意：一般创建爬虫文件时，以网站域名命名

    # scrapy项目的配置：详见scrapy框架2 关于配置文件.py文件
        有通用配置、项目配置和爬虫自定义配置三块。后面的配置会覆盖前面的配置。

        通用配置是所有的scrapy项目都会加载的配置，文件在scrapy框架目录下的settings文件夹的default_settings.py文件中。
        项目配置是当前项目文件夹下的settings.py文件中，覆盖该项目。
        爬虫的自定义配置是爬虫文件的custom_settings字典，覆盖该爬虫。

# 6 spiders 文件夹
    # 放爬虫py文件的地方
    # 爬虫文件
        # 爬虫文件由命令 < scrapy genspider 爬虫名字 爬取域 >依据基本模板创建,
            见 命令行产出的爬虫文件
        # 爬虫文件是定义爬取和解析页面行为的文件，是由一系列类（定义了一个网址或一组网址将被爬取）组成，
        # 具体包括如何执行爬取任务并且如何从页面中提取结构化的数据。
    
    # 详见 amazon.py 
        1 爬虫类有5种,最基本的是scrapy.Spider
        2 如何为爬虫增加自定义配置项 custom_settings={ }
        3 爬虫如何发送请求，其实不是发送请求，而是建立请求对象 scrapy.Request(url)，真正发送请求在下载器
            '''
            class Request(object_ref):
            
                def __init__(self, url, callback=None, method='GET', headers=None, body=None,
                             cookies=None, meta=None, encoding='utf-8', priority=0,
                             dont_filter=False, errback=None, flags=None, cb_kwargs=None):
            '''
            请求对象的默认回调 callback 就是解析函数 parse()，
            默认的请求方法 get，默认过滤重复的url（dont_filter=False），也就是不发送重复请求。

        4 如何自定义初始请求，覆盖 start_requests() 方法：可以封装一系列请求对象，返回请求对象任务列表，也可以用yield返回请求对象。
        5 如何自定义去重过滤。
            # 博客：https://www.cnblogs.com/linhaifeng/articles/7811861.html#_label5    
            # 视频：https://www.bilibili.com/video/BV1CE411i73L?p=41
            # 在settings.py 中 添加如下：
                # 原来去重过滤的控制项不在settings.py中，是在内存里。
                ['DUPEFILTER_CLASS']='scrapy.dupefilters.RFPDupeFilter'
                # 修改为自定义的类，添加到settings.py 文件中 就可以起自定义去重过滤的作用
                ['DUPEFILTER_CLASS']='某目录.某py文件.自定义类'
                # 当然要起作用 请求对象的 dont_filter=False, 即去重过滤。
                # 自定义类内容如下 覆盖去重过滤的主程序
                class MyDupeFilter(object):
                    def __init__(self):
                        self.visited=set()

                    # 实例化时，会先到这里，如果用到settings的配置项会从这里实例化，没有就到init去实例化。
                    
                    @classmethod
                    def from_settings(cls,settings):# 碰到cls 就考虑是用来实例化的
                        return cls()  

                    # 去重过滤的主程序 没重的就加入集合，重了的就返回True
                    def request_seen(self,request):
                        if request.url in self.visited:
                            return True
                        self.visited.add(request.url)

                    def open(self):  # can return deferred
                        pass
                    
                    def close(self, reason):  # can return a deferred
                        pass
                    
                    def log(self, request, spider):  # log that a request has been filtered
                        pass

        6 如何给url传参
            # 给爬虫文件爬虫类增加init，让参数key接收到命令行的参数值
                def __init__(self,参数key,*args,**kwargs):
                    super(类名,self).__init__(*args,**kwargs)
                    self.参数key=参数key

            # 1 通过命令行 传参
                scrapy crawl 爬虫名 -a 参数key=参数值 （比如该参数是搜索框中输入的内容 keyword='xxx'）
            
            # 2 通过entrypoint.py 传参
                execute(['scrapy','crawl','amazon','-a','参数key=参数值','--nolog'])

            # 编码 
                from urllib.parse import urlencode
                basurl='http://xxxx'
                url_args=urlencode({urlkey:self.参数key}) #解析成为网络格式
            # 拼接
                url=basurl+url_args

        7 爬虫结束时的钩子函数 def close(self,reason):    

    # amazon 爬虫对象的 self.settings 配置项 比 settings.py配置文件多的多。
        (venv) D:\pyj\st\study\8爬虫\AMAZON>d:/pyj/st/venv/Scripts/python.exe d:/pyj/st/study/8爬虫/AMAZON/entrypoint.py
        ('AJAXCRAWL_ENABLED', False)
        ('AUTOTHROTTLE_DEBUG', False)
        ('AUTOTHROTTLE_ENABLED', False)
        ('AUTOTHROTTLE_MAX_DELAY', 60.0)
        ('AUTOTHROTTLE_START_DELAY', 5.0)
        ('AUTOTHROTTLE_TARGET_CONCURRENCY', 1.0)
        ('BOT_NAME', 'egon_AMAZON')              # 原来('BOT_NAME', 'AMAZON')  在 amazon.py 的 class AmazonSpider类中的custom_settings覆盖
        ('CLOSESPIDER_ERRORCOUNT', 0)
        ('CLOSESPIDER_ITEMCOUNT', 0)
        ('CLOSESPIDER_PAGECOUNT', 0)
        ('CLOSESPIDER_TIMEOUT', 0)
        ('COMMANDS_MODULE', '')
        ('COMPRESSION_ENABLED', True)
        ('CONCURRENT_ITEMS', 100)
        ('CONCURRENT_REQUESTS', 16)
        ('CONCURRENT_REQUESTS_PER_DOMAIN', 8)
        ('CONCURRENT_REQUESTS_PER_IP', 0)
        ('COOKIES_DEBUG', False)
        ('COOKIES_ENABLED', True)
        ('DEFAULT_ITEM_CLASS', 'scrapy.item.Item')
        ('DEFAULT_REQUEST_HEADERS', <scrapy.settings.BaseSettings object at 0x000002B5FA7FAD88>)
        ('DEPTH_LIMIT', 0)
        ('DEPTH_PRIORITY', 0)
        ('DEPTH_STATS_VERBOSE', False)
        ('DNSCACHE_ENABLED', True)
        ('DNSCACHE_SIZE', 10000)
        ('DNS_RESOLVER', 'scrapy.resolver.CachingThreadedResolver')
        ('DNS_TIMEOUT', 60)
        ('DOWNLOADER', 'scrapy.core.downloader.Downloader')
        ('DOWNLOADER_CLIENTCONTEXTFACTORY', 'scrapy.core.downloader.contextfactory.ScrapyClientContextFactory')
        ('DOWNLOADER_CLIENT_TLS_CIPHERS', 'DEFAULT')
        ('DOWNLOADER_CLIENT_TLS_METHOD', 'TLS')
        ('DOWNLOADER_CLIENT_TLS_VERBOSE_LOGGING', False)
        ('DOWNLOADER_HTTPCLIENTFACTORY', 'scrapy.core.downloader.webclient.ScrapyHTTPClientFactory')
        ('DOWNLOADER_MIDDLEWARES', <scrapy.settings.BaseSettings object at 0x000002B5FA81C188>)
        ('DOWNLOADER_MIDDLEWARES_BASE', <scrapy.settings.BaseSettings object at 0x000002B5FA81C3C8>)
        ('DOWNLOADER_STATS', True)
        ('DOWNLOAD_DELAY', 0)
        ('DOWNLOAD_FAIL_ON_DATALOSS', True)
        ('DOWNLOAD_HANDLERS', <scrapy.settings.BaseSettings object at 0x000002B5FA821CC8>)
        ('DOWNLOAD_HANDLERS_BASE', <scrapy.settings.BaseSettings object at 0x000002B5FA821DC8>)
        ('DOWNLOAD_MAXSIZE', 1073741824)
        ('DOWNLOAD_TIMEOUT', 180)
        ('DOWNLOAD_WARNSIZE', 33554432)
        ('DUPEFILTER_CLASS', 'scrapy.dupefilters.RFPDupeFilter')
        ('EDITOR', '%s -m idlelib.idle')
        ('EXTENSIONS', <scrapy.settings.BaseSettings object at 0x000002B5FA826488>)
        ('EXTENSIONS_BASE', <scrapy.settings.BaseSettings object at 0x000002B5FA826588>)
        ('FEED_EXPORTERS', <scrapy.settings.BaseSettings object at 0x000002B5FA807C08>)
        ('FEED_EXPORTERS_BASE', <scrapy.settings.BaseSettings object at 0x000002B5FA807E88>)
        ('FEED_EXPORT_ENCODING', None)
        ('FEED_EXPORT_FIELDS', None)
        ('FEED_EXPORT_INDENT', 0)
        ('FEED_FORMAT', 'jsonlines')
        ('FEED_STORAGES', <scrapy.settings.BaseSettings object at 0x000002B5FA826AC8>)
        ('FEED_STORAGES_BASE', <scrapy.settings.BaseSettings object at 0x000002B5FA826BC8>)
        ('FEED_STORAGE_FTP_ACTIVE', False)
        ('FEED_STORAGE_S3_ACL', '')
        ('FEED_STORE_EMPTY', False)
        ('FEED_TEMPDIR', None)
        ('FEED_URI', None)
        ('FEED_URI_PARAMS', None)
        ('FILES_STORE_GCS_ACL', '')
        ('FILES_STORE_S3_ACL', 'private')
        ('FTP_PASSIVE_MODE', True)
        ('FTP_PASSWORD', 'guest')
        ('FTP_USER', 'anonymous')
        ('HTTPCACHE_ALWAYS_STORE', False)
        ('HTTPCACHE_DBM_MODULE', 'dbm')
        ('HTTPCACHE_DIR', 'httpcache')
        ('HTTPCACHE_ENABLED', False)
        ('HTTPCACHE_EXPIRATION_SECS', 0)
        ('HTTPCACHE_GZIP', False)
        ('HTTPCACHE_IGNORE_HTTP_CODES', [])
        ('HTTPCACHE_IGNORE_MISSING', False)
        ('HTTPCACHE_IGNORE_RESPONSE_CACHE_CONTROLS', [])
        ('HTTPCACHE_IGNORE_SCHEMES', ['file'])
        ('HTTPCACHE_POLICY', 'scrapy.extensions.httpcache.DummyPolicy')
        ('HTTPCACHE_STORAGE', 'scrapy.extensions.httpcache.FilesystemCacheStorage')
        ('HTTPPROXY_AUTH_ENCODING', 'latin-1')
        ('HTTPPROXY_ENABLED', True)
        ('IMAGES_STORE_GCS_ACL', '')
        ('IMAGES_STORE_S3_ACL', 'private')
        ('ITEM_PIPELINES', <scrapy.settings.BaseSettings object at 0x000002B5FA82CD08>)
        ('ITEM_PIPELINES_BASE', <scrapy.settings.BaseSettings object at 0x000002B5FA82CE08>)
        ('ITEM_PROCESSOR', 'scrapy.pipelines.ItemPipelineManager')
        ('LOGSTATS_INTERVAL', 60.0)
        ('LOG_DATEFORMAT', '%Y-%m-%d %H:%M:%S')
        ('LOG_ENABLED', False)
        ('LOG_ENCODING', 'utf-8')
        ('LOG_FILE', None)
        ('LOG_FORMAT', '%(asctime)s [%(name)s] %(levelname)s: %(message)s')
        ('LOG_FORMATTER', 'scrapy.logformatter.LogFormatter')
        ('LOG_LEVEL', 'DEBUG')
        ('LOG_SHORT_NAMES', False)
        ('LOG_STDOUT', False)
        ('MAIL_FROM', 'scrapy@localhost')
        ('MAIL_HOST', 'localhost')
        ('MAIL_PASS', None)
        ('MAIL_PORT', 25)
        ('MAIL_USER', None)
        ('MEMDEBUG_ENABLED', False)
        ('MEMDEBUG_NOTIFY', [])
        ('MEMUSAGE_CHECK_INTERVAL_SECONDS', 60.0)
        ('MEMUSAGE_ENABLED', True)
        ('MEMUSAGE_LIMIT_MB', 0)
        ('MEMUSAGE_NOTIFY_MAIL', [])
        ('MEMUSAGE_WARNING_MB', 0)
        ('METAREFRESH_ENABLED', True)
        ('METAREFRESH_IGNORE_TAGS', [])
        ('METAREFRESH_MAXDELAY', 100)
        ('NEWSPIDER_MODULE', 'AMAZON.spiders')
        ('RANDOMIZE_DOWNLOAD_DELAY', True)
        ('REACTOR_THREADPOOL_MAXSIZE', 10)
        ('REDIRECT_ENABLED', True)
        ('REDIRECT_MAX_TIMES', 20)
        ('REDIRECT_PRIORITY_ADJUST', 2)
        ('REFERER_ENABLED', True)
        ('REFERRER_POLICY', 'scrapy.spidermiddlewares.referer.DefaultReferrerPolicy')
        ('RETRY_ENABLED', True)
        ('RETRY_HTTP_CODES', [500, 502, 503, 504, 522, 524, 408, 429])
        ('RETRY_PRIORITY_ADJUST', -1)
        ('RETRY_TIMES', 2)
        ('ROBOTSTXT_OBEY', False)
        ('ROBOTSTXT_PARSER', 'scrapy.robotstxt.ProtegoRobotParser')
        ('ROBOTSTXT_USER_AGENT', None)
        ('SCHEDULER', 'scrapy.core.scheduler.Scheduler')
        ('SCHEDULER_DEBUG', False)
        ('SCHEDULER_DISK_QUEUE', 'scrapy.squeues.PickleLifoDiskQueue')
        ('SCHEDULER_MEMORY_QUEUE', 'scrapy.squeues.LifoMemoryQueue')
        ('SCHEDULER_PRIORITY_QUEUE', 'scrapy.pqueues.ScrapyPriorityQueue')
        ('SCRAPER_SLOT_MAX_ACTIVE_SIZE', 5000000)
        ('SPIDER_CONTRACTS', <scrapy.settings.BaseSettings object at 0x000002B5FA835748>)
        ('SPIDER_CONTRACTS_BASE', <scrapy.settings.BaseSettings object at 0x000002B5FA835848>)
        ('SPIDER_LOADER_CLASS', 'scrapy.spiderloader.SpiderLoader')
        ('SPIDER_LOADER_WARN_ONLY', False)
        ('SPIDER_MIDDLEWARES', <scrapy.settings.BaseSettings object at 0x000002B5FA835C48>)
        ('SPIDER_MIDDLEWARES_BASE', <scrapy.settings.BaseSettings object at 0x000002B5FA835D48>)
        ('SPIDER_MODULES', ['AMAZON.spiders'])
        ('STATSMAILER_RCPTS', [])
        ('STATS_CLASS', 'scrapy.statscollectors.MemoryStatsCollector')
        ('STATS_DUMP', True)
        ('TELNETCONSOLE_ENABLED', 1)
        ('TELNETCONSOLE_HOST', '127.0.0.1')
        ('TELNETCONSOLE_PASSWORD', None)
        ('TELNETCONSOLE_PORT', [6023, 6073])
        ('TELNETCONSOLE_USERNAME', 'scrapy')
        ('TEMPLATES_DIR', 'd:\\pyj\\st\\venv\\lib\\site-packages\\scrapy\\templates')
        ('TWISTED_REACTOR', None)
        ('URLLENGTH_LIMIT', 2083)
        ('USER_AGENT', 'Scrapy/2.0.1 (+https://scrapy.org)')
        ('SETTINGS_MODULE', 'AMAZON.settings')
        ('REQUEST_HEADERS', {})                 # 原来没有 在 amazon.py 的 class AmazonSpider类中的custom_settings新增

        (venv) D:\pyj\st\study\8爬虫\AMAZON

# 7 items.py 
    # 就是django的orm的models 
    # 一个类就是一个table或collection
    # spider返回一个item就是添加一行记录或文档。

    使用简单的类定义语法和Field 对象声明项目。这是一个例子：

    import scrapy   

    class Product(scrapy.Item):
        name = scrapy.Field()
        price = scrapy.Field()
        stock = scrapy.Field()
        tags = scrapy.Field()
        last_updated = scrapy.Field(serializer=str) 
    
    注意    

    那些熟悉Django的人会注意到，Scrapy Items的声明与Django Models类似，不同之处在于Scrapy Items更简单，
    因为没有不同字段类型的概念

# 8 pipelines.py 持久化
    # 爬虫启动时 连接mongodb 
    # 爬虫关闭时 关闭连接
    # 爬取过程中返回item时，添加item到db
    # 如果发现返回的item不对时，可用发起新的请求

    一 pipelines.py示范模板

        from scrapy.exceptions import DropItem  #异常

        class CustomPipeline(object):
            # 2 初始化 第一步创建的对象
            def __init__(self,v):
                self.value = v  
            
            # 1 创建CustomPipeline对象 即cls()
            @classmethod
            def from_crawler(cls, crawler):
                """
                Scrapy会先通过getattr判断我们是否自定义了from_crawler,有则调它来完
                成实例化
                """
                val = crawler.settings.getint('MMMM')
                return cls(val) 

        # ------上半部是完成实例化的，------下半部是爬虫启动和关闭的钩子函数，以及核心持久化函数------

            def open_spider(self,spider):
                """
                爬虫刚启动时执行一次
                """
                print('000000') 

            def close_spider(self,spider):
                """
                爬虫关闭时执行一次
                """
                print('111111') 


            def process_item(self, item, spider):
                # 操作并进行持久化  

                # return表示会被后续的pipeline继续处理
                return item 

                # 表示将item丢弃，不会被后续pipeline处理
                # raise DropItem()  


    二 可以写多个Pipeline类
        #1、如果优先级高的Pipeline的process_item返回一个值或者None，会自动传给下一个pipline的process_item,
        
        #2、如果只想让第一个Pipeline执行，那得让第一个pipline的process_item抛出异常raise DropItem()

        #3、可以用spider.name == '爬虫名' 来控制哪些爬虫用哪些pipeline

    三 例：
        #1、修改配置文件settings.py 添加mongodb 配置

            HOST="127.0.0.1"
            PORT=27017
            USER="root"
            PWD="123"
            DB="amazon"
            TABLE="goods"



            ITEM_PIPELINES = {
               'Amazon.pipelines.CustomPipeline': 200, 
            }

            项目管理={
                '目录.文件.类1'：优先级（1-1000，越小优先级越高）,# item 按优先级高低逐级返回
                '目录.文件.类2'：优先级（1-1000，越小优先级越高）,# item 按优先级高低逐级返回
                ...
            }

        #2、pipelines.py
        from pymongo import MongoClient
        class CustomPipeline(object):
            def __init__(self,host,port,user,pwd,db,table):
                self.host=host
                self.port=port
                self.user=user
                self.pwd=pwd
                self.db=db
                self.table=table

            @classmethod
            def from_crawler(cls, crawler):
                """
                Scrapy会先通过getattr判断我们是否自定义了from_crawler,有则调它来完
                成实例化
                """
                HOST = crawler.settings.get('HOST')
                PORT = crawler.settings.get('PORT')
                USER = crawler.settings.get('USER')
                PWD = crawler.settings.get('PWD')
                DB = crawler.settings.get('DB')
                TABLE = crawler.settings.get('TABLE')
                return cls(HOST,PORT,USER,PWD,DB,TABLE)

            def open_spider(self,spider):
                """
                爬虫刚启动时执行一次 
                """
                # 在这里实例化了mongo客户端对象 self.client,用该对象操作mongodb数据库。
                self.client = MongoClient('mongodb://%s:%s@%s:%s' %(self.user,self.pwd,self.host,self.port))

            def close_spider(self,spider):
                """
                爬虫关闭时执行一次
                """
                self.client.close()


            def process_item(self, item, spider):
                # 操作并进行持久化

                # 把item对象转为字典
                d=dict(item)
                if all(d.values()): #如果 该字典的值 都 不为空 将 该字典 持久化 
                    self.client[self.db][self.table].save(d)
                return item # 交给下一优先级的pipeline

# 9 下载中间件Downloader Middlewares和代理池(proxy pool)

    下载中间件的用途
        1、在process——request内，自定义下载，不用scrapy的下载
        2、对请求进行二次加工，比如
            设置请求头
            设置cookie
            添加代理

    下载中间件的使用说明：
        class DownMiddleware1(object):
            # 处理请求
            def process_request(self, request, spider):
                """
                请求需要被下载时，经过所有下载器中间件的process_request调用
                :param request: 封装的scrapy请求对象 scrapy.Request()
                :param spider: 爬虫，有spider.name可用来取爬虫名字，
                :return:  
                    None,让继续后续中间件去下载；比如让  后续优先级低的中间件 class DownMiddleware2 的 def process_request(self, request, spider):
                    Response对象，停止process_request的执行，开始执行process_response。停止后续优先级低的中间件的 请求的 执行，但并不地址后续中间件 响应的 执行。
                    Request对象，停止中间件的执行，request会被重新调度下载（将Request重新给引擎，→ 调度，→ 引擎 → 下载中间件）
                    raise IgnoreRequest异常，停止process_request的执行，开始执行process_exception
                """
                pass
            # 处理响应
            def process_response(self, request, response, spider):
                """
                spider处理完成，返回时调用
                :param response:
                :param result:
                :param spider:
                :return: 
                    Response 对象：转交给其他中间件process_response
                    Request 对象：停止中间件，request会被重新调度下载
                    raise IgnoreRequest 异常：调用Request.errback
                """
                print('response1')
                return response
            # 处理异常
            def process_exception(self, request, exception, spider):
                """
                当下载处理器(download handler)或 process_request() (下载中间件)抛出异常
                :param response:
                :param exception:
                :param spider:
                :return: 
                    None：继续交给后续中间件处理异常；
                    Response对象：停止后续process_exception方法
                    Request对象：停止中间件，request将会被重新调用下载
                """
                return None    

    为了防止爬取过程的ip被封，一般都会使用代理池，常用的开源代理池软件：
        jhao104/proxy_pool https://github.com/jhao104/proxy_pool

    加代理一般都是在下载中间件加，这样就都加了，如果代理失败会抛异常：
        在中间件处理异常的时候，就把该代理从代理池删除，同时，从代理池找出一个新代理，如此往复。

# 10 Spider中间件(Middleware)
    # 9.1 编写 spider中间件 类
        实现以下几个方法：
        编写spider中间件十分简单。每个中间件组件是一个定义了以下一个或多个方法的Python类:

        class SpiderMiddleware(object):
            # 1 创建 SpiderMiddleware对象 cls()
            @classmethod
            def from_crawler(cls, crawler):
                # This method is used by Scrapy to create your spiders.
                s = cls()
                # 用crawler对象将函数和信号绑定crawler.signals.connect(func,signal)
                # 绑定对象的spider_opened方法和爬取开始信号signals.spider_opened
                crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
                return s
            # --- 上面 是实例化
            def process_spider_input(self,response, spider):
                '''
                当response通过spider中间件时，该方法被调用，处理该response。

                process_spider_input() 应该返回 None 或者抛出一个异常。

                如果其返回 None ，Scrapy将会继续处理该response，调用所有其他的中间件直到spider处理该response。

                如果其跑出一个异常(exception)，Scrapy将不会调用任何其他中间件的 process_spider_input() 方法，并调用request的errback。 errback的输出将会以另一个方向被重新输入到中间件链中，使用 process_spider_output() 方法来处理，当其抛出异常时则带调用 process_spider_exception() 。

                参数:	
                response (Response 对象) – 被处理的response
                spider (Spider 对象) – 该response对应的spider
                process_spider_output(response, result, spider)
                当Spider处理response返回result时，该方法被调用。
                '''
                pass

            def process_spider_output(self, response, result, spider): 
                '''
                result必须返回包含 Request 、dict 或 Item 对象的可迭代对象(iterable)。

                参数:	
                response (Response 对象) – 生成该输出的response
                result (包含 Request 、dict 或 Item 对象的可迭代对象(iterable)) – spider返回的result
                spider (Spider 对象) – 其结果被处理的spider
                '''
                pass

            def process_spider_exception(response, exception, spider):
                '''
                当spider或(其他spider中间件的) process_spider_input() 跑出异常时， 该方法被调用。

                process_spider_exception() 必须要么返回 None ， 返回一个包含 Response 、dict 或 Item 对象的可迭代对象(iterable)。

                如果其返回 None ，Scrapy将继续处理该异常，调用中间件链中的其他中间件的 process_spider_exception() 方法，直到所有中间件都被调用，该异常到达引擎(异常将被记录并被忽略)。

                如果其返回一个可迭代对象，则中间件链的 process_spider_output() 方法被调用， 其他的 process_spider_exception() 将不会被调用。

                参数:	
                response (Response 对象) – 异常被抛出时被处理的response
                exception (Exception 对象) – 被跑出的异常
                spider (Spider 对象) – 抛出该异常的spider
                '''
                pass

            def process_start_requests(start_requests, spider):
                '''
                0.15 新版功能.

                该方法以spider 启动的request为参数被调用，执行的过程类似于 process_spider_output() ，
                只不过其没有相关联的response并且必须返回request(不是item)。

                其接受一个可迭代的对象(start_requests 参数)且必须返回另一个包含 Request 对象的可迭代对象。
                # Must return only requests (not items).

                注解

                当在您的spider中间件实现该方法时， 
                您必须返回一个可迭代对象(类似于参数start_requests)且不要遍历所有的 start_requests。 
                该迭代器会很大(甚至是无限)，进而导致内存溢出。 
                Scrapy引擎在其具有能力处理start request时将会拉起request， 
                因此start request迭代器会变得无限，而由其他参数来停止spider( 例如时间限制或者item/page记数)。

                参数:	
                start_requests (包含 Request 的可迭代对象) – start requests
                spider (Spider 对象) – start requests所属的spider
                '''
                pass

    # 9.2 激活 spider中间件
        修改settings.py配置文件，
            SPIDER_MIDDLEWARES = {
                '文件夹.文件.spider中间件类1': 优先级,
                '文件夹.文件.spider中间件类2': 优先级,
                ...
            }

# 11 信号（Signals）
    Scrapy使用信号来通知事情发生。是Scrapy的钩子框架。
    用于扩展(Extensions)和中间件(Middleware)的编写。

    # 信号的用法：
        用crawler对象将函数和信号绑定：
        
            crawler.signals.connect(func,signal=某信号)

    内置信号参考手册(Built-in signals reference)
    以下给出Scrapy内置信号的列表及其意义:

        # engine        钩子 引擎钩子函数
            engine_started
                scrapy.signals.engine_started()
                当Scrapy引擎启动爬取时发送该信号。

                该信号支持返回deferreds。

                注解

                该信号可能会在信号 spider_opened 之后被发送，取决于spider的启动方式。 所以不要 依赖 该信号会比 spider-opened 更早被发送。

            engine_stopped
                scrapy.signals.engine_stopped()
                当Scrapy引擎停止时发送该信号(例如，爬取结束)。

                该信号支持返回deferreds。

        # itempipelin   钩子 持久化钩子函数
            item_scraped
                scrapy.signals.item_scraped(item, response, spider)
                当item被爬取，并通过所有 Item Pipeline 后(没有被丢弃(dropped)，发送该信号。

                该信号支持返回deferreds。

                参数:	
                item (dict 或 Item 对象) – 爬取到的item
                spider (Spider 对象) – 爬取item的spider
                response (Response 对象) – 提取item的response

            item_dropped
                scrapy.signals.item_dropped(item, exception, spider)
                当item通过 Item Pipeline ，有些pipeline抛出 DropItem 异常，丢弃item时，该信号被发送。

                该信号支持返回deferreds。

                参数:	
                item (dict 或 Item 对象) – Item Pipeline 丢弃的item
                spider (Spider 对象) – 爬取item的spider
                exception (DropItem 异常) – 导致item被丢弃的异常(必须是 DropItem 的子类)
        
        # spider        钩子 爬取钩子函数
            spider_closed
                scrapy.signals.spider_closed(spider, reason)
                当某个spider被关闭时，该信号被发送。该信号可以用来释放每个spider在 spider_opened 时占用的资源。

                该信号支持返回deferreds。

                参数:	
                spider (Spider 对象) – 关闭的spider
                reason (str) – 描述spider被关闭的原因的字符串。如果spider是由于完成爬取而被关闭，则其为 'finished' 。否则，如果spider是被引擎的 close_spider 方法所关闭，则其为调用该方法时传入的 reason 参数(默认为 'cancelled')。如果引擎被关闭(例如， 输入Ctrl-C)，则其为 'shutdown' 。

            spider_opened
                scrapy.signals.spider_opened(spider)
                当spider开始爬取时发送该信号。该信号一般用来分配spider的资源，不过其也能做任何事。

                该信号支持返回deferreds。

                参数:	spider (Spider 对象) – 开启的spider

            spider_idle
                scrapy.signals.spider_idle(spider)
                当spider进入空闲(idle)状态时该信号被发送。空闲意味着:

                requests正在等待被下载
                requests被调度
                items正在item pipeline中被处理
                当该信号的所有处理器(handler)被调用后，如果spider仍然保持空闲状态， 引擎将会关闭该spider。当spider被关闭后， spider_closed 信号将被发送。

                您可以，比如，在 spider_idle 处理器中调度某些请求来避免spider被关闭。

                该信号 不支持 返回deferreds。

                参数:	spider (Spider 对象) – 空闲的spider

            spider_error
                scrapy.signals.spider_error(failure, response, spider)
                当spider的回调函数产生错误时(例如，抛出异常)，该信号被发送。

                参数:	
                failure (Failure 对象) – 以Twisted Failure 对象抛出的异常
                response (Response 对象) – 当异常被抛出时被处理的response
                spider (Spider 对象) – 抛出异常的spider

        # scheduler     钩子 调度器钩子函数
            request_scheduled
                scrapy.signals.request_scheduled(request, spider)
                当引擎调度一个 Request 对象用于下载时，该信号被发送。

                该信号 不支持 返回deferreds。

                参数:	
                request (Request 对象) – 到达调度器的request
                spider (Spider 对象) – 产生该request的spider

        # downloader    钩子 下载器钩子函数
            response_received
                scrapy.signals.response_received(response, request, spider)
                当引擎从downloader获取到一个新的 Response 时发送该信号。

                该信号 不支持 返回deferreds。

                参数:	
                response (Response 对象) – 接收到的response
                request (Request 对象) – 生成response的request
                spider (Spider 对象) – response所对应的spider

            response_downloaded
                scrapy.signals.response_downloaded(response, request, spider)
                当一个 HTTPResponse 被下载时，由downloader发送该信号。

                该信号 不支持 返回deferreds。

                参数:	
                response (Response 对象) – 下载的response
                request (Request 对象) – 生成response的request
                spider (Spider 对象) – response所对应的spider

# 12 扩展 (Extensions)
    扩展框架提供一个机制，使得你能将自定义功能绑定到Scrapy。

    扩展只是正常的类，它们在Scrapy启动时被实例化、初始化。

    # 设置扩展(Extension settings)
        扩展使用 Scrapy settings 管理它们的设置，这跟其他Scrapy代码一样。

        通常扩展需要给它们的设置加上前缀，以避免跟已有(或将来)的扩展冲突。 
        比如，一个扩展处理 Google Sitemaps， 则可以使用类似 GOOGLESITEMAP_ENABLED、GOOGLESITEMAP_DEPTH 等设置。 

        # 加载和激活扩展
            扩展在扩展类被实例化时加载和激活。 因此，所有扩展的实例化代码必须在类的构造函数(__init__)中执行。

            要使得扩展可用，需要把它添加到Scrapy的 EXTENSIONS 配置中。 在 EXTENSIONS 中，每个扩展都使用一个字符串表示，即扩展类的全Python路径。 比如:

            EXTENSIONS = {
                'scrapy.extensions.corestats.CoreStats': 500,
                'scrapy.telnet.TelnetConsole': 500,
            }
            如你所见，EXTENSIONS 配置是一个dict，key是扩展类的路径，value是顺序, 它定义扩展加载的顺序。
            扩展顺序不像中间件的顺序那么重要，而且扩展之间一般没有关联。 扩展加载的顺序并不重要，因为它们并不相互依赖。

            如果你需要添加扩展而且它依赖别的扩展，你就可以使用该特性了。

            [1] 这也是为什么Scrapy的配置项 EXTENSIONS_BASE (它包括了所有内置且开启的扩展)定义所有扩展的顺序都相同 (500)。

            # 可用的(Available)、开启的(enabled)和禁用的(disabled)的扩展
                并不是所有可用的扩展都会被开启。一些扩展经常依赖一些特别的配置。 
                比如，HTTP Cache扩展是可用的但默认是禁用的，除非 HTTPCACHE_ENABLED 配置项设置了。

            # 禁用扩展(Disabling an extension)
                为了禁用一个默认开启的扩展(比如，包含在 EXTENSIONS_BASE 中的扩展)，
                 需要将其顺序(order)设置为 None 。比如:

                EXTENSIONS = {
                    'scrapy.extensions.corestats.CoreStats': None,
                }

    # 实现你的扩展
        每个扩展是一个单一的Python class. Scrapy扩展(包括middlewares和pipelines)的主要入口是 from_crawler 类方法， 
        它接收一个 Crawler 类的实例.通过这个对象访问settings，signals，stats，控制爬虫的行为。

        通常来说，扩展关联到 signals 并执行它们触发的任务。

        最后，如果 from_crawler 方法抛出 NotConfigured 异常， 扩展会被禁用。否则，扩展会被开启。

        # 扩展例子(Sample extension)
            这里我们将实现一个简单的扩展来演示上面描述到的概念。 该扩展会在以下事件时记录一条日志：

                spider被打开
                spider被关闭
                爬取了特定数量的条目(items)
            该扩展通过 MYEXT_ENABLED 配置项开启， items的数量通过 MYEXT_ITEMCOUNT 配置项设置。

            以下是扩展的代码:
                import logging
                from scrapy import signals
                from scrapy.exceptions import NotConfigured

                logger = logging.getLogger(__name__)

                class SpiderOpenCloseLogging(object):
                
                    def __init__(self, item_count):
                        self.item_count = item_count

                        self.items_scraped = 0

                    @classmethod
                    def from_crawler(cls, crawler):
                        # first check if the extension should be enabled and raise

                        # NotConfigured otherwise

                        if not crawler.settings.getbool('MYEXT_ENABLED'):
                        
                            raise NotConfigured
                        
                        # get the number of items from settings

                        item_count = crawler.settings.getint('MYEXT_ITEMCOUNT', 1000)

                        # instantiate the extension object

                        ext = cls(item_count)

                        # connect the extension object to signals

                        crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)

                        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)

                        crawler.signals.connect(ext.item_scraped, signal=signals.item_scraped)

                        # return the extension object

                        return ext

                    def spider_opened(self, spider):
                        logger.info("opened spider %s", spider.name)

                    def spider_closed(self, spider):
                        logger.info("closed spider %s", spider.name)

                    def item_scraped(self, item, spider):
                        self.items_scraped += 1
                        if self.items_scraped % self.item_count == 0:
                            logger.info("scraped %d items", self.items_scraped)

    # 内置扩展介绍

        记录统计扩展(Log Stats extension)
            classscrapy.extensions.logstats.LogStats
            记录基本的统计信息，比如爬取的页面和条目(items)。

        核心统计扩展(Core Stats extension)
            classscrapy.extensions.corestats.CoreStats
            如果统计收集器(stats collection)启用了，该扩展开启核心统计收集(参考 数据收集(Stats Collection))。

        Telnet console 扩展
            classscrapy.telnet.TelnetConsole
            提供一个telnet控制台，用于进入当前执行的Scrapy进程的Python解析器， 这对代码调试非常有帮助。

            telnet控制台通过 TELNETCONSOLE_ENABLED 配置项开启， 服务器会监听 TELNETCONSOLE_PORT 指定的端口。

        内存使用扩展(Memory usage extension)
            classscrapy.extensions.memusage.MemoryUsage
            注解

            This extension does not work in Windows.

            监控Scrapy进程内存使用量，并且：

            如果使用内存量超过某个指定值，发送提醒邮件
            如果超过某个指定值，关闭spider
            当内存用量达到 MEMUSAGE_WARNING_MB 指定的值，发送提醒邮件。 
            当内存用量达到 MEMUSAGE_LIMIT_MB 指定的值，发送提醒邮件，同时关闭spider， Scrapy进程退出。

            该扩展通过 MEMUSAGE_ENABLED 配置项开启，可以使用以下选项：

            MEMUSAGE_LIMIT_MB
            MEMUSAGE_WARNING_MB
            MEMUSAGE_NOTIFY_MAIL
            MEMUSAGE_REPORT

        内存调试扩展(Memory debugger extension)
            classscrapy.extensions.memdebug.MemoryDebugger
            该扩展用于调试内存使用量，它收集以下信息：

            没有被Python垃圾回收器收集的对象
            应该被销毁却仍然存活的对象。更多信息请参考 使用 trackref 调试内存泄露
            开启该扩展，需打开 MEMDEBUG_ENABLED 配置项。 信息将会存储在统计信息(stats)中。

        关闭spider扩展
            classscrapy.extensions.closespider.CloseSpider
            当某些状况发生，spider会自动关闭。每种情况使用指定的关闭原因。

            关闭spider的情况可以通过下面的设置项配置：

            CLOSESPIDER_TIMEOUT
            CLOSESPIDER_ITEMCOUNT
            CLOSESPIDER_PAGECOUNT
            CLOSESPIDER_ERRORCOUNT
           
            CLOSESPIDER_TIMEOUT
                默认值: 0

                一个整数值，单位为秒。如果一个spider在指定的秒数后仍在运行， 
                它将以 closespider_timeout 的原因被自动关闭。 
                如果值设置为0（或者没有设置），spiders不会因为超时而关闭。

            CLOSESPIDER_ITEMCOUNT
                缺省值: 0

                一个整数值，指定条目的个数。如果spider爬取条目数超过了指定的数， 
                并且这些条目通过item pipeline传递，spider将会以 closespider_itemcount 的原因被自动关闭。

            CLOSESPIDER_PAGECOUNT
                0.11 新版功能.

                缺省值: 0

                一个整数值，指定最大的抓取响应(reponses)数。
                 如果spider抓取数超过指定的值，则会以 closespider_pagecount 的原因自动关闭。 
                 如果设置为0（或者未设置），spiders不会因为抓取的响应数而关闭。

            CLOSESPIDER_ERRORCOUNT
                0.11 新版功能.

                缺省值: 0

                一个整数值，指定spider可以接受的最大错误数。
                 如果spider生成多于该数目的错误，它将以 closespider_errorcount 的原因关闭。 
                 如果设置为0（或者未设置），spiders不会因为发生错误过多而关闭。

            StatsMailer extension
                classscrapy.extensions.statsmailer.StatsMailer
                这个简单的扩展可用来在一个域名爬取完毕时发送提醒邮件， 包含Scrapy收集的统计信息。 
                邮件会发送个通过 STATSMAILER_RCPTS 指定的所有接收人。

        Debugging extensions
            Stack trace dump extension
                classscrapy.extensions.debug.StackTraceDump
                当收到 SIGQUIT 或 SIGUSR2 信号，spider进程的信息将会被存储下来。 
                存储的信息包括：

                    1 engine状态(使用 scrapy.utils.engin.get_engine_status())
                    2 所有存活的引用(live references)(参考 使用 trackref 调试内存泄露)
                    3 所有线程的堆栈信息

                当堆栈信息和engine状态存储后，Scrapy进程继续正常运行。

                该扩展只在POSIX兼容的平台上可运行（比如不能在Windows运行）， 
                因为 SIGQUIT 和 SIGUSR2 信号在Windows上不可用。

                至少有两种方式可以向Scrapy发送 SIGQUIT 信号:

                    1 在Scrapy进程运行时通过按Ctrl-(仅Linux可行?)

                    2 运行该命令(<pid> 是Scrapy运行的进程):kill -QUIT <pid>
            
            调试扩展(Debugger extension)
                classscrapy.extensions.debug.Debugger
                当收到 SIGUSR2 信号，将会在Scrapy进程中调用 Python debugger 。 debugger退出后，Scrapy进程继续正常运行。

                更多信息参考 Debugging in Python 。

                该扩展只在POSIX兼容平台上工作(比如不能再Windows上运行)。

# 13 选择器
    response.selector.css()
    response.selector.xpath()
    可简写为
    response.css()
    response.xpath()

    #1 //与/
        response.xpath('//body/a/')#
        response.css('div a::text')

        >>> response.xpath('//body/a') #开头的//代表从整篇文档中寻找,body之后的/代表body的儿子
        []
        >>> response.xpath('//body//a') #开头的//代表从整篇文档中寻找,body之后的//代表body的子子孙孙
        [<Selector xpath='//body//a' data='<a href="image1.html">Name: My image 1 <'>, <Selector xpath='//body//a' data='<a href="image2.html">Name: My image 2 <'>, <Selector xpath='//body//a' data='<a href="
        image3.html">Name: My image 3 <'>, <Selector xpath='//body//a' data='<a href="image4.html">Name: My image 4 <'>, <Selector xpath='//body//a' data='<a href="image5.html">Name: My image 5 <'>]

    #2 text
        >>> response.xpath('//body//a/text()')
        >>> response.css('body a::text')

    #3、extract与extract_first:从selector对象中解出内容
        >>> response.xpath('//div/a/text()').extract()
        ['Name: My image 1 ', 'Name: My image 2 ', 'Name: My image 3 ', 'Name: My image 4 ', 'Name: My image 5 ']
        >>> response.css('div a::text').extract()
        ['Name: My image 1 ', 'Name: My image 2 ', 'Name: My image 3 ', 'Name: My image 4 ', 'Name: My image 5 ']

        >>> response.xpath('//div/a/text()').extract_first()
        'Name: My image 1 '
        >>> response.css('div a::text').extract_first()
        'Name: My image 1 '

    #4、属性：xpath的属性加前缀@
        >>> response.xpath('//div/a/@href').extract_first()
        'image1.html'
        >>> response.css('div a::attr(href)').extract_first()
        'image1.html'

    #4、嵌套查找
        >>> response.xpath('//div').css('a').xpath('@href').extract_first()
        'image1.html'

    #5、设置默认值
        >>> response.xpath('//div[@id="xxx"]').extract_first(default="not found")
        'not found'

    #4、按照属性查找
        response.xpath('//div[@id="images"]/a[@href="image3.html"]/text()').extract()
        response.css('#images a[@href="image3.html"]/text()').extract()

    #5、按照属性模糊查找
        response.xpath('//a[contains(@href,"image")]/@href').extract()
        response.css('a[href*="image"]::attr(href)').extract()

        response.xpath('//a[contains(@href,"image")]/img/@src').extract()
        response.css('a[href*="imag"] img::attr(src)').extract()

        response.xpath('//*[@href="image1.html"]')
        response.css('*[href="image1.html"]')

    #6、正则表达式
        response.xpath('//a/text()').re(r'Name: (.*)')
        response.xpath('//a/text()').re_first(r'Name: (.*)')

    #7、xpath相对路径
        >>> res=response.xpath('//a[contains(@href,"3")]')[0]
        >>> res.xpath('img')
        [<Selector xpath='img' data='<img src="image3_thumb.jpg">'>]
        >>> res.xpath('./img')
        [<Selector xpath='./img' data='<img src="image3_thumb.jpg">'>]
        >>> res.xpath('.//img')
        [<Selector xpath='.//img' data='<img src="image3_thumb.jpg">'>]
        >>> res.xpath('//img') #这就是从头开始扫描
        [<Selector xpath='//img' data='<img src="image1_thumb.jpg">'>, <Selector xpath='//img' data='<img src="image2_thumb.jpg">'>, <Selector xpath='//img' data='<img src="image3_thumb.jpg">'>, <Selector xpa
        th='//img' data='<img src="image4_thumb.jpg">'>, <Selector xpath='//img' data='<img src="image5_thumb.jpg">'>]

    #8、带变量的xpath
        >>> response.xpath('//div[@id=$xxx]/a/text()',xxx='images').extract_first()
        'Name: My image 1 '
        >>> response.xpath('//div[count(a)=$yyy]/@id',yyy=5).extract_first() #求有5个a标签的div的id
        'images'


#Scrapy官方中文 — Scrapy 1.0.5 文档 https://scrapy-chs.readthedocs.io/zh_CN/1.0/intro/overview.html