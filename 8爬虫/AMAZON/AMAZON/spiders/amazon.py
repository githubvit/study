# -*- coding: utf-8 -*-
import scrapy

# 1 scrapy 的爬虫类 共有 5种
from scrapy.spiders import Spider,CrawlSpider,XMLFeedSpider,CSVFeedSpider,SitemapSpider

    # 对于常用的爬虫类 提供了简写，即不用写 scrapy.spiders.Spider 只要写 scrapy.Spider
    # Spider是最常用的最基础的爬虫类，其余的爬虫类各有所长。


from scrapy.dupefilters import RFPDupeFilter
from scrapy.core.scheduler import Scheduler


class AmazonSpider(scrapy.Spider):
    name = 'amazon'                         # 爬虫名称
    allowed_domains = ['www.amazon.cn']     # 爬取的域
    start_urls = ['http://www.amazon.cn/']  # 起始请求地址

 # 2 settings.py 放的是项目的通用配置，custom_settings这个地方放的是该爬虫的自定义配置
    custom_settings={
        'BOT_NAME':'egon_AMAZON', # 将覆盖 settings文件中的 同名字段
        'REQUEST_HEADERS':{}, # 增加 settings 文件中没有的字段
    }

# 3 每个请求都一定要绑定一个回调函数，这个解析函数就是默认的回调函数
    def parse(self, response): 

        # 爬虫对象 self 上有配置settings 有日志loger
        # print(self.settings.get('BOT_NAME'))    # 会用custom_settings 覆盖 settings 同名字段 # egon_AMAZON
        # 用get没有该字段不报错，用['BOT_NAME']报错 见 下 dic

        # self.logger.warning(f"输出{self.settings['REQUEST_HEADERS']}") # 必须 关掉 --nolog 
        # 结果： 2020-04-18 15:25:32 [amazon] WARNING: 输出{}
        # 看出日志名默认为spider的名字 [amazon] 

        # 查看配置项
        # print(dir(self.settings))
        # for item in self.settings.items():
        #     print(item)
        
        # print(type(response)) ## <class 'scrapy.http.response.html.HtmlResponse'>

        # print(dir(response)) 
        # ['_DEFAULT_ENCODING', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
        # '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
        # '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
        # '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__weakref__', '_auto_detect_fun',
        #  '_body', '_body_declared_encoding', '_body_inferred_encoding', '_cached_benc', '_cached_selector', 
        # '_cached_ubody', '_declared_encoding', '_encoding', '_get_body', '_get_url', '_headers_encoding', 
        # '_set_body', '_set_url', '_url', 'body', 'body_as_unicode', 'cb_kwargs', 'certificate', 'copy', 'css', 
        # 'encoding', 'flags', 'follow', 'follow_all', 'headers', 'meta', 'replace', 'request', 'selector', 'status', 
        # 'text', 'url', 'urljoin', 'xpath']
        
        print(f'解析 : {response.url} ,len:{len(response.body)},{response.meta}') 
        # 解析 : https://www.amazon.cn/ipad2019/s?k=ipad2019 ,len:952534,{'abcd': 1, 'download_timeout': 180.0, 
        # 'download_slot': 'www.amazon.cn',  'download_latency': 0.20701885223388672, 'redirect_times': 1, 
        # 'redirect_ttl': 19, 'redirect_urls': ['https://www.amazon.cn/s?k=ipad2019&__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&crid=G1P7014A5783&sprefix=ip%2Caps%2C216&ref=nb_sb_ss_i_11_2'], 'redirect_reasons': [301]}

# 4 scrapy 发送请求 Request 其实并不是发送请求，而是封装请求对象，真正发送请求是下载器。
    # Request 提供简写  本来是 scrapy.http.Request 可以简写为 scrapy.Request 
    # print(scrapy.Request is scrapy.http.Request) #True

    # scrapy.Request(url,callback=func,meta={}) 
    # 每个请求后一定要有callback。
    # meta 字段 ，该请求到哪都会带着meta信息，值的格式为字典，可以在里面放代理等，解析回调时 可用response.meta查看。

    '''
    class Request(object_ref):

        def __init__(self, url, callback=None, method='GET', headers=None, body=None,
                     cookies=None, meta=None, encoding='utf-8', priority=0,
                     dont_filter=False, errback=None, flags=None, cb_kwargs=None):
    '''
    # 默认的请求方法 get，默认是过滤重复的url，也就是不重复发送请求。

# 5 如果你想要改变初始请求，你就需要覆盖这个方法
    def start_requests(self): 
        # 该方法用来发起第一个Requests请求，且必须返回一个可迭代的对象。
        # 它在爬虫程序打开时就被Scrapy调用，Scrapy只调用它一次。
        # 默认从start_urls里取出每个url来生成Request(url, dont_filter=True)
        
        # scrapy.Request()

        # 5.1 要注意的是：并不是真正发送请求，而是封装请求对象
        
        # 初始请求可以发送多个请求即封装多个请求对象，由于scrapy采用twisted模式，所以要把多个请求任务，放到任务列表中，去集成io阻塞。
        
        # tasks=[scrapy.Request(url) for url in self.start_urls]
        
        # 然后返回该请求列表，
        # return tasks

        # 因为 要返回可迭代的任务列表 可以用 yeild 返回生成器 每次返回一个请求对象
        # for url in self.start_urls:
        #     yield scrapy.Request(url)
        
        # url相同的三个请求
        yield scrapy.Request('https://www.amazon.cn/s?k=ipad2019&__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&crid=G1P7014A5783&sprefix=ip%2Caps%2C216&ref=nb_sb_ss_i_11_2',
                            callback=self.parse,
                            dont_filter=False,
                            meta={'abcd':1}
                            )
        yield scrapy.Request('https://www.amazon.cn/s?k=ipad2019&__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&crid=G1P7014A5783&sprefix=ip%2Caps%2C216&ref=nb_sb_ss_i_11_2',
                            callback=self.parse,
                            dont_filter=False
                            )
        yield scrapy.Request('https://www.amazon.cn/s?k=ipad2019&__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&crid=G1P7014A5783&sprefix=ip%2Caps%2C216&ref=nb_sb_ss_i_11_2',
                            callback=self.parse,
                            dont_filter=False
                            )
        # dont_filter=True 不去重的结果 有3个  请求失败时，和在用代理1爬取失败后更换代理2爬取等，这就不能去重。
            # 解析 : https://www.amazon.cn/ipad2019/s?k=ipad2019 ,len:952534
            # 解析 : https://www.amazon.cn/ipad2019/s?k=ipad2019 ,len:952530
            # 解析 : https://www.amazon.cn/ipad2019/s?k=ipad2019 ,len:952544

        # dont_filter=False 去重结果：就1个 解析 : https://www.amazon.cn/ipad2019/s?k=ipad2019 ,len:952561



        # dic={
        #     'a':1,
        #     "b":2
        # }
        # print(dic['c'])
        # Traceback (most recent call last):
        #  File "d:/pyj/st/study/8爬虫/AMAZON/AMAZON/spiders/amazon.py", line 52, in <module>
        #     print(dic['c'])
        # KeyError: 'c'
        # print(dic.get('c')) #None

    # 6 结束函数
    def close(self,reason):
        print('结束了')

# 解析 : https://www.amazon.cn/ipad2019/s?k=ipad2019 ,len:952520,{'abcd': 1, 'download_timeout': 180.0, 'download_slot': 'www.amazon.cn', 
# 'download_latency': 0.17754411697387695, 'redirect_times': 1, 'redirect_ttl': 19, 'redirect_urls': ['https://www.amazon.cn/s?k=ipad2019&__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&crid=G1P7014A5783&sprefix=ip%2Caps%2C216&ref=nb_sb_ss_i_11_2'], 'redirect_reasons': [301]}
# 结束了