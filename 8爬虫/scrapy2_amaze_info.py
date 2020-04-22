# 记录一个 scrapy 项目
# 爬取 亚马逊 

# 1 建立AMAZON项目 在8爬虫目录下 执行 scrapy startproject AMAZON命令，得到AMAZON项目包。
    # 切换目录 (venv) D:\pyj\st\study>cd 8爬虫
    # 执行 startproject命令在当前目录下创建项目
        (venv) D:\pyj\st\study\8爬虫>scrapy startproject AMAZON
        New Scrapy project 'AMAZON', using template directory 'd:\anaconda3\lib\site-packages\scrapy\templates\project', created in:        
            D:\pyj\st\study\8爬虫\AMAZON

        You can start your first spider with:
            cd AMAZON
            scrapy genspider example example.com
        # 该命令在该目录下建立了 AMAZON 目录，作为项目目录,项目目录结构：
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
        # 在项目目录下又建立了项目同名文件夹AMAZON和scrapy.cfg配置文件
            8爬虫\AMAZON\AMAZON
            8爬虫\AMAZON\AMAZON\__pycache__
            8爬虫\AMAZON\AMAZON\spiders
            8爬虫\AMAZON\AMAZON\__init__.py
            8爬虫\AMAZON\AMAZON\items.py
            8爬虫\AMAZON\AMAZON\middlewares.py
            8爬虫\AMAZON\AMAZON\pipelines.py
            8爬虫\AMAZON\AMAZON\settings.py
            8爬虫\AMAZON\scrapy.cfg
            # 项目同名文件夹下有：
                # spiders目录，爬虫文件夹
                # items.py    里面有一些类即数据持久化对象 类似于django的数据库的表即orm的class。
                    # 爬虫目录下的爬虫程序解析完后，进行持久化就是调用items.py下的相应类去实例化，即建立相应items对象，往相应表中去添加一行记录。
                    # itmes对象在添加记录返回时，会自动触发项目管理pipelines对相应items对象添加的记录进行检查、持久化。
                # middlewares.py 中间件应该包含 爬虫中间件 和 下载器中间件
                # pipelines.py   项目管理 清理、验证、持久化（比如存到数据库）和发送新的请求等操作
                # settings.py    项目的配置文件

            # scrapy.cfg 这个cfg配置文件是 scrapy 项目写完后，部署deploy时用的配置文件。
                # 内容如下：

                '''
                # Automatically created by: scrapy startproject
                #
                # For more information about the [deploy] section see:
                # https://scrapyd.readthedocs.io/en/latest/deploy.html

                [settings]
                default = AMAZON.settings

                [deploy]
                #url = http://localhost:6800/
                project = AMAZON
                '''
                # 从中可以看出 项目的配置文件默认是AMAZON.settings。

# 2 建立爬虫程序 在项目目录AMAZON下执行 scrapy genspider 爬虫名字 爬取域 命令 
    # 会产出 爬虫名.py 文件，自动放在项目同名文件夹的爬虫目录下。
    # 爬虫名必须唯一。
    # 切换到项目目录下
    (venv) D:\pyj\st\study\8爬虫>cd AMAZON
    # 执行scrapy genspider amazon www.amazon.cn 命令建立名为amazon的爬虫，爬取的域就是亚马逊中国
    (venv) D:\pyj\st\study\8爬虫\AMAZON>scrapy genspider amazon www.amazon.cn
    Created spider 'amazon' using template 'basic' in module:
      AMAZON.spiders.amazon
        # 在爬虫目录spiders下用'basic'模板产出了amazon爬虫，文件为amazon.py.
        
        #  命令行产出的爬虫文件 amazon.py 内容如下：

            # -*- coding: utf-8 -*-
            import scrapy
            class AmazonSpider(scrapy.Spider): #继承scrapy.Spider爬虫类
                name = 'amazon'                         #爬虫名
                allowed_domains = ['www.amazon.cn']     #爬取域
                start_urls = ['http://www.amazon.cn/']  #爬取的起始网址

                def parse(self, response):     #解析，请求的回调
                    pass


# 3 在项目目录下 执行<scrapy crawl 爬虫名> 命令 运行爬虫
    修改settings.py文件
        设定默认的请求头：
        DEFAULT_REQUEST_HEADERS = {
          'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        }
    (venv) D:\pyj\st\study\8爬虫\AMAZON>scrapy crawl amazon
    2020-04-17 21:21:43 [scrapy.utils.log] INFO: Scrapy 2.0.1 started (bot: AMAZON)
    # 项目依赖包
    2020-04-17 21:21:43 [scrapy.utils.log] INFO: Versions: lxml 4.4.1.0, libxml2 2.9.9, cssselect 1.1.0, parsel 1.5.2, w3lib 1.21.0, Twisted 20.3.0, Python 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 
    64 bit (AMD64)], pyOpenSSL 19.0.0 (OpenSSL 1.1.1d  10 Sep 2019), cryptography 2.7, Platform Windows-10-10.0.18362-SP0
    2020-04-17 21:21:43 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.selectreactor.SelectReactor
    # 项目配置信息
    2020-04-17 21:21:43 [scrapy.crawler] INFO: Overridden settings:
    {'BOT_NAME': 'AMAZON',
     'NEWSPIDER_MODULE': 'AMAZON.spiders',
     'ROBOTSTXT_OBEY': True,
     'SPIDER_MODULES': ['AMAZON.spiders']}
    #  项目的扩展信息 telnet连接
    2020-04-17 21:21:43 [scrapy.extensions.telnet] INFO: Telnet Password: baa9e73012870d44
    # 开启 扩展
    2020-04-17 21:21:43 [scrapy.middleware] INFO: Enabled extensions:
    ['scrapy.extensions.corestats.CoreStats',
     'scrapy.extensions.telnet.TelnetConsole',
     'scrapy.extensions.logstats.LogStats']
    #  开启中间件 下载器中间件
    2020-04-17 21:21:43 [scrapy.middleware] INFO: Enabled downloader middlewares:
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
     #  开启中间件 爬虫中间件
    2020-04-17 21:21:43 [scrapy.middleware] INFO: Enabled spider middlewares:
    ['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
     'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
     'scrapy.spidermiddlewares.referer.RefererMiddleware',
     'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
     'scrapy.spidermiddlewares.depth.DepthMiddleware']
    #  开启项目管理 item pipeline
    2020-04-17 21:21:43 [scrapy.middleware] INFO: Enabled item pipelines:
    []
    # 运行爬虫
    2020-04-17 21:21:43 [scrapy.core.engine] INFO: Spider opened
    # 爬取0个页面 持久化0个items
    2020-04-17 21:21:43 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
    # 监听在IP ：port
    2020-04-17 21:21:43 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023  
    # 重定向到 反爬协议 robots.txt 在settings中 关闭 反爬 将 ROBOTSTXT_OBEY = True 改为 False 即可
    2020-04-17 21:21:43 [scrapy.downloadermiddlewares.redirect] DEBUG: Redirecting (301) to <GET https://www.amazon.cn/robots.txt> from <GET http://www.amazon.cn/robots.txt>
    2020-04-17 21:21:44 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.amazon.cn/robots.txt> (referer: None)
    2020-04-17 21:21:44 [scrapy.downloadermiddlewares.redirect] DEBUG: Redirecting (301) to <GET https://www.amazon.cn/> from <GET http://www.amazon.cn/>
    # 爬取起始页
    2020-04-17 21:21:45 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.amazon.cn/> (referer: None)
    # 关闭爬虫
    2020-04-17 21:21:46 [scrapy.core.engine] INFO: Closing spider (finished) 
    # 爬虫状态
    2020-04-17 21:21:46 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
    {'downloader/request_bytes': 872,
     'downloader/request_count': 4,
     'downloader/request_method_count/GET': 4,
     'downloader/response_bytes': 69729,
     'downloader/response_count': 4,
     'downloader/response_status_count/200': 2,
     'downloader/response_status_count/301': 2,
     'elapsed_time_seconds': 2.152059,
     'finish_reason': 'finished',
     'finish_time': datetime.datetime(2020, 4, 17, 13, 21, 46, 2908),
     'log_count/DEBUG': 4,
     'log_count/INFO': 10,
     'response_received_count': 2,
     'robotstxt/request_count': 1,
     'robotstxt/response_count': 1,
     'robotstxt/response_status_count/200': 1,
     'scheduler/dequeued': 2,
     'scheduler/dequeued/memory': 2,
     'scheduler/enqueued': 2,
     'scheduler/enqueued/memory': 2,
     'start_time': datetime.datetime(2020, 4, 17, 13, 21, 43, 850849)}
    2020-04-17 21:21:46 [scrapy.core.engine] INFO: Spider closed (finished)

    (venv) D:\pyj\st\study\8爬虫\AMAZON>


# 4 用py执行爬虫：
    # 在项目目录下新建entrypoint.py

    from scrapy.cmdline import excute

    excute(['scrapy','crawl','amazon'])

    # 执行 报错：
    Traceback (most recent call last):
      File "d:/pyj/st/study/8爬虫/AMAZON/entrypoint.py", line 2, in <module>
        from scrapy.cmdline import execute
    ModuleNotFoundError: No module named 'scrapy'

    # 解决1：
    把scrapy所在目录'D:\Anaconda3\Lib\site-packages'加入系统目录 
    import sys
    path='D:\Anaconda3\Lib\site-packages'
    sys.path.append(path)

    # 解决2： 在该虚拟环境下 再安装一篇scrapy 此时，就会告诉系统已经安装了scrapy
    (venv) D:\pyj\st\study>pip install scrapy

    # 执行 报 项目没激活 no active project

    (venv) D:\pyj\st\study>d:/pyj/st/venv/Scripts/python.exe d:/pyj/st/study/8爬虫/AMAZON/entrypoint.py
    crapy 2.0.1 - no active project

    nknown command: crawl

    se "scrapy" to see available commands

    # 解决 切换到项目目录下
    (venv) D:\pyj\st\study>cd 8爬虫

    (venv) D:\pyj\st\study\8爬虫>cd AMAZON
    
    (venv) D:\pyj\st\study\8爬虫\AMAZON>d:/pyj/st/venv/Scripts/python.exe d:/pyj/st/study/8爬虫/AMAZON/entrypoint.py
    2020-04-18 12:32:41 [scrapy.utils.log] INFO: Scrapy 2.0.1 started (bot: AMAZON)
    2020-04-18 12:32:41 [scrapy.utils.log] INFO: Versions: lxml 4.5.0.0, libxml2 2.9.5, cssselect 1.1.0, parsel 1.5.2, w3lib 1.21.0, Twisted 20.3.0, Python 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)], pyOpenSSL 19.1.0 (OpenSSL 1.1.1f  31 Mar 2020), cryptography 2.9, Platform Windows-10-10.0.18362-SP0
    2020-04-18 12:32:41 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.selectreactor.SelectReactor       
    2020-04-18 12:32:41 [scrapy.crawler] INFO: Overridden settings:
    {'BOT_NAME': 'AMAZON',
     'NEWSPIDER_MODULE': 'AMAZON.spiders',
     'SPIDER_MODULES': ['AMAZON.spiders']}
    2020-04-18 12:32:41 [scrapy.extensions.telnet] INFO: Telnet Password: 472065dd02fd0d68
    2020-04-18 12:32:41 [scrapy.middleware] INFO: Enabled extensions:
    ['scrapy.extensions.corestats.CoreStats',
     'scrapy.extensions.telnet.TelnetConsole',
     'scrapy.extensions.logstats.LogStats']
    2020-04-18 12:32:42 [scrapy.middleware] INFO: Enabled downloader middlewares:
    ['scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
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
    2020-04-18 12:32:42 [scrapy.middleware] INFO: Enabled spider middlewares:
    ['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
     'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
     'scrapy.spidermiddlewares.referer.RefererMiddleware',
     'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
     'scrapy.spidermiddlewares.depth.DepthMiddleware']
    2020-04-18 12:32:42 [scrapy.middleware] INFO: Enabled item pipelines:
    []
    2020-04-18 12:32:42 [scrapy.core.engine] INFO: Spider opened
    2020-04-18 12:32:42 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
    2020-04-18 12:32:42 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
    2020-04-18 12:32:42 [scrapy.downloadermiddlewares.redirect] DEBUG: Redirecting (301) to <GET https://www.amazon.cn/> from <GET http://www.amazon.cn/>
    2020-04-18 12:32:43 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.amazon.cn/> (referer: None)
    2020-04-18 12:32:43 [scrapy.core.engine] INFO: Closing spider (finished)
    2020-04-18 12:32:43 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
    {'downloader/request_bytes': 426,
     'downloader/request_count': 2,
     'downloader/request_method_count/GET': 2,
     'downloader/response_bytes': 65710,
     'downloader/response_count': 2,
     'downloader/response_status_count/200': 1,
     'downloader/response_status_count/301': 1,
     'elapsed_time_seconds': 1.710669,
     'finish_reason': 'finished',
     'finish_time': datetime.datetime(2020, 4, 18, 4, 32, 43, 764545),
     'log_count/DEBUG': 2,
     'log_count/INFO': 10,
     'response_received_count': 1,
     'scheduler/dequeued': 2,
     'scheduler/dequeued/memory': 2,
     'scheduler/enqueued': 2,
     'scheduler/enqueued/memory': 2,
     'start_time': datetime.datetime(2020, 4, 18, 4, 32, 42, 53876)}
    2020-04-18 12:32:43 [scrapy.core.engine] INFO: Spider closed (finished)
    
    (venv) D:\pyj\st\study\8爬虫\AMAZON>
    
# 5 爬取商品的名称、价格、配送信息，放到mongodb 的 goods 表中。
    1 在items.py中 准备好表 新建类 class AmazonGoods(scrapy.Item):
    2 在pipelines.py中 
        2.1 准备好 class MongoPipeline(object): 高优先级 连接mongodb数据库 持久化item 
        2.2 准备好 class FilePipeline(object):  低优先级 打开文件，写入,
        