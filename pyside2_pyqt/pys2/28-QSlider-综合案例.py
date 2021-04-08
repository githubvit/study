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
        # sd.resize(30,200) # 这个是配合默认的垂直滑动条用的
    
        sd.move(50,50)
        sd.setOrientation(Qt.Horizontal) # 设定滑动条方向
        sd.resize(200,30) # 这个是配合水平滑动条用的
        
        # QSlider很少有自己的函数，大部分功能在QAbstractSlider中。
        # 最有用的函数是setValue()，用来设置滑块的当前值；
        # triggerAction()来模拟点击的效果（对快捷键有用），
        # setSingleStep()、setPageStep()用来设置步长，
        # setMinimum()和setMaximum()用于定义滚动条的范围。

        # 刻度位置

            # 枚举 QSlider::TickPosition，这个枚举指定刻度线相对于滑块和用户操作的位置。

            # 常量	                    值	        描述
            # QSlider::NoTicks	        0	        不绘制任何刻度线
            # QSlider::TicksBothSides	3	        在滑块的两侧绘制刻度线
            # QSlider::TicksAbove	    1	        在（水平）滑块上方绘制刻度线
            # QSlider::TicksBelow	    2	        在（水平）滑块下方绘制刻度线
            # QSlider::TicksLeft	    TicksAbove	在（垂直）滑块左侧绘制刻度线
            # QSlider::TicksRight	    TicksBelow	在（垂直）滑块右侧绘制刻度线
        
       

        # 数值标签 作为滑块的子控件
        lb=QLabel(self.sd)
        self.lb=lb
        lb.move(50,50)
        lb.setStyleSheet('color:red;')

        sd.setPageStep(5)
        sd.setTickPosition(QSlider.TicksBothSides)# 显示刻度 两边都显示

        
        # 跟踪数值变化信号 
        sd.valueChanged.connect(self.show_val)

        # QSlider继承了一组全面的信号：

        # valueChanged()：当滑块的值发生了改变，发射此信号。tracking()确定在用户交互时，是否发出此信号。
        # sliderPressed()：当用户按下滑块，发射此信号。
        # sliderMoved()：当用户拖动滑块，发射此信号。
        # sliderReleased()：当用户释放滑块，发射此信号。

        # 设置初始值
        sd.setValue(10)

        # 样式

        # sd.setStyleSheet('''
            
        #     QSlider::groove:horizontal {
        #            height: 6px;
        #            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgb(124, 124, 124), stop: 1.0 rgb(72, 71, 71));
        #     }
        #     QSlider::handle:horizontal {
        #            width: 5px;
        #            background: rgb(0, 160, 230);
        #            margin: -6px 0px -6px 0px;   
        #     }
        
        # ''')

    def show_val(self,val):
        self.lb.setText(str(val))
        self.lb.adjustSize()

        if self.sd.orientation() == Qt.Horizontal:
            # print('水平')
            # 水平滑动条用
            y=(self.sd.height()-self.lb.height())/2
            x=((self.sd.width()-self.lb.width())/(self.sd.maximum()-self.sd.minimum()))*(val)
            pass
        else:
            # 垂直滑动条用
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