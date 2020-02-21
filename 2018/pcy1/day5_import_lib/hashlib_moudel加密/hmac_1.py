
#-*- coding:utf8 -*-

import hmac

h=hmac.new(b'12345','你是250'.decode('utf-8').encode('utf-8'))#'12345'是key，'你是250'是消息。
print (h.digest())
print (h.hexdigest())