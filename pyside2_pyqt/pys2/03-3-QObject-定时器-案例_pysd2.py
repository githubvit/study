# 定时器 每个控件类都有
# 设置定时器
# startTimer(ms, Qt.TimerType) -> timer_id
# 定时器执行事件
# timerEvent()
# 关闭定时器
# killTimer(timer_id) 根据定时器id 关闭定时器

# 倒计时lable
from PySide2.QtWidgets import *
from PySide2.QtCore import *

app=QApplication([])

wd=QWidget()
wd.setWindowTitle('定时器案例')
# 设置label
class MyLabel(QLabel):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.resize(50,50)
        
        self.move(100,100)
        self.setStyleSheet('background-color: cyan;font-size:33px')
        # self.adjustSize() #自适应大小 要放在字体设置完后 不然会很小
        # 设置初始值
        # self.setText('10') #放在 self.adjustSize() 后面 就看不到'10' 只能看到'1' ,放在自适应前面没问题。
        # 设置定时器
        # self.t_id=self.startTimer(1000)
    
    # 设置定时器函数
    def setTime_ms(self,sec,ms):
        self.setText(str(sec))
        self.t_id=self.startTimer(ms)   
        # print(self.t_id)
    
    # 定时器 响应事件 （一定要加 *args,**kwargs 不然会报参数错误）
    def timerEvent(self,*args,**kwargs):
        # print('xx')
        # 获取当前标签内容 
        crt_sec=int(self.text())
        crt_sec-=1 #减1
        # 设置新值
        new_sec=str(crt_sec)
        self.setText(new_sec)
        if crt_sec==0:
            print('停止')
            self.killTimer(self.t_id)
        
# 实例化对象
lb=MyLabel(wd)
# 设置 定时器 
lb.setTime_ms(20,2000)#（初始数值，间隔时间）
print(lb.t_id)

wd.show()

app.exec_()