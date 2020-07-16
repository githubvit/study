from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('纯文本编辑器QPlainTextEdit的学习')
        self.setup_ui()

    # QPlainTextEdit是QTextEdit富文本编辑器的简化，针对纯文本进行了优化。
    # 1 更高效,滚动不是按像素而是按行、段落进行的;
    # 2 不支持列表、表格。

    def setup_ui(self):
        self.pte=QPlainTextEdit(self)
        self.pte.resize(300,300)
        self.pte.move(50,50)
        self.放大缩小()
        btn=QPushButton(self)
        btn.setText('测试')
        btn.adjustSize()
        btn.move(50,370)
        btn.clicked.connect(self.test) # 因为这里不能接收中文函数，所以借用test转一下

        print(self.pte.x())
        self.同步滚动行号案例()
    
    # 同步滚动行号案例
    def 同步滚动行号案例(self):
        
        # 设置外框
        self.r_frame=QWidget(self)
        self.r_frame.resize(20,self.pte.height())
        margin=2
        self.r_frame.move(self.pte.x()-self.r_frame.width()-margin,self.pte.y())
        # r_frame.setStyleSheet('border:1px solid red')

        # 设置行号条标签
        self.rlb=QLabel(self.r_frame)

        # 获取文本框光标开始位置 用来设置标签开始位置，保持高度方向一致
        # print(self.pte.cursorRect().y())

        self.rlb.move(0,self.pte.cursorRect().y())
        
        # 设置标签内样式右对齐
        self.rlb.setAlignment(Qt.AlignRight)
        # 填写行号
        self.add_rindex()

        # 做同步滚动的行号条
        def scroll_label(rect, dy):
            self.add_rindex()#保证标签行号自适应文本行数。
            self.rlb.move(self.rlb.x(), self.rlb.y() + dy)

        self.pte.updateRequest.connect(scroll_label)
        pass
        
    def add_rindex(self):
        # 获取文本行数
        # （小技巧：用.document().size().height()获取的文本高度取整后就是 行数，
        # document().size().width()宽度就是 宽度像素）
        dr_num=int(self.pte.document().size().height())
        # 循环写入 直到高度到了底
        rheight=0
        rnum=1
        rstr=''
        while rheight<self.pte.height():
            # print(rnum)
            rstr += str(rnum)+'\n'
            rnum+=1
            rheight+=10 # 这样设置是知道一定会超过文本框的高度一点。
        # 如果文本的行数，大于文本框的行数，标签的行号就应用文本的行数
        if dr_num>rnum:
            rstr="\n".join([str(i) for i in range(1, dr_num+1)])
            
        self.rlb.setText(rstr)
        self.rlb.adjustSize()


    def test(self):
        # self.覆盖模式()
        # self.Tab键控制()
        # self.文本操作()
        # self.块的操作()
        # self.滚动保证光标可见()
        # self.文本光标对象操作()
        # self.信号的操作()
        pass

    

    def 信号的操作(self):
        # self.pte.textChanged.connect(lambda :print("内容发生了改变"))
        # self.pte.cursorPositionChanged.connect(lambda :print("光标位置改变"))
        # self.pte.blockCountChanged.connect(lambda bc:print("块的个数改变", bc))
        # self.pte.selectionChanged.connect(lambda :print("选中内容发生了改变", self.pte.textCursor().selectedText()))
        
        # self.pte.modificationChanged.connect(lambda val:print("修改状态发生改变", val))
        # 一旦修改完毕，要保存，则状态应该置为False,表示修改完毕，
        # 再发生修改行为，就是在本次保存的基础上进行的修改。
        # doc = self.pte.document()
        # doc.setModified(False)

        # 页面变化（滚动、缩放），则内容更新，发射该信号
        # self.pte.updateRequest.connect(lambda rect, dy: print(f'页面变化（滚动、缩放等），内容更新，产生移动的左上到右下的矩形区域:{rect}，滚动的行高：{dy}，当前行高:',self.pte.HLine))
        
        # 利用这一点：滚动传递的行高。可以做同步滚动的行号条
        def scroll_label(rect, dy):
            self.add_rindex()#保证标签行号自适应文本高度。
            self.rlb.move(self.rlb.x(), self.rlb.y() + dy)

        self.pte.updateRequest.connect(scroll_label)
        pass

    def 文本光标对象操作(self):
        # tc = self.pte.textCursor()
        # tc.insertImage("rose.png") # 不能操作
        # tc.insertTable(5, 6) # 不能操作
        # tc = self.pte.cursorForPosition(QPoint(20, 60)) # 获取当前某一点的光标对象
        # print(tc)
        # tc.insertText("itlike") # 在某一点插入 不是在当前光标点
        self.pte.setCursorWidth(20)
        print(self.pte.document())
        # 选中 从当前选到文档的末尾
        self.pte.moveCursor(QTextCursor.End, QTextCursor.KeepAnchor)
        self.pte.setFocus()

        pass

    def 滚动保证光标可见(self):
        # self.pte.setCenterOnScroll(True) #当输入满一屏时，再回车输入下一行，会滚动到文本框中间位置。
        self.pte.centerCursor() # 保证能滚动到高度的中间位置的光标，滚动到中间位置 
        # self.pte.ensureCursorVisible() # 保证光标按高度的最近位置 滚动 
        self.pte.setFocus()

    def 放大缩小(self):
        btn1=QPushButton(self)
        btn1.setText('放大 +')
        btn1.adjustSize()
        btn1.move(50,10)
        btn1.setAutoRepeat(True)

        btn2=QPushButton(self)
        btn2.setText('缩小 -')
        btn2.adjustSize()
        btn2.move(150,10)
        btn2.setAutoRepeat(True)

        btn1.pressed.connect(lambda : self.pte.zoomIn(10))
        btn2.pressed.connect(lambda: self.pte.zoomIn(-5))
        # self.pte.zoomIn(10)
        # self.pte.zoomIn(-1)
        # self.pte.zoomOut(-10)

    def 块的操作(self):
        # 设置用户能够输入的最大块数
        print(self.pte.blockCount()) # 获取当前块的个数 共有几段
        self.pte.setMaximumBlockCount(3) # 设置最大块个数 最大段落数 留下最近的 删除最远的
        print(self.pte.toPlainText()) # 获取文档的文本 是删除了多余段落的文本

    def 文本操作(self):
        self.pte.setPlainText("社会我顺哥, 人狠话不多")
        # self.pte.setPlainText("itlike.com")
        self.pte.insertPlainText("itlike.com")
        self.pte.appendPlainText("<a href='http://www.itlike.com'>撩课</a>")
        self.pte.appendHtml("<a href='http://www.itlike.com'>撩课</a>")
        #
        table_str = "<table border=2>" \
                    "<tr><td>1</td><td>2</td><td>3</td></tr>" \
                    "<tr><td>4</td><td>5</td><td>6</td></tr>" \
                    "</table>"
        # self.pte.setHtml(table_str) # QPlainTextEdit object has no attribute 'setHtml'
        self.pte.appendHtml(table_str) # QPlainTextEdit 不支持列表、表格、图片。。。
        # print(self.pte.toPlainText())
        self.pte.setFocus()
        pass
    
    def Tab键控制(self):
        self.pte.setPlaceholderText('Tab键控制')
        self.pte.setTabChangesFocus(True) # 按下tab键 改变焦点
        # self.pte.setTabChangesFocus(False) # 这是默认设置 按下tab键 焦点不跳转 只是产生空格
       

    def 覆盖模式(self): #不好用 不要用 和QTextEdit中一样烂
        self.pte.setPlaceholderText('覆盖模式')
        # 指在光标处输入的内容 是新增 还是 覆盖
        # 获取默认
        print('覆盖模式',self.pte.overwriteMode()) #False
        self.pte.setOverwriteMode(True)
        self.pte.setFocus()
        pass    
if __name__ == "__main__":
    from PySide2.QtWidgets import *
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()