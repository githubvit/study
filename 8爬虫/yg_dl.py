import os
import sys
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import asyncio
# 定义目录
ml=r'F:\video'
# 下载程序
def yg_dl(url):
    os.system(f'you-get -o {ml} {url}')

if __name__ == "__main__":
    urls=[
        'https://www.bilibili.com/video/BV19441127ba?p=27',
        'https://www.bilibili.com/video/BV19441127ba?p=94',
    ]
    # 线程池 不填数量 默认=cpu核心数量*5
    pool=ThreadPoolExecutor(2)

    # 用线程池 异步
    for url in urls:
        pool.submit(yg_dl,url)
    pool.shutdown()#关池