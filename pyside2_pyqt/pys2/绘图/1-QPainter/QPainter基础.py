from PySide2.QtWidgets import QApplication,QWidget,QStyle,QLabel,QPushButton,QVBoxLayout,QRubberBand
from PySide2.QtCore import Qt,QEvent,QPoint,QRect,QLine,QSize
from PySide2.QtGui import QImage,QPicture,QPixmap,QPainter,QColor

import os,sys

# QPainter绘图系统 - 介绍篇

# 一 简介
    # QPainter 绘图系统绘制的图形不可交互操作，如果想要绘图交互，使用QGraphics View架构
    # QPainter 要指定绘图设备，有三种绘图设备，可以理解为一块画布
        # QWidget 
        # QPixmap 用于 手写
        # QImage  用于 保存
    # QPainter 在widget上绘图时，要重定义paintEvent()，在此事件内编写绘图代码

# 二 主要属性
    # 线条 pen属性，控制线条的颜色、宽度、线型等
    # 填充 brush属性，用户设置图形填充颜色、渐变、填充方式等
    # 字体 font属性，绘制文字时定义文字样式


class Window(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.setWindowTitle('QPainter基础1')
        self.setGeometry(1000,400,500,500)

        # 一 手写板
        lb=HandWrite()
        #lb.setGeometry(100,100,400,400)  # 这样 手写始终对不上，差标题栏高度
        v_layout=QVBoxLayout(self) # 一定要用布局，不然，lb手写始终对不上，差标题栏高度    ******
        v_layout.addWidget(lb)


        # 二  记录 绘图 一般不用
        # 1 用QPicture 记录 绘图 指令 这次没有绘图
        # self.painter_picture()
        # 2 重现QPicture 记录的绘图 这次有绘图
        # self.picture_show() 在这里是无法重现的，必须在绘图事件paintEvent中加载self.picture_show()，才能重现图形
        
        self.cnt=0

    #本次用QPicture 记录 绘图 指令  并不会 画出图形 而是记录本次绘图指令 以便下次加载该指令 便可实现绘图
    def painter_picture(self):
        # 定义QPicture对象
        pic=QPicture()
        # 用该对象记录绘画指令 
        painter=QPainter(pic) # 记录

        painter.begin(pic) # 开始 激活  Painter 
        pen=painter.pen()
        # pen.setColor(QColor('#000000')) 
        pen.setColor(QColor('#35e3e3')) # 青色
        pen.setWidth(4)# 像素
        painter.setPen(pen) # 要把修改好的笔设回来 
        painter.drawLine(10,10,100,100)
        painter.end()

        pic.save('1.pic')
        print(pic.size())


    # 重现绘图记录指令 一定要在 绘图事件中加载 才能看到图形
    def picture_show(self):
        # 定义picture
        pic=QPicture()
        # 定义 画家
        painter=QPainter(self) # 这次画在控件上
        # painter.begin(self)
        # 加载 picture 指令文件
        pic.load('1.pic')
        # 用画家画出来
        painter.drawPicture(0,10,pic) # 这里的 0,10 是相对坐标，即相对于第一次记录指令时 的起始点(10,10)的坐标
        # painter.end()

    # 重现QPicture 记录的绘图 
    def paintEvent(self,evt):
        self.cnt+=1
        # print(self.cnt)
       
        # 三 代码绘制图形
        painter=QPainter(self) # Qwidget 都可以当作画板
       
        pen=painter.pen()
        pen.setColor(QColor('#000000')) 
        # pen.setColor(QColor('#35e3e3')) # 青色
        pen.setWidth(4)# 像素
        painter.setPen(pen) # 要把修改好的笔设回来 
        
        painter.drawLine(10,10,100,100)
        # painter.drawLine(0,0,100,100)
        

        # 重现QPicture 记录的绘图 和上面绘制的图形对比 注意起始点坐标的差别 因此picture_show中的（0，10）是相对坐标 
        self.picture_show()
        return super().paintEvent(evt)

# 手写板 label
# 手写板 如果手写label不在布局里 则实际绘制差标题栏高度 因此 一定要放在布局里
class HandWrite(QLabel):
    def __init__(self,parent=None):
        super().__init__(parent)

        # 1 定义 光栅对象
        pix=QPixmap(1000,500)
        pix.fill(QColor('white'))# 不填充为白色 默认是黑色
        self.setPixmap(pix) # 设置给label
        # 2 定义 记录手写点 
        self.last_point=None # 起始值为None
        # 3 定义 画家
        self.painter=QPainter(self.pixmap()) # 将光栅对象当作画板
        # 4 防止 鼠标跟踪
        if self.hasMouseTracking():
            self.setMouseTracking(False)


        # 5 参数设置
        self.pen_color='#000000'
        self.pen_width=4

        # 6 动作列表
        self.action_list=["Line","Rect", 'RoundedRect', "Ellipse", "Pie", 'Chord', "Arc",
    "Path","Polygon", "Polyline", "Points", "Text", "Pixmap"]
        

            # [ 线条, 矩形, 圆角矩形, 椭圆, 扇形 pie, 弦 chord, 弧 Arc, 轨迹 path, 多边形 填充 poolygon,
            #   多边形线条 无填充 polyline, 点, 文本, 图片]

        # 7 动作参数 默认是线条
        # self.action_v='Line'
        self.action_v='Rect'

        # 8 清除
            # 全部
            # 部分

        # 9 撤销
        
            
        self.cnt=0 # 记录一次mouseMoveEvent 轨迹共有多少个点

    
    def mousePressEvent(self,evt):
        # 记录开始点
        self.last_point=evt.pos()
        # print(dir(self.last_point))
        # 设置笔
        self.pen_setting()

        if self.action_v=='Rect':
            # 2 生成橡皮筋控件
            self.rb=QRubberBand(QRubberBand.Rectangle,self)
            # 初始大小为一个空的QSize对象，即无大小
            self.rb.setGeometry(QRect(self.last_point,QSize())) 

            # 3 显示橡皮筋
            self.rb.show()

            # 光标 为十字
            self.setCursor(Qt.CrossCursor)
        return super().mousePressEvent(evt)

    def mouseMoveEvent(self,evt):
        # self.cnt+=1
        # print(self.cnt) # mouseMoveEvent移动的点数
        # 开始画
        if self.action_v=='Line':            
            # 1 线条
            self.painter.drawLine(self.last_point,evt.pos()) # 通过连续的drawLine 形成手写轨迹 *******
            self.update()# 触发更新 手写板 label 的绘图事件 paintEvent
            self.last_point=evt.pos() # 记录下一点的开始 这样才能 让mouseMoveEvent轨迹点连续
        
        elif self.action_v=='Rect':
            # 2 矩形
            # rw=evt.x()-self.last_point.x()
            # rh=evt.y()-self.last_point.y()
            # p1=QPoint(evt.x(),self.last_point.y())
            # p2=QPoint(self.last_point.x(),evt.y())
            # p3=evt.pos()
            # line1=QLine(self.last_point,p1)
            # line2=QLine(self.last_point,p2)
            # line3=QLine(p1,p3)
            # line4=QLine(p2,p3)
            # self.painter.drawLines([line1,line2,line3,line4]) # 3,4条线不能画，

            # 用橡皮筋显示将要画的矩形
            self.rb.setGeometry(QRect(self.last_point,evt.pos()).normalized())

            
        elif self.action_v=='RoundedRect':
            self.painter.drawRoundedRect
        elif self.action_v=='Ellipse':
            self.painter.drawEllipse()
        elif self.action_v=='Pie':
            self.painter.drawPie()
        elif self.action_v=='Chord':
            self.painter.drawChord()
        elif self.action_v=='Arc':
            self.painter.drawArc()
        elif self.action_v=='Path':
            self.painter.drawPath()
        elif self.action_v=='Polygon':
            self.painter.drawPolygon()
        elif self.action_v=='Polyline':
            self.painter.drawPolyline()
        elif self.action_v=='Points':
            self.painter.drawPoints()
        elif self.action_v=='Text':
            self.painter.drawText()
        elif self.action_v=='Pixmap':
            self.painter.drawPixmap()
        

        return super().mouseMoveEvent(evt)

    def mouseReleaseEvent(self,evt):
        if self.action_v=='Rect':
            rect=self.rb.geometry()
            self.painter.drawRect(rect)
            self.update()
            # 隐藏橡皮筋
            self.rb.hide()
            # 还原光标
            self.setCursor(Qt.ArrowCursor)
   
        self.last_point = None  # 松开鼠标 就把坐标清空    *******
    
        return super().mouseReleaseEvent(evt)

    # 笔的设置
    def pen_setting(self):
        pen=self.painter.pen()
        pen.setColor(QColor(self.pen_color)) 
        # pen.setColor(QColor('#35e3e3')) # 青色
        pen.setWidth(self.pen_width)# pen_width像素
        self.painter.setPen(pen) # 要把修改好的笔设回来 

    # 画图
    # 1 线条
    def drawLine(self)
        def mousePressEvent(self,evt):
            # 记录开始点
            self.last_point=evt.pos()
            # print(dir(self.last_point))
            # 设置笔
            self.pen_setting()
            return super().mousePressEvent(evt)

        def mouseMoveEvent(self,evt):
            # 1 线条
            self.painter.drawLine(self.last_point,evt.pos()) # 通过连续的drawLine 形成手写轨迹 *******
            self.update()# 触发更新 手写板 label 的绘图事件 paintEvent
            self.last_point=evt.pos() # 记录下一点的开始 这样才能 让mouseMoveEvent轨迹点连续
            return super().mouseMoveEvent(evt)

        def mouseReleaseEvent(self,evt):
    
            self.last_point = None  # 松开鼠标 就把坐标清空    *******

            return super().mouseReleaseEvent(evt)
    # 2 矩形
    def drawRect(self)
        def mousePressEvent(self,evt):
            # 记录开始点
            self.last_point=evt.pos()
            # print(dir(self.last_point))
            # 设置笔
            self.pen_setting()
            # 2 生成橡皮筋控件
            self.rb=QRubberBand(QRubberBand.Rectangle,self)
            # 初始大小为一个空的QSize对象，即无大小
            self.rb.setGeometry(QRect(self.last_point,QSize())) 

            # 3 显示橡皮筋
            self.rb.show()

            # 光标 为十字
            self.setCursor(Qt.CrossCursor)
            return super().mousePressEvent(evt)

        def mouseMoveEvent(self,evt):
            # 用橡皮筋显示将要画的矩形
            self.rb.setGeometry(QRect(self.last_point,evt.pos()).normalized())
            self.update()
            return super().mouseMoveEvent(evt)

        def mouseReleaseEvent(self,evt):
            rect=self.rb.geometry()
            self.painter.drawRect(rect)
            self.update()
            # 隐藏橡皮筋
            self.rb.hide()
            # 还原光标
            self.setCursor(Qt.ArrowCursor)
    
            self.last_point = None  # 松开鼠标 就把坐标清空    *******

            return super().mouseReleaseEvent(evt)

        


    


if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()