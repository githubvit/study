#_*_coding:utf-8_*_
'''
利用sys模块的标准输出stdout在屏幕上输出进度条
'''
import sys,time
for i in range(20):
    sys.stdout.write('#')
    sys.stdout.flush()#实时，不然看不到一个一个出来的效果，而是整体出来
    time.sleep(0.1)#间隔，不然太快，没有效果