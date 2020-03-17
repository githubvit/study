# python asyncio抓取B站最热视频
# https://www.bilibili.com/video/av85985296

# 安装 aiohttp 报错
#  Collecting aiohttp
#   Could not find a version that satisfies the requirement aiohttp (from versions: )
#   No matching distribution found for aiohttp
#  问题原因：包在国外，网络连接慢，长时间连接不成功或下载不成功，就报错。

# 解决方案：增加连接等待的时长

# 解决语句：pip --default-timeout=100 install aiohttp
# 实际解决：翻墙

import asyncio                  # 异步标准库
# 基于 该异步标准库 python 有一堆生态 ，比如：
# 今天要讲的 异步http框架 aiohttp
# 还有 异步 mysql aiomysql 、异步aio 消息队列RabbitMQ (这也许是最全面透彻的一篇RabbitMQ指南！https://dbaplus.cn/news-141-1464-1.html), 
# 异步aio 批量分布订阅系统(批量消息队列)kafka(震惊了！原来这才是 Kafka！（多图+深入）https://blog.csdn.net/zl1zl2zl3/article/details/88566122)
# 还有很多 。。。就是把原来的很多框架实现了异步aio
import aiohttp                  # 下载库 aiohttp是基于asyncio实现的HTTP框架 
from bs4 import BeautifulSoup   # 分析库
import re




# import async_scher
# scher=async_scher.scher
# 在这里不能用自定义的async方法，必须用协程标准库 即py原生的协程库
# 因为 aiohttp 与 asyncio 深度耦合的

# 下载 列表页 并在 列表页 中 建立 详情页 下载任务 并发
async def list_page(url):
    # 进来以后呢，先拿到一个session对象，用这个session去下载页面
    # 用 aiohttp 的 ClientSession() 方法 拿到 一个 session。
    # 用 该 session 去 登录 各大网站
    # 为什么是 async with 不是 with 
    # 原来 with / as 是调用 with 对象 的enter方法 def __enter__()
    # 而async with / as 是调用 with 对象 的aenter协程方法 async def __aenter__()
    # 返回的结果 是用协程 返回的 
    async with aiohttp.ClientSession() as session:
        # 假设有很多列表页 比如列表页1、2、。。。
        # 我们隔5秒下载新的列表页，用while或for
        while True:
            try:
                # 下载 url 页面
                async with session.get(url) as response:
                    # 获取页面
                    html=await response.text()
                    # 拿到页面 在浏览器 用F12分析页面
                    # 建立BeautifulSoup分析对象
                    soup=BeautifulSoup(html,'html.parser')#传入页面html,使用html解析器（'html.parser）解析页面
                    # 拿到该页所有的class=ebox列表，用选择器
                    res_list=soup.select('.ebox')
                    # 取出每项 a 标签下的 href 和 title
                    for item in res_list:

                    
                        # print(f"地址: http:{item.select_one('a').get('href')}")
                        # print(f"标题:{item.select_one('a').get('title')}")
                        # print(f"播放:{item.select_one('.dlo .play').contents} 次")

                        # 去除 换行'\n'和多个空格'  '

                        # 方法一 替换法 sub  
                        # 用空''去替换换行和多个空格'\n +'
                        # play_num=re.sub('\n +','',item.select_one('.dlo .play').text)

                        # 方法二 分割法 split
                        # 用换行'\n'做分隔符，获得列表，取第0项即可
                        # play_num=re.split('\n', item.select_one('.dlo .play').text)[0]
                        # print(f"播放:{play_num}次")

                        href=f"http:{item.select_one('a').get('href')}"
                        title=f"{item.select_one('a').get('title')}"
                        play_num=re.split('\n', item.select_one('.dlo .play').text)[0]

                        # print(f'链接：{href}  标题:{title}  播放量:{play_num}次')

                        # 建立详情页下载任务
                        # 开始爬取详情页 即爬取每个item的链接
                        # 1 建立 爬取 字典
                        # task={title,href,play_num,session} #不行 不支持
                        task={
                            'title':title,
                            'href':href,
                            'play_num':play_num,
                            'session':session

                        }
                        # 2 建立详情页下载任务
                        asyncio.create_task(detail_page(task))
                        # 如果 没有 await asyncio.sleep(5) ，则 session 会关闭 Session is closed  详情页无法下载
                        # 原因在于：
                        #  巧妙的利用了 协程 的 await 暂停特性，因为是暂停，所以，session 没有关闭，可以继续使用
                    
            except Exception as e:
                print(e)
            await asyncio.sleep(5) 

# 下载 详情页
async def detail_page(task):
    # 直接用task中的session 下载 详情页
    try:
        # print('2')
        async with task['session'].get(task['href']) as response:
            # print('3',task['session'])
            # 获取页面
            html=await response.text()
            # print(len(html))#查看页面大小
            # 拿到页面 在浏览器 用F12分析页面
            # 建立BeautifulSoup分析对象
            soup=BeautifulSoup(html,'html.parser')#传入页面html,使用html解析器（'html.parser）解析页面
            # 取详情页的信息简介
            res=soup.select_one('#v_desc')
            if res:
                # print(res.select_one('.info').text)
                task['info']=res.select_one('.info').text
            else:
                # print('这个家伙很懒')
                 task['info']='这个家伙很懒'

            print(f"链接：{task['href']}  标题:{task['title']}  播放量:{task['play_num']}次")
            print(f"简介：{task['info']}")
            print('-----------------------------------------------------------------------------')
    except Exception as e:
        print(e)


# 直接用标准库的run方法去启动协程
asyncio.run(list_page('https://www.bilibili.com/video/online.html'))

# 最要注意的点： 在列表页 创建详情页 中的session，列表页要await 暂停，不然session会closed，导致详情页下载失败。