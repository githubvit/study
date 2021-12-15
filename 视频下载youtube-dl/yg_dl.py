import os
import sys
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import asyncio
# 定义目录
ml=r'F:\video\789'
# 下载程序
def yg_dl(url):
    # 单个下载
    os.system(f'you-get -o {ml} {url}')
    # os.system(f'youtube-dl {url}') # 用youtube-dl 下载 YouTube 视频 下载的视频 就在 study 文件夹下
    # 列表下载
    # os.system(f'you-get -o {ml} -l {url}')

# 重命名文件 -O
# def yg_dl_rename(idx,url):
#     os.system(f'you-get -o {ml} -O 7-{idx+158} {url}')

if __name__ == "__main__":
    urls=[
        
        'https://www.bilibili.com/video/BV1sh411y7uE?p=1',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=2',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=3',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=4',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=5',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=6',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=7',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=8',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=9',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=10',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=11',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=12',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=13',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=14',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=15',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=16',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=17',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=18',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=19',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=20',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=21',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=22',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=23',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=24',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=25',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=26',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=27',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=28',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=29',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=30',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=31',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=32',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=33',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=34',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=35',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=36',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=37',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=38',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=39',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=40',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=41',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=42',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=43',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=44',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=45',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=46',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=47',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=48',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=49',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=50',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=51',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=52',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=53',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=54',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=55',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=56',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=57',
        'https://www.bilibili.com/video/BV1sh411y7uE?p=58',
        

    ]
    # 线程池 不填数量 默认=cpu核心数量*5
    pool=ThreadPoolExecutor(3)

    # for idx,url in enumerate(urls):
    #     pool.submit(yg_dl_rename,idx,url)

    # 用线程池 异步
    # for url_s in urls:
    #     # url=eval(url_s) 
    #     # print(url_s)
    #     url=url_s.lstrip("'").rstrip(" ' ") #取消字符串两端的引号
    #     print(url)
    #     pool.submit(yg_dl,url)

    # for i in range(120,378):
    #     # print(i)
    # #     n=i+1
    #     url='https://www.bilibili.com/video/BV17J41177ro?p={str(i)}'
    #     pool.submit(yg_dl,url)

    url='https://www.bilibili.com/video/BV1rb4y117Sz/'
    # url='https://www.bilibili.com/video/BV17J41177ro?p=119'

    pool.submit(yg_dl,url)
    pool.shutdown()#关池
# 
'''

'''