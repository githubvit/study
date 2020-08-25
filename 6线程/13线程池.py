#  线程池

from concurrent.futures import ThreadPoolExecutor
from threading import current_thread
import requests,time
# requests 模块是模拟浏览器发送http请求

# 模拟爬虫 
# 爬虫 主要是两大任务 
#   从网络获取数据 这是io型任务
#   解析数据，获得结果 这是计算型任务
# 总体来说，解析数据是很快的，主要的消耗是io，因此该任务是io型 
# 所以，应该用 线程池 来解决问题。


# 1 下载数据 -- 数据生产者
def get(url):
    print('get [%s]...thread name=[%s]'%(url,current_thread().getName()))
    res=requests.get(url)
    # time.sleep(2)
    if res.status_code==200:
        return {'url':url,'content':res.text}

# 2 解析数据 得到结果 -- 数据消费者
def parse(obj):
    res=obj.result()
    print('url[%s] parse result len = [%s] ,thread name=[%s]'%(res['url'],len(res['content']),current_thread().getName()))

if __name__ == "__main__":
    # 网站列表
    urls=[
        'https://www.baidu.com',
        'https://www.python.org',
        'https://www.openstack.org',
        'https://www.baidu.com',
        'https://www.python.org',
        'https://www.openstack.org',
    ]

    # 线程池 不填数量 默认=cpu核心数量*5
    pool=ThreadPoolExecutor(3)

    # 用线程池 异步+回调
    for url in urls:
        pool.submit(get,url).add_done_callback(parse)

    pool.shutdown()#关池
    print('主线程',current_thread().getName())

# get [https://www.baidu.com]...thread name=[ThreadPoolExecutor-0_0]
# get [https://www.python.org]...thread name=[ThreadPoolExecutor-0_1]
# get [https://www.openstack.org]...thread name=[ThreadPoolExecutor-0_2]
# url[https://www.baidu.com] parse result len = [2443] ,thread name=[ThreadPoolExecutor-0_0]
# get [https://www.baidu.com]...thread name=[ThreadPoolExecutor-0_0]
# url[https://www.baidu.com] parse result len = [2443] ,thread name=[ThreadPoolExecutor-0_0]
# get [https://www.python.org]...thread name=[ThreadPoolExecutor-0_0]
# url[https://www.openstack.org] parse result len = [36791] ,thread name=[ThreadPoolExecutor-0_2]
# get [https://www.openstack.org]...thread name=[ThreadPoolExecutor-0_2]
# url[https://www.python.org] parse result len = [48876] ,thread name=[ThreadPoolExecutor-0_1]
# url[https://www.openstack.org] parse result len = [36602] ,thread name=[ThreadPoolExecutor-0_2]
# url[https://www.python.org] parse result len = [48876] ,thread name=[ThreadPoolExecutor-0_0]
# 主线程 MainThread