from PySide2.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QGraphicsItem,QGraphicsView,QGraphicsScene,QVBoxLayout

from PySide2.QtCore import Qt,Signal,Slot
from PySide2.QtGui import QPainter,QPen,QBrush




class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QGraphicsView学习1')
        self.setGeometry(1000,400,500,500)
        # 创建graphicsview视图
        self.creat_graphicsview()

    def creat_graphicsview(self):
        # 定义场景
        self.scene=QGraphicsScene() # 场景坐标原点 默认 在视图的中心
        # self.scene.setSceneRect(-200,-200,400,400) # 这样写 场景坐标原点 就是 视图中心 就是默认的效果
        # self.scene.setSceneRect(0,0,400,400) # 这样写 场景坐标原点 和 视图坐标原点 重合 改变了场景坐标的原点
        # 定义视图
        self.g_view=QGraphicsView() # 使用布局 后面设置场景
        # self.g_view=QGraphicsView(self.scene) # 放入场景  使用布局
        # self.g_view=QGraphicsView(self.scene,self) # 放入场景 和 父元素
        # self.g_view.setGeometry(0,0,350,350)

        # 使用布局
        v_layout=QVBoxLayout(self)
        v_layout.addWidget(self.g_view)

        # 窗口的缩放 resizEvent 是以 场景坐标为中心 进行缩放 场景坐标的原点在场景的中心，当前就是视图的中心，视图的坐标原点依然是左上
        
        # 单独设置场景
        self.g_view.setScene(self.scene)

        # 定义笔 轮廓
        self.pen_black=QPen(Qt.black)
        self.pen_blue=QPen(Qt.blue)
        # 定义刷 填充
        self.brush_green=QBrush(Qt.green)
        self.brush_red=QBrush(Qt.red)

        # 添加图元
        self.add_item()

    def add_item(self):
        # 用场景添加图元 有返回值 是各种图元 item 
        # (x,y,w,h,pen,brush) 
        # 操作都是以 场景坐标 添加 
        # 场景坐标的的原点在中心，就是当前视图的中心，视图的坐标原点依然是左上
        ellipse=self.scene.addEllipse(20,20,200,200,self.pen_black,self.brush_red) # 椭圆 -> PySide2.QtWidgets.QGraphicsEllipseItem
        rect=self.scene.addRect(-100,-100,200,200,self.pen_blue,self.brush_green) # 矩形 -> PySide2.QtWidgets.QGraphicsRectItem

        # 设定图元item属性 可移动 可选择
        ellipse.setFlags(QGraphicsItem.ItemIsMovable|QGraphicsItem.ItemIsSelectable)
        rect.setFlags(QGraphicsItem.ItemIsMovable|QGraphicsItem.ItemIsSelectable)

        

if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()