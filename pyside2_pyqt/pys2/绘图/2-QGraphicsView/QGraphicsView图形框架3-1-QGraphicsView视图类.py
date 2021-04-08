'''
34.3 QGraphicsView视图类
视图其实是一个滚动区域，如果视图小于场景大小的话，那窗口就会显示滚动条;
好让用户可以观察到全部场景(在Linux和Windows系统上，如果视图和场景大小一样，滚动条也会显示出来)。
在下面的代码中，笔者让场景大于视图：
'''
import sys
from PyQt5.QtCore import QRectF
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView


class Demo(QGraphicsView):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(300, 300)

        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 500, 500)
        self.scene.addEllipse(QRectF(200, 200, 50, 50))

        self.setScene(self.scene)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

'''
视图大小为300x300，场景大小为500x500。


---
'''