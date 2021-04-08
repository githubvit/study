"""
Qt-for-Python (PySide2) GUI drawing framework
"""

import sys
import math
from PySide2 import QtGui, QtCore, QtWidgets


__author__ = 'Andreas Ennemoser'
__copyright__ = '2018'
__credits__ = []
__license__ = "MIT"
__version__ = "0.3"
__email__ = 'andreas.ennemoser@aon.at'
__status__ = 'Prototype'


class GraphicsItem(QtWidgets.QGraphicsItem):
    """
     From the QT docs:
     To write your own graphics item, you first create a subclass
     of QGraphicsItem, and then start by implementing its two pure
     virtual public functions: boundingRect(), which returns an estimate
     of the area painted by the item, and paint(),
     which implements the actual painting.

     从QT文档：

     要编写自己的图形项，首先要创建一个子类
     
     然后从实现它的两个纯
     
     虚拟公共函数：boundingRect（），它返回一个估计值
     
     项目绘制的区域的，和paint（），
     
     实现了真正的绘画。
    """
    # call constructor of GraphicsItem
    def __init__(self, rect, pen, brush, tooltip='No tip here', parent=None):
        # call constructor of QGraphicsItem 调用QGraphicsItem的构造函数
        super(GraphicsItem, self).__init__()

        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, False)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, True)

        self.setAcceptHoverEvents(True)

        self.pen = pen
        pw = self.pen.widthF()
        self.brush = QtGui.QBrush(QtCore.Qt.blue)
        self.brush = brush
        self.setToolTip(tooltip)
        self.parent = parent

        self.rect = QtCore.QRectF(rect[0], rect[1], rect[2], rect[3])
        self.focusrect = QtCore.QRectF(rect[0]-pw/2, rect[1]-pw/2,
                rect[2]+pw, rect[3]+pw) # 聚焦框的中心 到笔宽的中心，外形宽高都要加上笔宽

    def mousePressEvent(self, event):
        self.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        # set item as topmost in stack 将点击的item设置为堆栈中的最顶层
        self.setZValue(self.parent.items()[0].zValue() + 1)
        self.setSelected(True)
        # propagate event
        QtWidgets.QGraphicsItem.mousePressEvent(self, event)

    def mouseReleaseEvent(self, event):
        self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        # propagate event
        QtWidgets.QGraphicsItem.mouseReleaseEvent(self, event)

    def mouseMoveEvent(self, event):
        # propagate event
        QtWidgets.QGraphicsItem.mouseMoveEvent(self, event)

    def boundingRect(self):
        # bounding box rect shall be set to the bounds of the item. Due to the
        # line thickness this rect is bigger than the rect of the ellipse or rect, etc.
        # 边界框rect应设置为项目的边界。由于线的厚度，这个矩形比椭圆或矩形等的矩形大。
        return self.focusrect

    def paint(self, painter, option, widget):
        painter.setBrush(self.brush)
        painter.setPen(self.pen)
        painter.drawEllipse(self.rect)
        if self.isSelected():
            self.drawFocusRect(painter)
            self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)

    def drawFocusRect(self, painter):
        self.focusbrush = QtGui.QBrush()
        self.focuspen = QtGui.QPen(QtCore.Qt.DotLine)
        self.focuspen.setColor(QtCore.Qt.black)
        self.focuspen.setWidthF(1.5)
        painter.setBrush(self.focusbrush)
        painter.setPen(self.focuspen)
        painter.drawRect(self.focusrect)

    def hoverEnterEvent(self, event):
        self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pen.setStyle(QtCore.Qt.DotLine)
        # propagate event
        QtWidgets.QGraphicsItem.hoverEnterEvent(self, event)

    def hoverLeaveEvent(self, event):
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pen.setStyle(QtCore.Qt.SolidLine)
        # propagate event
        QtWidgets.QGraphicsItem.hoverLeaveEvent(self, event)


class GraphicsScene (QtWidgets.QGraphicsScene):
    # call constructor of GraphicsScene
    def __init__ (self, parent=None):
        # call constructor of QGraphicsScene
        super(GraphicsScene, self).__init__(parent)

        self.parent = parent
        self.setSceneRect(-200, -200, 400, 400)

    def mousePressEvent(self, event):
        self.clearSelection()
        # propagate event
        super(GraphicsScene, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        # propagate event
        super(GraphicsScene, self).mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        super(GraphicsScene, self).mouseMoveEvent(event)

    def addGraphicsItem(self, rect, pw, pc, bc, tooltip):
        pen = QtGui.QPen(QtCore.Qt.SolidLine)
        pen.setColor(QtGui.QColor(pc[0], pc[1], pc[2], 255))
        pen.setWidth(pw)
        brush = QtGui.QBrush(QtGui.QColor(bc[0], bc[1], bc[2], 255))
        self.item = GraphicsItem(rect, pen, brush, tooltip, self)
        self.parent.scene.addItem(self.item)


class GraphicsView (QtWidgets.QGraphicsView):
    # call constructor of GraphicsView
    def __init__(self, parent=None):
        # call constructor of QGraphicsView 调用QGraphicsView的构造函数
        super(GraphicsView, self).__init__(parent)

        # set QGraphicsView attributes 设置QGraphicsView属性
        self.setRenderHints(QtGui.QPainter.Antialiasing |
                QtGui.QPainter.HighQualityAntialiasing)
        self.setViewportUpdateMode(QtWidgets.QGraphicsView.FullViewportUpdate)
        self.setResizeAnchor(QtWidgets.QGraphicsView.AnchorViewCenter)
        self.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        # save home position 保存原始位置
        self.home = self.matrix()

        # set background style 设置背景样式
        self.viewstyle = \
            'background-color:QLinearGradient(  \
            x1: 0.0, y1: 0.0, x2: 0.0, y2: 1.0,  \
            stop: 0.3 white,  \
            stop: 1.0 blue); \
            '
        self.setStyleSheet(self.viewstyle)

    def keyPressEvent(self, event):
        key = event.key()

        if key == QtCore.Qt.Key_Escape:
            sys.exit(QtGui.qApp.quit())
        elif key == QtCore.Qt.Key_Plus:  # 放大
            self.scaleView(1.2)
        elif key == QtCore.Qt.Key_Minus: # 缩小 
            self.scaleView(1 / 1.2)
        elif key == QtCore.Qt.Key_Home:  # 还原
            self.setMatrix(self.home)
        else:
            # propagate event
            super(GraphicsView, self).keyPressEvent(event) # 覆盖

    def wheelEvent(self, event):
        self.scaleView(math.pow(2.0, -event.delta() / 500.0))
        # propagate event
        super(GraphicsView, self).wheelEvent(event)

    def scaleView(self, factor):
        f = self.matrix().scale(factor, factor). \
                    mapRect(QtCore.QRectF(0, 0, 1, 1)).width()
        if f < 0.05 or f > 50:
            return
        self.scale(factor, factor)


class CentralWidget(QtWidgets.QWidget):
    # call constructor of CentralWidget
    def __init__(self, parent=None):
        # call constructor of QWidget QWidget的调用构造函数
        super(CentralWidget, self).__init__(parent)

        self.parent = parent

        # create toolbox widget for left side of splitter 为拆分器左侧创建工具箱小部件
        self.toolBox = QtWidgets.QToolBox()

        self.item1 = self.toolBox.addItem(QtWidgets.QWidget(), "Item 1")
        self.item2 = self.toolBox.addItem(QtWidgets.QWidget(), "Item 2")
        self.item3 = self.toolBox.addItem(QtWidgets.QWidget(), "Item 3")
        self.item4 = self.toolBox.addItem(QtWidgets.QWidget(), "Item 4")
        self.toolBox.setItemToolTip(0, 'Mal sehn ... aus Item 1')
        icon = QtGui.QIcon('icons/document-open.png')
        self.toolBox.setItemIcon(2, icon)
        self.toolBox.setCurrentIndex(3)

        # split main window horizontally into two panes 将主窗口水平拆分为两个窗格
        self.splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        self.splitter.addWidget(self.toolBox)
        self.splitter.addWidget(self.parent.view)
        self.splitter.setStretchFactor(0, 1) # 0 ... left pane, 1 ... fraction of split
        self.splitter.setStretchFactor(1, 4) # 1 ... right pane, 4 ... fraction of split

        # put splitter in a layout box 将拆分器放在布局框中
        
        hbox = QtWidgets.QHBoxLayout(self)
        hbox.addWidget(self.splitter)
        self.setLayout(hbox)
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Cleanlooks'))


class MainWindow(QtWidgets.QMainWindow):
    # call constructor of MainWindow
    def __init__(self, parent=None):
        # call constructor of QMainWindow
        super(MainWindow, self).__init__(parent)

        self.view = GraphicsView(self)
        self.scene = GraphicsScene(self)
        # set the scene
        self.view.setScene(self.scene)

        # add items to the scene
        self.scene.addGraphicsItem((0, 0, 250, 250), 8.0, (255, 0, 0), (0, 0, 255), 'My first item')
        self.scene.addGraphicsItem((-250, -250, 300, 200), 4.0, (0, 0, 0), (255, 0, 100), 'My 2nd item')
        self.scene.addGraphicsItem((200, -200, 200, 200), 10.0, (0, 0, 255), (0, 255, 100), 'My 3rd item')

        # set central widget for the application
        self.setCentralWidget(CentralWidget(self))

        # setup user interface and menus
        self.initUI()

    def initUI(self):

        # window size, position and title
        self.setGeometry(600, 100, 1200, 900)
        self.setWindowTitle('Qt for Python (PySide2) Graphics View Framework')
        self.show()

        # create a status bar
        self.statusbar = self.statusBar()
        self.statusbar.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.statusbar.showMessage('Ready.')
        self.statusbarstyle = 'background-color:rgb(200,200,200); color:black'
        self.statusbar.setStyleSheet(self.statusbarstyle)

        # define extension to be filtered in file dialogs
        self.filefilter = \
            'Airfoil mesh files (*.txt *.msh);;Airfoil contour files (*.dat)'

        # create a menu bar
        menubar = self.menuBar()

        # populate menus
        fileMenu = menubar.addMenu('&File')

        icon = QtGui.QIcon('icons/document-open.png')
        actionOpen = QtWidgets.QAction(icon, '&Open', self, shortcut='CTRL+o',
                statusTip='Open file ...', triggered=self.onOpen)
        f_open = fileMenu.addAction(actionOpen)

        icon = QtGui.QIcon('icons/document-save.png')
        actionSave = QtWidgets.QAction(icon, '&Save', self, shortcut='CTRL+s',
                statusTip='Save file ...', triggered=self.onSave)
        f_save = fileMenu.addAction(actionSave)

        icon = QtGui.QIcon('icons/system-log-out.png')
        actionExit = QtWidgets.QAction(icon, '&Exit', self, shortcut='CTRL+x',
                statusTip='Exit application', triggered=self.onExit)
        exit = fileMenu.addAction(actionExit)

        toolMenu = menubar.addMenu('&Tools')
        prevMenu = toolMenu.addMenu('Preferences')
        calcMenu = toolMenu.addMenu('Calculator')

        helpMenu = menubar.addMenu('&Help')
        icon = QtGui.QIcon('icons/info.png')

        # self.aboutQtAct = QtWidgets.QAction("About &Qt", self,
        #         statusTip="Show the Qt library's About box",
        #         triggered=QtGui.qApp.aboutQt)
        # qtabout = helpMenu.addAction(self.aboutQtAct)

        actionAbout = QtWidgets.QAction(icon, '&About', self, shortcut='',
                statusTip='Information about the software and its licensing.',
                triggered=self.onAbout)
        about = helpMenu.addAction(actionAbout)

    def onOpen(self):
        (fname, thefilter) = QtWidgets.QFileDialog.getOpenFileName(self,
                            'Open file', '.', filter=self.filefilter)
        if not fname: return
        with open(fname, 'r') as f:
            self.data = f.read()

    def onSave(self):
        (fname, thefilter) = QtWidgets.QFileDialog.getSaveFileName(self,
                            'Save file', '.', filter=self.filefilter)
        if not fname: return
        with open(fname, 'w') as f:
            f.write('This test worked for me ...')

    def onExit(self):
        sys.exit(QtGui.qApp.quit())

    def onAbout(self):
        QtWidgets.QMessageBox.about(self, "About Graphics View Framework",
                "Qt-for-Python (PySide2) Graphics View Framework is used as "
                "a starting point for GUIs with a scene containing items"
                "and a specific, modifiable view on them (zoom, pan, etc.).<br><br>"
                "License: " + __license__ + " <br><br>"
                "Copyright (C) 2018 Andreas Ennemoser.")


def main():
    app = QtWidgets.QApplication(sys.argv)
    # app.setWindowIcon(QtGui.QIcon('icons/some_icon.png'))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()