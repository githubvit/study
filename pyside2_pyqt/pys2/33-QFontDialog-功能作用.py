from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('字体对话框QFontDialog的学习')

        self.setup_ui()

    def setup_ui(self):
        # 怎么用
        # 怎么配置
        # 实时配置

        # 构造函数
        # 
        # self.fd = QFontDialog(self)
        font = QFont()
        font.setFamily("宋体")
        font.setPointSize(36)
        # 设置 对话框当前字体 
        # self.fd.setCurrentFont(font)
        # 一步到位 
        self.fd = QFontDialog(font, self) #(字体对象,父控件)
        #  self.fd.show() #非模态模式一般不用
        
       
        btn = QPushButton(self)
        self.btn=btn
        btn.setText("弹出字体对话框")
        btn.adjustSize()
        btn.move(50, 100)

        label = QLabel(self)
        self.label=label
        label.move(200, 100)
        label.setText("江上往来人")

        # self.怎么用()

        # self.配置选项()
        
        self.实时配置()

        pass

    def 怎么用(self):
        # 把字体对话框 的 字体 用在 标签文字上
        # 3种方式 pyside2只有两种

        def get_font():
            print('获取选中的字体',self.fd.selectedFont().family(),self.fd.selectedFont().pointSize())
            self.label.setFont(self.fd.selectedFont())
            self.label.adjustSize()

        # 1 弹出字体对话框 连接 槽 函数 设置标签字体
        # self.btn.clicked.connect(lambda : self.fd.open(get_font)) # pyside2 不支持 打开对话框 连接槽函数。pyqt5支持。
        
        #2  用fontSelected信号 设置标签字体
        self.btn.clicked.connect(lambda : self.fd.open())# pyside2 不支持 打开对话框 连接槽函数。
        self.fd.fontSelected.connect(lambda font:(self.label.setFont(font),self.label.adjustSize()) )
        # self.fd.fontSelected.connect(get_font)

        # 3 用静态方法获取 QFontDialog.getFont() 不需要self.fd 对话框对象
        # 得到的结果是元组（布尔值，字体对象）
        # 布尔值说明 ： 字体对话框最后选的 是ok 还是 cancel
        def static_getFont():
            g_font=QFontDialog.getFont(self) # (boll,QFont())
            # pyside2的结果是(boll,QFont())
            if g_font[0]:
                self.label.setFont(g_font[1])
                self.label.adjustSize()

            # pyqt5 的结果是反过来的
            # if g_font[1]:
            #     self.label.setFont(g_font[0])
            #     self.label.adjustSize()
            
        # self.btn.clicked.connect(static_getFont)
        

        pass

    def 配置选项(self):
        self.btn.clicked.connect(lambda : self.fd.show()) #y用非模态对话框打开
        # 设置没有确定和取消按钮 一般用于实时配置
        self.fd.setOption(QFontDialog.NoButtons)
        # 实时配置 用于标签 字体
        self.fd.currentFontChanged.connect(lambda font:(self.label.setFont(font),self.label.adjustSize()))
        # 设置多个选项setOptions 用按位 或 '|'
        # self.fd.setOptions(QFontDialog.NoButtons | QFontDialog.MonospacedFonts)
        # 测试选项是否生效
        # print(self.fd.testOption(QFontDialog.MonospacedFonts))    #测试 显示等宽字体
        # print(self.fd.testOption(QFontDialog.ScalableFonts))    #测试 显示可缩放字体
        pass
    
    def 实时配置(self):
        # 使用 currentFontChanged 信号 光标在字体对话框所指样式 在 label标签上实时生效
        # 一般和 无按钮 样式搭配
        # 使用非模态对话框 可以一边更改 一边设置样式

        self.btn.clicked.connect(lambda : self.fd.show()) 
        # 无按钮样式
        self.fd.setOption(QFontDialog.NoButtons)

        # 设置一个文本框 
        le=QLineEdit(self)
        le.move(200,150)
        le.adjustSize()
        le.textEdited.connect(lambda : le.adjustSize())

        self.fd.currentFontChanged.connect(lambda font:(le.setFont(font),le.adjustSize()))
        
        pass

  
if __name__ == "__main__":
    app = QApplication([])
    wd=Window()
    wd.show()
    app.exec_()