#_*_coding:utf-8_*_
'''
同步与异步的性能区别：异步只有同步3分之1的时间，大大提高效能
注意：
    gevent补丁！
        gevent补丁！！
            gevent补丁！！！
            
    在实际应用中，gevent并不知道当前程序引入模块的io操作在哪里，需要引入gevent补丁，才能实现。
'''
import urllib
import gevent,time

from gevent import monkey #注意补丁的引入
monkey.patch_all() #把当前程序的所有的io操作给我单独的做上标记

def f(url):
    print('GET: %s' % url)
    resp = urllib.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))
# -------------同步操作-----------------------
urls = ['http://news.ifeng.com//',
        'https://www.yahoo.com/',
        'https://github.com/' ]
time_start = time.time()
for url in urls:
    f(url)
print "同步cost",time.time() - time_start
# -------------异步操作-----------------------
async_time_start = time.time()
gevent.joinall([
    gevent.spawn(f, 'http://news.ifeng.com/'),
    gevent.spawn(f, 'https://www.yahoo.com/'),
    gevent.spawn(f, 'https://github.com/'),
])
print "异步cost",time.time() - async_time_start