from PySide2.QtWidgets import *
from PySide2.QtGui import *
# from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)


window = QWidget()

window.setWindowTitle("QAbstractButton")
window.resize(500, 500)

# 自定义的按钮类继承自抽象类（抽象类一般就是用来被继承的）
class Btn(QAbstractButton):
    # 子类必须要重写绘制事件。
    def paintEvent(self, evt):
        # print("绘制按钮")
        # 绘制按钮上要展示的一个界面内容
        # 可以看不懂
        
        # 1 定义一张画纸
        # QWidget即是继承QObject，也是继承QPaintDevice的
        # 所以，任何QWidget都可以作为画纸
        # Btn对象self就可以作为画纸 QPainter(self)
        painter = QPainter(self)

       
        # 2 定义一只笔（颜色，笔宽）
        pen = QPen(QColor(111, 200, 20), 5)
        # 3 用定义的画纸设置这只笔，就把纸笔连在一起了
        painter.setPen(pen)

        # 3 开始画
        # 先画一段文本，文本不受笔宽影响，无论怎么改笔宽，字体的粗细不变。
        painter.drawText(40, 40, self.text()) #(x,y,str)x,y是边距
        # 再画一个椭圆 
        painter.drawEllipse(0, 0, 100, 100) #(x,y,width,heigt) x，y不是圆心，是左上角边距。

btn = Btn(window)
btn.setText("xxx")
btn.resize(100, 100)
btn.move(50,50)

btn.pressed.connect(lambda : print("点击了这个按钮"))



window.show()
sys.exit(app.exec_())