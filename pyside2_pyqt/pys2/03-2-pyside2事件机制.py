# 事件机制
# 事件机制偏向底层，信号与槽机制是对事件机制的封装，偏向应用层。

# 每个程序app，有两个消息队列
    # 系统产生的消息队列：接收系统产生的消息，比如 鼠标点击、键盘输入等产生的消息。
    # 程序内部的消息队列：接收程序内部产生的消息，比如 定时器、绘屏事件等。

    # 事件传递顺序 os→app→子控件→父控件→...
    
# 消息循环
    # 当执行 app.exec_() 就进入消息循环
    # 不停的顺序监听两个队列是否有消息 
    # 一旦有消息，系统就会把消息通知应用程序的notify函数，由该函数进行信号分发。

# 信号分发 
    # 层层分发 app.notify→recevier.event→recevier.evtfunc→signal
    # 第一层应用程序的notify(recevier,evt)：队列中一旦有消息，就会由QApplication中的notify(recevier,evt)接收
        # recevier:接收控件QObject，evt：事件对象QEvent
    # 第二层接收控件的event(evt)：最终要根据evt的事件类型，由recevier的event(evt)方法来分发 给该事件类型的具体函数evtfunc(*args,**kwargs)
    # 第三层接收控件的evtfunc(*args,**kwargs)：由这个具体函数产生相应的发射信号pressed、clicked...。


from PySide2.QtWidgets import *
from PySide2.QtCore import * #QEvent对象

class App(QApplication):
    # 第一层 
    def notify(self,recevier,evt):
        # print(recevier,evt) #非常忙
        # 过滤出 recevier控件是继承自Qpushbutton 并且 事件类型是 鼠标按下pressed
        if recevier.inherits("QPushButton") and evt.type() == QEvent.MouseButtonPress:
            print(recevier,evt)
            print('1 程序通知事件 按钮 被 鼠标点击了...')
            # <PySide2.QtWidgets.QPushButton(0x1ae2cba0210) at 0x000001AE2C1809C8> <PySide2.QtGui.QMouseEvent object at 0x000001AE2CF16448>
            # 按钮被点击了
        # else:
            # return super().notify(recevier,evt) # 阻断pressed信号分发 这样槽函数就不会执行
        return super().notify(recevier,evt) # notify通知 也叫信号分发
        # 如果 父类有返回值，用 return 可以返回父类的返回值
        # 因此，不管有没有，用 return super().方法(xx) 都是更好的继承

        #父类QApplication进行信号分发  没有信号分发 就没有信号发射 也就没有信号与槽的运行

class Btn(QPushButton):
    # 第二层 event
    def event(self,evt):
        # print(evt) #非常忙
        # 筛选出 鼠标按下事件类型
        if evt.type()==QEvent.MouseButtonPress:
            print(evt)
            print('2 按钮控件 接到 程序通知事件 鼠标点击了我......')
        return super().event(evt)
    # 第三层 具体函数
    def mousePressEvent(self, *args, **kwargs):
        print("3 按钮控件启动 鼠标点击事件应用程序 发射 pressed 信号......")
        return super().mousePressEvent(*args, **kwargs)
 
app=App([])
wd=QWidget()
wd.setWindowTitle('事件机制')

btn=Btn(wd)
btn.setText('按钮')
btn.move(100,100)
btn.pressed.connect(lambda: print('4 接到 pressed信号 后启动的 程序....'))
wd.show()
app.exec_()