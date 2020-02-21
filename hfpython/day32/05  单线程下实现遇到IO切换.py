# from greenlet import greenlet
# import time
#
# def eat(name):
#     print('%s eat 1' %name)
#     time.sleep(30)
#     g2.switch('alex')
#     print('%s eat 2' %name)
#     g2.switch()
# def play(name):
#     print('%s play 1' %name)
#     g1.switch()
#     print('%s play 2' %name)
#
# g1=greenlet(eat)
# g2=greenlet(play)
#
# g1.switch('egon')













# import gevent
#
# def eat(name):
#     print('%s eat 1' %name)
#     gevent.sleep(5)
#     print('%s eat 2' %name)
# def play(name):
#     print('%s play 1' %name)
#     gevent.sleep(3)
#     print('%s play 2' %name)
#
# g1=gevent.spawn(eat,'egon')
# g2=gevent.spawn(play,'alex')
#
# # gevent.sleep(100)
# # g1.join()
# # g2.join()
# gevent.joinall([g1,g2])



# from gevent import monkey;monkey.patch_all()
# import gevent
# import time
#
# def eat(name):
#     print('%s eat 1' %name)
#     time.sleep(5)
#     print('%s eat 2' %name)
# def play(name):
#     print('%s play 1' %name)
#     time.sleep(3)
#     print('%s play 2' %name)
#
# g1=gevent.spawn(eat,'egon')
# g2=gevent.spawn(play,'alex')
#
# # gevent.sleep(100)
# # g1.join()
# # g2.join()
# gevent.joinall([g1,g2])



from gevent import monkey;monkey.patch_all()
from threading import current_thread
import gevent
import time

def eat():
    print('%s eat 1' %current_thread().name)
    time.sleep(5)
    print('%s eat 2' %current_thread().name)
def play():
    print('%s play 1' %current_thread().name)
    time.sleep(3)
    print('%s play 2' %current_thread().name)

g1=gevent.spawn(eat)
g2=gevent.spawn(play)

# gevent.sleep(100)
# g1.join()
# g2.join()
print(current_thread().name)
gevent.joinall([g1,g2])