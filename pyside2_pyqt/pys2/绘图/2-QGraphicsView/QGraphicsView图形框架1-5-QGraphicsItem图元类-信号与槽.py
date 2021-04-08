'''
34.1-5 QGraphicsItem 信号与槽
出于性能考虑，QGraphicsItem不继承自QObject，所以本身并不能使用信号和槽机制，我们也无法给它添加动画。
不过我们可以自定义一个类，并让该类继承自QGraphicsObject。
请看下面的解决方案：
'''
import sys
from PyQt5.QtCore import QPropertyAnimation, QPointF, QRectF, pyqtSignal
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView,  QGraphicsObject


class CustomRect(QGraphicsObject):
    # 1
    my_signal = pyqtSignal()

    def __init__(self):
        super(CustomRect, self).__init__()

    # 2
    def boundingRect(self):
        return QRectF(0, 0, 100, 30)

    # 3
    def paint(self, painter, styles, widget=None):
        painter.drawRect(self.boundingRect())


class Demo(QGraphicsView):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(300, 300)

        # 4
        self.rect = CustomRect()
        self.rect.my_signal.connect(lambda: print('signal and slot'))
        self.rect.my_signal.emit()

        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 300, 300)
        self.scene.addItem(self.rect)

        self.setScene(self.scene)

        # 5
        self.animation = QPropertyAnimation(self.rect, b'pos')
        self.animation.setDuration(3000)
        self.animation.setStartValue(QPointF(100, 30))
        self.animation.setEndValue(QPointF(100, 200))
        self.animation.setLoopCount(-1)
        self.animation.start()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

'''
1. 自定义一个信号；

2-3. 继承QGraphicsObject的话，我们最好把boundingRect()和paint()方法重新实现下。在boundingRect()中我们返回一个QRectF类型值来确定CustomRect的默认位置和大小。在paint()中调用drawRect()方法将矩形画到界面上；

4. 将自定义的信号和槽函数连接，槽函数中打印“signal and slot”字符串。接着调用信号的emit()方法来发射信号，那么槽函数也就会启动了；

5. 加上QPropertyAnimation属性动画，将矩形从(100, 30)移动到(100, 200)，时间为3秒，动画无限循环。


'''