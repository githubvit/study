'''
QT自定义图形项中的boundingRect()和shape()函数的理解 -2 
https://blog.csdn.net/weixin_39583140/article/details/93599949?utm_medium=distribute.pc_relevant_bbs_down.none-task-blog-baidujs-1.nonecase&depth_1-utm_source=distribute.pc_relevant_bbs_down.none-task-blog-baidujs-1.nonecase
图形绘制都在paint()中进行 上一节 没有讲到shape() 
本节 要用到shape() 返回一个QPainterPath()对象，用来定义外形。


添加 shape() 绘制三角形
在keyPressEvent()函数中添加一个旋转的响应（按下R键）
实验碰撞检测
若有碰撞则绘制的图形将以黑色作为画刷填充


'''
import sys
from PySide2.QtCore import Signal,Qt,QPointF,QRectF
from PySide2.QtWidgets import QApplication,QWidget,QGraphicsScene,QGraphicsView,QGraphicsObject,QGraphicsItem,QStyleOptionGraphicsItem
from PySide2.QtGui import QPainter,QPainterPath,QPen,QBrush,QColor


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
   
    def keyPressEvent(self,evt):
        
        if evt.key()==Qt.Key_Left:
            self.moveBy(-1,0)
        elif evt.key()==Qt.Key_Right:
            self.moveBy(1,0)
        elif evt.key()==Qt.Key_Up:
            self.moveBy(0,-1)
        elif evt.key()==Qt.Key_Down:
            self.moveBy(0,1)
    
        elif evt.key()==Qt.Key_R: # 添加旋转
            self.setRotation(90)
            self.update()

        else:
            super().keyPressEvent(evt)

    # 添加shape

    def shape(self):
        trianglePath=QPainterPath() # 三角形路径对象
        trianglePath.moveTo(0,-50) # 顶点
        trianglePath.lineTo(50,50) # 右下点
        trianglePath.lineTo(-50,50) # 左下点
        trianglePath.closeSubpath() # 回到顶点
        return trianglePath
    # 绘制shape
    def drawPath(self,painter):
    
        shapePath=self.shape()
        painter.setPen(QPen(Qt.red,1,Qt.SolidLine,Qt.SquareCap,Qt.MiterJoin)) 
        painter.drawPath(shapePath)
        


    def paint(self,painter,QStyleOptionGraphicsItem,QWidget): 
        
        # 在之前的绘图上我们绘制出QboundingRect的虚线方框 
        rect=self.boundingRect()
        painter.setPen(QPen(Qt.black,1,Qt.DotLine,Qt.SquareCap,Qt.MiterJoin))
        painter.drawRect(rect)

        # 碰撞检测 如果聚焦和外框碰撞 就填充绿色
        if self.hasFocus() and len(self.collidingItems(Qt.IntersectsItemBoundingRect)):
            # print('1')
            brush1 = QBrush(Qt.SolidPattern)
            brush1.setColor(Qt.green)
            painter.setBrush(brush1) # 移动的item 的 外框虚线 碰到 另一个item的实线 变绿
        # 碰撞检测 如果聚焦和外形碰撞 就填充黑色
        if self.hasFocus() and len(self.collidingItems(Qt.IntersectsItemShape)):
            # print('2')
            brush2 = QBrush(Qt.SolidPattern)
            brush2.setColor(Qt.black)
            painter.setBrush(brush2)# 移动的item 的 实线 碰到 另一个item的实线 变黑

        # 绘制外形
        self.drawPath(painter)
           



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

        # self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
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

        #这里把外形和虚线外框都在这里paint()中绘制 下一节 要用到shape()
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view=MyView()
    view.show()
    sys.exit(app.exec_())