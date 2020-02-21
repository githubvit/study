# from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
# import requests
# import os
# import time
# import random
#
# def get(url):
#     print('%s GET %s' %(os.getpid(),url))
#     response=requests.get(url)
#     time.sleep(random.randint(1,3))
#
#     if response.status_code == 200:
#         return response.text
#
# def pasrse(res):
#     print('%s 解析结果为：%s' %(os.getpid(),len(res)))
#
# if __name__ == '__main__':
#     urls=[
#         'https://www.baidu.com',
#         'https://www.baidu.com',
#         'https://www.baidu.com',
#         'https://www.baidu.com',
#         'https://www.baidu.com',
#         'https://www.baidu.com',
#         'https://www.baidu.com',
#         'https://www.baidu.com',
#         'https://www.python.org',
#
#     ]
#
#     pool=ProcessPoolExecutor(4)
#     objs=[]
#     for url in urls:
#         obj=pool.submit(get,url)
#         objs.append(obj)
#
#     pool.shutdown(wait=True)
#     # 问题：
#     # 1、任务的返回值不能得到及时的处理，必须等到所有任务都运行完毕才能统一进行处理
#     # 2、解析的过程是串行执行的,如果解析一次需要花费2s,解析9次则需要花费18s
#     for obj in objs:
#         res=obj.result()
#         pasrse(res)



# from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
# import requests
# import os
# import time
# import random
#
# def get(url):
#     print('%s GET %s' %(os.getpid(),url))
#     response=requests.get(url)
#     time.sleep(random.randint(1,3))
#
#     if response.status_code == 200:
#         pasrse(response.text)
#
# def pasrse(res):
#     print('%s 解析结果为：%s' %(os.getpid(),len(res)))
#
# if __name__ == '__main__':
#     urls=[
#         'https://www.baidu.com',
#         'https://www.baidu.com',
#         'https://www.baidu.com',
#         'https://www.baidu.com',
#         'https://www.baidu.com',
#         'https://www.baidu.com',
#         'https://www.baidu.com',
#         'https://www.baidu.com',
#         'https://www.python.org',
#
#     ]
#
#     pool=ProcessPoolExecutor(4)
#     for url in urls:
#         pool.submit(get,url)
#





# from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
# import requests
# import os
# import time
# import random
#
# def get(url):
#     print('%s GET %s' %(os.getpid(),url))
#     response=requests.get(url)
#     time.sleep(random.randint(1,3))
#
#     if response.status_code == 200:
#         # 干解析的活
#         return response.text
#
# def pasrse(obj):
#     res=obj.result()
#     print('%s 解析结果为：%s' %(os.getpid(),len(res)))
#
# if __name__ == '__main__':
#     urls=[
#         'https://www.baidu.com',
#         'https://www.baidu.com',
#         'https://www.baidu.com',
#         'https://www.baidu.com',
#         'https://www.baidu.com',
#         'https://www.baidu.com',
#         'https://www.baidu.com',
#         'https://www.baidu.com',
#         'https://www.python.org',
#     ]
#
#     pool=ProcessPoolExecutor(4)
#     for url in urls:
#         obj=pool.submit(get,url)
#         obj.add_done_callback(pasrse)
#
#     # 问题：
#     # 1、任务的返回值不能得到及时的处理，必须等到所有任务都运行完毕才能统一进行处理
#     # 2、解析的过程是串行执行的,如果解析一次需要花费2s,解析9次则需要花费18s
#     print('主进程',os.getpid())





from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
from threading import current_thread
import requests
import os
import time
import random

def get(url):
    print('%s GET %s' %(current_thread().name,url))
    response=requests.get(url)
    time.sleep(random.randint(1,3))

    if response.status_code == 200:
        # 干解析的活
        return response.text

def pasrse(obj):
    res=obj.result()
    print('%s 解析结果为：%s' %(current_thread().name,len(res)))

if __name__ == '__main__':
    urls=[
        'https://www.baidu.com',
        'https://www.baidu.com',
        'https://www.baidu.com',
        'https://www.baidu.com',
        'https://www.baidu.com',
        'https://www.baidu.com',
        'https://www.baidu.com',
        'https://www.baidu.com',
        'https://www.python.org',
    ]

    pool=ThreadPoolExecutor(4)
    for url in urls:
        obj=pool.submit(get,url)
        obj.add_done_callback(pasrse)

    # 问题：
    # 1、任务的返回值不能得到及时的处理，必须等到所有任务都运行完毕才能统一进行处理
    # 2、解析的过程是串行执行的,如果解析一次需要花费2s,解析9次则需要花费18s
    print('主线程',current_thread().name)