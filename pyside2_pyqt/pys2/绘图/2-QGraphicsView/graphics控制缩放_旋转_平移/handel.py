from PySide2.QtWidgets import QApplication,QGraphicsScene,QGraphicsView,QGraphicsItem,QGraphicsObject,QGraphicsPathItem,\
    QVBoxLayout,QHBoxLayout,QAbstractGraphicsShapeItem
from PySide2.QtCore import Slot,Signal,Qt,QPointF,QLineF,QRect,QRectF,QSize,QUuid,QEvent,QSettings,QObject
from PySide2.QtGui import QPainter,QPainterPath,QPen,QBrush,QTransform,QPixmap

from enum import Enum # 枚举类
'''
知识点：
1 枚举类
    导入枚举模块可以是Enum(枚举值可以是任意类型)，也可以是IntEnum(枚举值只能是整型)；
    枚举的特点：
        1 枚举类中不能存在相同的标签名
        2 枚举是可迭代的
        3 不同的枚举标签可以对应相同的值，但它们都会被视为该值对应第一个标签的别名
        4 如果要限制定义枚举时，不能定义相同值的成员。可以使用装饰器@unique【要导入unique模块】
        5 枚举成员之间不能进行大小比较，可进行等值(==)和同一性(is)比较
        6 枚举成员为单例，不可实例化，不可更改

2 QSettings
    QSettings 用法总结（很好用） https://blog.csdn.net/komtao520/article/details/79636665

    用户对应用程序经常有这样的要求：要求它能记住它的settings，比如窗口大小，位置，一些别的设置，
    还有一个经常用的，就是recent files，等等这些都可以通过Qsettings来实现。

    我们知道，这些settings一般都是存在系统里的，比如windows一般都写在系统注册表或者写INI文件，
    mac系统一般都在XML文件里，那么按照一般的标准来说，许多应用程序是用INI文件来实现的。
    而Qsettings就是提供了一种方便的方法来存储和恢复应用程序的settings。

    QSettings的API是基于Qvariant，Qvariant是一种数据类型的集合，它包含了大部分通常的Qt数据类型，比如QString，QRec，QImage，等等。
    当我们创建一个Qsettings的对象时，我们需要传递给它两个参数，第一个是你公司或者组织的名称，第二个是你的应用程序的名称。比如：

        Settings = Qsettings(“MySoft”,”QtPad”)

        公司名称：MySoft，程序名称：QtPad

    假如我们在应用程序中多次要用到Qsettings，为了简单其间，我们可以在主程序中先如下声明。

        QtCore.QCoreApplication.setOrganizationName("MySoft")

        QtCore.QCoreApplication.setOrganizationDomain("mysoft.com")

        QtCore.QCoreApplication.setApplicationName("QtPad")

    当然前提是已经from PyQt4 import QtCore

    然后在应用程序的任何地方想要声明一个Qsettings类型的变量，便不需要书写两个参数了，直接用settings = Qsettings即可。

    那么如何用它来保持应用程序的settings信息呢？我们以字典数据类型与之类比，它也有key，以及对应的value。比如下面例子：

        settings = Qsettings(“MySoft”,”QtPad”)

        Mainwindow = QmainWindow()
            settings.setValue(“pos”,QVariant(Mainwindow.pos())

        settings.setValue(“size”,QVariant(Mainwindow.size())

    上面两句就是把当前窗口的位置，和大小两个信息记录到了settings中，其中的key就是”pos”和”size”两个Qstring类型，而它所对应的值就是QVariant类型的。
    当然如果我们要写的key已在settings中存在的话，则会覆盖原来的值，写入新值。

    如何读取Qsettings里的内容呢？如下：

        Pos = settngs.value(“pos”).toPoint()

        Size = settings.value(“size”).toSize()

    当然如果key所对应的value是int型的，也可toInt(),如果没有我们要找的key，则会返回一个null QVariant如果用toInt的话会得到0。

    那么实际应用中我们一般会如下：

        pos= settings.value("pos", QVariant(QPoint(200, 200))).toPoint()

        size= settings.value("size", QVariant(QSize(400, 400))).toSize()

        self.resize(size)

        self.move(pos)

    意思是，如果settings里有以前存下的(用setValue设置的)pos和size的值，则读取，如果没有，不会返回null，
    而会使用我们给它的起始值——default value——即应用程序第一次运行时的情况。

 
    注意：因为QVariant是不会提供所有数据类型的转化的，比如有toInt(),toPoint(),toSize(),但是却没有对Qcolor，Qimage和Qpixmap等数据类型的转化，
    此时我们可以用QVariant.value（），具体参看QVariant模块说明。

    下面看看如何在应用程序中使用：

        import sys

        from PyQt4.QtCore import *

        from PyQt4.QtGui import *

        class MainWindow(QMainWindow):

            def __init__(self):

                QMainWindow.__init__(self)

                ...

                self.readSettings()

                ...

            def readSettings(self):

                settings = Qsettings(“MySoft”,”QtPad”)

                pos=settings.value("pos",QVariant(QPoint(200,200))).toPoint()

                size=settings.value("size",QVariant(QSize(400,400))).toSize()

                self.resize(size)

                self.move(pos)

            def writeSettings(self):

                settings = Qsettings(“MySoft”,”QtPad”)

                settings.setValue("pos", QVariant(self.pos()))

                settings.setValue("size", QVariant(self.size()))

            def closeEvent(self,event):

                if self.maybeSave():

                    self.writeSettings()

                    event.accept()

                else:

                    event.ignore()

    上面是一般应用程序的应用方法。

 
    下面再看一些Qsettings里常用的metho：

        Qsettings.annKeys(self)返回所有的key，以list的形式

        Qsettings.applicationName(self)返回应用程序名称

        Qsettings.clear(self) 清楚此settings里的内容

        Bool Qsettings.contains(self,key)返回真，如果存在名为key的key

        Qsettings.remove(self, keyname)清楚key及其所对应的value

        Qsetting.fileName() 返回写入注册表地址，或者INI文件路径

    等等，请参看帮助文档。

 

    我们可以探索一下，这些settings在应用程序关闭以后到底存到了什么地方呢？

    我们可以在上面的程序中的writeSettings中，后面加一句话：

        Print Settings.fileName()

    这个在windows下，默认Qsettings会打印出这个程序的系统注册表所在地：

    这个结果是：HKEY_CURRENT_USERSoftwareMySoftQtPad

    如下图：



    由此我们可以看出，这个writesettings其实就是个写注册表的过程。

    当然，我们也可以不写注册表，我们写ini文件：

        ettings = QSettings("./QtPad.ini", QSettings.IniFormat)

        ettings.setValue("pos", QVariant(self.pos()))

        ettings.setValue("size", QVariant(self.size()))

    就会在当前文件夹下产生一个QtPad.ini文件，打开后文件内容为：

        [General]

        pos=@Point(200 200)

        size=@Size(400 400)



    特别说明：

    Qtcreater中的"./"的目录指的是build dir的路径！！如图红色部分，必须去掉！！！否则可能不能生成.ini文件！！！


3 在可能改变QGraphicsItem大小或者形状的时候，QGraphicsItem子类函数中要先调用prepareGeometryChange()，实现预加载; *****
    以保证 QGraphicsScene 中的索引是最新的，否则容易产生意想不到的错误，甚至崩溃，
    该功能放置的位置不当（比如放在boundingRect中），也会导致崩溃，
    一般放在 itemChange 图元变化函数中，用'if change == QGraphicsItem.ItemSelectedChange:' 选择切换开关 控制。 

4 拖尾和场景刷新：
  在mouseReleseEvent事件中加入 场景刷新 ，不能解决缩放时拖尾，可以让拖尾现象在鼠标释放时消失。
  在mouseMoveEvent事件中加入 场景刷新 解决缩放拖尾的现象。


'''

# 定义全局 settings
settings=QSettings(r'D:\pyj\st\study\pyside2_pyqt\pys2\绘图\graphics控制\settings.ini',QSettings.IniFormat)
settings.setValue("drawing/gridSize",10)
settings.setValue("drawing/hanleSize",15)
settings.setValue("drawing/gridEnabled",False) # 网格打开之后，一跳一跳的,说明有了效果， 而只有设置了QGraphicsItem.ItemSendsGeometryChanges,覆盖的函数self.itemChange()函数才能接收QGraphicsItem.ItemPositionChange位置变化信息

# 控制点 外形类别
class HandleShape(Enum):
    HANDLE_SHAPE_RECT='HANDLE_SHAPE_RECT'
    HANDLE_SHAPE_CIRCLE='HANDLE_SHAPE_CIRCLE'
    HANDLE_SHAPE_TRIANGLE='HANDLE_SHAPE_TRIANGLE'
# 控制点 类别
class HandleType(Enum):
    HANDLE_TYPE_TOPLEFT='HANDLE_TYPE_TOPLEFT'
    HANDLE_TYPE_TOP='HANDLE_TYPE_TOP'
    HANDLE_TYPE_TOPRIGHT='HANDLE_TYPE_TOPRIGHT'
    HANDLE_TYPE_LEFT='HANDLE_TYPE_LEFT'
    HANDLE_TYPE_RIGHT='HANDLE_TYPE_RIGHT'
    HANDLE_TYPE_BOTTOMLEFT='HANDLE_TYPE_BOTTOMLEFT'
    HANDLE_TYPE_BOTTOM='HANDLE_TYPE_BOTTOM'
    HANDLE_TYPE_BOTTOMRIGHT='HANDLE_TYPE_BOTTOMRIGHT'
    HANDLE_TYPE_ROTATE='HANDLE_TYPE_ROTATE'
    HANDLE_TYPE_ORIGIN='HANDLE_TYPE_ORIGIN'
    HANDLE_TYPE_CTRL='HANDLE_TYPE_CTRL'

# 控制点
class Handle():
    def __init__(self,pos,size,hshape,htype):
        
        # 下面的顺序不能错
        # 尺寸 size int
        self.setSize(size)

        # 矩形 外框 
        self.rect=QRectF(pos.x()-size/2,pos.y()-size/2,size,size)
        
        # 更新位置pos和区域rect
        self.setPos(pos)
        
        # 外形 HandleShape 是自定义的 外形 枚举类 HandleShape
        self.setShape(hshape)

        # 类型 HandleType 是自定义的 类型 枚举类 HandleType 
        self.setType(htype)
        

    # 更新位置pos和区域rect
    def setPos(self,pos):
        if isinstance(pos,QPointF):
            # 重设大小和位置
            self.rect.setRect(pos.x()-self.size/2,pos.y()-self.size/2,self.size,self.size)
            self.pos=pos

    def setSize(self,size):
        if isinstance(size,int):
            self.size=size

    def setType(self,htype):
        if isinstance(htype,HandleType):
            self.htype=htype
        
    def setShape(self,hshape):
        if isinstance(hshape,HandleShape):
            self.hshape=hshape

    def boundingRect(self):
        return self.rect


# 带控制点图元基础单元
class BaseItem(QGraphicsItem):
    def __init__(self,rect=None,scene=None,parent=None):
        super().__init__(parent)
        id=QUuid.createUuid()
        self.id=id.toString()
        self.setFlags(QGraphicsItem.ItemIsMovable|QGraphicsItem.ItemIsSelectable|QGraphicsItem.ItemSendsGeometryChanges|QGraphicsItem.ItemIsFocusable)
        # 原来作者使用了 QGraphicsItem.ItemIsMovable 来实现平移，导致 缩放时 mouseMoveEvent 不能被继承；
        # 如果继承，则就不能实现缩放，或带来莫名错误。***所以，原作者在缩放和旋转后并没有继承该事件，而是在移动时继承了该事件。
       
        # 解决：
            # 不能使用 QGraphicsItem.ItemIsMovable 来实现平移；
            # 必须在mouseMoveEvent中手动实现平移， 这就能在缩放、旋转、平移后继承mouseMoveEvent事件；
            # 带来的新问题 ： 不能多选后，同时移动。
        # self.setFlags(QGraphicsItem.ItemIsSelectable|QGraphicsItem.ItemSendsGeometryChanges|QGraphicsItem.ItemIsFocusable)
        
        # 一个bug：
            # 现象：
                # 图元在放大到新区域后，图元新区域部分怎么都不能被选择；
                # 图元老区域部分可以选择，选择后，轻轻移动，原来不能被选择的新区域又可以选择；
            # 解决：
                # 在可能改变QGraphicsItem大小或者形状的时候，
                # QGraphicsItem子类函数中要先调用prepareGeometryChange()，实现预加载;
                    # 在itemChange(change,val)函数中，打开itemselectchange开关，实现
                    #  if change == QGraphicsItem.ItemSelectedChange: 
                        
                        # self.prepareGeometryChange() 

        

        if rect:
            self.rect=QRectF(rect[0],rect[1],rect[2],rect[3])  # 外框
        else:
            self.rect=None
        # self.origin=QPointF(0,0)  # 原点 初值
        self.origin=None  # 原点 初值
        
        # 绘制外框开关
        self.isDrawBoundingRect=True
        # 当前控制句柄
        self.CurrentHandle=None
        # 控制句柄列表
        self.Handles=[]
        self.scene=None
        # scene=QGraphicsScene()
        if scene:
            self.scene=scene
            self.scene.addItem(self)

        # 最小尺寸
        self.rect_min_width=30
        self.rect_min_height=30

        # 控制最小尺寸 的 固定边
        self.current_fix_v_edge=None # control_min_width 控制最小宽度
        self.current_fix_h_edge=None # control_min_height 控制最小高度

        # 旋转中心到框架中心 的宽高 等效距离  设定初值为0
        self.rect_width_dx=0
        self.rect_height_dy=0

        # self.isRefulsh=False
        
    def setId(self,id):
        if isinstance(id,str):
            self.id=id

    def setDrawBoundingRect(self,val):
        if isinstance(val,bool):
            self.isDrawBoundingRect=bool

    # 确定绘图区域
    def boundingRect(self):
        # if self.isSelected:
            # self.prepareGeometryChange() # 这个预加载程序 写在这里 会引起程序崩溃
        if self.isDrawBoundingRect:
        
            # 调整边界矩形外框以包含控制柄，以便单击时检测到它们。
            size=settings.value("drawing/hanleSize",10)
            # 调整的是左上和右下点，
            # 左上往左（-size/2）、上（-size/2 - 50）调，50 是 rotate旋转句柄到top句柄的连线；
            # 右下往右（size/2）、下（size/2）调。
            return self.rect.adjusted(-size/2,-size/2 - 50,size/2,size/2) # 选择区域为 调整后的 self.rect 的副本
           
        else:
            return self.rect
     

    '''
        QRect QRectF 的 adjust()及adjusted() 

        void adjust(dx1,dy1,dx2,dy2)的功能在于 微调位置 修改这个变量本身

        QRect adjusted(dx1,dy1,dx2,dy2)的功能在于 微调位置 不修改变量本身，而是   返回一个调整过后的QRect

        dx1,dy1调整矩形左上角点位置
        dx2,dy2调整矩形右下角点位置
        QRect rect1 = QRect(0,0,10,20);
        rect1.adjust(5,5,-1,-2);//rect1的区域(5,5,9,18)
        auto rect2 = rect1.adjusted(-2,-1,5,-3);//rect1依然为(5,5,9,18) rect2为(3,4,14,15)
    
    '''
    
    # 精确的确定 可选择的区域  否则 可选择区域 就是 boundingRect 返回的绘图区域
    def shape(self):
        path=QPainterPath()
        path.setFillRule(Qt.WindingFill) # 该路径填充很重要，如果注释掉，则小句柄handle路径和大外框rect路径相交的部分（交集），就不能被选择。
        # windingFill 可以理解为相交路径的并集。 

        # handle=Handle()
        # handle.hshape
        # handle.boundingRect()
        if self.isSelected():
            # 从句柄列表中取出句柄 定义路径对象
            for handle in self.Handles:
                if handle.hshape==HandleShape.HANDLE_SHAPE_CIRCLE or handle.hshape==HandleShape.HANDLE_SHAPE_RECT:
                    rect=handle.boundingRect()
                    path.addRect(rect)     #句柄路径
                
                if handle.hshape==HandleShape.HANDLE_SHAPE_TRIANGLE:   
                    break   

        path.addRect(self.rect) #外框路径
        return path
      
    
    # 绘制 外框 和 句柄
    def paint(self, painter, option, widget):
        # painter=QPainter()
        if self.isSelected() and self.isDrawBoundingRect:
            # 绘制选择矩形外框
            pen=QPen(Qt.green)
            painter.setPen(pen)
            painter.drawRect(self.rect)
            # painter.drawRect(self.boundingRect()) # 这个 是 绘制区域 

            # 绘制句柄
            # 顶点 和 旋转点
            p1=None
            p2=None
            # 从句柄列表中取出句柄 绘制
            for handle in self.Handles:
                # handle=Handle()
                if handle.htype == HandleType.HANDLE_TYPE_ROTATE: # 旋转中心
                    p1=handle.pos
                if handle.htype == HandleType.HANDLE_TYPE_TOP: # 顶点
                    p2=handle.pos

                if handle.htype == HandleType.HANDLE_TYPE_CTRL:
                    painter.save() # 先保存状态
                    painter.setPen(QPen(Qt.green))
                    painter.setBackground(QBrush(Qt.green))
                    painter.drawRect(handle.boundingRect())
                    painter.restore() # 恢复保存的状态
                else:
                    # 其他类型 按外形 分类 绘制
                    if handle.hshape == HandleShape.HANDLE_SHAPE_RECT:
                        painter.drawRect(handle.boundingRect())
                    
                    elif handle.hshape == HandleShape.HANDLE_SHAPE_CIRCLE:
                        painter.drawEllipse(handle.boundingRect())

                    elif handle.hshape == HandleShape.HANDLE_SHAPE_TRIANGLE:
                        break
            
            painter.drawLine(p1,p2) # 连接 顶点和旋转中心
            # painter.drawPoint(self.origin) # 绘制原点
            
            

        pass

    # 创建各个句柄 放入句柄列表
    def createHandles(self):
        size=settings.value('drawing/hanleSize',10)

        self.origin=self.rect.center()
        left=QPointF(self.rect.left(),self.rect.top()+self.rect.height()/2)
        right=QPointF(self.rect.right(),self.rect.top()+self.rect.height()/2)
        top=QPointF(self.rect.left()+self.rect.width()/2,self.rect.top())
        bottom=QPointF(self.rect.left()+self.rect.width()/2,self.rect.bottom())

        rotate=QPointF(top.x(),top.y()-50)


        self.Handles.append(Handle(self.rect.topLeft(),size,HandleShape.HANDLE_SHAPE_RECT,HandleType.HANDLE_TYPE_TOPLEFT))
        self.Handles.append(Handle(top,size,HandleShape.HANDLE_SHAPE_RECT,HandleType.HANDLE_TYPE_TOP))
        self.Handles.append(Handle(self.rect.topRight(),size,HandleShape.HANDLE_SHAPE_RECT,HandleType.HANDLE_TYPE_TOPRIGHT))
        self.Handles.append(Handle(left,size,HandleShape.HANDLE_SHAPE_RECT,HandleType.HANDLE_TYPE_LEFT))
        self.Handles.append(Handle(right,size,HandleShape.HANDLE_SHAPE_RECT,HandleType.HANDLE_TYPE_RIGHT))
        self.Handles.append(Handle(self.rect.bottomLeft(),size,HandleShape.HANDLE_SHAPE_RECT,HandleType.HANDLE_TYPE_BOTTOMLEFT))
        self.Handles.append(Handle(bottom,size,HandleShape.HANDLE_SHAPE_RECT,HandleType.HANDLE_TYPE_BOTTOM))
        self.Handles.append(Handle(self.rect.bottomRight(),size,HandleShape.HANDLE_SHAPE_RECT,HandleType.HANDLE_TYPE_BOTTOMRIGHT))
        
        self.Handles.append(Handle(rotate,size,HandleShape.HANDLE_SHAPE_CIRCLE,HandleType.HANDLE_TYPE_ROTATE)) # 旋转句柄
        self.Handles.append(Handle(self.origin,size,HandleShape.HANDLE_SHAPE_CIRCLE,HandleType.HANDLE_TYPE_ORIGIN)) # 原点
        pass
    
    # 三大鼠标事件
    # 确定选中了哪个句柄
    def mousePressEvent(self,evt):
        # print('item:',evt.pos())
        # print('item:',evt.scenePos())
        
        if evt.buttons() == Qt.LeftButton:
            # 检测单击了哪个句柄，赋值给当前句柄
            for handle in self.Handles:
                # handle=Handle()
                if handle.boundingRect().contains(evt.pos()):
                    self.CurrentHandle=handle
            # 计算 旋转中心到框架中心 的 宽 高 等效距离
            if self.origin:
                self.define_dx_dy()
        # 处理光标和固定边
        self.handle_cusor_fix_edge()
        # print('self.current_fix_v_edge',self.current_fix_v_edge)
                
        return super().mousePressEvent(evt)

    # 计算 旋转中心到框架中心 的 宽 高 等效距离
    def define_dx_dy(self):
        # self.origin到self.rect.center的x、y宽高等效距离dx dy在缩放过程中是不变的，常量。
        self.rect_width_dx=(self.origin.x()-self.rect.center().x())/self.rect.width()
        self.rect_height_dy=(self.origin.y()-self.rect.center().y())/self.rect.height()

        # 如果没有 平移 原点（即 self.CurrentHandle.htype == HandleType.HANDLE_TYPE_ORIGIN:）
        # 则origin到center的x、y等效距离dx dy为零 ，因为 自定义的原点self.origin 和 默认的原点 也就是图元的中心点self.rect.center()
        # 重合。实际上 self.origin 应该 命名为 旋转中心 self.rotate_center 更妥贴
        # 而 类型 HandleType.HANDLE_TYPE_ORIGIN 应该 定义为 HandleType.HANDLE_TYPE_ROTATE_CENTER
        # 只有平移了原点之后，dx 和 dy 才不为零

        # print(f'self.origin:{self.origin},self.rect.center:{self.rect.center()}')
        # print(f'dx:{dx},dy:{dy},self.rect.width{self.rect.width()}')


    # 处理光标和固定边
    def handle_cusor_fix_edge(self):
        if self.CurrentHandle:
            # 左右拉伸缩放
            if self.CurrentHandle.htype == HandleType.HANDLE_TYPE_LEFT:
                self.setCursor(Qt.SizeHorCursor)
                self.current_fix_v_edge=self.rect.right()

            elif self.CurrentHandle.htype == HandleType.HANDLE_TYPE_RIGHT:
                self.setCursor(Qt.SizeHorCursor)
                self.current_fix_v_edge=self.rect.left()

            # 上下拉伸缩放
            elif self.CurrentHandle.htype == HandleType.HANDLE_TYPE_TOP:
                self.setCursor(Qt.SizeVerCursor)
                self.current_fix_h_edge=self.rect.bottom()


            elif self.CurrentHandle.htype == HandleType.HANDLE_TYPE_BOTTOM:
                self.setCursor(Qt.SizeVerCursor)
                self.current_fix_h_edge=self.rect.top()

            # 左上 右上 左下 右下 拉伸缩放
            elif self.CurrentHandle.htype == HandleType.HANDLE_TYPE_TOPLEFT:
                self.setCursor(Qt.SizeFDiagCursor)
                self.current_fix_v_edge=self.rect.right()
                self.current_fix_h_edge=self.rect.bottom()


            elif self.CurrentHandle.htype == HandleType.HANDLE_TYPE_TOPRIGHT:
                self.setCursor(Qt.SizeBDiagCursor)
                self.current_fix_v_edge=self.rect.left()
                self.current_fix_h_edge=self.rect.bottom()

            elif self.CurrentHandle.htype == HandleType.HANDLE_TYPE_BOTTOMRIGHT:
                self.setCursor(Qt.SizeFDiagCursor)
                self.current_fix_v_edge=self.rect.left()
                self.current_fix_h_edge=self.rect.top()

            elif self.CurrentHandle.htype == HandleType.HANDLE_TYPE_BOTTOMLEFT:
                self.setCursor(Qt.SizeBDiagCursor)
                self.current_fix_v_edge=self.rect.right()
                self.current_fix_h_edge=self.rect.top()

            #  绕 旋转中心 self.origin 旋转
            elif self.CurrentHandle.htype == HandleType.HANDLE_TYPE_ROTATE:
                self.setCursor(Qt.PointingHandCursor) # 手指
                pass

            # 平移 原点 旋转中心
            elif self.CurrentHandle.htype == HandleType.HANDLE_TYPE_ORIGIN:
                self.setCursor(Qt.CrossCursor) # 十字
                pass


            elif self.CurrentHandle.htype == HandleType.HANDLE_TYPE_CTRL:
                self.setCursor(Qt.SizeAllCursor)
                pass

        else:
            self.setCursor(Qt.SizeAllCursor)

        pass
    
    # 根据 选中的句柄 确定 缩放 旋转 移动的结果
    def mouseMoveEvent(self,evt):
        if evt.buttons() == Qt.LeftButton:
            if self.CurrentHandle:
                # 缩放或旋转
                
                # 左右拉伸缩放
                
                if self.CurrentHandle.htype == HandleType.HANDLE_TYPE_LEFT:
                    # 固定右端
                    # 移动左端
                    if evt.pos().x()<=self.current_fix_v_edge-self.rect_min_width:
                        # 设置外框的左侧
                        self.rect.setLeft(evt.pos().x())
                    else:
                        # print(self.rect.width())
                        self.rect.setLeft(self.current_fix_v_edge-self.rect_min_width)
                        
                    # self.rect.center() 会自动更新
                    # self.origin必须手动更新 依据dx dy 与 移动中心同步移动
                    # 更新原点 的 x
                    self.origin.setX((self.rect_width_dx*self.rect.width())+self.rect.center().x())
                
                       
                elif self.CurrentHandle.htype == HandleType.HANDLE_TYPE_RIGHT:
                    # 固定左端
                    # 移动右端
                    if evt.pos().x()>=self.current_fix_v_edge+self.rect_min_width:
                        # 设置外框的左侧
                        self.rect.setRight(evt.pos().x())
                    else:
                        # print(self.rect.width())
                        self.rect.setRight(self.current_fix_v_edge+self.rect_min_width)

                    self.origin.setX((self.rect_width_dx*self.rect.width())+self.rect.center().x())
               

                # 上下拉伸缩放
                elif self.CurrentHandle.htype == HandleType.HANDLE_TYPE_TOP:
                    # 固定下端
                    # 移动上端
                    if evt.pos().y()<=self.current_fix_h_edge-self.rect_min_height:
                        # 设置外框的顶部
                        self.rect.setTop(evt.pos().y())
                    else:
                        self.rect.setTop(self.current_fix_h_edge-self.rect_min_height)

                    # 更新原点 的 y
                    self.origin.setY((self.rect_height_dy*self.rect.height())+self.rect.center().y())

                elif self.CurrentHandle.htype == HandleType.HANDLE_TYPE_BOTTOM:
                    # 固定上端
                    # 移动下端
                    if evt.pos().y()>=self.current_fix_h_edge+self.rect_min_height:
                        # 设置外框的顶部
                        self.rect.setBottom(evt.pos().y())
                    else:
                        self.rect.setBottom(self.current_fix_h_edge+self.rect_min_height)

                    # 更新原点 的 y
                    self.origin.setY((self.rect_height_dy*self.rect.height())+self.rect.center().y())
                    
                # 左上 右上 左下 右下 拉伸缩放
                elif self.CurrentHandle.htype == HandleType.HANDLE_TYPE_TOPLEFT:

                    # 固定右端
                    # 移动左端
                    if evt.pos().x()<=self.current_fix_v_edge-self.rect_min_width:
                        # 设置外框的左侧
                        x=evt.pos().x()
                    else:
                        # print(self.rect.width())
                        x=self.current_fix_v_edge-self.rect_min_width

                    # 固定下端
                    # 移动上端
                    if evt.pos().y()<=self.current_fix_h_edge-self.rect_min_height:
                        # 设置外框的顶部
                        y=evt.pos().y()
                    else:
                        y=self.current_fix_h_edge-self.rect_min_height

                    # 设置 外框的 左上顶点
                    self.rect.setTopLeft(QPointF(x,y))
                    # 更新 原点 的 x y
                    self.origin.setX((self.rect_width_dx*self.rect.width())+self.rect.center().x())
                    self.origin.setY((self.rect_height_dy*self.rect.height())+self.rect.center().y())

                elif self.CurrentHandle.htype == HandleType.HANDLE_TYPE_TOPRIGHT:
                    # 固定左端
                    # 移动右端
                    if evt.pos().x()>=self.current_fix_v_edge+self.rect_min_width:
                        # 设置外框的左侧
                        x=evt.pos().x()
                    else:
                        # print(self.rect.width())
                        x=self.current_fix_v_edge+self.rect_min_width

                    # 固定下端
                    # 移动上端
                    if evt.pos().y()<=self.current_fix_h_edge-self.rect_min_height:
                        # 设置外框的顶部
                        y=evt.pos().y()
                    else:
                        y=self.current_fix_h_edge-self.rect_min_height

                    self.rect.setTopRight(QPointF(x,y))
                    self.origin.setX((self.rect_width_dx*self.rect.width())+self.rect.center().x())
                    self.origin.setY((self.rect_height_dy*self.rect.height())+self.rect.center().y())

                elif self.CurrentHandle.htype == HandleType.HANDLE_TYPE_BOTTOMRIGHT:
                    # 固定左端
                    # 移动右端
                    if evt.pos().x()>=self.current_fix_v_edge+self.rect_min_width:
                        # 设置外框的左侧
                        x=evt.pos().x()
                    else:
                        # print(self.rect.width())
                        x=self.current_fix_v_edge+self.rect_min_width

                    # 固定上端
                    # 移动下端
                    if evt.pos().y()>=self.current_fix_h_edge+self.rect_min_height:
                        # 设置外框的顶部
                        y=evt.pos().y()
                    else:
                        y=self.current_fix_h_edge+self.rect_min_height

                    self.rect.setBottomRight(QPointF(x,y))
                    self.origin.setX((self.rect_width_dx*self.rect.width())+self.rect.center().x())
                    self.origin.setY((self.rect_height_dy*self.rect.height())+self.rect.center().y())

                elif self.CurrentHandle.htype == HandleType.HANDLE_TYPE_BOTTOMLEFT:
                    # 固定右端
                    # 移动左端
                    if evt.pos().x()<=self.current_fix_v_edge-self.rect_min_width:
                        # 设置外框的左侧
                        x=evt.pos().x()
                    else:
                        # print(self.rect.width())
                        x=self.current_fix_v_edge-self.rect_min_width

                    # 固定上端
                    # 移动下端
                    if evt.pos().y()>=self.current_fix_h_edge+self.rect_min_height:
                        # 设置外框的顶部
                        y=evt.pos().y()
                    else:
                        y=self.current_fix_h_edge+self.rect_min_height

                    self.rect.setBottomLeft(QPointF(x,y))
                    
                    self.origin.setX((self.rect_width_dx*self.rect.width())+self.rect.center().x())
                    self.origin.setY((self.rect_height_dy*self.rect.height())+self.rect.center().y())

                #  绕 旋转中心 self.origin 旋转
                elif self.CurrentHandle.htype == HandleType.HANDLE_TYPE_ROTATE:
                    # 坐标 变换
                    # self.setTransform(QTransform().translate(self.origin.x(),self.origin.y()).rotate(-QLineF(evt.scenePos(),mapToScene(self.origin)).angle() + QLineF(evt.lastScenePos(),mapToScene(self.origin)).angle()).translate(-self.origin.x(),-self.origin.y()),True)
                    # self.setTransform(QTransform().translate(self.origin.x(),self.origin.y()).rotate(-QLineF(evt.scenePos(),self.mapToScene(self.origin)).angle()+ QLineF(evt.lastScenePos(),self.mapToScene(self.origin)).angle()).translate(-self.origin.x(),-self.origin.y()),True)
                    self.setTransform(QTransform().translate(self.origin.x(),self.origin.y()).rotate(-QLineF(evt.pos(),self.origin).angle()+ QLineF(evt.lastPos(),self.origin).angle()).translate(-self.origin.x(),-self.origin.y()),True)
                    
                    # 图元 坐标变换 
                    # 实际上 图元的旋转 就是 旋转图元坐标轴
                    # self.setTransform(变换矩阵matrix:PySide2.QtGui.QTransform,布尔值 bool)
                    # 1. 原点平移到 self.origin 
                        # QTransform().translate(self.origin.x(),self.origin.y()) 坐标  默认坐标原点是左上
                    # 2. 绕 self.origin 旋转  坐标轴
                        # .rotate(-QLineF(evt.scenePos(),self.mapToScene(self.origin)).angle()+ QLineF(evt.lastScenePos(),self.mapToScene(self.origin)).angle())
                            # 起点和原点连线 的角度 QLineF(evt.lastScenePos(),self.mapToScene(self.origin)).angle()  
                            # 减去 终点和原点连线 的角度 -QLineF(evt.scenePos(),self.mapToScene(self.origin)).angle() 
                    # 3. 原点 还原 回到 旋转后的 左上
                        # 移动了多少 就还原多少 .translate(-self.origin.x(),-self.origin.y())
                    # 下一次旋转时，又来一遍123循环

                # 平移 原点 旋转中心
                elif self.CurrentHandle.htype == HandleType.HANDLE_TYPE_ORIGIN:
                    # 平移
                    self.CurrentHandle.setPos(evt.pos())
                    # 更新 原点 旋转中心
                    self.origin=self.CurrentHandle.pos
                elif self.CurrentHandle.htype == HandleType.HANDLE_TYPE_CTRL:
                    self.CurrentHandle.setPos(evt.pos())

                

                # 更新 handle pos
                left=QPointF(self.rect.left(),self.rect.top()+self.rect.height()/2)
                right=QPointF(self.rect.right(),self.rect.top()+self.rect.height()/2)
                top=QPointF(self.rect.left()+self.rect.width()/2,self.rect.top())
                bottom=QPointF(self.rect.left()+self.rect.width()/2,self.rect.bottom())
                rotate=QPointF(top.x(),top.y()-50)
                for handle in self.Handles:
                    # handle=Handle()
                    if handle.htype == HandleType.HANDLE_TYPE_LEFT:
                        # 更新handle的位置pos和区域rect
                        # print('leftpos',handle.pos)
                        handle.setPos(left)
                    elif handle.htype == HandleType.HANDLE_TYPE_RIGHT:
                        handle.setPos(right)
                    elif handle.htype == HandleType.HANDLE_TYPE_TOP:
                        handle.setPos(top)
                    elif handle.htype == HandleType.HANDLE_TYPE_BOTTOM:
                        handle.setPos(bottom)
                    elif handle.htype == HandleType.HANDLE_TYPE_TOPLEFT:
                        handle.setPos(self.rect.topLeft())
                    elif handle.htype == HandleType.HANDLE_TYPE_TOPRIGHT:
                        handle.setPos(self.rect.topRight())
                    elif handle.htype == HandleType.HANDLE_TYPE_BOTTOMLEFT:
                        handle.setPos(self.rect.bottomLeft())
                    elif handle.htype == HandleType.HANDLE_TYPE_BOTTOMRIGHT:
                        handle.setPos(self.rect.bottomRight())
                    elif handle.htype == HandleType.HANDLE_TYPE_ROTATE:
                        handle.setPos(rotate)
                    elif handle.htype == HandleType.HANDLE_TYPE_ORIGIN:
                        handle.setPos(self.origin)
                        pass
                    else:
                        break
                    
            else:
                # 平移方案一 打开 QGraphicsItem.ItemIsMovable 开关 
                # 用继承实现平移 
                return super().mouseMoveEvent(evt)
                # pass
                # 平移 方案二 关闭 QGraphicsItem.ItemIsMovable 开关  带来的问题 多选后 不能同时移动
                # 实现手动平移
                # print('move')
                # last_pos=evt.lastPos() # 上次的图元坐标
                # current_pos=evt.pos()  # 当前的图元坐标
                # o_pos=self.pos() # 图元的图元坐标 不动 就是(0,0) 即图元原点 ，动了 就是 以该图元原点为基点的坐标 不是视图和场景坐标

                # print(f'last_pos：{last_pos}, current_pos：{current_pos}, o_pos：{o_pos}')

                # 计算偏差 加上 图元坐标，即得到 新的图元坐标
                # updated_cursor_x=current_pos.x()-last_pos.x()+o_pos.x()
                # updated_cursor_y=current_pos.y()-last_pos.y()+o_pos.y()
                # 用计算的图元坐标 更新位置
                # self.setPos(QPointF(updated_cursor_x,updated_cursor_y))

            self.update()
            self.scene.update() # 手动刷新 场景 没有就会出现拖尾 *****

        # 手动平移后： 缩放、旋转、平移后都可以继承   ***** 
            
        # return super().mouseMoveEvent(evt)
           

    # 将当前句柄复位归零 为None
    def mouseReleaseEvent(self,evt):
        self.CurrentHandle=None
        self.current_fix_v_edge=None
        self.current_fix_h_edge=None
        self.setCursor(Qt.ArrowCursor)
        # self.scene.update()
        return super().mouseReleaseEvent(evt)
        
    # 键盘事件
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
    
        elif evt.key()==Qt.Key_R: # 添加旋转  每次绕 旋转中心self.origin 旋转10°
            self.setTransform(QTransform().translate(self.origin.x(),self.origin.y()).rotate(10).translate(-self.origin.x(),-self.origin.y()),True)

        elif evt.key()==Qt.Key_O: # 将 self.origin 旋转中心 复位到 图形中心 self.rect.center()
            # 取值
            self.origin=self.rect.center()
            # 更新位置
            for handle in self.Handles:
                if handle.htype == HandleType.HANDLE_TYPE_ORIGIN:
                    handle.setPos(self.origin)
            self.scene.update() # 解决 复位后 原来原点图形有残留 场景刷新后 就没有了残留的原点
        else:
            super().keyPressEvent(evt)

    # 当项目状态的某些部分发生了变化 该函数会响应 用来进行 
    # 1 在可能改变QGraphicsItem大小或者形状的时候，先调用prepareGeometryChange()，完成预加载;
    # 2 网格grid 控制 当前无用 当网格打开时才有用

    def itemChange(self,change,value):
        # 在可能改变QGraphicsItem大小或者形状的时候，
        # QGraphicsItem子类函数中要先调用prepareGeometryChange()，完成预加载;
        if change == QGraphicsItem.ItemSelectedChange: 
            # print('ItemSelectedChange')
            self.prepareGeometryChange()  # 预加载 否则 点击图元放大后的新区域 图元没反应*****
            # 根据Qt文档,
                # 在更改项目的边界之前调用此函数,以使QGraphicsScene的索引保持最新,
                # 如果需要,则prepareGeometryChange()将调用update().
            # 无论以任何方式更改 item 的几何形状，必须首先调用prepareGeometryChange()，以保证 QGraphicsScene 中的索引是最新的。

        if change == QGraphicsItem.ItemPositionChange:
            # ItemPositionChange用于通知所属QGraphicsItem的位置即将发生变化，而value的值即为QGraphicsItem将来的位置坐标
            # 根据需要，更改value，使得QGraphicsItem到达新的位置 newPos 在网格点上
            
            gridSize = settings.value("drawing/gridSize")
            gridEnabled = settings.value("drawing/gridEnabled")

            newPos = value
            if gridEnabled:# 当网格打开 移动一跳一跳的 非常卡顿 并且 右移 和 下移 快捷键 失效
                # 去掉余数 就是grid的整数倍
                if newPos.x()%gridSize != 0:
                    x = newPos.x() - newPos.x()%gridSize
                    newPos.setX(x)
                
                if newPos.y()%gridSize != 0:
                    y = newPos.y() - newPos.y()%gridSize
                    newPos.setY(y)
                
            return newPos

        return super().itemChange(change,value)
       

# 图元类别
class ItemType(Enum):
    ITEM_LINE=0
    ITEM_CIRCLE=1
    ITEM_TRIANGLE=2
    ITEM_RECTANGLE=3
    ITEM_ELLIPSE=4
    ITEM_PIXMAP=5
    pass

# 应用图元 继承自 基础图元
class BaseShapeItem(BaseItem):
    def __init__(self,rect,itemType,scene=None,parent=None):
        super().__init__(rect,scene,parent)
        self.rect=QRectF(rect[0],rect[1],rect[2],rect[3])
        self.mType=itemType
        self.mPixmap=None
        self.createHandles()

    def boundingRect(self): # 注释掉 没有什么影响

        return super().boundingRect()

    def paint(self,painter,option,widget):
        # painter=QPainter()
        # 图形矫正
        if self.rect.left()>self.rect.right():
            left=self.rect.right()
            right=self.rect.left()
            self.rect.setLeft(left)
            self.rect.setRight(right)
        if self.rect.top()>self.rect.bottom():
            top=self.rect.bottom()
            botttom=self.rect.top()
            self.rect.setTop(top)
            self.rect.setBottom(botttom)
        painter.setRenderHint(QPainter.Antialiasing,True) # 反锯齿

        # 根据类型 绘制图形
        if self.mType ==ItemType.ITEM_RECTANGLE:
            painter.drawRect(self.rect)

        elif self.mType == ItemType.ITEM_ELLIPSE:
            painter.drawEllipse(self.rect)

        elif self.mType == ItemType.ITEM_LINE:
            painter.drawLine(self.rect.topLeft(),self.rect.bottomRight())

        elif self.mType == ItemType.ITEM_PIXMAP:
            painter.drawPixmap(self.rect.toRect(),self.mPixmap) # 不能时QRectF 必须是 QRect 所以用QRectF.toRect() 进行转换

        self.update()

        super().paint(painter,option,widget)
        
        pass

   
    def setPixmap(self,path):
        self.mPixmap=QPixmap(path)
        pass
    pass

class EditAbleItems():
    pass

# 线段类型
class SegmentType(Enum):
    SEGEMENT_LINE=0
    SEGEMENT_CURVE=1

# 线段
class Segment():
    def __init__(self,stype,handle):
        if isinstance(stype,SegmentType):
            self.stype=stype
        else:
            self.stype=None
        if isinstance(handle,Handle):
            self.handle=handle
        else:
            self.handle=None

class ComplexShapeItem(BaseItem):
    def __init__(self,scene,parent=None):
        super().__init__(scene,parent)
        self.ShapeHandles=[]
        self.Segments=[]
        self.setDrawBoundingRect(False)
    
    # def boundingRect(self):
    #     return 
    '''
    def paint(self,painter,option,widget):
        path=QPainterPath()
        for i,handle in enumerate(self.Handles):
            if i==0:
                path.moveTo(handle.pos)
            else:
                path.lineTo(handle.pos)
                
        path.moveTo(self.Handles[0].pos)# 开始于 句柄列表的 第一个添加点
        for(int i=0 ; i < mHandles.size() ; i++) {
            if(i == 0) {
                path.moveTo(mHandles.at(0)->pos());
            } else {
                //: Check segment type. 检查 段 类型。
                //Create a cubic. 建立一个 cubic 曲线
                //path.quadTo();
                QLineF line1(path.currentPosition(),mHandles.at(i)->pos());
                QLineF line2(mHandles.at(i+1)->pos(),mHandles.at(i+2)->pos());
                path.cubicTo(mHandles.at(i)->pos(),mHandles.at(i+1)->pos(),mHandles.at(i+2)->pos());
                if(this->isSelected()) {
                    //Draw the handle lines. 绘制 线的句柄
                    painter->drawLine(line1);
                    painter->drawLine(line2);
                }
                //qDebug()<<path.elementCount();
                //Skip used points.
                i = i+2;
            }

        }
        painter->drawPath(path);
        BaseItem::paint(painter,option,widget);
        pass
    def addPoint(self,pointf,stype):
        pass
    def recalculateRect(self):
        pass
    def mouseReleaseEvent(self,evt):
        pass
    pass
    '''

class EditorScene(QGraphicsScene):
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

    pass

class GraphicsView(QGraphicsView):
    def __init__(self):
        super().__init__()
        scene=EditorScene()
        self.setScene(scene)
        # rect (0,0,200,200) 绘图区域
        item = BaseShapeItem((0,0,200,200),ItemType.ITEM_PIXMAP,scene) # 这里的 0,0 是在图元坐标系下。
        item2 = BaseShapeItem((0,0,200,200),ItemType.ITEM_ELLIPSE,scene)
        item3 = BaseShapeItem((0,0,200,200),ItemType.ITEM_RECTANGLE,scene)
        item.setPos(0,100)#这里的pos是视图坐标
        item2.setPos(200,100)
        item3.setPos(400,100)
        item.setPixmap(r'D:\pyj\st\study\pyside2_pyqt\pys2\绘图\2-QGraphicsView\QtEditableItems-master\Resources\character_design.jpg')
        # self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate) # 反拖尾
        # self.setViewportUpdateMode(QGraphicsView.MinimalViewportUpdate) # 反拖尾 无效
        self.setDragMode(QGraphicsView.RubberBandDrag)# 开启橡皮筋选择
    

    # def mousePressEvent(self,evt):
    #     print('view:',evt.pos())
    #     # print('view:',evt.scenePos()) #view 没有场景坐标
    #     return super().mousePressEvent(evt)

    # def mouseReleaseEvent(self,evt):
    #     print('view:',evt.pos())
    #     # print('view:',evt.scenePos()) #view 没有场景坐标
    #     return super().mouseReleaseEvent(evt)
    pass

if __name__ == "__main__":
    app=QApplication([])
    view=GraphicsView()
    view.show()
    app.exec_()