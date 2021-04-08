from PySide2.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QGraphicsPathItem,QGraphicsView,QGraphicsScene,\
    QColorDialog,QGraphicsItem
from PySide2.QtCore import Slot,QEvent,Qt,Signal,QRectF,QPointF,QSizeF
from PySide2.QtGui import QKeySequence,QPixmap,QPicture,QImage,QPalette,QPainter,QPen,QColor,QPaintEngine,QPainterPath

import os,sys

from ui.Ui_qv1 import Ui_Form

# 自定义基础图元 点
class BPointItem(QGraphicsItem):
    pass


# 自定义场景类
class MyScene(QGraphicsScene):
    # 自定义信号
    shapeChange=Signal()
    def __init__(self):
        super().__init__()
        # 初始化
        self.setSceneRect(0,0,800,800) # 设定场景大小
        self.pen_width=4
        self.pen_color=Qt.black
        # self.pen_color='black'
        # self.background_color=Qt.white
        self.shape='Line' # 形状

        # self.isEarse=False # 橡皮擦 开关
        self.earse_width=4

        # 绘图
        self.handle_action()
    
    def handle_action(self):
        if self.shape=='Line':
            self.mousePressEvent,self.mouseMoveEvent,self.mouseReleaseEvent=self.draw_line()
            
        elif self.shape=='Rect':
            self.mousePressEvent,self.mouseMoveEvent,self.mouseReleaseEvent=self.draw_rect()

        elif self.shape=='Earse':
            self.mousePressEvent,self.mouseMoveEvent,self.mouseReleaseEvent=self.earse()
        pass

    def pen_setting(self,pen):
        # if self.isEarse:
        #     # 取回来
        #     self.pen_color=self.last_color
        #     self.pen_width=self.last_width
        #     # 关闭开关
        #     self.isEarse=False
            
       
        pen.setWidth(self.pen_width)
        pen.setColor(QColor(self.pen_color))


    def draw_line(self):
            
        def start(evt):
            if evt.button()==Qt.LeftButton: # 左键触发  AttributeError: 'MyScene' object has no attribute 'painter_path'
                # 定义 图元 graphict_item  路径图元
                self.graphics_path_item=QGraphicsPathItem()

                # 设置 图元 笔
                self.graphics_path_item.setFlags(QGraphicsItem.ItemIsMovable|QGraphicsItem.ItemIsSelectable)
                pen=self.graphics_path_item.pen()
                self.pen_setting(pen)
                self.graphics_path_item.setPen(pen) # 一定要记得设回来

                # 为场景添加图元
                self.addItem(self.graphics_path_item)

                # 定义 对象 painter_path 路径对象
                self.painter_path=QPainterPath()
                # 设定 对象 起点
                self.painter_path.moveTo(evt.scenePos()) # 场景坐标 evt.scenePos() 路径开始于  1 路径对象起点
               
                
                pass
        
        def process(evt):
            if self.painter_path:
                self.painter_path.lineTo(evt.scenePos()) #                 2 连接到点

                # 为路径图元设定路径对象
                self.graphics_path_item.setPath(self.painter_path)
                # print('2')

            pass
        def end(evt):
            if self.painter_path:
                self.painter_path.closeSubpath()    # 路径对象              3  结束路径
                # self.painter_path.closePath() # 没有这个功能
                # print('3')
            pass

        return [start,process,end]
        pass
    

    def earse(self): #与 手写 draw_line() 是一样的 就是 下面笔色和笔宽不同
            
        def start(evt):
            if evt.button()==Qt.LeftButton: # 左键触发  AttributeError: 'MyScene' object has no attribute 'painter_path'
                # 定义 图元 graphict_item  路径图元
                self.graphics_path_item=QGraphicsPathItem()
                # 设置 图元 笔
                pen=self.graphics_path_item.pen()

                #--------- 与 手写 draw_line() 是一样的 就是 下面笔色和笔宽不同 下面两行 其余都一致
                pen.setWidth(self.earse_width)
                pen.setColor(QColor(self.background_color))
                # ----------------------------------------------------------------------------
               
                self.graphics_path_item.setPen(pen) # 一定要记得设回来
                
                # 为场景添加图元
                self.addItem(self.graphics_path_item)

                # 定义 对象 painter_path 路径对象
                self.painter_path=QPainterPath()
                # 设定 对象 起点
                self.painter_path.moveTo(evt.scenePos()) # 场景坐标 evt.scenePos() 路径开始于  1 路径对象起点
                pass
        
        def process(evt):
            if self.painter_path:
                self.painter_path.lineTo(evt.scenePos()) #                 2 连接到点

                # 为路径图元设定路径对象
                self.graphics_path_item.setPath(self.painter_path)
               

            pass
        def end(evt):
            if self.painter_path:
                self.painter_path.closeSubpath()    # 路径对象              3  结束路径
               

        return [start,process,end]
        pass

    def draw_rect(self):
        def start(evt):
            if evt.button()==Qt.LeftButton: # 左键触发  AttributeError: 'MyScene' object has no attribute 'painter_path'
                # 定义 图元 graphict_item  路径图元
                self.graphics_path_item=QGraphicsPathItem()
                # 设置 图元 笔
                pen=self.graphics_path_item.pen()
                self.pen_setting(pen)
                self.graphics_path_item.setPen(pen) # 一定要记得设回来

                # 为场景添加图元
                self.addItem(self.graphics_path_item)

                # 定义 对象 painter_path 路径对象
                self.painter_path=QPainterPath()
                # 设定 对象 起点
                # self.painter_path.moveTo(evt.scenePos()) # 场景坐标 evt.scenePos() 路径开始于  1 路径对象起点
                self.startpoint=evt.scenePos()
                
                pass
        
        def process(evt):
            if self.painter_path:
                w=evt.scenePos().x()-self.startpoint.x()
                h=evt.scenePos().y()-self.startpoint.y()
                rs=QSizeF(w,h)
                rect_f=QRectF(self.startpoint,rs)
                self.painter_path.addRect(rect_f) #                 2 增加矩形到路径

                # 为路径图元设定路径对象
                self.graphics_path_item.setPath(self.painter_path)
                # print('2')

            pass
        def end(evt):
            if self.painter_path:
                self.painter_path.closeSubpath()    # 路径对象              3  结束路径
                # self.painter_path.closePath() # 没有这个功能
                # print('3')
            pass

        return [start,process,end]

'''    
    def mousePressEvent(self,evt):
        # print(type(evt)) # <class 'PySide2.QtWidgets.QGraphicsSceneMouseEvent'>
        # print(dir(evt))
        if evt.button()==Qt.LeftButton: # 左键触发  AttributeError: 'MyScene' object has no attribute 'painter_path'
            # 定义 图元 graphict_item  路径图元
            self.graphics_path_item=QGraphicsPathItem()
            # 设置 图元 笔
            pen=self.graphics_path_item.pen()
            pen.setWidth(self.pen_width)
            pen.setColor(self.pen_color)
            self.graphics_path_item.setPen(pen) # 一定要记得设回来

            # 为场景添加图元
            self.addItem(self.graphics_path_item)

            # 定义 对象 painter_path 路径对象
            self.painter_path=QPainterPath()
            # 设定 对象 起点
            self.painter_path.moveTo(evt.scenePos()) # 场景坐标 evt.scenePos() 路径开始于  1 路径对象起点

            
            
            # print('1')
            
        pass
    def mouseMoveEvent(self,evt):
        if self.painter_path:
            self.painter_path.lineTo(evt.scenePos()) #                 2 连接到点

            # 为路径图元设定路径对象
            self.graphics_path_item.setPath(self.painter_path)
            # print('2')
        pass
    def mouseReleaseEvent(self,evt):
        if self.painter_path:
            self.painter_path.closeSubpath()    # 路径对象              3  结束路径
            # self.painter_path.closePath() # 没有这个功能
            # print('3')
        pass
'''
    

    

class Qv1Ui(QWidget,Ui_Form):
    def __init__(self,parent=None):
        super().__init__(parent) 
        # 导入界面类setupUi函数，填入 self 参数作为父类。
        self.setupUi(self)

        # 实例化场景
        self.scene=MyScene() 

        self.tkness_sld.setValue(self.scene.pen_width)
        self.hw_btn
        # 为视图设置场景
        self.handwrite_grv.setScene(self.scene) 
        # 画板 防止鼠标跟踪
        if self.handwrite_grv.hasMouseTracking():
            self.handwrite_grv.setMouseTracking(False)

        self.rect_btn
        
    
    # 按钮 槽
    @Slot()
    def on_hw_btn_clicked(self):
        print('Line')
        self.scene.shape='Line'
        self.state_lb.setText(self.hw_btn.text())
        self.tkness_sld.setValue(self.scene.pen_width)
        self.scene.handle_action()

    @Slot()
    def on_rect_btn_clicked(self):
        print('Rect')
        self.scene.shape='Rect'
        self.state_lb.setText(self.rect_btn.text())
        self.scene.handle_action()

    # 橡皮擦
    @Slot()
    def on_earse_btn_clicked(self):
        print('Earse')
        self.scene.shape='Earse'
        self.state_lb.setText(self.earse_btn.text())
        self.tkness_sld.setValue(self.scene.earse_width)
        self.scene.handle_action()
        
        

    # 改变笔色
    @Slot()
    def on_pen_color_btn_clicked(self):
        # self.state_lb.setText(self.pen_color_btn.text())
        color=QColorDialog(self)
        color.show()
        def change_color(col):
            self.scene.pen_color=col
            # print(col)

        # 用 colorSelected 改变
        # color.colorSelected.connect(change_color)

        # 用 currentColorChanged 实时改变
        color.setOption(QColorDialog.NoButtons) # 实时改变 就不要按钮了
        color.currentColorChanged.connect(change_color)
    
    # 改变粗细
    @Slot(int)
    def on_tkness_sld_valueChanged(self,val):
        if self.state_lb.text()==self.earse_btn.text(): #如果状态是橡皮 就调节橡皮
            self.scene.earse_width=val
        else:
            self.scene.pen_width=val

    # 清除
    @Slot()
    def on_clear_btn_clicked(self):
        self.state_lb.setText(self.clear_btn.text())
        self.scene.clear()

if __name__ == "__main__":
    app=QApplication([]) 
    wd=Qv1Ui()
    wd.show()
    app.exec_()