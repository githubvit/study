# scrapy项目的配置，有通用配置、项目配置和爬虫自定义配置三块。后面的配置会覆盖前面的配置。


# scrapy 通用配置文件 default_settings  位置 D:\pyj\st\venv\Lib\site-packages\scrapy\settings\default_settings.py

    """
    This module contains the default values for all settings used by Scrapy.

    For more information about these settings you can read the settings
    documentation in docs/topics/settings.rst

    Scrapy developers, if you add a setting here remember to:

    * add it in alphabetical order
    * group similar settings without leaving blank lines
    * add its documentation to the available settings documentation
      (docs/topics/settings.rst)

    """

    import sys
    from importlib import import_module
    from os.path import join, abspath, dirname

    AJAXCRAWL_ENABLED = False

    AUTOTHROTTLE_ENABLED = False
    AUTOTHROTTLE_DEBUG = False
    AUTOTHROTTLE_MAX_DELAY = 60.0
    AUTOTHROTTLE_START_DELAY = 5.0
    AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

    BOT_NAME = 'scrapybot'

    CLOSESPIDER_TIMEOUT = 0
    CLOSESPIDER_PAGECOUNT = 0
    CLOSESPIDER_ITEMCOUNT = 0
    CLOSESPIDER_ERRORCOUNT = 0

    COMMANDS_MODULE = ''

    COMPRESSION_ENABLED = True

    CONCURRENT_ITEMS = 100

    CONCURRENT_REQUESTS = 16
    CONCURRENT_REQUESTS_PER_DOMAIN = 8
    CONCURRENT_REQUESTS_PER_IP = 0

    COOKIES_ENABLED = True
    COOKIES_DEBUG = False

    DEFAULT_ITEM_CLASS = 'scrapy.item.Item'

    DEFAULT_REQUEST_HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en',
    }

    DEPTH_LIMIT = 0
    DEPTH_STATS_VERBOSE = False
    DEPTH_PRIORITY = 0

    DNSCACHE_ENABLED = True
    DNSCACHE_SIZE = 10000
    DNS_RESOLVER = 'scrapy.resolver.CachingThreadedResolver'
    DNS_TIMEOUT = 60

    DOWNLOAD_DELAY = 0

    DOWNLOAD_HANDLERS = {}
    DOWNLOAD_HANDLERS_BASE = {
        'data': 'scrapy.core.downloader.handlers.datauri.DataURIDownloadHandler',
        'file': 'scrapy.core.downloader.handlers.file.FileDownloadHandler',
        'http': 'scrapy.core.downloader.handlers.http.HTTPDownloadHandler',
        'https': 'scrapy.core.downloader.handlers.http.HTTPDownloadHandler',
        's3': 'scrapy.core.downloader.handlers.s3.S3DownloadHandler',
        'ftp': 'scrapy.core.downloader.handlers.ftp.FTPDownloadHandler',
    }

    DOWNLOAD_TIMEOUT = 180      # 3mins

    DOWNLOAD_MAXSIZE = 1024 * 1024 * 1024   # 1024m
    DOWNLOAD_WARNSIZE = 32 * 1024 * 1024    # 32m

    DOWNLOAD_FAIL_ON_DATALOSS = True

    DOWNLOADER = 'scrapy.core.downloader.Downloader'

    DOWNLOADER_HTTPCLIENTFACTORY = 'scrapy.core.downloader.webclient.ScrapyHTTPClientFactory'
    DOWNLOADER_CLIENTCONTEXTFACTORY = 'scrapy.core.downloader.contextfactory.ScrapyClientContextFactory'
    DOWNLOADER_CLIENT_TLS_CIPHERS = 'DEFAULT'
    # Use highest TLS/SSL protocol version supported by the platform, also allowing negotiation:
    DOWNLOADER_CLIENT_TLS_METHOD = 'TLS'
    DOWNLOADER_CLIENT_TLS_VERBOSE_LOGGING = False

    DOWNLOADER_MIDDLEWARES = {}

    DOWNLOADER_MIDDLEWARES_BASE = {
        # Engine side
        'scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware': 100,
        'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware': 300,
        'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware': 350,
        'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware': 400,
        'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 500,
        'scrapy.downloadermiddlewares.retry.RetryMiddleware': 550,
        'scrapy.downloadermiddlewares.ajaxcrawl.AjaxCrawlMiddleware': 560,
        'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware': 580,
        'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 590,
        'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': 600,
        'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 700,
        'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 750,
        'scrapy.downloadermiddlewares.stats.DownloaderStats': 850,
        'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware': 900,
        # Downloader side
    }

    DOWNLOADER_STATS = True

    DUPEFILTER_CLASS = 'scrapy.dupefilters.RFPDupeFilter'

    EDITOR = 'vi'
    if sys.platform == 'win32':
        EDITOR = '%s -m idlelib.idle'

    EXTENSIONS = {}

    EXTENSIONS_BASE = {
        'scrapy.extensions.corestats.CoreStats': 0,
        'scrapy.extensions.telnet.TelnetConsole': 0,
        'scrapy.extensions.memusage.MemoryUsage': 0,
        'scrapy.extensions.memdebug.MemoryDebugger': 0,
        'scrapy.extensions.closespider.CloseSpider': 0,
        'scrapy.extensions.feedexport.FeedExporter': 0,
        'scrapy.extensions.logstats.LogStats': 0,
        'scrapy.extensions.spiderstate.SpiderState': 0,
        'scrapy.extensions.throttle.AutoThrottle': 0,
    }

    FEED_TEMPDIR = None
    FEED_URI = None
    FEED_URI_PARAMS = None  # a function to extend uri arguments
    FEED_FORMAT = 'jsonlines'
    FEED_STORE_EMPTY = False
    FEED_EXPORT_ENCODING = None
    FEED_EXPORT_FIELDS = None
    FEED_STORAGES = {}
    FEED_STORAGES_BASE = {
        '': 'scrapy.extensions.feedexport.FileFeedStorage',
        'file': 'scrapy.extensions.feedexport.FileFeedStorage',
        'stdout': 'scrapy.extensions.feedexport.StdoutFeedStorage',
        's3': 'scrapy.extensions.feedexport.S3FeedStorage',
        'ftp': 'scrapy.extensions.feedexport.FTPFeedStorage',
    }
    FEED_EXPORTERS = {}
    FEED_EXPORTERS_BASE = {
        'json': 'scrapy.exporters.JsonItemExporter',
        'jsonlines': 'scrapy.exporters.JsonLinesItemExporter',
        'jl': 'scrapy.exporters.JsonLinesItemExporter',
        'csv': 'scrapy.exporters.CsvItemExporter',
        'xml': 'scrapy.exporters.XmlItemExporter',
        'marshal': 'scrapy.exporters.MarshalItemExporter',
        'pickle': 'scrapy.exporters.PickleItemExporter',
    }
    FEED_EXPORT_INDENT = 0

    FEED_STORAGE_FTP_ACTIVE = False
    FEED_STORAGE_S3_ACL = ''

    FILES_STORE_S3_ACL = 'private'
    FILES_STORE_GCS_ACL = ''

    FTP_USER = 'anonymous'
    FTP_PASSWORD = 'guest'
    FTP_PASSIVE_MODE = True

    HTTPCACHE_ENABLED = False
    HTTPCACHE_DIR = 'httpcache'
    HTTPCACHE_IGNORE_MISSING = False
    HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
    HTTPCACHE_EXPIRATION_SECS = 0
    HTTPCACHE_ALWAYS_STORE = False
    HTTPCACHE_IGNORE_HTTP_CODES = []
    HTTPCACHE_IGNORE_SCHEMES = ['file']
    HTTPCACHE_IGNORE_RESPONSE_CACHE_CONTROLS = []
    HTTPCACHE_DBM_MODULE = 'dbm'
    HTTPCACHE_POLICY = 'scrapy.extensions.httpcache.DummyPolicy'
    HTTPCACHE_GZIP = False

    HTTPPROXY_ENABLED = True
    HTTPPROXY_AUTH_ENCODING = 'latin-1'

    IMAGES_STORE_S3_ACL = 'private'
    IMAGES_STORE_GCS_ACL = ''

    ITEM_PROCESSOR = 'scrapy.pipelines.ItemPipelineManager'

    ITEM_PIPELINES = {}
    ITEM_PIPELINES_BASE = {}

    LOG_ENABLED = True
    LOG_ENCODING = 'utf-8'
    LOG_FORMATTER = 'scrapy.logformatter.LogFormatter'
    LOG_FORMAT = '%(asctime)s [%(name)s] %(levelname)s: %(message)s'
    LOG_DATEFORMAT = '%Y-%m-%d %H:%M:%S'
    LOG_STDOUT = False
    LOG_LEVEL = 'DEBUG'
    LOG_FILE = None
    LOG_SHORT_NAMES = False

    SCHEDULER_DEBUG = False

    LOGSTATS_INTERVAL = 60.0

    MAIL_HOST = 'localhost'
    MAIL_PORT = 25
    MAIL_FROM = 'scrapy@localhost'
    MAIL_PASS = None
    MAIL_USER = None

    MEMDEBUG_ENABLED = False        # enable memory debugging
    MEMDEBUG_NOTIFY = []            # send memory debugging report by mail at engine shutdown

    MEMUSAGE_CHECK_INTERVAL_SECONDS = 60.0
    MEMUSAGE_ENABLED = True
    MEMUSAGE_LIMIT_MB = 0
    MEMUSAGE_NOTIFY_MAIL = []
    MEMUSAGE_WARNING_MB = 0

    METAREFRESH_ENABLED = True
    METAREFRESH_IGNORE_TAGS = []
    METAREFRESH_MAXDELAY = 100

    NEWSPIDER_MODULE = ''

    RANDOMIZE_DOWNLOAD_DELAY = True

    REACTOR_THREADPOOL_MAXSIZE = 10

    REDIRECT_ENABLED = True
    REDIRECT_MAX_TIMES = 20  # uses Firefox default setting
    REDIRECT_PRIORITY_ADJUST = +2

    REFERER_ENABLED = True
    REFERRER_POLICY = 'scrapy.spidermiddlewares.referer.DefaultReferrerPolicy'

    RETRY_ENABLED = True
    RETRY_TIMES = 2  # initial response + 2 retries = 3 requests
    RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408, 429]
    RETRY_PRIORITY_ADJUST = -1

    ROBOTSTXT_OBEY = False
    ROBOTSTXT_PARSER = 'scrapy.robotstxt.ProtegoRobotParser'
    ROBOTSTXT_USER_AGENT = None

    SCHEDULER = 'scrapy.core.scheduler.Scheduler'
    SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleLifoDiskQueue'
    SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.LifoMemoryQueue'
    SCHEDULER_PRIORITY_QUEUE = 'scrapy.pqueues.ScrapyPriorityQueue'

    SCRAPER_SLOT_MAX_ACTIVE_SIZE = 5000000

    SPIDER_LOADER_CLASS = 'scrapy.spiderloader.SpiderLoader'
    SPIDER_LOADER_WARN_ONLY = False

    SPIDER_MIDDLEWARES = {}

    SPIDER_MIDDLEWARES_BASE = {
        # Engine side
        'scrapy.spidermiddlewares.httperror.HttpErrorMiddleware': 50,
        'scrapy.spidermiddlewares.offsite.OffsiteMiddleware': 500,
        'scrapy.spidermiddlewares.referer.RefererMiddleware': 700,
        'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware': 800,
        'scrapy.spidermiddlewares.depth.DepthMiddleware': 900,
        # Spider side
    }

    SPIDER_MODULES = []

    STATS_CLASS = 'scrapy.statscollectors.MemoryStatsCollector'
    STATS_DUMP = True

    STATSMAILER_RCPTS = []

    TEMPLATES_DIR = abspath(join(dirname(__file__), '..', 'templates'))

    URLLENGTH_LIMIT = 2083

    USER_AGENT = 'Scrapy/%s (+https://scrapy.org)' % import_module('scrapy').__version__

    TELNETCONSOLE_ENABLED = 1
    TELNETCONSOLE_PORT = [6023, 6073]
    TELNETCONSOLE_HOST = '127.0.0.1'
    TELNETCONSOLE_USERNAME = 'scrapy'
    TELNETCONSOLE_PASSWORD = None

    TWISTED_REACTOR = None

    SPIDER_CONTRACTS = {}
    SPIDER_CONTRACTS_BASE = {
        'scrapy.contracts.default.UrlContract': 1,
        'scrapy.contracts.default.CallbackKeywordArgumentsContract': 1,
        'scrapy.contracts.default.ReturnsContract': 2,
        'scrapy.contracts.default.ScrapesContract': 3,
    }

# scrapy 项目配置文件 settings.py 详解

    #==>第一部分：基本配置<===
    #1、项目名称，默认的USER_AGENT由它来构成，也作为日志记录的日志名
    BOT_NAME = 'Amazon'

    #2、爬虫应用路径
    SPIDER_MODULES = ['Amazon.spiders']
    NEWSPIDER_MODULE = 'Amazon.spiders'

    #3、客户端User-Agent请求头
    #USER_AGENT = 'Amazon (+http://www.yourdomain.com)'

    #4、是否遵循爬虫协议
    # Obey robots.txt rules
    ROBOTSTXT_OBEY = False

    #5、是否支持cookie，cookiejar进行操作cookie，默认开启
    #COOKIES_ENABLED = False

    #6、Telnet用于查看当前爬虫的信息，操作爬虫等...使用telnet ip port ，然后通过命令操作
    #TELNETCONSOLE_ENABLED = False
    #TELNETCONSOLE_HOST = '127.0.0.1'
    #TELNETCONSOLE_PORT = [6023,]

    #7、Scrapy发送HTTP请求默认使用的请求头
    #DEFAULT_REQUEST_HEADERS = {
    #   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    #   'Accept-Language': 'en',
    #}



    #===>第二部分：并发与延迟<===
    #1、下载器总共最大处理的并发请求数,默认值16
    #CONCURRENT_REQUESTS = 32

    #2、每个域名能够被执行的最大并发请求数目，默认值8
    #CONCURRENT_REQUESTS_PER_DOMAIN = 16

    #3、能够被单个IP处理的并发请求数，默认值0，代表无限制，需要注意两点
    #I、如果不为零，那CONCURRENT_REQUESTS_PER_DOMAIN将被忽略，即并发数的限制是按照每个IP来计算，而不是每个域名
    #II、该设置也影响DOWNLOAD_DELAY，如果该值不为零，那么DOWNLOAD_DELAY下载延迟是限制每个IP而不是每个域
    #CONCURRENT_REQUESTS_PER_IP = 16

    #4、如果没有开启智能限速，这个值就代表一个规定死的值，代表对同一网址延迟请求的秒数
    #DOWNLOAD_DELAY = 3


    #===>第三部分：智能限速/自动节流：AutoThrottle extension<===
    #一：介绍
    from scrapy.contrib.throttle import AutoThrottle #http://scrapy.readthedocs.io/en/latest/topics/autothrottle.html#topics-autothrottle
    设置目标：
    1、比使用默认的下载延迟对站点更好
    2、自动调整scrapy到最佳的爬取速度，所以用户无需自己调整下载延迟到最佳状态。用户只需要定义允许最大并发的请求，剩下的事情由该扩展组件自动完成


    #二：如何实现？
    在Scrapy中，下载延迟是通过计算建立TCP连接到接收到HTTP包头(header)之间的时间来测量的。
    注意，由于Scrapy可能在忙着处理spider的回调函数或者无法下载，因此在合作的多任务环境下准确测量这些延迟是十分苦难的。 不过，这些延迟仍然是对Scrapy(甚至是服务器)繁忙程度的合理测量，而这扩展就是以此为前提进行编写的。


    #三：限速算法
    自动限速算法基于以下规则调整下载延迟
    #1、spiders开始时的下载延迟是基于AUTOTHROTTLE_START_DELAY的值
    #2、当收到一个response，对目标站点的下载延迟=收到响应的延迟时间/AUTOTHROTTLE_TARGET_CONCURRENCY
    #3、下一次请求的下载延迟就被设置成：对目标站点下载延迟时间和过去的下载延迟时间的平均值
    #4、没有达到200个response则不允许降低延迟
    #5、下载延迟不能变的比DOWNLOAD_DELAY更低或者比AUTOTHROTTLE_MAX_DELAY更高

    #四：配置使用
    #开启True，默认False
    AUTOTHROTTLE_ENABLED = True
    #起始的延迟
    AUTOTHROTTLE_START_DELAY = 5
    #最小延迟
    DOWNLOAD_DELAY = 3
    #最大延迟
    AUTOTHROTTLE_MAX_DELAY = 10
    #每秒并发请求数的平均值，不能高于 CONCURRENT_REQUESTS_PER_DOMAIN或CONCURRENT_REQUESTS_PER_IP，调高了则吞吐量增大强奸目标站点，调低了则对目标站点更加”礼貌“
    #每个特定的时间点，scrapy并发请求的数目都可能高于或低于该值，这是爬虫视图达到的建议值而不是硬限制
    AUTOTHROTTLE_TARGET_CONCURRENCY = 16.0
    #调试
    AUTOTHROTTLE_DEBUG = True
    CONCURRENT_REQUESTS_PER_DOMAIN = 16
    CONCURRENT_REQUESTS_PER_IP = 16



    #===>第四部分：爬取深度与爬取方式<===
    #1、爬虫允许的最大深度，可以通过meta查看当前深度；0表示无深度
    # DEPTH_LIMIT = 3

    #2、爬取时，0表示深度优先Lifo(默认)；1表示广度优先FiFo

    # 后进先出，深度优先
    # DEPTH_PRIORITY = 0
    # SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleLifoDiskQueue'
    # SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.LifoMemoryQueue'
    # 先进先出，广度优先

    # DEPTH_PRIORITY = 1
    # SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
    # SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'


    #3、调度器队列
    # SCHEDULER = 'scrapy.core.scheduler.Scheduler'
    # from scrapy.core.scheduler import Scheduler

    #4、访问URL去重
    # DUPEFILTER_CLASS = 'step8_king.duplication.RepeatUrl'



    #===>第五部分：中间件、Pipelines、扩展<===
    #1、Enable or disable spider middlewares
    # See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
    #SPIDER_MIDDLEWARES = {
    #    'Amazon.middlewares.AmazonSpiderMiddleware': 543,
    #}

    #2、Enable or disable downloader middlewares
    # See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
    DOWNLOADER_MIDDLEWARES = {
       # 'Amazon.middlewares.DownMiddleware1': 543,
    }

    #3、Enable or disable extensions
    # See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
    #EXTENSIONS = {
    #    'scrapy.extensions.telnet.TelnetConsole': None,
    #}

    #4、Configure item pipelines
    # See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
    ITEM_PIPELINES = {
       # 'Amazon.pipelines.CustomPipeline': 200,
    }



    #===>第六部分：缓存<===
    """
    1. 启用缓存
        目的用于将已经发送的请求或相应缓存下来，以便以后使用

        from scrapy.downloadermiddlewares.httpcache import HttpCacheMiddleware
        from scrapy.extensions.httpcache import DummyPolicy
        from scrapy.extensions.httpcache import FilesystemCacheStorage
    """
    # 是否启用缓存策略
    # HTTPCACHE_ENABLED = True

    # 缓存策略：所有请求均缓存，下次在请求直接访问原来的缓存即可
    # HTTPCACHE_POLICY = "scrapy.extensions.httpcache.DummyPolicy"
    # 缓存策略：根据Http响应头：Cache-Control、Last-Modified 等进行缓存的策略
    # HTTPCACHE_POLICY = "scrapy.extensions.httpcache.RFC2616Policy"

    # 缓存超时时间
    # HTTPCACHE_EXPIRATION_SECS = 0

    # 缓存保存路径
    # HTTPCACHE_DIR = 'httpcache'

    # 缓存忽略的Http状态码
    # HTTPCACHE_IGNORE_HTTP_CODES = []

    # 缓存存储的插件
    # HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


    #===>第七部分：线程池<===
    REACTOR_THREADPOOL_MAXSIZE = 10
    
    #Default: 10
    #scrapy基于twisted异步IO框架，downloader是多线程的，线程数是Twisted线程池的默认大小(The maximum limit for Twisted Reactor thread pool size.)
    
    #关于twisted线程池：
    http://twistedmatrix.com/documents/10.1.0/core/howto/threading.html
    
    #线程池实现：twisted.python.threadpool.ThreadPool
    twisted调整线程池大小：
    from twisted.internet import reactor
    reactor.suggestThreadPoolSize(30)
    
    #scrapy相关源码：
    D:\python3.6\Lib\site-packages\scrapy\crawler.py
    
    #补充：
    windows下查看进程内线程数的工具：
        https://docs.microsoft.com/zh-cn/sysinternals/downloads/pslist
        或
        https://pan.baidu.com/s/1jJ0pMaM
        
        命令为：
        pslist |findstr python
    
    linux下：top -p 进程id


    #===>第八部分：其他默认配置参考<===
    D:\python3.6\Lib\site-packages\scrapy\settings\default_settings.py

# scrapy 某爬虫文件自定义配置字典 
    custom_settings={

    }