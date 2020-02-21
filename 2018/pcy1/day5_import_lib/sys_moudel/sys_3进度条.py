#-*- coding:utf8 -*-


# 标准输出，进度条
import sys,time
for i in range(50):
    sys.stdout.write('#')
# 上面的效果，是一次性输出了50个，也就是先全部写到内存，再从内存中一次读取到屏幕，没有动画效果
# 加入实时写入，也就是每次循环都实时输出到屏幕，让其产生动画效果
    sys.stdout.flush()
# 有一点动画效果，不明显，用time的sleep，让其循环间隔0.1
    time.sleep(0.1)
#  现在进度条的时间完全可控，效果明显