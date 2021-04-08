# 在 QPainter基础2.py 的基础上 增加 用 picture 记录指令 在paintEvent事件中 重现

from PySide2.QtWidgets import QApplication,QWidget,QStyle,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,\
QRubberBand,QSizePolicy
from PySide2.QtCore import Signal,Slot,Qt,QEvent,QPoint,QRect,QLine,QSize
from PySide2.QtGui import QImage,QPicture,QPixmap,QPainter,QColor

import os,sys,shutil

# 自定义形状按钮
class ShapeBtn(QPushButton):
    # 形状信号
    shapeSignal=Signal(str)
    def __init__(self,shape):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Fixed)
        self.setProperty('shape',shape)
        

    def mousePressEvent(self,evt):
        super().mousePressEvent(evt)
        if evt.button()==Qt.MouseButton.LeftButton:
            self.shapeSignal.emit(self.property('shape'))

        
        

class Window(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.setWindowTitle('QPainter基础1')
        # self.setGeometry(1000,400,500,500)

        # 动作列表
        self.action_list=["Line","Rect", 'RoundedRect', "Ellipse", "Pie", 'Chord', "Arc",\
    "Path","Polygon", "Polyline", "Points", "Text", "Pixmap"]
        self.btn_list=['线条', '矩形','圆角矩形','椭圆','扇形 pie','弦 chord','弧 Arc','轨迹 path','多边形 填充 poolygon',\
    '多边形线条 无填充 polyline','点','文本','图片']

        # 定义手写板对象
        self.hw=HandWrite()

        h_layout=QHBoxLayout()
        
        # 定义按钮
        for i,btn in enumerate(self.btn_list):
            item_btn=ShapeBtn(self.action_list[i])
            item_btn.setText(btn)
            item_btn.shapeSignal.connect(self.change_shape)

            h_layout.addWidget(item_btn)

        # 布局
        v_layout=QVBoxLayout(self) # 一定要用布局，不然，lb手写始终对不上，差标题栏高度    ******
        
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.hw)
        # v_layout.addWidget(lb)

       

 
   
    def change_shape(self,v):
        print(v)
        self.hw.action_v=v
        self.hw.do_action()
        
        
# 手写板 label
# 1 手写板一定要放在布局里 如果手写label不在布局里 则实际绘制差中标题栏高度 
# 2 手写板的光栅对象一定要在resizEven缩放事件中定义，并且宽高为label缩放的宽高，这样才能在缩放时，光栅对象大小和手写板保持一致。
    # 切记不能用图片自动适应label的设置 这样会导致坐标乱了，画不出来，这个设置是绘制的天敌。
# 3 如果画面缩放，就在paintEvent事件让其重构，即把缩放前画的再重现出来（这就要求把缩放前的画面保存），否则一缩放，以前画的就没了。
# 4 在光栅对象手写的同时，用picture来进行手写记录指令的保存，保存在pic目录里。在paintEvent事件重构时，就从文件夹里依次读取pic文件，重现指令即可。
# 5 用os模块在刚开始加载时生成pic 文件夹目录
# 6 用shutil 模块 在 程序结束时 删除 pic 文件夹目录
class HandWrite(QLabel):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.setMinimumWidth(400)
        self.setMinimumHeight(400)
       
        # 2 定义 记录手写点 
        self.last_point=None # 
        self.last_rect=None
        
        
        # 3 定义 画家
        self.painter=QPainter() 
        self.painter2=QPainter() 

        #  定义 picture  基础4   记录指令
        self.picture=QPicture()
        
        # 4 防止 鼠标跟踪
        if self.hasMouseTracking():
            self.setMouseTracking(False)

        # 5 参数设置
        self.pen_color='#000000'
        self.pen_width=4
        self.bgdcolor='#ffffff'
        self.re_flag=False # 重新绘制
        self.save_flag=False # 保存

        self.start=True # 开始不加载 pic 文件
        self.n=0 # pic 文件名 从0开始  0.pic 1.pic  ...
        self.pic_dir=self.build_pic_dir()

        # 7 动作参数 默认是线条
        self.action_v='Line'
        # self.action_v='Rect'

        # 8 清除
            # 全部
            # 部分

        # 9 撤销

        self.do_action()

    
    
    # 建立pic目录 #  基础4
    def build_pic_dir(self):
        pic_dir=r'D:\pyj\st\study\pic'
        if not os.path.exists(pic_dir):
            os.mkdir(pic_dir)
            print('建立pic目录')
        return pic_dir

    # pic文件存储 #  基础4
    def save_pic(self):
        self.n+=1
        self.picture.save(f'{self.pic_dir}\{self.n}.pic') 
            
    def do_action(self):
        
        if self.action_v=='Line':
            self.mousePressEvent,self.mouseMoveEvent,self.mouseReleaseEvent=self.drawLine()
            
        elif self.action_v=='Rect':
            self.mousePressEvent,self.mouseMoveEvent,self.mouseReleaseEvent=self.drawRect()

    # 缩放时 resizEvent 会在 paintEvent 之前执行， 可以保证重构。
    def resizeEvent(self,evt):
        # 打开重构
        self.re_flag=True
        # 定义新光栅对象
        pix=QPixmap(self.width(),self.height())
        pix.fill(QColor(self.bgdcolor)) # 不填充为白色 默认是黑色
        self.setPixmap(pix)


    def paintEvent(self,evt):
        
        # print(self.start)
        # 如果画面缩放 就让其重构 即把缩放前画的再重现出来
        if self.re_flag and not self.start:
    
            painter=QPainter(self.pixmap()) # 基础4

            # 加载pic指令 # 基础4
            pic=QPicture()
            filelist=os.listdir(self.pic_dir)
            # 将self.pic_dir文件夹下的所有文件都加载出来 就构成了 画面缩放前（即resizeEvent事件）的画面 
            for name in filelist:
                filepath=f'{self.pic_dir}\{name}'
                # 加载pic指令
                pic.load(filepath)
                painter.drawPicture(0,0,pic) 
            painter.end()

            # print(' 画面缩放 重构 re_flag drawPicture')

        self.re_flag=False  # 关闭 重构
        self.start=False    # 取消 开始 
        
        super().paintEvent(evt)

        # print('后',self.size())
        

    # 笔的设置
    def pen_setting(self,painter,color):
        pen=painter.pen()
        pen.setColor(QColor(color)) 
        # pen.setColor(QColor('#35e3e3')) # 青色
        pen.setWidth(self.pen_width)# pen_width像素
        painter.setPen(pen) # 要把修改好的笔设回来 
        
    def brush_settig(self,painter,color):
        brush=painter.brush()
        brush.setColor(QColor(color)) 
        brush.setStyle(Qt.SolidPattern)# 填充 色块 
        painter.setBrush(brush)
        
    # 画图
    # 1 线条
    def drawLine(self):
        def start(evt):# 不能写  start(self,evt),不能有self，才能覆盖成功。在一个实例函数中，不能再套一个实例函数，这是语法错误。
            # 记录开始点
            self.last_point=evt.pos()

            # 开始画图
            self.painter.begin(self.pixmap())
            self.painter2.begin(self.picture) #  基础4
            # print('self.painter.isActive',self.painter.isActive())
            # 设置笔
            self.pen_setting(self.painter,self.pen_color)
            self.pen_setting(self.painter2,self.pen_color)
            # print('start')
            
            # print(dir(self.last_point))
            # return super().mousePressEvent(evt) # 会报错
            pass  
        def process(evt):
            # 1 线条
            self.painter.drawLine(self.last_point,evt.pos()) # 通过连续的drawLine 形成手写轨迹 *******
            self.painter2.drawLine(self.last_point,evt.pos()) # 通过连续的drawLine 形成手写轨迹 *******
            self.update()# 触发更新 手写板 label 的绘图事件 paintEvent
            self.last_point=evt.pos() # 记录下一点的开始 这样才能 让mouseMoveEvent轨迹点连续
            # print('process')
            # return super().mouseMoveEvent(evt)
        def end(evt):
            self.last_point = None  # 松开鼠标 就把坐标清空    *******
            # self.painter.restore()

            # 结束画图
            self.painter.end()
            self.painter2.end()
            # print('end')
            # print('self.painter.isActive',self.painter.isActive())
            # return super().mouseReleaseEvent(evt)
            # self.pixmap().save('1.png')
            
            # 存储指令
            self.save_pic()
            pass

            
        return [start,process,end]

    # 2 矩形
    def drawRect(self):
        def start(evt):
            # 记录开始点
            self.last_point=evt.pos()

            # 开始画图
            self.painter.begin(self.pixmap())
            self.painter2.begin(self.picture) #  基础4
            # print('self.painter.isActive',self.painter.isActive())
            # 设置笔
            self.pen_setting(self.painter,self.pen_color)
            self.pen_setting(self.painter2,self.pen_color)
            # 设置笔刷 填充 与背景色保持一致
            self.brush_settig(self.painter,self.bgdcolor)
            self.brush_settig(self.painter2,self.bgdcolor)
            
            # 2 生成橡皮筋控件
            # self.rb=QRubberBand(QRubberBand.Rectangle,self)
            # 初始大小为一个空的QSize对象，即无大小
            # self.rb.setGeometry(QRect(self.last_point,QSize())) 
            

            # 3 显示橡皮筋
            # self.rb.show()

            # 光标 为十字
            self.setCursor(Qt.CrossCursor)
            # print('start')
           
        def process(evt):
            # 用橡皮筋显示将要画的矩形
            # self.rb.setGeometry(QRect(self.last_point,evt.pos()).normalized())
            # rect=self.rb.geometry()
            # 清除上次画的矩形 所谓清除就是用背景色 再画一遍 就把原来的 清除了
            if self.last_rect:
                self.pen_setting(self.painter,self.bgdcolor)
                self.pen_setting(self.painter2,self.bgdcolor)
                self.painter.drawRect(self.last_rect)
                self.painter2.drawRect(self.last_rect)

            self.pen_setting(self.painter,self.pen_color)
            self.pen_setting(self.painter2,self.pen_color)

            rect=QRect(self.last_point,evt.pos()).normalized()# .normalized() 表示反过来也可。

            self.painter.drawRect(rect)
            self.painter2.drawRect(rect)

            self.last_rect=rect
            
            self.update()
            # print('process')
            
        def end(evt):
            self.last_rect=None # 还原矩形默认值
            
            self.update()
            # 隐藏橡皮筋
            # self.rb.hide()
            # 还原光标
            self.setCursor(Qt.ArrowCursor)
            # self.painter.restore()

            # 结束画图
            self.painter.end()
            self.painter2.end()
            # self.pixmap().save('1.png')
            # print('self.painter.isActive',self.painter.isActive())
            # print('end')
            # 存储指令
            self.save_pic()
    
        return [start,process,end]



if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
    print('删除pic目录')
    shutil.rmtree(wd.hw.pic_dir)
    
    