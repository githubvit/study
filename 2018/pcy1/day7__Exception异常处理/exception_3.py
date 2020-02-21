#_*_coding:utf-8_*_
# 1，定位是什么异常
# s1 = 'hello'
# try:
#     int(s1)
# except IndexError,e:
#     print '索引错误',e
# except KeyError,e:
#     print 'key错误',e
# except ValueError,e:
#     print 'value错误',e
#

#2，万能异常，可以捕获未知的异常
# s1 = 'hello'
# try:
#     int(s1)
# except Exception,e:
#     print '未知异常'

# 3，异常try-except...-else-finally结构
# s1 = 'hello'
# try:
#     # 主代码块
#     int(s1)
#
#
# except KeyError,e:
#     # 异常时，执行该块
#     print 'key错误', e
# except Exception,e:
#     print '未知异常'
#
# else:
#     print '这是else', s1# 没异常，执行该块
#
# finally:
#     # 无论异常与否，最终执行该块
#     print '无论怎么样，我都要出现'

#,4，主动触发异常raise
# try:
#     raise Exception('错误了。。。')
# except Exception,e:
#     print e

#5， 自定义异常
class SgqException(Exception):

    def __init__(self, msg):
        self.message = msg

    def __str__(self):#py3.x可以没有这个，py2.7不行。
        return self.message

try:
    # i=raw_input('>>:')
    i = input('>>:')
    a=SgqException('我的异常')#实例化异常类，因为定义了__str__,所以，a的结果为return的值。
    b=SgqException('你的异常')
    c=SgqException('它的异常')#那么就可以定义各种异常
    if int(i)==1:
      raise a#主动触发
    elif int(i)==2:
        raise b
    else:
        raise c
    # 也可以一步搞定
    # raise SgqException('我的异常')
# except SgqException,e:#捕捉的方式也可以用万能异常捕捉Exception
except SgqException as e:
    print (e)

# 6,断言 过安检
# s=raw_input('>>')
s=input('>>')
next='下一步'

try:
    # assert s=='aaa'#条件设定
    # assert s is str#这样写是错的
    assert type(s) is str#应该这样写，判断它的类型才对
# 不满足条件，就报如下异常：
# Traceback (most recent call last):
#   File "D:/wksp1/pcy1/day7__Exception�쳣����/exception_3.py", line 67, in <module>
#     assert s=='aaa'#条件设定
# AssertionError
except AssertionError :
    print ('你错了')
else:
    print (next)