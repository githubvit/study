#_*_coding:utf-8_*_
'''
MTV框架
'''
'''
web MTV框架之根据路径返回

'''
from wsgiref.simple_server import make_server
from django.core.handlers.wsgi import WSGIRequest
from views import account #引入分开的路径处理函数

# 1，视图--路径处理函数 把路径处理统一放入views目录 就是业务处理
# def handle_index():
#     f=open('templet/index.html','r')
#     data=f.read()
#     f.close()
#     return data
# def handle_date():
#     f = open('templet/date.html', 'r')
#     data = f.read()
#     f.close()
#     return data

# 2，路由映射--建立路径处理关系字典,注意保留’/‘
URL_DICT={
    '/index':account.handle_index,
    '/date':account.handle_date,
    # ...每个路径都有1个处理函数，对于分页路径/#1，2，3等可以使用正则匹配\d+，统一处理。
}
def RunServer(environ, start_response):

    start_response('200 OK', [('Content-Type', 'text/html')])
    # environ 可以获得客户端的PATH_INFO 数据，就可以根据请求的路径信息做出不同的返回
    current_url=environ['PATH_INFO']#获取路径
    print current_url
    func=None
    if current_url in URL_DICT:#路径是否在路径字典
        func=URL_DICT[current_url]#获取该路径的处理函数名
    if func:
        return func()#返回函数处理结果
    else:
        return '<h1>404!</h1>'#没有就返回404


if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)#启动socket服务 （ip、端口、处理方法）
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()

