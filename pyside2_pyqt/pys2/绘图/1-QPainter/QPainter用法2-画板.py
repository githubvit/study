import random
import sys
 
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QPainter, QColor,QPicture
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout
 
# 沙画变量
SPRAY_PARTICLES = 100 # 沙画的密度
SPRAY_DIAMMETER = 10  # 沙画的笔宽

# 笔色列表
COLORS = [
  '#000000', '#141923', '#414168', '#3a7fa7', '#35e3e3', '#8fd970', '#5ebb49',
  '#458352', '#dcd37b', '#fffee5', '#ffd035', '#cc9245', '#a15c3e', '#a42f3b',
  '#f45b7a', '#c24998', '#81588d', '#bcb0c2', '#ffffff',
]
 
#  调色板按钮
class QPlatteButton(QPushButton):
  def __init__(self, color):
    super().__init__()
 
    self.setFixedSize(QSize(24, 24))
    self.color = color
    self.setStyleSheet("background-color: %s" % self.color)
 
# 画板
class Canvas(QLabel):
  def __init__(self):
    super().__init__()

    # 先定义一个 光栅图形 对象
    canvas = QPixmap(1200, 800)
    canvas.fill(QColor('white')) # 填充背景色
    self.setPixmap(canvas) # 将 光栅对象 设置给标签label
 
    self.last_x, self.last_y = None, None # 定义 坐标点 初始 为 空
    self.pen_color = QColor('#000') # 设定 笔 默认的颜色 为 黑色
 
  def set_pen_color(self, c): #设置笔的颜色
    self.pen_color = QColor(c)
 
  def mouseReleaseEvent(self, *args, **kwargs):
    """
    松开鼠标事件
    """
    self.last_x, self.last_y = None, None # 松开鼠标 就把坐标清空    *******
 
  # 手写轨迹 线条
  def mouseMoveEvent(self, e):
    # """
    # 移动鼠标事件 利用两点之间不断的连线，画出轨迹线条
    # """
    if self.last_x is None: # 如果刚开始 坐标为空 就开始记录鼠标移动的坐标
      self.last_x = e.x()    
      self.last_y = e.y()
      return
#  
    painter = QPainter(self.pixmap()) # 画布 设为 label的 pixmap图形 即 上面定义的 canvas
    pen = painter.pen() 
    pen.setWidth(4)
    pen.setColor(self.pen_color)
    painter.setPen(pen)
    painter.drawLine(self.last_x, self.last_y, e.x(), e.y()) # 有锯齿 
    # painter.drawPoint(e.x(),e.y()) # 只能慢，不能快，一快就出现断点，不连续。
    painter.end() # 本次 绘制 结束
    self.update() # 在移动过程中 标签 不断更新 
# 
    # 用line画轨迹 移动过程中不断更新下一点的起始坐标 才能形成连续轨迹 
    # update the origin for next time
    self.last_x = e.x()
    self.last_y = e.y()
# 
 
  # 沙画效果
  # def mouseMoveEvent(self, e):
    # painter = QPainter(self.pixmap())
    # p = painter.pen()
    # p.setWidth(1)
    # p.setColor(self.pen_color)
    # painter.setPen(p)
# 
    # 共 SPRAY_PARTICLES 粒 沙子  也就是 画一点 就画了 SPRAY_PARTICLES 点，点的范围在(SPRAY_DIAMMETER,SPRAY_DIAMMETER)里。
    # for n in range(SPRAY_PARTICLES): 
      # 每一粒 沙子 在 以 按下的点为中心 的 (SPRAY_DIAMMETER,SPRAY_DIAMMETER) 大的范围 随机产生
      # xo = random.gauss(0, SPRAY_DIAMMETER)
      # yo = random.gauss(0, SPRAY_DIAMMETER)
      # painter.drawPoint(e.x() + xo, e.y() + yo)
  # 
    # self.update()
 
#  主窗口
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("画板小程序")
 
    self.canvas = Canvas()
 
    widget = QWidget()
    vlayout = QVBoxLayout(widget)
    
    palette = QHBoxLayout()
    self.add_palette_buttons(palette)
    self.setCentralWidget(widget)

    vlayout.addWidget(self.canvas)
    vlayout.addLayout(palette)
 
  def add_palette_buttons(self, layout):
    """
    在水平布局中放入一行调色板
    """
    for c in COLORS:
      b = QPlatteButton(c)
      b.pressed.connect(lambda c=c: self.canvas.set_pen_color(c))
      layout.addWidget(b)
 
 
if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = MainWindow()
  window.move(120, 120)
  window.show()
  app.exec_()