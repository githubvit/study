from PySide2.QtWidgets import QApplication,QWidget,QStyle,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,\
QRubberBand
from PySide2.QtCore import Signal,Slot,Qt,QEvent,QPoint,QRect,QLine,QSize
from PySide2.QtGui import QImage,QPicture,QPixmap,QPainter,QColor

import os,sys

# 核心思路：
    # 1 先用一个画家self.painter 在 self.pix 光栅图形对象 上 画
    # 2 然后再用 一个画家lb_painter 在 widget 上把 画好的光栅图形对象 画出来

# 和基础2对比 流畅度不是一个量级 差很多
    # 基础2 是 全程没有干预paintEvent事件，直接在鼠标的pressed、Move、Release三大事件上用QPainter对象对光栅设备进行绘画操作。
    # 基础3 则是 全程在paintEvent事件上操作，鼠标的三大事件只是用来取轨迹坐标。先在 光栅图形上画，再把画好的光栅图形画出来。

# 自定义形状按钮
class ShapeBtn(QPushButton):
    # 形状信号
    shapeSignal=Signal(str)
    def __init__(self,shape):
        super().__init__()
        self.setProperty('shape',shape)

    def mousePressEvent(self,evt):
        super().mousePressEvent(evt)
        if evt.button()==Qt.MouseButton.LeftButton:
            self.shapeSignal.emit(self.property('shape'))

        
        

class Window(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.setWindowTitle('QPainter基础1')
        # self.setGeometry(1000,400,500,500)

        # 动作列表
        self.action_list=["Line","Rect", 'RoundedRect', "Ellipse", "Pie", 'Chord', "Arc",\
    "Path","Polygon", "Polyline", "Points", "Text", "Pixmap"]
        self.btn_list=['线条', '矩形','圆角矩形','椭圆','扇形 pie','弦 chord','弧 Arc','轨迹 path','多边形 填充 poolygon',\
    '多边形线条 无填充 polyline','点','文本','图片']

        # 定义手写板对象
        self.hw=HandWrite()

        h_layout=QHBoxLayout()
        
        # 定义按钮
        for i,btn in enumerate(self.btn_list):
            item_btn=ShapeBtn(self.action_list[i])
            item_btn.setText(btn)
            item_btn.shapeSignal.connect(self.change_shape)
            h_layout.addWidget(item_btn)

        # 布局
        v_layout=QVBoxLayout(self) # 一定要用布局，不然，lb手写始终对不上，差标题栏高度    ******
        
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.hw)
        # 1 定义 光栅对象
        self.pix=QPixmap(self.hw.width(),self.hw.height())
        # pix=QPixmap()
        self.pix.fill(QColor('white'))# 不填充为白色 默认是黑色
        self.hw.setPixmap(self.pix) # 设置给label)


    # def resizeEvent(self,evt):
    #     print(evt)
        
       

    def change_shape(self,v):
        print(v)
        self.hw.action_v=v
        # self.hw.do_action()


# 手写板 label
# 手写板 如果手写label不在布局里 则实际绘制差标题栏高度 因此 一定要放在布局里
class HandWrite(QLabel):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setMinimumHeight(400)
        self.setScaledContents(True) 
        
        
       
        # 2 设置pix 适应label大小
        # self.setScaledContents(True) 
        # 2 定义 记录手写点 
        self.point_0=None # 
        self.point_1=None
        self.draw_flag=False # 绘画开关
        
    
        # 4 防止 鼠标跟踪
        if self.hasMouseTracking():
            self.setMouseTracking(False)

        # 5 参数设置
        self.pen_color='#000000'
        self.pen_width=4
        


        # 7 动作参数 默认是线条
        self.action_v='Line'
        # self.action_v='Rect'

    def paintEvent(self,evt):
        # 先用一个画家self.painter 在 self.pix 光栅图形对象 上 画
        # 然后再用 一个画家lb_painter 在 widget 上把 画好的光栅图形对象 画出来
        #    
        # 1 在 self.pix 光栅图形对象 上 画
        self.painter=QPainter()
        self.painter.begin(self.pixmap()) 

        # 设置笔
        self.pen_setting()

        if self.draw_flag:

            if self.action_v=='Line':

                self.drawLine(self.point_0,self.point_1)

            elif self.action_v=='Rect':
                self.drawRect(self.point_0,self.point_1)
        self.painter.end()

        # return super().paintEvent(evt)
        
        # 2 画出self.pix
        # 在 widget 上把 画好的光栅图形对象 画出来
        lb_painter=QPainter(self)
        lb_painter.drawPixmap(0,0,self.pixmap())

        # super().paintEvent(evt)

    def mousePressEvent(self,evt):
        super().mousePressEvent(evt)
        # 记录开始点
        self.point_0=evt.pos()
        # 打开绘画开关
        self.draw_flag=True

    def mouseMoveEvent(self,evt):
        super().mouseMoveEvent(evt)
        if self.draw_flag:
            # 记录过程点
            self.point_1=evt.pos()
            # 交换
            self.point_0=self.point_1
            self.update()

    def mouseReleaseEvent(self,evt):
        super().mouseReleaseEvent(evt)
        # 关闭绘画开关
        self.draw_flag=False


     # 笔的设置
    def pen_setting(self):
        pen=self.painter.pen()
        pen.setColor(QColor(self.pen_color)) 
        # pen.setColor(QColor('#35e3e3')) # 青色
        pen.setWidth(self.pen_width)# pen_width像素
        self.painter.setPen(pen) # 要把修改好的笔设回来 

    def drawLine(self,start,end):
        self.painter.drawLine(start,end)

    def drawRect(self,start,end):
        rect=QRect(start,end)
        self.painter.drawRect(rect)


if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()