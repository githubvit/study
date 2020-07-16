from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
# 
# from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('QCalendarWidget的学习')
        self.setup_ui()

    def setup_ui(self):
        # 添加标签内容
        # 1 添加文本
        lb1=QLabel('构造函数文本',self)
        self.lb1=lb1
        lb1.resize(100,100)
        lb1.move(10,10)
        lb1.setStyleSheet('background-color:#ddd')
        
        # 1.1 设置对齐
        # lb1.setAlignment(Qt.AlignCenter)  # 居中
        # lb1.setAlignment(Qt.AlignLeft)    # 左上角
        # lb1.setAlignment(Qt.AlignBaseline)# 左上角 把所有文本变成一行
        # lb1.setAlignment(Qt.AlignHCenter) # 水平居中
        # lb1.setAlignment(Qt.AlignVCenter) #垂直居中 默认
        # lb1.setAlignment(Qt.AlignRight)   # 右上角
        # lb1.setAlignment(Qt.AlignTop)     # 左上角
        # lb1.setAlignment(Qt.AlignBottom)  # 左下角

        # 多个选项叠加 按位或 
        # lb1.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter) #= Qt.AlignCenter
        # lb1.setAlignment(Qt.AlignRight|Qt.AlignVCenter)   # 水平靠右+垂直居中
        # lb1.setAlignment(Qt.AlignRight)   # 水平靠右+垂直居中

        # 1.2 设置缩进和边距
        # lb1.setIndent(10) # 缩进10
        # lb1.setMargin(20) # 周围20一圈为边距

        # 1.3 文本格式
        # lb1.setTextFormat(Qt.PlainText) # 文本格式为纯文本格式
        # lb1.setTextFormat(Qt.RichText)  # 富文本格式 html
        lb1.setTextFormat(Qt.AutoText)  # 自动识别文本格式 默认

        # 1.4 文本交互设置
        # lb1.setTextInteractionFlags(Qt.TextSelectableByMouse)#可以用鼠标选中
        # lb1.setTextInteractionFlags(Qt.TextSelectableByMouse|Qt.TextSelectableByKeyboard|Qt.TextEditable)#可以用鼠标选中 也可以用键盘选中 还可以编辑
        # lb1.setTextInteractionFlags(Qt.TextEditorInteraction)#这一个选项（文本编辑器的默认值）就等于上面三个选项
        # 交换选项
            # Qt.NoTextInteraction	
	            # 不可能与文本进行交互。 默认
            # Qt.TextSelectableByMouse
            	# 可以使用鼠标选择文本并使用上下文菜单或标准键盘快捷键将其复制到剪贴板。
            # Qt.TextSelectableByKeyboard
            	# 可以使用键盘上的光标键选择文本。显示文本光标。
            # Qt.LinksAccessibleByMouse
            	# 可以使用鼠标突出显示和激活链接。
            # Qt.LinksAccessibleByKeyboard
            	# 可以使用选项卡聚焦链接并使用enter激活。
            # Qt.TextSelectableByKeyboard
            	# 该文字完全可编辑。
            # Qt.TextEditorInteraction
            	# 文本编辑器的默认值。
            	# TextSelectableByMouse | TextSelectableByKeyboard | TextEditable
            # Qt.TextBrowserInteraction
            	# QTextBrowser的默认值。
            	# TextSelectableByMouse | LinksAccessibleByMouse | LinksAccessibleByKeyboard
        
        

        btn1=QPushButton(self)
        self.btn1=btn1
        btn1.setText('文本')
        btn1.adjustSize()
        btn1.move(10,120)
        
        # 单行输入框
        le=QLineEdit(self)
        # le=QTextEdit(self)
        self.le=le
        le.resize(100,25)
        le.move(10,150)
        le.setText('test abc')
        # le.setEnabled(False)
        le.setStyleSheet('background-color:rgba(255, 255, 255, 1);color:rgb(100,200,50);')

        # 1.5 快捷键
        # 小伙伴 (绑定伙伴控件，让设置在QLabel对象上的快捷键 聚焦在伙伴控件上)
        lb1.setBuddy(le) # 绑定伙伴控件 le 输入框 
        # 用&l设置快捷键alt+l 
        lb1.setText('聚焦(&le)<a href="https://www.baidu.com">百度</a>') #按下alt+l，'l'字符下有下划线，光标聚焦到伙伴控件le输入框身上

        # 1.6 设置选中文本
        # lb1.setSelection(1,2)# 选中的 起始位置，结束位置 
        # 获取选中文本
        # print('标签lb1选中的文本',lb1.selectedText())

        # 1.7 设置可以打开/链接
        # 在标签中如有链接，可以设置可以打开/链接,要可以打开 还要把前面设置的文本可选中选项关闭（因为它会拦截点击行为），同样的原因，当然还要把选中文本关闭，不然还是打不开浏览器。
       
        # lb1.setOpenExternalLinks(True)#默认是False 不能打开
        # 链接有关 信号
        # lb1.linkHovered.connect(lambda link: print(link))
        # lb1.linkActivated.connect(lambda link: print(link)) # 必须关闭打开链接设置，否则不会打印，因为该信号被拦截了

        # 1.8 文本换行
        # 多行文本换行，保证完整单词 换行
        # lb1.setText('123 456 789'*10)
        lb1.setWordWrap(True) #不设置，则标签就是一行，不会自动换行。
        # 竖着排标签文本
        # lb1.setText(' \n'.join('竖着排标签文本 '))

    
        # 打字软件
        # 把这个le1设置透明 贴在le上 le上文本作为打字的范本。
        # 对比两个文本输入框的文本，错字符标红
        le1=QLineEdit(self)
        # le1=QTextEdit(self)
        self.le1=le1
        le1.resize(100,25)
        le1.move(le.x(),le.y()+le.height())
        
        le1.setText('tes')
        # le1.setStyleSheet('background-color: rgba(0, 0, 0, 0);color:green') # 背景透明 *****
        # le1.setWindowOpacity(0)#这个设置不了背景透明
        
        # 多行输入框
        te=QTextEdit(self)
        te.resize(100,100)
        te.move(10,200)

        btn1.clicked.connect(lambda : lb1.setText(le.text().strip()+'\n'+te.toPlainText().strip()))
        
        # 1.9 清除
        btn2=QPushButton(self)
        btn2.setText('清除')
        btn2.adjustSize()
        btn2.move(10,320)
        btn2.clicked.connect(lambda : lb1.clear())

        
        
         
        # 2 添加图片
        lb2=QLabel(self)
        self.lb2=lb2
        lb2.resize(100,100)
        lb2.move(150,10)
        lb2.setStyleSheet('background-color:#ddd')

        # 2.1 用富文本方式添加
        # lb2.setText('<img src="pyside2_pyqt\pys2\xxx.png" width=60 height=60>')# 打不开 不能解析 要加r
        # lb2.setText(r'<img src="pyside2_pyqt\pys2\xxx.png" width=60 height=60>')# 打不开 不能解析 要加r

        # 2.2 用Qpicture对象添加
        # Qpicture 是 绘画设备QPaintDevice的子类 因此可以绘画
        # 定义绘画对象
        pic=QPicture()
        # 在pic上生成画布
        painter=QPainter(pic)
        # 用该画布对象绘画
        # 拿个画刷
        painter.setBrush(QColor(100,200,100))
        # 画个圆
        painter.drawEllipse(0,0,50,50)# 矩形框（x,y,width,height） 0，0点不是左上角点，是圆的左切点，即矩形框左边线中点。
        # 结束绘画 否则 报 QPaintDevice: Cannot destroy paint device that is being painted
        painter.end()
        # 将该Qpicture对象添加到标签内
        lb2.setPicture(pic)




        

        # 2.3 用现有图片展示
        btn2=QPushButton(self)
        self.btn2=btn2
        btn2.setText('图片')
        btn2.adjustSize()
        btn2.move(150,120)
        
        btn2.clicked.connect(self.get_picture)

        # 3 添加动图
        lb3=QLabel(self)
        self.lb3=lb3
        lb3.resize(100,100)
        lb3.move(290,10)
        lb3.setStyleSheet('background-color:#ddd')

        btn3=QPushButton(self)
        self.btn3=btn3
        btn3.setText('动图')
        btn3.adjustSize()
        btn3.move(290,120)
        btn3.clicked.connect(self.get_gif)

        self.start_btn=QPushButton(self)
        self.start_btn.setText('start')
        self.start_btn.adjustSize()
        self.start_btn.move(250,150)
        self.start_btn.setEnabled(False)
        

        self.stop_btn=QPushButton(self)
        self.stop_btn.setText('stop')
        self.stop_btn.adjustSize()
        self.stop_btn.move(self.start_btn.x()+self.start_btn.width(),self.start_btn.y())
        self.stop_btn.setEnabled(False)

        self.paused_btn=QPushButton(self)
        self.paused_btn.setText('paused')
        self.paused_btn.adjustSize()
        self.paused_btn.move(self.stop_btn.x()+self.stop_btn.width(),self.start_btn.y())
        self.paused_btn.setEnabled(False)

        self.speed_btn=QPushButton(self)
        self.speed_btn.setText('speed')
        self.speed_btn.adjustSize()
        self.speed_btn.move(self.paused_btn.x()+self.paused_btn.width(),self.start_btn.y())
        self.speed_btn.setEnabled(False)


        # 4 直接输入数值 整型或浮点型
        # 设置这个功能是为了让数值不用转换成字符串，可以直接使用，方便程序员。
        # lb1.setNum(888.88)
        pass
    # 获取图片地址
    def get_picture(self):
        # 打开文件对话框 
        path=QFileDialog.getOpenFileName(self,'','./','All(*.*);;Imag(*.jpg *.jpge *.gif *.png *.bmp)','Imag(*.jpg *.jpge *.gif *.png *.bmp)')[0]
        if len(path.strip()):
            # 设置图片适应控件尺寸
            self.lb2.setScaledContents(True) 
            # 设置图片
            self.lb2.setPixmap(path)
            
            
    # 获取动图地址
    def get_gif(self):
        # 打开文件对话框 
        path=QFileDialog.getOpenFileName(self,'','./','All(*.*);;Imag(*.jpg *.jpge *.gif *.png *.bmp)','Imag(*.jpg *.jpge *.gif *.png *.bmp)')[0]
        if len(path.strip()):
            # 设置动图大小适应控件
            self.lb3.setScaledContents(True)
            # 定义QMovie()对象
            mov=QMovie(path)
             # 大小
            # mov.setScaledSize(QSize(100,100))

            # 开始 不然看不见
            self.start_btn.setEnabled(True)
            self.start_btn.clicked.connect(lambda : mov.start())

            # 停止
            self.stop_btn.setEnabled(True)
            self.stop_btn.clicked.connect(lambda : mov.stop())

            # 暂停
            self.paused_btn.setEnabled(True)                
            self.paused_btn.clicked.connect(lambda : mov.setPaused(True))

            # 加速
            self.speed_btn.setEnabled(True)
            self.speed_btn.clicked.connect(lambda : mov.setSpeed(200))#两倍数
            
            
            # 设置动图
            self.lb3.setMovie(mov)
           
            

        pass


if __name__ == "__main__":
    app = QApplication([])
    wd=Window()
    wd.show()
    app.exec_()