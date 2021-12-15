from PySide2.QtWidgets import QApplication,QGraphicsScene,QGraphicsView,QGraphicsItem,QGraphicsObject,QGraphicsPathItem,\
    QGraphicsTextItem,QGraphicsPolygonItem,QGraphicsLineItem,QGraphicsRectItem,QGraphicsEllipseItem,QGraphicsPixmapItem,\
    QAbstractGraphicsShapeItem,QVBoxLayout,QHBoxLayout,QTextEdit,QGraphicsProxyWidget,QPushButton,QGraphicsWidget,QStyle
from PySide2.QtCore import Slot,Signal,Qt,QPointF,QLineF,QRect,QRectF,QSize,QUuid,QEvent,QSettings,QObject
from PySide2.QtGui import QPainter,QPainterPath,QPen,QBrush,QTransform,QPixmap,QColor,QTextItem,QFont,QTextOption

from enum import Enum # 枚举类

handle_size=15 # 句柄大小
grid_size=10 # 网格大小
grid_enabled=False # 网格控制

# grid_enabled=True # 网格控制
class HandleShape(Enum): #外形
    HANDLE_SHAPE_RECT='HANDLE_SHAPE_RECT'
    HANDLE_SHAPE_CIRCLE='HANDLE_SHAPE_CIRCLE'
    HANDLE_SHAPE_TRIANGLE='HANDLE_SHAPE_TRIANGLE'
    pass

class HandleType(Enum): #类型
    HANDLE_TYPE_TOPLEFT='HANDLE_TYPE_TOPLEFT'
    HANDLE_TYPE_TOP='HANDLE_TYPE_TOP'
    HANDLE_TYPE_TOPRIGHT='HANDLE_TYPE_TOPRIGHT'
    HANDLE_TYPE_LEFT='HANDLE_TYPE_LEFT'
    HANDLE_TYPE_RIGHT='HANDLE_TYPE_RIGHT'
    HANDLE_TYPE_BOTTOMLEFT='HANDLE_TYPE_BOTTOMLEFT'
    HANDLE_TYPE_BOTTOM='HANDLE_TYPE_BOTTOM'
    HANDLE_TYPE_BOTTOMRIGHT='HANDLE_TYPE_BOTTOMRIGHT'
    HANDLE_TYPE_ROTATE='HANDLE_TYPE_ROTATE'
    HANDLE_TYPE_ROTATE_CENTER='HANDLE_TYPE_ROTATE_CENTER' # 旋转中心 取代 原来的origin
    HANDLE_TYPE_CTRL='HANDLE_TYPE_CTRL'

    pass

# 控制点 句柄
class Handle():
    def __init__(self,pos,hshape,htype):
        self.size=handle_size
        self.set_pos(pos)
        self.set_shape(hshape)
        self.set_type(htype)

    def set_size(self,size):
        if isinstance(size,int):
            self.size=size

    def set_pos(self,pos):
        if isinstance(pos,QPointF):
            self.rect=QRectF(pos.x()-self.size/2,pos.y()-self.size/2,self.size,self.size)
            self.pos=pos
    
    def set_shape(self,hshape):
        if isinstance(hshape,HandleShape):
            self.hshape=hshape

    def set_type(self,htype):
        if isinstance(htype,HandleType):
            self.htype=htype

    # def boundingRect(self):
    #     return self.rect
    pass

# 基础图元
class BaseItem(QGraphicsItem):
    def __init__(self,rect,scene,parent=None): # 必须有区域rect 和 场景 scene 
        super().__init__(parent)
        id=QUuid.createUuid()
        self.id=id.toString()
       
        self.setFlags(QGraphicsItem.ItemIsMovable|QGraphicsItem.ItemIsSelectable|QGraphicsItem.ItemSendsGeometryChanges|QGraphicsItem.ItemIsFocusable)
        self.rect=QRectF(rect[0],rect[1],rect[2],rect[3])  # QRectF(self, left: float, top: float, width: float, height: float)
        self.scene=scene
        self.scene.addItem(self)
        self.currentHandle=None # 当前句柄
        self.createHandles() # 创建句柄 

        # 最小尺寸  用以控制 缩放的极限位置
        self.rect_min_size=2*handle_size # 宽高的最小值为2倍句柄尺寸,就是2个方形控制器handle的尺寸

        # 缩放算法 的 固定边 初始值
        self.current_fix_v_edge=None # 控制x方向的极限位置
        self.current_fix_h_edge=None # 控制y方向的极限位置

        # 旋转角度
        self.angle=0

    def setId(self,i):
        if isinstance(i,str):
            self.id=i 

    # 创建句柄 句柄列表 
    def createHandles(self):
        self.rotate_center=self.rect.center() # 设定默认的旋转中心就是图形的中心
        self.Handles=[] # 句柄列表
        left=QPointF(self.rect.left(),self.rect.top()+self.rect.height()/2)
        right=QPointF(self.rect.right(),self.rect.top()+self.rect.height()/2)
        top=QPointF(self.rect.left()+self.rect.width()/2,self.rect.top())
        bottom=QPointF(self.rect.left()+self.rect.width()/2,self.rect.bottom())

        rotate=QPointF(top.x(),top.y()-50)

        self.Handles.append(Handle(self.rect.topLeft(),HandleShape.HANDLE_SHAPE_RECT,HandleType.HANDLE_TYPE_TOPLEFT))
        self.Handles.append(Handle(top,HandleShape.HANDLE_SHAPE_RECT,HandleType.HANDLE_TYPE_TOP))
        self.Handles.append(Handle(self.rect.topRight(),HandleShape.HANDLE_SHAPE_RECT,HandleType.HANDLE_TYPE_TOPRIGHT))
        self.Handles.append(Handle(left,HandleShape.HANDLE_SHAPE_RECT,HandleType.HANDLE_TYPE_LEFT))
        self.Handles.append(Handle(right,HandleShape.HANDLE_SHAPE_RECT,HandleType.HANDLE_TYPE_RIGHT))
        self.Handles.append(Handle(self.rect.bottomLeft(),HandleShape.HANDLE_SHAPE_RECT,HandleType.HANDLE_TYPE_BOTTOMLEFT))
        self.Handles.append(Handle(bottom,HandleShape.HANDLE_SHAPE_RECT,HandleType.HANDLE_TYPE_BOTTOM))
        self.Handles.append(Handle(self.rect.bottomRight(),HandleShape.HANDLE_SHAPE_RECT,HandleType.HANDLE_TYPE_BOTTOMRIGHT))
        
        self.Handles.append(Handle(rotate,HandleShape.HANDLE_SHAPE_CIRCLE,HandleType.HANDLE_TYPE_ROTATE)) # 旋转句柄
        self.Handles.append(Handle(self.rotate_center,HandleShape.HANDLE_SHAPE_CIRCLE,HandleType.HANDLE_TYPE_ROTATE_CENTER)) # 旋转中心
        pass

    # 确定绘制区域  
    def boundingRect(self):
        size=handle_size
        return self.rect.adjusted(-size/2,-size/2 - 50,size/2,size/2) # 调整绘制区域 使其可以绘出句柄

    # 确定选择区域 = 外框区域 + 句柄区域 并集
    def shape(self):
        path=QPainterPath()
        path.setFillRule(Qt.WindingFill) # 路径填充 没有 则 句柄路径和外框路径的交集不能被选择，windingFill表示取路径的并集。*****
        if self.isSelected:
            for handle in self.Handles:
                if handle.hshape==HandleShape.HANDLE_SHAPE_RECT or handle.hshape==HandleShape.HANDLE_SHAPE_CIRCLE:
                    path.addRect(handle.rect) # 句柄路径
                else:
                    break
        path.addRect(self.rect) # 外框路径
        return path

    # 绘制 外框 和 句柄
    def paint(self,painter,option,widget):
        # painter=QPainter() #为了 代码 好写
        if self.isSelected():
            pen=QPen(Qt.green)
            painter.setPen(pen)
            # 绘制外框
            painter.drawRect(self.rect)

            # 绘制句柄
            p1=None
            p2=None
            for handle in self.Handles:
                # 取出两点 旋转点 和 顶点
                if handle.htype==HandleType.HANDLE_TYPE_ROTATE:
                    p1=handle.pos
                if handle.htype==HandleType.HANDLE_TYPE_TOP:
                    p2=handle.pos
                # 绘制句柄
                if handle.hshape==HandleShape.HANDLE_SHAPE_RECT:
                    painter.drawRect(handle.rect)
                elif handle.hshape==HandleShape.HANDLE_SHAPE_CIRCLE:
                    painter.drawEllipse(handle.rect)
                
            # 绘制旋转点和顶部中心连线
            painter.drawLine(p1,p2)

            self.scene.update() # 反拖尾
        pass
    
    # 改变图元大小和外形 要进行预加载
    def itemChange(self,change,value):
        if change==QGraphicsItem.ItemSelectedChange: #切换选择有可能改变大小和形状
            self.prepareGeometryChange() #预加载
        if change == QGraphicsItem.ItemPositionChange:
            newPos = value
            if grid_enabled: # 将位置移到网格上
                # 去掉余数 就是grid的整数倍
                if newPos.x()%grid_size != 0:
                    x = newPos.x() - newPos.x()%grid_size
                    newPos.setX(x)
                
                if newPos.y()%grid_size != 0:
                    y = newPos.y() - newPos.y()%grid_size
                    newPos.setY(y)
                
            return newPos
        return super().itemChange(change,value)  

    # 旋转中心 xy宽高比 
    def define_dx_dy(self):
        self.rotate_center_dx=(self.rotate_center.x()-self.rect.center().x())/self.rect.width()
        self.rotate_center_dy=(self.rotate_center.y()-self.rect.center().y())/self.rect.width()

    # 确定光标和固定边
    def define_cusor_fix_edge(self):
        if self.currentHandle:
            # 左右拉伸缩放
            if self.currentHandle.htype == HandleType.HANDLE_TYPE_LEFT:
                
                self.setCursor(Qt.SizeHorCursor)
                self.current_fix_v_edge=self.rect.right()

            elif self.currentHandle.htype == HandleType.HANDLE_TYPE_RIGHT:
                self.setCursor(Qt.SizeHorCursor)
                self.current_fix_v_edge=self.rect.left()

            # 上下拉伸缩放
            elif self.currentHandle.htype == HandleType.HANDLE_TYPE_TOP:
                self.setCursor(Qt.SizeVerCursor)
                self.current_fix_h_edge=self.rect.bottom()


            elif self.currentHandle.htype == HandleType.HANDLE_TYPE_BOTTOM:
                self.setCursor(Qt.SizeVerCursor)
                self.current_fix_h_edge=self.rect.top()

            # 左上 右上 左下 右下 拉伸缩放
            elif self.currentHandle.htype == HandleType.HANDLE_TYPE_TOPLEFT:
                self.setCursor(Qt.SizeFDiagCursor)
                self.current_fix_v_edge=self.rect.right()
                self.current_fix_h_edge=self.rect.bottom()

            elif self.currentHandle.htype == HandleType.HANDLE_TYPE_TOPRIGHT:
                self.setCursor(Qt.SizeBDiagCursor)
                self.current_fix_v_edge=self.rect.left()
                self.current_fix_h_edge=self.rect.bottom()

            elif self.currentHandle.htype == HandleType.HANDLE_TYPE_BOTTOMRIGHT:
                self.setCursor(Qt.SizeFDiagCursor)
                self.current_fix_v_edge=self.rect.left()
                self.current_fix_h_edge=self.rect.top()

            elif self.currentHandle.htype == HandleType.HANDLE_TYPE_BOTTOMLEFT:
                self.setCursor(Qt.SizeBDiagCursor)
                self.current_fix_v_edge=self.rect.right()
                self.current_fix_h_edge=self.rect.top()

            #  绕 旋转中心 self.origin 旋转
            elif self.currentHandle.htype == HandleType.HANDLE_TYPE_ROTATE:
                self.setCursor(Qt.PointingHandCursor) # 手指
                pass

            # 平移 旋转中心
            elif self.currentHandle.htype == HandleType.HANDLE_TYPE_ROTATE_CENTER:
                self.setCursor(Qt.CrossCursor) # 十字
                pass


            elif self.currentHandle.htype == HandleType.HANDLE_TYPE_CTRL:
                self.setCursor(Qt.SizeAllCursor) # 平移
                pass

        else:
            self.setCursor(Qt.SizeAllCursor) # 平移

    # 三大鼠标事件
    # 确定当前句柄 状态设置
    def mousePressEvent(self,evt):
        if evt.buttons()==Qt.LeftButton:
            for handle in self.Handles:
                # 确定当前句柄
                if handle.rect.contains(evt.pos()):
                    self.currentHandle=handle
        # 状态设置
        self.define_dx_dy() # 确定本次 旋转中心 xy宽高比
        self.define_cusor_fix_edge() # 确定 本次 光标和固定边
        
        return super().mousePressEvent(evt)

    # 拉伸和旋转 rect
    def stretch_rotate(self,evt):
        # 左右拉伸
        if self.currentHandle.htype == HandleType.HANDLE_TYPE_LEFT:
            # 固定右端
            # 移动左端
            if evt.pos().x()<=self.current_fix_v_edge-self.rect_min_size: # 极限位置 = 固定边-最小尺寸
                self.rect.setLeft(evt.pos().x())
            else:
                self.rect.setLeft(self.current_fix_v_edge-self.rect_min_size) # 就 设为 极限位置 
                
            # self.rect.center() 会自动更新

            # 根据 xy宽高比self.rotate_center_dx self.rotate_center_dy 更新 旋转中心 的 位置
            self.rotate_center.setX((self.rotate_center_dx*self.rect.width())+self.rect.center().x())
               
        elif self.currentHandle.htype == HandleType.HANDLE_TYPE_RIGHT:
            # 固定左端
            # 移动右端
            if evt.pos().x()>=self.current_fix_v_edge+self.rect_min_size:
                self.rect.setRight(evt.pos().x())
            else:
                self.rect.setRight(self.current_fix_v_edge+self.rect_min_size)
            self.rotate_center.setX((self.rotate_center_dx*self.rect.width())+self.rect.center().x())
        
        # 上下拉伸
        elif self.currentHandle.htype == HandleType.HANDLE_TYPE_TOP:
            # 固定下端
            # 移动上端
            if evt.pos().y()<=self.current_fix_h_edge-self.rect_min_size:
                self.rect.setTop(evt.pos().y())
            else:
                self.rect.setTop(self.current_fix_h_edge-self.rect_min_size)
            # 更新 旋转中心 的 y
            self.rotate_center.setY(self.rotate_center_dy*self.rect.height()+self.rect.center().y())
            
        elif self.currentHandle.htype == HandleType.HANDLE_TYPE_BOTTOM:
            # 固定上端
            # 移动下端
            if evt.pos().y()>=self.current_fix_h_edge+self.rect_min_size:
                self.rect.setBottom(evt.pos().y())
            else:
                self.rect.setBottom(self.current_fix_h_edge+self.rect_min_size)
            self.rotate_center.setY(self.rotate_center_dy*self.rect.height()+self.rect.center().y())
            
        # 左上 右上 左下 右下 拉伸
        elif self.currentHandle.htype == HandleType.HANDLE_TYPE_TOPLEFT:
            # 固定右端
            # 移动左端
            if evt.pos().x()<=self.current_fix_v_edge-self.rect_min_size:
                x=evt.pos().x()
            else:
                x=self.current_fix_v_edge-self.rect_min_size
            # 固定下端
            # 移动上端
            if evt.pos().y()<=self.current_fix_h_edge-self.rect_min_size:
                y=evt.pos().y()
            else:
                y=self.current_fix_h_edge-self.rect_min_size
            # 设置 外框的 左上顶点
            self.rect.setTopLeft(QPointF(x,y))
            # 更新 旋转中心 的 x y
            self.rotate_center.setX((self.rotate_center_dx*self.rect.width())+self.rect.center().x())
            self.rotate_center.setY((self.rotate_center_dy*self.rect.height())+self.rect.center().y())

        elif self.currentHandle.htype == HandleType.HANDLE_TYPE_TOPRIGHT:
            # 固定左端
            # 移动右端
            if evt.pos().x()>=self.current_fix_v_edge+self.rect_min_size:
                x=evt.pos().x()
            else:
                x=self.current_fix_v_edge+self.rect_min_size
            # 固定下端
            # 移动上端
            if evt.pos().y()<=self.current_fix_h_edge-self.rect_min_size:
                y=evt.pos().y()
            else:
                y=self.current_fix_h_edge-self.rect_min_size
            self.rect.setTopRight(QPointF(x,y))
            self.rotate_center.setX((self.rotate_center_dx*self.rect.width())+self.rect.center().x())
            self.rotate_center.setY((self.rotate_center_dy*self.rect.height())+self.rect.center().y())

        elif self.currentHandle.htype == HandleType.HANDLE_TYPE_BOTTOMRIGHT:
            # 固定左端
            # 移动右端
            if evt.pos().x()>=self.current_fix_v_edge+self.rect_min_size:
                x=evt.pos().x()
            else:
                x=self.current_fix_v_edge+self.rect_min_size
            # 固定上端
            # 移动下端
            if evt.pos().y()>=self.current_fix_h_edge+self.rect_min_size:
                y=evt.pos().y()
            else:
                y=self.current_fix_h_edge+self.rect_min_size
            self.rect.setBottomRight(QPointF(x,y))
            self.rotate_center.setX((self.rotate_center_dx*self.rect.width())+self.rect.center().x())
            self.rotate_center.setY((self.rotate_center_dy*self.rect.height())+self.rect.center().y())

        elif self.currentHandle.htype == HandleType.HANDLE_TYPE_BOTTOMLEFT:
            # 固定右端
            # 移动左端
            if evt.pos().x()<=self.current_fix_v_edge-self.rect_min_size:
                x=evt.pos().x()
            else:
                x=self.current_fix_v_edge-self.rect_min_size
            # 固定上端
            # 移动下端
            if evt.pos().y()>=self.current_fix_h_edge+self.rect_min_size:
                y=evt.pos().y()
            else:
                y=self.current_fix_h_edge+self.rect_min_size
            self.rect.setBottomLeft(QPointF(x,y))
            self.rotate_center.setX((self.rotate_center_dx*self.rect.width())+self.rect.center().x())
            self.rotate_center.setY((self.rotate_center_dy*self.rect.height())+self.rect.center().y())

        #  绕 旋转中心 self.rotate_center 旋转
        elif self.currentHandle.htype == HandleType.HANDLE_TYPE_ROTATE:
            angle=-QLineF(evt.pos(),self.rotate_center).angle()+ QLineF(evt.lastPos(),self.rotate_center).angle()
            self.angle += angle

            # 坐标 变换 (平移和旋转再平移回来)
            self.setTransform(QTransform().translate(self.rotate_center.x(),self.rotate_center.y()).rotate(-QLineF(evt.pos(),self.rotate_center).angle()+ QLineF(evt.lastPos(),self.rotate_center).angle()).translate(-self.rotate_center.x(),-self.rotate_center.y()),True)
            
            # 图元的旋转
                # 实际上 图元的旋转 就是 旋转图元坐标轴
                # self.setTransform(变换矩阵matrix:PySide2.QtGui.QTransform,布尔值 bool)
                # 1. 原点平移到 self.rotate_center 旋转中心
                    # QTransform().translate(self.rotate_center.x(),self.rotate_center.y()) 坐标  默认坐标原点是左上
                # 2. 绕 self.rotate_center 旋转  坐标轴
                    # .rotate(-QLineF(evt.scenePos(),self.mapToScene(self.rotate_center)).angle()+ QLineF(evt.lastScenePos(),self.mapToScene(self.rotate_center)).angle())
                        # 起点和原点连线 的角度 QLineF(evt.lastScenePos(),self.mapToScene(self.rotate_center)).angle()  这里统一使用了场景坐标 实际使用了图元坐标，都可以
                        # 减去 终点和原点连线 的角度 -QLineF(evt.scenePos(),self.mapToScene(self.rotate_center)).angle() 
                # 3. 原点 还原 回到 旋转后的 
                    # 移动了多少 就还原多少 .translate(-self.rotate_center.x(),-self.rotate_center.y())
                # 下一次旋转时，又来一遍123循环

        # 平移 旋转中心
        elif self.currentHandle.htype == HandleType.HANDLE_TYPE_ROTATE_CENTER:
            # 平移
            self.currentHandle.set_pos(evt.pos())
            # 更新 旋转中心
            self.rotate_center=self.currentHandle.pos

        elif self.currentHandle.htype == HandleType.HANDLE_TYPE_CTRL:
            self.currentHandle.set_pos(evt.pos())

    # 更新handle句柄  位置
    def update_handle_pos(self):
        # 更新 handle pos
        left=QPointF(self.rect.left(),self.rect.top()+self.rect.height()/2)
        right=QPointF(self.rect.right(),self.rect.top()+self.rect.height()/2)
        top=QPointF(self.rect.left()+self.rect.width()/2,self.rect.top())
        bottom=QPointF(self.rect.left()+self.rect.width()/2,self.rect.bottom())
        rotate=QPointF(top.x(),top.y()-50)
        for handle in self.Handles:
            # handle=Handle()
            if handle.htype == HandleType.HANDLE_TYPE_LEFT:
                # 更新handle的位置pos和handle区域rect
                # print('leftpos',handle.pos)
                handle.set_pos(left)
            elif handle.htype == HandleType.HANDLE_TYPE_RIGHT:
                handle.set_pos(right)
            elif handle.htype == HandleType.HANDLE_TYPE_TOP:
                handle.set_pos(top)
            elif handle.htype == HandleType.HANDLE_TYPE_BOTTOM:
                handle.set_pos(bottom)
            elif handle.htype == HandleType.HANDLE_TYPE_TOPLEFT:
                handle.set_pos(self.rect.topLeft())
            elif handle.htype == HandleType.HANDLE_TYPE_TOPRIGHT:
                handle.set_pos(self.rect.topRight())
            elif handle.htype == HandleType.HANDLE_TYPE_BOTTOMLEFT:
                handle.set_pos(self.rect.bottomLeft())
            elif handle.htype == HandleType.HANDLE_TYPE_BOTTOMRIGHT:
                handle.set_pos(self.rect.bottomRight())
            elif handle.htype == HandleType.HANDLE_TYPE_ROTATE:
                handle.set_pos(rotate)
            elif handle.htype == HandleType.HANDLE_TYPE_ROTATE_CENTER:
                handle.set_pos(self.rotate_center)

    # 根据当前句柄 确定动作(缩放、旋转、平移)
    def mouseMoveEvent(self,evt):
        if self.isSelected:
            if self.currentHandle:
                # 拉伸和旋转
                self.stretch_rotate(evt)
                # 更新 handle 位置
                self.update_handle_pos()
                self.update()
                
            else:
                # 平移 用继承方案
                return super().mouseMoveEvent(evt)

    # 释放当前句柄 状态复原
    def mouseReleaseEvent(self,evt):
        # 释放句柄
        self.currentHandle=None
        # 释放固定边
        self.current_fix_v_edge=None
        self.current_fix_h_edge=None
        # 恢复光标
        self.setCursor(Qt.ArrowCursor)
        # print(self.angle)
        return super().mouseReleaseEvent(evt)

     # 键盘事件
   
    # 键盘快捷键
    def keyPressEvent(self,evt):
        # moveBy 不受 移动开关 的约束
        if evt.key()==Qt.Key_Left:
            self.moveBy(-1,0)
        elif evt.key()==Qt.Key_Right:
            self.moveBy(1,0)
        elif evt.key()==Qt.Key_Up:
            self.moveBy(0,-1)
        elif evt.key()==Qt.Key_Down:
            self.moveBy(0,1)
    
        elif evt.key()==Qt.Key_R: # 添加旋转  每次绕 旋转中心self.rotate_center 旋转10°
            self.setTransform(QTransform().translate(self.rotate_center.x(),self.rotate_center.y()).rotate(10).translate(-self.rotate_center.x(),-self.rotate_center.y()),True)

        elif evt.key()==Qt.Key_O: # 将 self.rotate_center 旋转中心 复位到 图形中心 self.rect.center()
            self.rotate_center=self.rect.center()
            # 更新位置
            for handle in self.Handles:
                if handle.htype == HandleType.HANDLE_TYPE_ROTATE_CENTER:
                    handle.set_pos(self.rotate_center)
        else:
            super().keyPressEvent(evt)
    
# 应用图元 类型
class ItemType(Enum):
    ITEM_LINE=0
    ITEM_CIRCLE=1
    ITEM_TRIANGLE=2
    ITEM_RECTANGLE=3
    ITEM_ELLIPSE=4
    ITEM_PIXMAP=5
    ITEM_TEXT=6
    ITEM_PIE=7
    ITEM_RT_TRIANGLE=8
    ITEM_WRITE=9
    ITEM_POLYGON=10
    
    pass

# 应用图元
class AppItem(BaseItem):
    def __init__(self,rect,itemType,scene,parent=None):
        super().__init__(rect,scene,parent)
        self.rect=QRectF(rect[0],rect[1],rect[2],rect[3])
        self.mType=itemType
        self.mPixmap=None
        
        
        # 子item 方案一
        if self.mType == ItemType.ITEM_TEXT:
            # t_item=QGraphicsTextItem('hello view ',self)
            # t_item.setTextInteractionFlags(Qt.TextEditorInteraction) 
            # t_item.setPos(0,0)
            # 让widget代理图元item
            pwgt=QGraphicsProxyWidget(self)
            te_obj=QTextEdit('hello proxywidget item')
            # te_obj.setStyleSheet('background-color: transparent;')
            pwgt.setWidget(te_obj)
            # pwgt.setAutoFillBackground(False)
            pwgt.setGeometry(self.rect.adjusted(+10,+10,-10,-10)) # 调整大小 不能完全填充父元素，留边10→以便选择到父元素 self， 便于移动 旋转
           
        elif self.mType == ItemType.ITEM_ELLIPSE:
            ellipse=QGraphicsEllipseItem(self.rect,self)

        elif self.mType == ItemType.ITEM_PIXMAP:
            # pixmap=QGraphicsPixmapItem(self)
            pass
            
        elif self.mType ==ItemType.ITEM_RECTANGLE:
            rect=QGraphicsRectItem(self.rect,self) 

        elif self.mType == ItemType.ITEM_WRITE: # 手写图元
            # 手写图元
            self.write_item=QGraphicsPathItem(self)
            # 手写开关 双击打开或关闭
            self.write_edit=False 
            # 手写对象
            self.write_path=QPainterPath()
            # 手写控制点列表
            self.write_list=[]
            # 列表开关 为 False 就关闭手写了 列表开关，就不能再往列表里添加节点，即就不能再往里手写了。
            self.write_list_onoff=True  # 右击时关闭
            # 手写控制点 等效比 列表
            self.write_point_dx_list=[]
            self.write_point_dy_list=[]

            # 程序容器
            self.a_press=self.mousePressEvent 
            self.b_move=self.mouseMoveEvent
            self.c_release=self.mouseReleaseEvent
            
            
            # 手写图元外框 用 笔
            self.write_item_pen_wk=QPen(Qt.DashDotDotLine)
            # 手写图元 线条 用 笔
            self.write_item_pen_line=QPen(Qt.black,3,Qt.SolidLine,Qt.RoundCap,Qt.RoundJoin)
            # QPen(颜色,宽度,线条样式,笔端样式,线条连接样式)
            # 为手写图元 设置 线条 用笔
            self.write_item.setPen(self.write_item_pen_line)
            
        elif self.mType == ItemType.ITEM_POLYGON: #封闭多边形
            self.polygon_item=QGraphicsPathItem(self) # 图元
            self.polygon_edit=False # 编辑 开关
            self.polygon_path=QPainterPath() # 路径对象
            # 封闭多边形 顶点列表
            self.polygon_list=[]
            self.current_polygon_handle=None # 当前顶点
            # 列表开关 为 False 就关闭了 列表开关，就不能再往列表里添加节点
            self.polygon_list_onoff=True  # 添加该开关，就使得 只能 添加1个多边形
            # 多边形 顶点 等效比 列表
            self.polygon_point_dx_list=[]
            self.polygon_point_dy_list=[]
            # 程序容器
            self.a_press=self.mousePressEvent 
            self.b_move=self.mouseMoveEvent
            self.c_release=self.mouseReleaseEvent
            # 封闭多边形 图元 外框 用 笔
            self.polygon_item_pen_wk=QPen(Qt.DashDotDotLine)
           
            # 手写图元 线条 用 笔
            self.polygon_item_pen_line=QPen(Qt.black,3,Qt.SolidLine,Qt.RoundCap,Qt.RoundJoin)
            # QPen(颜色,宽度,线条样式,笔端样式,线条连接样式)
            # 为手写图元 设置 线条 用笔
            self.polygon_item.setPen(self.polygon_item_pen_line)


        self.keyEvent=False

    def setPixmap(self,path):
        self.mPixmap=QPixmap(path)

    # def boundingRect(self): # 注释掉 没有什么影响

    #     return super().boundingRect()

    # def shape(self):
    #     path=QPainterPath()
    #     path.setFillRule(Qt.WindingFill) # 该路径填充很重要，
    #     if self.mType == ItemType.ITEM_TEXT:
    #         path.addRect(self.childItems()[0].boundingRect())
    #         return path
      
    #     return super().shape()

    def paint(self,painter,option,widget):
        # painter=QPainter()
        painter.setRenderHint(QPainter.Antialiasing,True) # 反锯齿

        # 根据类型 绘制图形
        if self.mType ==ItemType.ITEM_RECTANGLE:
            # 方式一 定义 item 作为 self 的 子item
            self.childItems()[0].setRect(self.rect)
            
            # 方案二 用笔画 
            # painter.drawRect(self.rect) # 该方案 拉伸 时  无 矩形 重叠
            pass

        elif self.mType == ItemType.ITEM_ELLIPSE:
            # 方案一 子item
            self.childItems()[0].setRect(self.rect)

            # 方案二 用笔画 
            # painter.drawEllipse(self.rect)

        elif self.mType == ItemType.ITEM_LINE:
            painter.drawLine(self.rect.topLeft(),self.rect.bottomRight())

        elif self.mType == ItemType.ITEM_PIXMAP:
            # 方案一 子item
            # self.childItems()[0].setPixmap(self.mPixmap.scaled(self.rect.width(),self.rect.height()))
            # self.childItems()[0].setOffset(self.rect.topLeft())
            # self.childItems()[0].setZValue(self.childItems()[0].zValue()-1)
            # 位置在最上面，挡住了旋转中心

            # 方案二 绘制
            painter.drawPixmap(self.rect.toRect(),self.mPixmap) 
            # 不能是QRectF 必须是 QRect 所以用QRectF.toRect() 进行转换
            # 位置在最后 ，可以看见旋转中心

        elif self.mType == ItemType.ITEM_TEXT:     
            # 方案一 子item方案
            self.childItems()[0].setGeometry(self.rect.adjusted(+10,+10,-10,-10))
           
            # 方案二 绘制  问题是 不可编辑
            # ft=QFont('微软雅黑',20,QFont.Bold,True) #QFont(self, family: str, pointSize: int = -1, weight: int = -1, italic: bool = False) 
            # ft.setUnderline(True) # 设置下划线
            # ft.setOverline(True) # 设置上划线
            # ft.setCapitalization(QFont.SmallCaps) # 设置大小写
            # ft.setLetterSpacing(QFont.AbsoluteSpacing,10) # 设置 字符间距

            # painter.setFont(ft)
            # painter.drawText(self.rect,Qt.AlignRight,'hello')
            # option=QTextOption(Qt.AlignCenter|Qt.AlignHCenter)
            # QTextOption 设置对齐方式、换行方式以及文本显示方向等效果。
            # painter.drawText(self.rect,'hello',option) #PySide2.QtGui.QPainter.drawText(PySide2.QtCore.QRectF, str, PySide2.QtGui.QTextOption = Default(QTextOption))



        elif self.mType == ItemType.ITEM_PIE:

            painter.save() # 保存 状态
            painter.setBrush(Qt.green) # 改变 状态
            
            painter.drawPie(self.rect,0,45*16) # 0到45°的 扇形
            painter.restore() # 恢复 状态 不然 点击该图元 整个都是黑色

        elif self.mType == ItemType.ITEM_RT_TRIANGLE:
            path=QPainterPath()
            path.moveTo(self.rect.topLeft())
            path.lineTo(self.rect.bottomRight())
            path.lineTo(self.rect.bottomLeft())
            path.closeSubpath()
            painter.drawPath(path)

        elif self.mType ==ItemType.ITEM_WRITE: # 手写图元
            #绘制 外框 
            painter.setPen(self.write_item_pen_wk)
            painter.drawRect(self.rect)
            # 如果 手写 处于 非编辑状态 即 缩放状态 ，
            # 且 宽高等效比 存在 ，
            # 那 就用 等效比 处理 每个点 的 位置，即让图形 实现缩放。
            if not self.write_edit:
                if len(self.write_point_dx_list):
                    for i,write_handle in enumerate(self.write_list):
                        pos_x=self.write_point_dx_list[i]*self.rect.width()+self.rect.center().x()
                        pos_y=self.write_point_dy_list[i]*self.rect.height()+self.rect.center().y()
                        pos=QPointF(pos_x,pos_y)
                        write_handle.set_pos(pos)
                        # write path 节点 跟随 同下标控制节点
                        self.write_path.setElementPositionAt(i,pos_x,pos_y)
                       
                        # 重设 item 的 path对象 
                        self.write_item.setPath(self.write_path) 
            pass

        elif self.mType == ItemType.ITEM_POLYGON: # 封闭多边形
            # 绘制 外框
            painter.setPen(self.polygon_item_pen_wk)
            painter.drawRect(self.rect)

            
            if self.isSelected():
                # 绘制 多边形顶点
                if len(self.polygon_list):
                    for polygon_handle in self.polygon_list:
                        if polygon_handle.hshape==HandleShape.HANDLE_SHAPE_RECT:
                            painter.drawRect(polygon_handle.rect)
                        elif polygon_handle.hshape==HandleShape.HANDLE_SHAPE_CIRCLE:
                            painter.drawEllipse(polygon_handle.rect)

                # 填充  变色
                if self.current_polygon_handle:
                    # print('填充 变色')
                    painter.save()
                    painter.setBrush(Qt.green)
                    painter.drawRect(self.current_polygon_handle.rect)
                    painter.restore()

            # 如果 多边形 处于 非编辑状态 即 缩放状态 ，
            # 且 宽高等效比 存在 ，
            # 那 就用 等效比 处理 每个点 的 位置，即让图形 实现缩放。
            if not self.polygon_edit:
                if len(self.polygon_point_dx_list):
                    for i,polygon_handle in enumerate(self.polygon_list):
                        pos_x=self.polygon_point_dx_list[i]*self.rect.width()+self.rect.center().x()
                        pos_y=self.polygon_point_dy_list[i]*self.rect.height()+self.rect.center().y()
                        pos=QPointF(pos_x,pos_y)
                        polygon_handle.set_pos(pos)
                        # 多边形 path 节点 跟随 同下标控制节点
                        self.polygon_path.setElementPositionAt(i,pos_x,pos_y)
                        # 开始点 就是 结束点
                        if i==0:
                            self.polygon_path.setElementPositionAt(len(self.polygon_list),pos_x,pos_y)
                        # 重设 item 的 path对象 
                        self.polygon_item.setPath(self.polygon_path) 
                    pass
                pass

    
        self.update()

        super().paint(painter,option,widget)
    
    
   
    # 用双击来切换 可编辑 状态
    def mouseDoubleClickEvent(self,evt):
        if evt.buttons() == Qt.LeftButton:
            self.setZValue(self.zValue() + 1)
            # print('左键')
            if self.mType == ItemType.ITEM_WRITE: # 手写
                print('double_click',self.write_edit)
                self.write_edit=not self.write_edit
                if self.write_edit:
                    self.write_item_pen_wk.setStyle(Qt.DotLine) # 绘图区域外框 
                    # 覆盖三大鼠标事件
                    self.mousePressEvent,self.mouseMoveEvent,self.mouseReleaseEvent=self.edit_write()
                    
                else:
                    self.write_item_pen_wk.setStyle(Qt.DashDotDotLine) # 绘图区域外框 
                    # 还原三大鼠标事件
                    self.mousePressEvent,self.mouseMoveEvent,self.mouseReleaseEvent=self.a_press,self.b_move,self.c_release
                    
            elif self.mType == ItemType.ITEM_POLYGON: # 封闭多边形
                print('封闭多边形开关',self.polygon_edit)
                self.polygon_edit = not self.polygon_edit
                if self.polygon_edit:
                    self.polygon_item_pen_wk.setStyle(Qt.DotLine)
                    self.polygon_item_pen_wk.setColor(Qt.red)
                    self.mousePressEvent,self.mouseMoveEvent,self.mouseReleaseEvent=self.edit_polygon()
                    
                else:
                    self.polygon_item_pen_wk.setStyle(Qt.DashDotDotLine)
                    self.polygon_item_pen_wk.setColor(QColor(0x00ffffff)) #设置 笔的颜色 为透明
                    self.mousePressEvent,self.mouseMoveEvent,self.mouseReleaseEvent=self.a_press,self.b_move,self.c_release
    
    def edit_write(self):
        def start(evt):
            if evt.button()==Qt.LeftButton: 
                if self.write_list_onoff:
                    print('开始手写')
                    # 生成控制节点
                    point=Handle(evt.pos(),HandleShape.HANDLE_SHAPE_RECT,HandleType.HANDLE_TYPE_CTRL)
                    # 将该点加入列表
                    self.write_list.append(point)
                    # if len(self.write_list)==1:
                    # 设定 对象 起点
                    self.write_path.moveTo(point.pos) # 场景坐标 evt.scenePos() 路径开始于  1 路径对象起点
                    self.write_item.setPath(self.write_path)
                    
            if evt.button()==Qt.RightButton: # 右键 结束
                
                if self.write_list_onoff:
                    if len(self.write_list):
                        print('关闭绘制,计算等效宽高比')
                        self.write_list_onoff=False
                        for write_handle in self.write_list:
                            dx=(write_handle.pos.x()-self.rect.center().x())/self.rect.width()
                            self.write_point_dx_list.append(dx)
                            dy=(write_handle.pos.y()-self.rect.center().y())/self.rect.height()
                            self.write_point_dy_list.append(dy)
                    else:
                        print('还没开始写，空白')


                else:
                    print('已经关闭手写')

                pass
        
        def process(evt):
            # 开始手写
            if self.write_list_onoff:
                # 生成控制节点
                point=Handle(evt.pos(),HandleShape.HANDLE_SHAPE_RECT,HandleType.HANDLE_TYPE_CTRL)
                # 将该点加入列表
                self.write_list.append(point)

                self.write_path.lineTo(point.pos) #       2 连接到点
                self.write_item.setPath(self.write_path)
                

            pass
        def end(evt):
            if self.write_list_onoff:
                print('还可以继续写')
            else:
                print('已经关闭')
                pass
                

        return [start,process,end]

    def edit_polygon(self):
        def start(evt):
            if evt.button()==Qt.LeftButton:
                for polygon_handle in self.polygon_list:
                    if polygon_handle.rect.contains(evt.pos()):
                        print('点在控制点上，作为当前控制点')
                        self.current_polygon_handle=polygon_handle

            if self.current_polygon_handle:
                # 填充 变色
                print('操作当前控制点')
            else:
                if evt.button()==Qt.LeftButton:
                    if self.polygon_list_onoff:
                        print('添加节点，绘制线条')
                        # print('press',self.polygon_list)
                        # 生成控制节点
                        point=Handle(evt.pos(),HandleShape.HANDLE_SHAPE_RECT,HandleType.HANDLE_TYPE_CTRL)
                        # 将该点加入列表
                        self.polygon_list.append(point)
                        if len(self.polygon_list)==1:
                            # 设定 对象 起点
                            self.polygon_path.moveTo(evt.pos()) # 场景坐标 evt.scenePos() 路径开始于  1 路径对象起点
                            self.polygon_item.setPath(self.polygon_path)
                        else:
                            # 不是起点 就用来连接上一个点
                            self.polygon_path.lineTo(self.polygon_list[-1].pos)
                            self.polygon_item.setPath(self.polygon_path)
                        pass
                
                if evt.button()==Qt.RightButton: # 右键 结束
                    print('关闭绘制，或清空列表')
                    if self.polygon_list_onoff:
                        self.polygon_path.closeSubpath() # 封闭图形 
                        self.polygon_item.setPath(self.polygon_path)
                        if len(self.polygon_list) >= 2:
                            # 关闭 列表
                            self.polygon_list_onoff=False 
                            # 此时 列表 有值 且 不止一个点
                            # 计算 每个 点的 中心 宽高等效比 self.polygon_point_dx,self.polygon_point_dy
                            for polygon_handle in self.polygon_list:
                                dx=(polygon_handle.pos.x()-self.rect.center().x())/self.rect.width()
                                self.polygon_point_dx_list.append(dx)
                                dy=(polygon_handle.pos.y()-self.rect.center().y())/self.rect.height()
                                self.polygon_point_dy_list.append(dy)
                        else:
                            self.polygon_list=[] #清空列表 结束
                    else:
                        print('已经关闭列表')

        def process(evt):
            # 实现 移动节点 线条跟随 的效果
            if self.current_polygon_handle and self.isSelected():
                
                # print('实现移动节点，线条也跟随')

                # 1 设定当前多边形控制节点handle的 新位置
                self.current_polygon_handle.set_pos(evt.pos()) # 但这样只能移动节点 而 多边形 线条 没跟随
                # print('当前点的下标',self.polygon_list.index(self.current_polygon_handle))
                
                # 2  设定 path对象 节点元素的新位置 api : setElementPositionAt(self, i:int, x:float, y:float):
                # 用该api 设置 多边形 节点 的位置 则多边形 的线条 会 跟着移动 ，但 控制节点handle 不动，所以 上面也必须移动
                # 让path对象的 同下标节点 跟随 当前控制节点 handle 的 移动
                x=self.current_polygon_handle.pos.x()
                y=self.current_polygon_handle.pos.y()
                list_index=self.polygon_list.index(self.current_polygon_handle)
                self.polygon_path.setElementPositionAt(list_index,x,y)
                
                # 3 如果是起点 也就是终点
                if self.polygon_list.index(self.current_polygon_handle)==0:
                    # print('0')
                    # 就把 最后一点 也设为 x，y
                    self.polygon_path.setElementPositionAt(len(self.polygon_list),x,y)
                    
                # 4 重设 item 的 path对象 
                self.polygon_item.setPath(self.polygon_path) 

                # 5 重设 该点 的 宽高等效比 
                if len(self.polygon_point_dx_list):
                    
                    dx=(x-self.rect.center().x())/self.rect.width()
                    self.polygon_point_dx_list[list_index]=dx
                    dy=(y-self.rect.center().y())/self.rect.height()
                    self.polygon_point_dy_list[list_index]=dy

                self.update()

            
            

            
        def end(evt):
            # 状态复原
            self.current_polygon_handle=None
            pass
                
                

        return [start,process,end]
    
# 场景
class CustomGraphicsScene(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.setSceneRect(0,0,1024,1024)
        
    
    # def mousePressEvent(self,evt):
    #     print('scene:',evt.pos())
    #     print('scene:',evt.scenePos())
    #     return super().mousePressEvent(evt)

    # def mouseReleaseEvent(self,evt):
    #     print('scene:',evt.pos())
    #     print('scene:',evt.scenePos())
    #     return super().mouseReleaseEvent(evt)

    # 删除 选中的item
    def keyPressEvent(self,evt):
        if evt.key()==Qt.Key_Delete:
            print('scene',self.selectedItems())
            if len(self.selectedItems()):
                for item in self.selectedItems():
                    self.removeItem(item)
        return super().keyPressEvent(evt) # 如果没有继承，就会阻断图元响应keyEvent事件。
    
    pass

# 视图
class CustomGraphicsView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        # self.use_custom=False
        self.use_custom=True 

        if self.use_custom:
            # 使用 自定义图元 customItem
            scene=CustomGraphicsScene()
            self.setScene(scene)

            item =  AppItem((0,0,200,200),ItemType.ITEM_PIXMAP,scene) # 这里的 0,0 是在视图坐标系下。通过后面的setpos 把位置就错开了
            item2 = AppItem((0,0,200,200),ItemType.ITEM_ELLIPSE,scene)
            item3 = AppItem((0,0,200,200),ItemType.ITEM_RECTANGLE,scene)
            item4 = AppItem((0,0,200,200),ItemType.ITEM_TEXT,scene)
            item5 = AppItem((100,100,200,200),ItemType.ITEM_PIE,scene) # 位置效果 是 item5的setpos x+100，y+100.
            item6 = AppItem((0,0,200,200),ItemType.ITEM_LINE,scene) 
            item7 = AppItem((0,0,200,200),ItemType.ITEM_RT_TRIANGLE,scene) 
            item8 = AppItem((0,0,200,200),ItemType.ITEM_WRITE,scene) 
            item9 = AppItem((0,0,200,200),ItemType.ITEM_POLYGON,scene) 

            # 为了避免上面的图形黏在一起，通过setPos把图形错开。 也可以说这种风格：先给大小，再定位置。
            item.setPos(0,100)
            item2.setPos(200,100)
            item3.setPos(400,100)
            item4.setPos(0,300)
            item5.setPos(200,300)
            item6.setPos(400,300)
            item7.setPos(0,500)
            item8.setPos(200,500)
            item9.setPos(400,500)
            
            item.setPixmap(r'D:\pyj\st\study\pyside2_pyqt\pys2\绘图\2-QGraphicsView\QtEditableItems-master\Resources\character_design.jpg')
            
            self.setDragMode(QGraphicsView.RubberBandDrag)# 开启橡皮筋选择
            pass
        else:
            # 使用 现成 的 图元
            self.use_exist_item()

        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate) # 反拖尾
            
    # 使用 现成 的 item 
    def use_exist_item(self):
        # 使用 已有item图元
        self.scene=QGraphicsScene()
        self.scene.setSceneRect(0,0,498,498) # 498 不会有滚动条，499有 因此 边框线可能是1

        # 1 line
        self.line=QGraphicsLineItem()
        self.line.setLine(QLineF(100,30,200,10))

        # 2 rect
        self.rect=QGraphicsRectItem()
        self.rect.setRect(QRectF(100,50,200,50))

        # 3 ellipse
        self.ellipse=QGraphicsEllipseItem(QRectF(100,120,200,50))

        # 4 text
        self.textitem=QGraphicsTextItem('hello view ')
        self.textitem.setDefaultTextColor(QColor(Qt.green))
        self.textitem.setTextInteractionFlags(Qt.TextEditable)
        self.textitem.setPos(100,190)

        # 5 path
        self.path=QGraphicsPathItem()
        self.path_obj=QPainterPath()
        self.path_obj.moveTo(150,250)
        self.path_obj.lineTo(200,300)
        self.path_obj.lineTo(100,300)
        self.path_obj.closeSubpath()
        self.path.setPath(self.path_obj)

        # 6 ProxyWidget
        self.pwgt=QGraphicsProxyWidget()
        self.pwgt.setWidget(QTextEdit('hello proxywidget item'))
        self.pwgt.setGeometry(QRectF(150,300,200,50))



        self.scene.addItem(self.line)
        self.scene.addItem(self.rect)
        self.scene.addItem(self.ellipse)
        self.scene.addItem(self.textitem)
        self.scene.addItem(self.path)
        self.scene.addItem(self.pwgt)

        self.line.setFlags(QGraphicsItem.ItemIsSelectable|QGraphicsItem.ItemIsMovable|QGraphicsItem.ItemIsFocusable)
        self.rect.setFlags(QGraphicsItem.ItemIsSelectable|QGraphicsItem.ItemIsMovable|QGraphicsItem.ItemIsFocusable)
        self.ellipse.setFlags(QGraphicsItem.ItemIsSelectable|QGraphicsItem.ItemIsMovable|QGraphicsItem.ItemIsFocusable)
        self.textitem.setFlags(QGraphicsItem.ItemIsSelectable|QGraphicsItem.ItemIsMovable|QGraphicsItem.ItemIsFocusable)
        self.path.setFlags(QGraphicsItem.ItemIsSelectable|QGraphicsItem.ItemIsMovable|QGraphicsItem.ItemIsFocusable)
        self.pwgt.setFlags(QGraphicsItem.ItemIsSelectable|QGraphicsItem.ItemIsMovable|QGraphicsItem.ItemIsFocusable)

        self.setScene(self.scene)
        pass
    
    # def mousePressEvent(self,evt):
    #     print('view:',evt.pos())
    #     # print('view:',evt.scenePos()) #view 没有场景坐标
    #     return super().mousePressEvent(evt)

    # def mouseReleaseEvent(self,evt):
    #     print('view:',evt.pos())
    #     # print('view:',evt.scenePos()) #view 没有场景坐标
    #     return super().mouseReleaseEvent(evt)

    # def keyPressEvent(self,evt):
    #     if evt.key()==Qt.Key_Delete:
    #         print('view',self.items())
    pass

if __name__ == "__main__":
    app=QApplication([])
    view=CustomGraphicsView()
    view.show()
    app.exec_()
    pass