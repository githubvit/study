
'''
34章 图形视图框架

图形视图框架主要包含三个类：
    QGraphicsItem图元类、QGraphicsScene场景类和QGraphicsView视图类。
    简单一句话来概括下三者的关系就是：图元放在场景上，场景内容通过视图来显示。

下面我们来一一进行讲解。

34.1 QGraphicsItem图元类 

    图元可以是文本、图片，规则几何图形或者任意自定义图形。该类已经提供了一些标准的图元，比如：

        直线图元QGraphicsLineItem
        矩形图元QGraphicsRectItem
        椭圆图元QGraphicsEllipseItem
        图片图元QGraphicsPixmapItem
        文本图元QGraphicsTextItem
        路径图元QGraphicsPathItem

    想必通过名称也可以知道这些图元是用来干嘛的，我们通过以下代码来演示如何使用：

'''
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QColor, QPainterPath
from PyQt5.QtWidgets import QApplication, QGraphicsItem, QGraphicsLineItem, QGraphicsRectItem, QGraphicsEllipseItem, \
                            QGraphicsPixmapItem, QGraphicsTextItem, QGraphicsPathItem, QGraphicsScene, QGraphicsView


class Demo(QGraphicsView):
    def __init__(self):
        super(Demo, self).__init__()
        # 1
        self.resize(300, 300)

        # 2
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 300, 300)

        # 3
        self.line = QGraphicsLineItem()
        self.line.setLine(100, 10, 200, 10)
        # self.line.setLine(QLineF(100, 10, 200, 10))

        # 4
        self.rect = QGraphicsRectItem()
        self.rect.setRect(100, 30, 100, 30)
        # self.rect.setRect(QRectF(100, 30, 100, 30))

        # 5
        self.ellipse = QGraphicsEllipseItem()
        self.ellipse.setRect(100, 80, 100, 20)
        # self.ellipse.setRect(QRectF(100, 80, 100, 20))

        # 6
        self.pic = QGraphicsPixmapItem()
        self.pic.setPixmap(QPixmap(r'D:\pyj\st\study\pyside2_pyqt\pys2\rose.png').scaled(60, 60))
        self.pic.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable) # 图元可以移动和被选
        self.pic.setOffset(100, 120) # 图片位置 左上角
        # self.pic.setOffset(QPointF(100, 120))

        # 7
        self.text1 = QGraphicsTextItem()
        self.text1.setPlainText('Hello PyQt5') # 不可编辑
        self.text1.setDefaultTextColor(QColor(66, 222, 88)) 
        self.text1.setPos(100, 180)

        self.text2 = QGraphicsTextItem()
        self.text2.setPlainText('Hello World')
        self.text2.setTextInteractionFlags(Qt.TextEditorInteraction) # 文本编辑 交互方式  可编辑
        self.text2.setPos(100, 200)

        self.text3 = QGraphicsTextItem()
        self.text3.setHtml('<a href="https://baidu.com">百度</a>')
        self.text3.setOpenExternalLinks(True) # 点击可以打开外部链接 不设置不能打开
        self.text3.setTextInteractionFlags(Qt.TextBrowserInteraction) # 富文本 交互方式 不可编辑 
        self.text3.setPos(100, 220)

        # 8
        self.path = QGraphicsPathItem()

        self.tri_path = QPainterPath() # 路径对象
        self.tri_path.moveTo(100, 250) # 开始于
        self.tri_path.lineTo(130, 290) # 连接到
        self.tri_path.lineTo(100, 290) # 连接到
        self.tri_path.lineTo(100, 250) # 连接到
        self.tri_path.closeSubpath()   # 关闭路径 *****

        self.path.setPath(self.tri_path) # 为 路径图元 设置 路径对象

        # 9 将 图元 添加到 场景
        self.scene.addItem(self.line)
        self.scene.addItem(self.rect)
        self.scene.addItem(self.ellipse)
        self.scene.addItem(self.pic)
        self.scene.addItem(self.text1)
        self.scene.addItem(self.text2)
        self.scene.addItem(self.text3)
        self.scene.addItem(self.path)

        # 10 将 场景 设置给 视图
        self.setScene(self.scene)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

'''
1. 该类直接继承QGraphicsView，那么窗口就是视图，且大小为300x300；

2. 实例化一个QGraphicsScene场景，并调用setSceneRect(x, y, w, h)方法来设置场景坐标原点和大小。
从代码中我们得知坐标原点为(0, 0)，之后往场景中添加的图元就会都根据该坐标来设置位置(关于坐标的更多内容，笔者会在34.4小节中进行讲解)。
场景的大小为300x300，跟视图大小一样；

3. 实例化一个QGraphicsLineItem直线图元，并调用setLine()方法设置直线两端的坐标。
该方法既可以直接传入四个数值，也可以传入一个QLineF对象。


4-5. 跟直线图元类似，这里分别实例化矩形图元和椭圆图元，并调用相应的方法来设置位置和大小；

6. 实例化一个图片图元，并调用setPixmap()方法设置图片，
QPixmap对象有个scaled()方法可以设置图片的大小(当然我们也可以使用QGraphicsItem的setScale()方法来设置)，
接着我们设置该图元的Flag属性，让他可以被选中以及移动，这是所有图元共有的方法。
最后调用setOffset()方法来设置图片相对于场景坐标原点的偏移量；

7. 这里实例化了三个文本图元，分别显示普通绿色文本，可编辑文本以及超链接文本(HTML)。
setDefaultColor()方法可以用来设置文本的颜色，setPos()用来设置文本图元相对于场景坐标原点的位置。
setTextInteractionFlags()用来设置文本属性，这里的Qt.TextEditorInteraction参数表示为可编辑属性(相当于在QTextEdit上编辑文本)，
最后的Qt.TextBrowserInteraction表明该文本用于浏览(相当于在QTextBrowser上的文本)。
有关更多的属性，大家可以在文档里搜索Qt::TextInteractionFlags来了解。
当然如果要让超链接文本能够被打开，我们还需要使用setOpenExternalLinks()方法，传入一个True参数即可。

8. 路径图元可以用于显示任意形状的图形，setPath()方法需要传入一个QPainterPath对象，而我们就是用该对象来进行绘画操作的。
moveTo()方法表示将画笔移动到相应位置上，lineTo()表示画一条直线，
closeSubpath()方法表示当前作画结束 (查阅文档来了解更多有关QPaintPath对象的方法)，这里我们画了一个直角三角形；

9. 调用场景的addItem()方法将所有图元添加进来；

10. 调用setScene()方法来让场景居中显示在视图中。


'''