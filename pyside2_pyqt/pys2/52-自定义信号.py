from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# from PyQt5.Qt import *

# 自定义右击信号 和 左键装饰器自动连接信号

class Btn(QPushButton):
    # 定义无参信号
    # rightPressed=pyqtSignal() #仅仅对pyqt5有效，对pyside2无效。
    rightPressed=Signal() # 这是pyside2的信号

    # 定义有参信号 规定参数的类型
    # rightPressed=Signal(str)
    # rightPressed=Signal(int)

    # 定义多类型参数信号
    rightPressed=Signal([str],[int])#排在最前面的是默认的

    # 定义多类型 多参数信号
    # rightPressed=Signal([str],[int,str])#排在最前面的是默认的
    # rightPressed=pyqtSignal([str],[int,str])#排在最前面的是默认的


    def mousePressEvent(self,evt):
        super().mousePressEvent(evt)
        # 判断键位==右键
        if evt.button()==Qt.MouseButton.RightButton:
            # print('点击了右键')
            # 发射信号 
            # self.rightPressed.emit() 
            # 必须用self.rightPressed 即从实例调信号 才能有emit()  才可以 self.rightPressed.emit() 
            # 如果用Btn.rightPressed 即用类调信号，没有emit属性，也就是qt规定信号的发射必须用实例信号。
            # 发射文本或数值信号
            # self.rightPressed.emit(self.text()) 
            # self.rightPressed.emit(888) 
            # 多类型参数选择发射
            # self.rightPressed[str].emit(self.text())
            # self.rightPressed[int].emit(888)

            # 多类型 多参数发射
            self.rightPressed[str].emit(self.text()) #定义默认
            self.rightPressed[int,str].emit(888,self.text())
           

            
        

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('自定义信号')
        self.setup_ui()

    def setup_ui(self):
        btn=Btn('自定义信号',self)
        btn.adjustSize()
        btn.move(100,100)
        btn.setObjectName('zsqbtn')
        # pressed 响应的是鼠标左键
        btn.pressed.connect(lambda : print('pressed了鼠标左键'))

        def test_solt(val,text):
            print('pressed了鼠标右键',val,text)
        # rightPressed 是自定义的鼠标右键
        # btn.rightPressed.connect(test_solt)
        # btn.rightPressed[int].connect(test_solt)
        # 多类型、多参数的接收
        # btn.rightPressed[int,str].connect(test_solt)
        # btn.rightPressed.connect(lambda v: print('默认',v))
        


        # 装饰器 根据id即objectName定义 槽函数 
        # 用于设计师Designer设计ui时，解耦界面和槽函数 
        # 在把ui转成py时，这行代码会生成在最后。
        QMetaObject.connectSlotsByName(self) #必须放在最后，即所有控件创建完毕后执行，才有效果。
       
        # 因此，在使用该ui转成的py文件时，如果要定义槽函数，就只要知道发射控件的objectName，
        # 按如下方式，使用装饰器就可以定义槽函数。槽函数会自动链接控件信号。

        pass

    # 装饰器定义槽函数 on_发射控件ObjectName_信号()
    # @pyqtSlot()#pyqt5
    @Slot()#pyside2
    def on_zsqbtn_pressed(self):
        print('装饰器效果')

    @Slot(int,str)    #多类型、多参数 
    def on_zsqbtn_rightPressed(self,val,text):
        print('装饰器效果-右击',val,text)

if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()