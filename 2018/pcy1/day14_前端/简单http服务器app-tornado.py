#_*_coding:utf-8_*_
'''
简单http网页服务器3

tornado

'''
import tornado,tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        print 'get 收到'
        u=self.get_argument('user')
        e=self.get_argument('email')
        p=self.get_argument('pwd')
        if u=='alex' and e=='alex@123.com' and p=='111':
            self.write('get ok')
        else:
            self.write('滚')
    def post(self, *args, **kwargs):
        print 'post 收到'
        u = self.get_argument('user')
        e = self.get_argument('email')
        p = self.get_argument('pwd')
        print u,e,p
        if u=='alex' and e=='alex@123.com' and p=='111':
            self.write('post ok')
        else:
            self.write('滚')
application=tornado.web.Application([(r'/index',MainHandler)])

if __name__=='__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
