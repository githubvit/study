from PySide2.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QGraphicsItem,QGraphicsView,QGraphicsScene,\
    QVBoxLayout,QGraphicsEllipseItem,QGraphicsRectItem

from PySide2.QtCore import Qt,Signal,Slot,QPointF,QRectF
from PySide2.QtGui import QPen,QBrush

# 自定义 图元 移动

# class MoveItem(QGraphicsRectItem):
class MoveItem(QGraphicsEllipseItem):
    def __init__(self,x,y,r):
        super().__init__(x,y,r,r) # 椭圆
        self.setPen(QPen(Qt.black))
        self.setBrush(Qt.blue)
        self.setAcceptHoverEvents(True) # 开启鼠标在上事件 设置鼠标
        self.setCacheMode(self.DeviceCoordinateCache) # 加速图形的渲染
        # 移动方案 一 使用QGraphicsItem本身的移动标志实现
        # self.setFlag(QGraphicsItem.ItemIsMovable) 
        self.setFlag(QGraphicsItem.ItemIsSelectable) 

    # mouse hover Events
    def hoverEnterEvent(self,evt):
        # print('enter')
        # 改变光标形状
        self.setCursor(Qt.OpenHandCursor)

    # def hoverLeaveEvent(self,evt):
    #     print('leave')
        # 光标形状不用设置会自动变回来
        

    # mouse click Evens 完成平移


    
    # 移动方案 二 通过重写鼠标的相关事件实现 效果同方案一 完全一致 
    # 发现 多选后 不能像方案一一样 多个item同时移动
    def mousePressEvent(self,evt):
        # 必须写一个空的在这，又不能继承，一继承就不能移动
        # return super().mousePressEvent(evt)
        pass
    def mouseMoveEvent(self,evt):
        # 获取mouse坐标 QPointF()
        # orig_cursor_position=evt.lastScenePos() # 上次的场景坐标
        # updated_cursor_position=evt.scenePos()  # 当前的场景坐标
        # orig_position=self.scenePos() # 图元的场景坐标=图元的图元坐标 
        
        orig_cursor_position=evt.lastPos() # 上次的图元坐标
        updated_cursor_position=evt.pos()  # 当前的图元坐标
        orig_position=self.pos() # 图元的图元坐标 不动 就是(0,0) 即图元原点 ，动了 就是 以该图元原点为基点的坐标 不是视图和场景坐标

        print(f'orig_cursor_position：{orig_cursor_position}, updated_cursor_position：{updated_cursor_position}, orig_position：{orig_position}')
        
        # 以场景坐标和以图元坐标计算偏差是一样的
        # 计算偏差 加上 图元坐标，即得到 新的图元坐标
        updated_cursor_x=updated_cursor_position.x()-orig_cursor_position.x()+orig_position.x()
        updated_cursor_y=updated_cursor_position.y()-orig_cursor_position.y()+orig_position.y()
        # 用计算的图元坐标 更新位置
        self.setPos(QPointF(updated_cursor_x,updated_cursor_y))
        self.update()
        return super().mouseMoveEvent(evt)
        pass
    def mouseReleaseEvent(self,evt):
        print(f'x:{self.pos().x()},y:{self.pos().y()}') # 图元坐标 
        return super().mouseReleaseEvent(evt)
        pass
    
class MyScene(QGraphicsScene):
    pass
class GraphicsView(QGraphicsView):
    def __init__(self):
        super().__init__()
        # self.scene=QGraphicsScene()
        self.scene=QGraphicsScene(QRectF(0,0,800,800))
        # self.setSceneRect(0,0,1000,800) # 设定 场景原点位于 视图原点 否则在视图中心
        self.setScene(self.scene)
        
        self.pen=QPen(Qt.black)
        self.brush=QBrush(Qt.red)

        self.m_obj=MoveItem(0,0,50)

        self.m_obj2=MoveItem(100,100,100)

        self.scene.addItem(self.m_obj)
        
        self.scene.addItem(self.m_obj2)

        self.m_obj2.setZValue(-1) #设置在最下层  避免挡住self.m_obj 值越大 层越高

        self.setDragMode(GraphicsView.RubberBandDrag)# 开启橡皮筋选择
       
        # self.horizontalScrollBar().setSliderPosition(0) # 设定滚动条开始位置为 场景坐标 x=0 处 同默认
        # self.verticalScrollBar().setSliderPosition(0)  # 设定滚动条开始位置为  场景坐标 y=0 处 同默认
        # print(self.hasMouseTracking())

    # def mousePressEvent(self,evt):
    #     # print(evt) # <PySide2.QtGui.QMouseEvent object at 0x000001FFF045B588> 普通的 QMouseEvent
    #     # print(dir(evt))
    #     print(
    #         f'''
    #         evt.pos():{evt.pos()}, 
    #         evt.locaPos():{evt.localPos()}, 
            
    #         evt.globalPos():{evt.globalPos()}
    #         evt.globalX():{evt.globalX()},
    #         evt.globalY():{evt.globalY()},
    #         ''')

        
    #     # x():{x()},y():{y()},
    #     x=evt.pos().x()
    #     y=evt.pos().y()
    #     self.m_obj_n=MoveItem(x,y,50)
    #     self.scene.addItem(self.m_obj_n)




if __name__ == "__main__":
    app=QApplication([])
    wd=QWidget()
    wd.setWindowTitle('QGraphicsView 学习2')
    wd.setGeometry(1000,400,1200,1000) 
    # 当场景坐标开始设为（0，0），如果视图外框宽高 小于或等于 场景宽高 则 场景坐标(0,0)原点等于视图坐标原点 位于左上
    # 当场景坐标开始设为（0，0），如果视图宽高 大于 场景宽高 则 场景坐标(0,0)原点不等于视图坐标原点 位于（x大-x小，y大-y小）

    grv=GraphicsView()
    v_layout=QVBoxLayout(wd)
    v_layout.addWidget(grv)
    # grv.show()
    wd.show()

    app.exec_()