from PySide2.QtWidgets import QApplication,QWidget,QStyle,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,\
QRubberBand,QSizePolicy
from PySide2.QtCore import Signal,Slot,Qt,QEvent,QPoint,QRect,QLine,QSize
from PySide2.QtGui import QImage,QPicture,QPixmap,QPainter,QColor

import os,sys,shutil


'''
 在 qpainter基础.py 的基础上，

 把原来每一个功能都要要分散在mousePressEvent\mouseMoveEvent\mouseReleseEvent三个事件中写的结构，

 改为统一写功能函数,并输出函数列表，
    (比如 def drawLine(self): -> [start,process,end]) 

 再根据功能分别覆盖三个mouse事件的方式：
     if self.action_v=='Line':
            self.mousePressEvent,self.mouseMoveEvent,self.mouseReleaseEvent=self.drawLine()
            
    elif self.action_v=='Rect':
        self.mousePressEvent,self.mouseMoveEvent,self.mouseReleaseEvent=self.drawRect()

这样写更利于编写和调试功能函数。
'''

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
# 手写板 如果手写label不在布局里 则实际绘制差标题栏高度 因此 一定要放在布局里
class HandWrite(QLabel):
    def __init__(self,parent=None):
        super().__init__(parent)
        # self.setScaledContents(True) #设置图片跟随label 在手写板中 不能这样设置，这样设置，就看不到手写轨迹了，因为坐标乱了

       
        # 2 设置pix 适应label大小
        # self.setScaledContents(True) 
        # 2 定义 记录手写点 
        self.last_point=None # 
        self.setMinimumWidth(400)
        self.setMinimumHeight(400)
        
        # 3 定义 画家
        self.painter=QPainter() 
        
        # 4 防止 鼠标跟踪
        if self.hasMouseTracking():
            self.setMouseTracking(False)

        # 5 参数设置
        self.pen_color='#000000'
        self.pen_width=4

        self.re_flag=False # 重新绘制
        self.save_flag=False # 保存

        # 7 动作参数 默认是线条
        self.action_v='Line'
        # self.action_v='Rect'

        # 8 清除
            # 全部
            # 部分

        # 9 撤销

        self.do_action()

             
            
    def do_action(self):
        
        if self.action_v=='Line':
            self.mousePressEvent,self.mouseMoveEvent,self.mouseReleaseEvent=self.drawLine()
            
        elif self.action_v=='Rect':
            self.mousePressEvent,self.mouseMoveEvent,self.mouseReleaseEvent=self.drawRect()

    def paintEvent(self,evt):
        # print('前',self.size())
        # if os.path.exists('1.png'):
           
        # self.pixmap().load('1.png')
        
        if self.re_flag:
            painter=QPainter(self.pixmap())

            pix=QPixmap('1.png')
            painter.drawPixmap(0,0,pix)
            print(' re_flag drawPixmap')
            painter.end()
        
        
        self.re_flag=False
        
        super().paintEvent(evt)

        # print('后',self.size())
        

    def resizeEvent(self,evt):
        
        # 重构开关
        self.re_flag=True
        # 1 定义 光栅对象
        pix=QPixmap(self.width(),self.height())
        pix.fill(QColor('white')) ## 不填充为白色 默认是黑色
    
        self.setPixmap(pix)


       
        print('hw resiz')
        

        
        

    '''        
        def mousePressEvent(self,evt):
            # 记录开始点
            self.last_point=evt.pos()
            # print(dir(self.last_point))


            if self.action_v=='Line':
                self.drawLine()[0](evt)
            elif self.action_v=='Rect':
                self.drawRect()[0](evt)

            return super().mousePressEvent(evt)

        def mouseMoveEvent(self,evt):
            if self.action_v=='Line':
                self.drawLine()[1](evt)
            elif self.action_v=='Rect':
                self.drawRect()[1](evt)

            return super().mouseMoveEvent(evt)

        def mouseReleaseEvent(self,evt):
            if self.action_v=='Line':
                self.drawLine()[-1](evt)
            elif self.action_v=='Rect':
                self.drawRect()[-1](evt)

            self.last_point = None  # 松开鼠标 就把坐标清空    *******
            return super().mouseReleaseEvent(evt)
'''

    # 笔的设置
    def pen_setting(self):
        pen=self.painter.pen()
        pen.setColor(QColor(self.pen_color)) 
        # pen.setColor(QColor('#35e3e3')) # 青色
        pen.setWidth(self.pen_width)# pen_width像素
        self.painter.setPen(pen) # 要把修改好的笔设回来 
        

    # 画图
    # 1 线条
    def drawLine(self):
        def start(evt):# 不能写  start(self,evt),不能有self，才能覆盖成功。在一个实例函数中，不能再套一个实例函数，这是语法错误。
            # 记录开始点
            self.last_point=evt.pos()

            # 开始画图
            self.painter.begin(self.pixmap())
            # print('self.painter.isActive',self.painter.isActive())
            # 设置笔
            self.pen_setting()
            # print('start')
            
            # print(dir(self.last_point))
            # return super().mousePressEvent(evt) # 会报错
            pass  
        def process(evt):
            # 1 线条
            self.painter.drawLine(self.last_point,evt.pos()) # 通过连续的drawLine 形成手写轨迹 *******
            self.update()# 触发更新 手写板 label 的绘图事件 paintEvent
            self.last_point=evt.pos() # 记录下一点的开始 这样才能 让mouseMoveEvent轨迹点连续
            # print('process')
            # return super().mouseMoveEvent(evt)
        def end(evt):
            self.last_point = None  # 松开鼠标 就把坐标清空    *******
            # self.painter.restore()

            # 结束画图
            self.painter.end()
            # print('end')
            # print('self.painter.isActive',self.painter.isActive())
            # return super().mouseReleaseEvent(evt)
            self.pixmap().save('1.png')
            
            pass

            
        return [start,process,end]

    # 2 矩形
    def drawRect(self):
        def start(evt):
            # 记录开始点
            self.last_point=evt.pos()

            # 开始画图
            self.painter.begin(self.pixmap())
            # print('self.painter.isActive',self.painter.isActive())
            # 设置笔
            self.pen_setting()
            
            # 2 生成橡皮筋控件
            self.rb=QRubberBand(QRubberBand.Rectangle,self)
            # 初始大小为一个空的QSize对象，即无大小
            self.rb.setGeometry(QRect(self.last_point,QSize())) 

            # 3 显示橡皮筋
            self.rb.show()

            # 光标 为十字
            self.setCursor(Qt.CrossCursor)
            # print('start')
           
        def process(evt):
            # 用橡皮筋显示将要画的矩形
            self.rb.setGeometry(QRect(self.last_point,evt.pos()).normalized())
            self.update()
            # print('process')
            
        def end(evt):
            rect=self.rb.geometry()
            self.painter.drawRect(rect)
            self.update()
            # 隐藏橡皮筋
            self.rb.hide()
            # 还原光标
            self.setCursor(Qt.ArrowCursor)
            # self.painter.restore()

            # 结束画图
            self.painter.end()
            self.pixmap().save('1.png')
            # print('self.painter.isActive',self.painter.isActive())
            # print('end')
    
        return [start,process,end]



if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()



'''
参考：
   


问题解决：
 问题1： 
    Traceback (most recent call last):
        File "d:/pyj/st/study/pyside2_pyqt/pys2/QPainter基础2.py", line 140, in end
            return super().mouseReleaseEvent(evt)
    TypeError: super(type, obj): obj must be an instance or subtype of type 
    必须是一个实例或类型的子类，这个函数没有了self，所以既不是实例也不是子类。
  解决：
       在start\process\end中注释掉所有的继承：

           # return super().mousePressEvent(evt)

           # return super().mouseMoveEvent(evt)

           # return super().mouseReleaseEvent(evt)

 问题2：QWidget::paintEngine: Should no longer be called
   原因：Warning: When the paintdevice is a widget, QPainter can only be used inside a paintEvent() function or in a function called by paintEvent().
   对于绘画设备是widget时，比如label、button等，只能在这些widget的paintEvent()事件里用。
   而QPixmap对象不是widget，即可以在paintEvent()事件里面画，也可以在该事件外画图。

 问题3：报 QPaintDevice: Cannot destroy paint device that is being painted
    解决2：
       1、添上begin(), end()
           原来：无
           现在：
               在start中加上：
                   # 开始画图
                   self.painter.begin(self.pixmap())

               在end中加上：
                   # 结束画图
                   self.painter.end()


 问题4：报 QPainter::begin: A paint device can only be painted by one painter at a time.
    解决3：
        因为解决问题2 添加了self.painter.begin(self.pixmap())，
        这就将绘画对象self.painter的指针指向了paint device绘画设备self.pixmap()，
        而原来定义的时候QPainter(self.pixmap())，已经将指针指向了该绘画设备，
        导致两个QPainter指针都指向了同一个（paint device）绘画设备self.pixmap()。

        一个绘画设备一次只能被一个画家指定。

        1、begin是必须要有指针的，只有取消QPainter定义的指针。
           原来：
               # 3 定义 画家
               self.painter=QPainter(self.pixmap()) # 将光栅对象当作画板

           现在:
               # 3 定义 画家
               self.painter=QPainter()           


 问题5：QPixmap不能自适应label的大小变化
  第一次解决：label设置图片自适应大小 self.setScaledContents(True)  好像可以了 ，带来了问题5，看不到手写轨迹了。
  原因分析：setScaledContents(True)对于展示现有图片没有问题，
    因为这是图片缩放，和下面的比例缩放是一个意思，按比例或不按比例缩放等。
     # self.hw.setPixmap(self.pix.scaled(self.hw.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation)) # 设置给label
     #  AspectRatioMode

            # {
                # IgnoreAspectRatio,

                # KeepAspectRatio,

                # KeepAspectRatioByExpanding

            # };

            # IgnoreAspectRatio  矩形框有多大，图片就缩放成多大，不限制原图片的长宽比
            # 
            # KeepAspectRatio    保持原图片的长宽比，且不超过矩形框的大小
            # 
            # KeepAspectRatioByExpanding   根据矩形框的大小最大缩放图片

    但是，我们这里是手写，不是缩放，是要扩充画布宽高，而不是缩放。 如果用缩放，则坐标就乱了。因此，不能用这种解决方法。

  第二次解决：在resizEvent缩放事件中，去设置画布，让其等于label尺寸，如果画面缩放 就让其重构 即把缩放前画的再重现出来
    # 1 定义 光栅对象
        pix=QPixmap(self.width(),self.height())
        pix.fill(QColor('white')) ## 不填充为白色 默认是黑色
    
        self.setPixmap(pix)

 问题6：label设置图片自适应大小 self.setScaledContents(True)  解决了4的问题，带来的问题是画不出来了。
    解决：取消self.setScaledContents(True)。因为这是手写板的天敌。
 
 问题7：在在resizEvent缩放事件中，设置画布，解决了4的问题，也解决了5的问题，可以画了，但是，一缩放，原来画的就都没了。
    解决：如果画面缩放，就在paintEvent事件让其重构，即把缩放前画的再重现出来，这就要求把缩放前的画面保存，这里每次
        在end()时，都保存到容器'1.png'中，
            self.painter.end()
            self.pixmap().save('1.png')

        也就是在paintEvent事件中把'1.png',再用drawPixmap()画出来就可以了。
            pix=QPixmap('1.png')
            painter.drawPixmap(0,0,pix)
        

 

 
'''