# 使用sched模块
# sched 模块是Python内置模块，它是一个调度（延时处理机制），每次想要定时执行任务都必须写入一个调度。

import sched
import time
from datetime import datetime

# 初始化sched模块的scheduler类
# 第一个参数是一个可以返回时间戳的函数，第二参数可以在定时未到达之前阻塞
schedule = sched.scheduler(time.time, time.sleep) # 参数必须是函数

# 被周期性调度触发函数
def printTime(inc):
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    # 加入调度事件
    schedule.enter(inc, 0, printTime, (inc,))
    # 执行
    schedule.run()
printTime(5)

# 默认参数60s
def main(inc=60):
    # enter四个参数分别为：间隔事件,优先级（用于同时到达两个事件同时执行的顺序），
    # 被调度触发的函数
    # 给该触发器函数的参数（tuple形式）
    # 定义
    schedule.enter(0, 0, printTime, (inc,))
    # 执行
    schedule.run()
# 5秒输出一次
# main(5)