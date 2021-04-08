## 案例
# 在一个空白窗口内, 展示多个复选框控件
# 通过橡皮筋实现批量选中与取消选中效果

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

# from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('橡皮筋框选案例')
        self.setup_ui()

    def setup_ui(self):
        # 1 子控件布局
        # 30个checkbox 4列
        cl_num=4
        # 起始点
        start_x=10
        start_y=10
        # 大小
        cbx_width=50
        cbx_hieght=60
        for i in range(30):
            cbx=QCheckBox(self)
            cbx.setText(str(i+1))
            cbx.resize(cbx_width,cbx_hieght)
            x=start_x+i%cl_num*cbx_width
            y=start_y+i//cl_num*cbx_hieght
            cbx.move(x,y)
        
        # 2 生成橡皮筋控件
        self.rb=QRubberBand(QRubberBand.Rectangle,self)
        pass
    # 实现框选+切换 
    # 用鼠标的三个事件
    def mousePressEvent(self,evt):
        super().mousePressEvent(evt)
        # 1 获取按下的点
        self.start_point=evt.pos()
        # 2 设定橡皮筋控件 初始位置和大小 
        # 用QRect的（开始点、大小）设置
        # 初始大小为一个空的QSize对象，即无大小
        self.rb.setGeometry(QRect(self.start_point,QSize())) 
        
        # 3 显示橡皮筋
        self.rb.show()
        
        # 光标 为十字
        self.setCursor(Qt.CrossCursor)
        
        pass   
    def mouseMoveEvent(self,evt):
        super().mouseMoveEvent(evt)
        # 1 改变橡皮筋大小 
        # 用QRect的两点设定（左上开始点，右下移动点）和
        # 当发现两点位置不对时交换两点的方法.normalized，从而保证从右下选到左上也是可以的
        self.rb.setGeometry(QRect(self.start_point,evt.pos()).normalized())

        pass
    def mouseReleaseEvent(self,evt):
        super().mouseReleaseEvent(evt)
        # 1 获取框选的大小
        rect=self.rb.geometry()
        # 2 选择框选范围的子控件 切换子控件状态
        # 获取子控件 
        for child_widget in self.children():
            # 判断子控件是否在框选的范围内 rect.contains(child_widget.geometry())
            # 如果在范围内 并且 是checkbox类型 就切换状态
            if rect.contains(child_widget.geometry()) and child_widget.inherits('QCheckBox'):
                # print(child_widget)
                # 状态切换
                child_widget.toggle()
        # 3 隐藏橡皮筋
        self.rb.hide()
        # 光标 还原
        self.setCursor(Qt.ArrowCursor)

        pass

if __name__ == "__main__":
    app = QApplication([])
    wd=Window()
    wd.show()
    app.exec_()

