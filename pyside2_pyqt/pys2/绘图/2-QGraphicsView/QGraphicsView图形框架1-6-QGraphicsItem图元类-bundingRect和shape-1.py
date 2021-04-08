'''
QT自定义图形项中的boundingRect()和shape()函数的理解 -1
https://blog.csdn.net/weixin_39583140/article/details/93599949?utm_medium=distribute.pc_relevant_bbs_down.none-task-blog-baidujs-1.nonecase&depth_1-utm_source=distribute.pc_relevant_bbs_down.none-task-blog-baidujs-1.nonecase

实现自定义图形项经常需要重绘的函数有boundingRect()、paint()、shape()。
针对霍亚飞的Qt creator中所说，boundingRect()函数具有以下特点：
1.paint绘制的图像必须在boundingRect()函数之中。
2.用来确定哪些区域需要重构（repaint）。
3.用来检测碰撞

'''
import sys
from PySide2.QtCore import Signal,Qt,QPointF,QRectF
from PySide2.QtWidgets import QApplication,QWidget,QGraphicsScene,QGraphicsView,QGraphicsObject,QGraphicsItem,QStyleOptionGraphicsItem
from PySide2.QtGui import QPainter,QPainterPath,QPen,QBrush


class MyItem(QGraphicsItem):
    

    def __init__(self):
        super().__init__()
        #一定要获得焦点ItemIsFocusable，否则keyPressEvent 键盘事件不响应
        self.setFlags(QGraphicsItem.ItemIsMovable|QGraphicsItem.ItemIsFocusable)


        
    # 2
    def boundingRect(self):
        penwidth=1
        return QRectF(-50-penwidth/2,-50-penwidth/2,100+penwidth,100+penwidth)

    # 3
    def drawRectPath(self, painter):
        # painter=QPainter()
        rectPath=QPainterPath()
        rectPath.moveTo(-50,-50)
        rectPath.lineTo(50,-50)
        rectPath.lineTo(50,50)
        rectPath.lineTo(-50,50)
        rectPath.closeSubpath() # 返回绘图开始点

        # pen参数别设置错了，要不不好看出来
        # pen=QPen()
        # pen.setColor(Qt.red)
        # pen.setWidth(20)
        # pen.setStyle(Qt.SolidLine)
        # pen.setCapStyle(Qt.SquareCap)
        # pen.setJoinStyle(Qt.MiterJoin)
        # painter.setPen(pen)

        # 这样更方便 效果一样
        painter.setPen(QPen(Qt.red,20,Qt.SolidLine,Qt.SquareCap,Qt.MiterJoin)) 
        painter.drawPath(rectPath)

        # 由上图，虽然我们绘制的图像和boundingRect返回的QRect是一样大的,
        # 但是因为我们的pen宽度，绘制的图形已经超出了boudingRect.

        # 为了看到视图更新的效果，我们为图形项添加移动效果：
    def keyPressEvent(self,evt):
        
        if evt.key()==Qt.Key_Left:
            self.moveBy(-1,0)
        elif evt.key()==Qt.Key_Right:
            self.moveBy(1,0)
        elif evt.key()==Qt.Key_Up:
            self.moveBy(0,-1)
        elif evt.key()==Qt.Key_Down:
            self.moveBy(0,1)
        else:
            super().keyPressEvent(evt)
            


        # 好了，点中方框图形（点击在虚线里边），就可以上下左右键移动了， 但是，没有点在虚线里面就不能移动图形，不管是鼠标还是键盘。

    def paint(self,painter,QStyleOptionGraphicsItem,QWidget): 
        # 绘制图形
        self.drawRectPath(painter)
        # 在之前的绘图上我们绘制出QboundingRect的虚线方框 
        rect=self.boundingRect()
        painter.setPen(QPen(Qt.black,1,Qt.DotLine,Qt.SquareCap,Qt.MiterJoin))

        painter.drawRect(rect)

class MyView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)
        item1=MyItem()
        item2=MyItem()
        item1.setPos(0,0)
        item2.setPos(150,150)
      

        self.scene = QGraphicsScene()
        
        self.scene.addItem(item1)
        self.scene.addItem(item2)
        self.setScene(self.scene)

        # 移动图元时有很严重的 拖尾现象，在于没有设置视图的更新模式

        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        '''
            总共有五种模式，很容易理解：
            QGraphicsView::FullViewportUpdate 全视口更新，整体都更新的意思啦
            QGraphicsView::MinimalViewportUpdate 最小更新，哪里有变动更新哪里
            QGraphicsView::SmartViewportUpdate 智能选择，它要自己选
            QGraphicsView::BoundingRectViewportUpdate 来了，来了，它就是我们要注意的。
            QGraphicsView::NoViewportUpdate 不更新
            其中默认为QGraphicsView::MinimalViewportUpdate，也就是上例中我们没有进行设置的情况。
            事实上除了设置为FullViewportUpdate 其余四种皆会出现问题，不妨试一试。
            我们可以通过在MyView的构造函数中设置为FullViewportUpdate 的全视口更新得到我们想要的结果，但是却是以牺牲性能为代价的。
        '''

        #图形绘制都在paint()中 没有讲到shape() 下一节 要用到shape() 返回一个QPainterPath()对象，用来定义外形。
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view=MyView()
    view.show()
    sys.exit(app.exec_())