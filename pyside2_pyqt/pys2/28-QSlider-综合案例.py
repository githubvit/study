from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
# from PyQt5.Qt import *

# 滑动输入案例：数值在滑块同步实时显示，比顺子做的案例好。
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('滑动输入案例的学习')
        self.setup_ui()

    def setup_ui(self):
        sd=QSlider(self)
        self.sd=sd
        sd.resize(30,200)
        sd.move(50,50)

        # 数值标签 作为滑块的子控件
        lb=QLabel(self.sd)
        self.lb=lb
        lb.move(50,50)
        lb.setStyleSheet('color:red;')

        # sd.setPageStep(5)
        sd.setTickPosition(QSlider.TicksBothSides)
        # 跟踪数值变化信号 
        sd.valueChanged.connect(self.show_val)

        # 设置初始值
        # sd.setValue(10)

    def show_val(self,val):
        self.lb.setText(str(val))
        self.lb.adjustSize()

        x=(self.sd.width()-self.lb.width())/2
        y=((self.sd.height()-self.lb.height())/(self.sd.maximum()-self.sd.minimum()))*(self.sd.maximum()-val)
        self.lb.move(x,y)
        # print(val)
        
       
        pass
        

if __name__ == "__main__":
    from PySide2.QtWidgets import *
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()