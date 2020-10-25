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
        'https://www.ixigua.com/6874804933674304012',
        'https://www.ixigua.com/6854771607940891144',
    ]
    # 线程池 不填数量 默认=cpu核心数量*5
    pool=ThreadPoolExecutor(2)

    # 用线程池 异步
    for url in urls:
        pool.submit(yg_dl,url)
    pool.shutdown()#关池

'''
用chrome插件 edit this cookie 导出的西瓜视频的cookie
[
{
    "domain": ".ixigua.com",
    "expirationDate": 1664342427,
    "hostOnly": false,
    "httpOnly": false,
    "name": "_ga",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "GA1.2.1262755817.1601270427",
    "id": 1
},
{
    "domain": ".ixigua.com",
    "expirationDate": 1601356827,
    "hostOnly": false,
    "httpOnly": false,
    "name": "_gid",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "GA1.2.541522414.1601270427",
    "id": 2
},
{
    "domain": ".ixigua.com",
    "hostOnly": false,
    "httpOnly": false,
    "name": "Hm_lpvt_db8ae92f7b33b6596893cdf8c004a1a2",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "1601270426",
    "id": 3
},
{
    "domain": ".ixigua.com",
    "expirationDate": 1632806426,
    "hostOnly": false,
    "httpOnly": false,
    "name": "Hm_lvt_db8ae92f7b33b6596893cdf8c004a1a2",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "1601268399",
    "id": 4
},
{
    "domain": ".www.ixigua.com",
    "expirationDate": 1609046426.574331,
    "hostOnly": false,
    "httpOnly": false,
    "name": "MONITOR_WEB_ID",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "4996d594-72a9-4af6-a215-6f63ccef250e",
    "id": 5
},
{
    "domain": "www.ixigua.com",
    "hostOnly": true,
    "httpOnly": true,
    "name": "ixigua-a-s",
    "path": "/",
    "sameSite": "unspecified",
    "secure": true,
    "session": true,
    "storeId": "0",
    "value": "0",
    "id": 6
},
{
    "domain": "www.ixigua.com",
    "expirationDate": 1609046424.456337,
    "hostOnly": true,
    "httpOnly": true,
    "name": "ttwid",
    "path": "/",
    "sameSite": "unspecified",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "6877404077664994827",
    "id": 7
},
{
    "domain": "www.ixigua.com",
    "expirationDate": 1609046424.456404,
    "hostOnly": true,
    "httpOnly": true,
    "name": "ttwid.sig",
    "path": "/",
    "sameSite": "unspecified",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "62mtLNgpxBwez3lfFOfV3vYF33Q",
    "id": 8
},
{
    "domain": "www.ixigua.com",
    "expirationDate": 1609046424.456432,
    "hostOnly": true,
    "httpOnly": false,
    "name": "xiguavideopcwebid",
    "path": "/",
    "sameSite": "unspecified",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "6877404077664994827",
    "id": 9
},
{
    "domain": "www.ixigua.com",
    "expirationDate": 1609046424.456453,
    "hostOnly": true,
    "httpOnly": false,
    "name": "xiguavideopcwebid.sig",
    "path": "/",
    "sameSite": "unspecified",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "zL7GD1sXgsaQm-mT0C_A0WAWE9M",
    "id": 10
}
]
'''