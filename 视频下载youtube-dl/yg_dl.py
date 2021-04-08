import os
import sys
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import asyncio
# 定义目录
ml=r'F:\video\456'
# 下载程序
def yg_dl(url):
    os.system(f'you-get -o {ml} {url}')

if __name__ == "__main__":
    urls=[
        'https://www.youtube.com/watch?v=lQpIVvACteo',
        'https://www.youtube.com/watch?v=EortFRT1aJM',
        'https://www.youtube.com/watch?v=f16BU5F7psQ',
        'https://www.youtube.com/watch?v=SAdXrWb0Nrs',
        
    
    ]
    # 线程池 不填数量 默认=cpu核心数量*5
    pool=ThreadPoolExecutor()


    # 用线程池 异步
    for url in urls:
        pool.submit(yg_dl,url)
    pool.shutdown()#关池

