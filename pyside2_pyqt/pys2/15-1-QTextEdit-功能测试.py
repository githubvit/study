from PySide2.QtWidgets import *
# from PySide2.QtGui import QTextCharFormat,QTextImageFormat,QTextFrameFormat,\
# QTextDocumentFragment,QTextListFormat,QTextTableFormat,QTextLength,QTextBlock,\
# QTextBlockFormat,QTextCharFormat,QTextFrameFormat,QBrush,QColor,QTextList
# from PySide2.QtCore import Qt
from PySide2.QtGui import *
from PySide2.QtCore import *
# from PyQt5.Qt import *

# 覆盖mousePressEvent 利用锚点方法获取按下位置的超链接
class MyTextEdit(QTextEdit):
    def mousePressEvent(self,evt):
        # 用锚点方法anchorAt(QPoint())获取点击位置的超链接
        # print(self.anchorAt(self.pos())) # https://www.baidu.com 没有超链接 则为空
        url=self.anchorAt(self.pos())
        if len(url):
            QDesktopServices.openUrl(QUrl(url)) #用桌面浏览器打开超链接
        return super().mousePressEvent(evt)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QTextEdit的学习')
        self.resize(500,500)
        self.setup_ui()
        
    def setup_ui(self):
        te=MyTextEdit(self)
        # te=QTextEdit(self)
        self.te=te
        te.resize(300,300)
        te.move(20,20)
        te.setPlaceholderText('请输入个人简历')
        # te.setText('xxx')
        # self.文本内容的设置()
        # self.文本光标插入操作()
        # self.文本格式设置和合并()
        # self.内容和格式的获取()
        # self.文本选中()
        # self.选中文本内容获取()
        # self.选中文本的取消()
        # self.选中文本的移除()
        # self.位置相关操作()
        # self.开始和结束标识()

        # self.自动格式化() # 上述操作都是先获取文本光标的操作，是二级操作，从现在开始是一级操作，直接快速
        # self.软换行模式()
        # self.覆盖模式()
        # self.对齐模式()
        self.字体格式()
        # self.颜色设置()
        # self.当前的字符格式()
        # self.常用编辑操作()
        # self.滚动到锚点()
        # self.只读设置()
        # self.tab功能测试()
        # self.打开超链接()
        self.信号测试()
        pass
    def 信号测试(self):
        # self.te.textChanged.connect(lambda:print('文本内容发生改变时, 发射的信号'))
        # self.te.selectionChanged.connect(lambda:print('选中内容发生改变时, 发射的信号'))
        # self.te.cursorPositionChanged.connect(lambda:print('光标位置发生改变时, 发射的信号'))
        self.te.currentCharFormatChanged.connect(lambda tcf:print('当前字符格式发生改变时, 发射的信号',tcf))
        # self.te.copyAvailable.connect(lambda val:print('复制可用时',val))
        # self.te.redoAvailable.connect(lambda val:print('重做可用时',val))
        # self.te.undoAvailable.connect(lambda val:print('撤销可用时',val))
        pass
    def 打开超链接(self):
        
        # 定义自己的类 打开超链接
            # QTextEdit并没有pressed或clicked信号，需要定义自己的QTextEdit类 class MyTextEdit(QTextEdit):，
            # 覆盖mousePressEvent方法，当按下超链接时刻：

                # 1 获取超链接
                # 获取鼠标按下位置的超链接 anchorAt(QPoint) -> str
                # 2 打开超链接
                # QDesktopServices.openUrl(QUrl(urlString)) 用桌面浏览器打开指定链接地址

        
        # 设置超链接
        self.te.insertHtml('xxx'*300+'<a name="bd" href="https://www.baidu.com"> 百度 </a>'+'aa '*400)
        
        # 定义按钮
        btn=QPushButton(self)
        btn.setText('滚动到锚点,打开超链接')
        btn.adjustSize()
        btn.move(20,340)
        # 滚动到锚点函数
        def test():
            self.te.scrollToAnchor("bd")
        btn.clicked.connect(test)
        pass
    def tab功能测试(self):
        # self.te.setTabChangesFocus(True)
        # 默认的tab距离或宽度
        print(self.te.tabStopDistance()) #80.0
        print(self.te.tabStopWidth())   #80
        btn=QPushButton(self)
        btn.setText('改变tab宽度')
        btn.adjustSize()
        btn.move(20,340)
        def test():
            # 设定tab距离为100
            self.te.setTabStopDistance(100)
            print(self.te.tabStopWidth())
        btn.clicked.connect(test)
        pass
    def 只读设置(self):
        print(self.te.isReadOnly())
        # 设置只读
        self.te.setReadOnly(True)
        self.te.insertPlainText("itlike")#代码还是可以写入的
        print(self.te.isReadOnly())
        pass
    def 滚动到锚点(self):
        # 锚点设置 <a name="锚点名称" href="#锚点内容"> xxx </a>
        # 设置文本
        self.te.insertHtml('xxx'*300+'<a name="bd" href="#baidu">锚点 </a>'+'aa '*400)
        
        btn=QPushButton(self)
        btn.setText('滚动到锚点')
        btn.adjustSize()
        btn.move(20,340)
        def test():
            self.te.scrollToAnchor("bd") # 
        btn.clicked.connect(test)
        pass
    def 常用编辑操作(self):
        btn=QPushButton(self)
        btn.setText('常用编辑操作')
        btn.adjustSize()
        btn.move(20,340)
        def test():
            # self.te.copy()
            # self.te.paste()
            # self.te.selectAll()
            # 查找   
            # QTextDocument.FindBackward            向后查找
            # QTextDocument.FindCaseSensitively     区分大小写查找
            # QTextDocument.FindWholeWords          完整匹配单词查找
            print(self.te.find("she", QTextDocument.FindBackward | QTextDocument.FindCaseSensitively | QTextDocument.FindWholeWords)) # False
            self.te.setFocus()
        btn.clicked.connect(test)
        
        pass
    def 当前的字符格式(self):
        btn=QPushButton(self)
        btn.setText('当前的字符格式')
        btn.adjustSize()
        btn.move(20,340)
        def test():
            # 1 设置当前字符格式
            # 设置字符格式对象
            tcf=QTextCharFormat()
            tcf.setFontFamily('宋体')
            tcf.setFontPointSize(20)
            tcf.setFontCapitalization(QFont.Capitalize) # 首字符大写
            # tcf.setForeground(QColor(100, 200, 150))    # 设置前景色
            tcf.setForeground(QColor(250,250, 0))    # 设置前景色 即 字体颜色
           
            tcf.setBackground(QColor(250,0,0))    # 设置背景色
         
            self.te.setCurrentCharFormat(tcf)
            # 2 合并当前字符格式
            # 再设置一个字符格式对象
            tcf2 = QTextCharFormat()
            tcf2.setFontOverline(True)
            self.te.mergeCurrentCharFormat(tcf2)

            # 3 获取当前字符格式
            print(self.te.currentCharFormat()) 
            # <PySide2.QtGui.QTextCharFormat(QTextFormat::FormatType(2)) at 0x0000014A7CC87048>
            pass
        btn.clicked.connect(test)
        pass
        # 字体
	        # 统一设置
	        	# setFont(QFont)
	        	# font() -> QFont
	        # 字体家族
	        	# setFontFamily(family_str)
	        	# fontFamily() -> str
	        # 字体大小
	        	# setFontPointSize(float)
	        	# fontPointSize() -> float
	        # 字体粗细
	        	# setFontWeight(int)
	        	# fontWeight() -> int
	        # 字体上划线
	        	# setFontOverline(bool)
	        	# fontOverline() -> bool
	        # 字体中划线
	        	# setFontStrikeOut(bool)
	        	# fontStrikeOut() -> bool
	        # 字体下划线
	        	# setFontUnderline(bool)
	        	# fontUnderline() -> bool
	        # 字体大小写
	        	# setFontCapitalization(QFont.Capitalization) 首字符大写
	        	# fontCapitalization() -> QFont.Capitalization
	        		# QFont.MixedCase
	        			# 这是正常的文本呈现选项，不应用大写更改。
	        		# QFont.AllUppercase
	        			# 这会改变要以全大写类型呈现的文本。
	        		# QFont.AllLowercase
	        			# 这会改变要以全小写类型呈现的文本。
	        		# QFont.SmallCaps
	        			# 这会改变要以小型大写字母呈现的文本。
	        		# QFont.Capitalize
	        			# 这会将要呈现的文本更改为每个单词的第一个字符作为大写字符。
    
    def 颜色设置(self):
        btn=QPushButton(self)
        btn.setText('颜色设置')
        btn.adjustSize()
        btn.move(20,340)
        def test():
            # 改变光标 选中字符 的背景颜色，并不是整个文本框，或整行的背景颜色，
            self.te.setTextBackgroundColor(QColor(255,0,0)) # 红底
            # self.te.setTextBackgroundColor(QColor(255,255,0)) # 黄底
            # 字体颜色
            self.te.setTextColor(QColor(255, 255, 255)) # 白字
            self.te.setFocus()   
        btn.clicked.connect(test)
        pass
    def 字体格式(self):
        btn=QPushButton(self)
        btn.setText('字体格式')
        btn.adjustSize()
        btn.move(20,340)
        def test():
            # 获取字体设置对话框
            # QFontDialog.getFont() 

            # 设置字体
            # self.te.setFontFamily("幼圆")
            # self.te.setFontWeight(QFont.Black)
            # self.te.setFontItalic(True)
            # self.te.setFontPointSize(30)
            # self.te.setFontUnderline(True)

            # 用字体对象QFont() 设置字体  更细，比上面更全面，比如删除线，上面就没有
            font = QFont()
            font.setFamily('微软雅黑')
            font.setPointSize(60)
            font.setStrikeOut(True)
            self.te.setCurrentFont(font) 

            self.te.setFocus()       
        btn.clicked.connect(test)
       
        pass
    
    def 对齐模式(self):
        btn=QPushButton(self)
        btn.setText('对齐模式')
        btn.adjustSize()
        btn.move(20,340)
        def test():
            # 获取默认
            # print('默认对齐模式',self.te.alignment()) 
            # 设置对齐模式
            self.te.setAlignment(Qt.AlignCenter) # 作用于段落 不是整个文档 也不是单行
            self.te.setFocus()
        btn.clicked.connect(test)
    def 覆盖模式(self):
        btn=QPushButton(self)
        btn.setText('覆盖模式+光标宽度')
        btn.adjustSize()
        btn.move(20,340)
        def test():
            # 指在光标处输入的内容 是新增 还是 覆盖

            # 获取默认
            print('覆盖模式',self.te.overwriteMode()) #False
            # 获取光标宽度
            print('光标宽度',self.te.cursorWidth()) #False
            print('光标矩形',self.te.cursorRect()) #False
            # 设置
            # self.te.setOverwriteMode(True)
            # print(self.te.overwriteMode())
            if self.te.overwriteMode():
                self.te.setOverwriteMode(False)
                self.te.setCursorWidth(10)
            else:
                self.te.setOverwriteMode(True)
                self.te.setCursorWidth(1)
            self.te.setFocus()
        btn.clicked.connect(test)
        pass
    def 软换行模式(self):
        # 设置当用户输入内容过多时, 是否进行软换行, 以及如何进行软换行
        btn=QPushButton(self)
        btn.setText('软换行模式')
        btn.adjustSize()
        btn.move(20,340)
        def test():
            # 1 设置软换行模式
            self.te.setLineWrapMode(QTextEdit.WidgetWidth) # 到达宽度，自动换行，单词默认整体换行。这就是默认设置
            # self.te.setLineWrapMode(QTextEdit.NoWrap) # 超过宽度不换行，产生水平滚动条
           
            # self.te.setLineWrapMode(QTextEdit.FixedPixelWidth) # 到达一定的像素宽度后自动换行，保持单词的完整性
            # 设置换行的像素宽度或换行列数 
            # self.te.setLineWrapColumnOrWidth(100) #与FixedPixelWidth搭配就是像素

            # self.te.setLineWrapMode(QTextEdit.FixedColumnWidth) # 到达一定的列数宽度后自动换行 不保持单词的完整性。
            # self.te.setLineWrapColumnOrWidth(10)#与FixedColumnWidth搭配就是列数

            # 2 设置单词换行模式 就是设置换行时 单词是否整体换行
            # self.te.setWordWrapMode(QTextOption.WrapAnywhere) #宽度够了之后, 随意在任何位置换行，不保持单词完整性 
            # self.te.setWordWrapMode(QTextOption.WordWrap)  #保持单词完整性  
            
            self.te.setFocus()
            pass
        btn.clicked.connect(test)
        pass
    def 自动格式化(self):
        btn=QPushButton(self)
        btn.setText('自动格式化-列表')
        btn.adjustSize()
        btn.move(20,340)
        def test():
            # 输入一些特定字符, 会转换成为对应的效果
            # 自动创建项目符号列表（例如，设置完成后，当用户在最左侧列中输入星号（'*'）时，会产生列表及标识符，按Enter键，会转入列表的下一项。
            self.te.setAutoFormatting(QTextEdit.AutoBulletList)
            self.te.setFocus()
        btn.clicked.connect(test)


        pass

    def 开始和结束标识(self):
        # 设置 开始和结束标识 方便 Undo撤销 和 Redo恢复 操作
        # 通过 右击选择 Undo撤销，发现设置了 开始和结束标识的可以将 多步撤销操作 变成 一步撤销 操作
        # 通过 右击选择 Redo恢复，发现设置了 开始和结束标识的可以将 多步恢复操作 变成 一步恢复 操作
    
        tc=self.te.textCursor()
        tc.insertText('123')
        tc.insertBlock()
        tc.insertBlock()

        # 设置开始标识
        tc.beginEditBlock()

        tc.insertText('456')
        tc.insertBlock()
        tc.insertBlock()
        tc.insertText('789')
        tc.insertBlock()
        tc.insertBlock()

        # 设置结束标识
        tc.endEditBlock()

        tc.insertText('123')
        tc.insertBlock()
        tc.insertBlock()
        tc.insertText('456')
        pass
    def 位置相关操作(self):
        # 测试按钮
        btn=QPushButton(self)
        btn.setText('位置相关操作')
        btn.adjustSize()
        btn.move(20,340)
        def test():
            tc=self.te.textCursor()
            # 1 判断
            # 是否在段落的开始和末尾
            print(tc.atBlockStart())
            print(tc.atBlockEnd())

            # 是否在文档的开始和末尾
            print(tc.atStart())
            print(tc.atEnd())

            # 2 获取
            # 在第几列
            print('1',tc.columnNumber())
            # 光标位置
            print('2',tc.position())
            # 在段落中的位置
            print('3',tc.positionInBlock())

            self.te.setFocus()

        btn.clicked.connect(test)
        pass
    def 选中文本的移除(self):
        # 测试按钮
        btn=QPushButton(self)
        btn.setText('选中文本的移除')
        btn.adjustSize()
        btn.move(20,340)
        def test():
            # 获取光标对象
            tc=self.te.textCursor()
            # 1 移除选中的文本，没有选中的文本，不动作
            tc.removeSelectedText()
            # 2 移除选中的文本，没有选中的文本，删除后面一个
            # tc.deleteChar()
            # 3 移除选中的文本，没有选中的文本，删除前面一个
            # tc.deletePreviousChar()
            self.te.setFocus()
        btn.clicked.connect(test)
        pass

    def 选中文本的取消(self):
        # 测试按钮
        btn=QPushButton(self)
        btn.setText('选中文本的取消')
        btn.adjustSize()
        btn.move(20,340)
        def test():
            # 获取光标对象
            tc=self.te.textCursor()
            # 是否有选中的文本
            print('1',tc.hasSelection())
            # 取消选中的文本
            tc.clearSelection()
            # 将取消选中的光标对象 设置为当前光标对象 才可以看到是取消了 这步非常重要
            self.te.setTextCursor(tc)
            print('2',tc.hasSelection())
            self.te.setFocus()
        btn.clicked.connect(test)
        pass  
    def 选中文本内容获取(self):
        # 插入列表
        self.te.textCursor().insertTable(5,3)
        # 测试按钮
        btn=QPushButton(self)
        btn.setText('选中文本内容获取')
        btn.adjustSize()
        btn.move(20,340)
        def test():
            # 获取光标对象
            tc=self.te.textCursor()
            # 1 获取选中的文本
            print(tc.selectedText())
            # 2 获取选中的文本片段
            # print(tc.selection())
            # 将  获取选中的文本片段 按纯文本输出
            # print(tc.selection().toPlainText())
            # 3 获取选中表格单元数 结果是元组(起始行，总行，起始列，总列)
            print(tc.selectedTableCells())#(0, 2, 0, 3)
            # print(self.te.textCursor().selectedTableCells())#(0, 2, 0, 3)
            # 4 选中位置的获取
            print(tc.selectionStart())
            print(tc.selectionEnd())
            self.te.setFocus()
        btn.clicked.connect(test)
        pass

    def 文本选中(self):
        # 测试按钮
        btn=QPushButton(self)
        btn.setText('文本选中')
        btn.adjustSize()
        btn.move(20,340)
        def test():
            # 锚点Anchor和光标位置 的 一致与否 带来光标的选中和移动
            # 1 设置光标位置
            # 获取光标对象
            tc=self.te.textCursor()

            # 2 操作光标对象
            # 2.1 改变光标对象位置 setPosition(光标位置，锚点位置)
            # tc.setPosition(6) #锚点位置默认是移动 实现光标移动

            # 2.2 设置锚点位置保持不动 实现从改变后的位置6到锚点位置（即改变前的位置）的选中
            # tc.setPosition(6,QTextCursor.KeepAnchor) 

            # 2.3 移动光标
            # movePosition（光标移动选项，锚点移动模式，移动值）
            # 光标移动选项有移动到行首、段首、上一行、下一行。。。
                # QTextCursor.NoMove              将光标保持在原位
                # QTextCursor.Start               移至文档的开头。
                # QTextCursor.StartOfLine         移动到当前行的开头。
                # QTextCursor.StartOfBlock        移动到当前块的开头。
                # QTextCursor.StartOfWord         移动到当前单词的开头。
                # QTextCursor.PreviousBlock       移动到上一个块的开头。
                # QTextCursor.PreviousCharacter   移至上一个字符。
                # QTextCursor.PreviousWord        移到上一个单词的开头。
                # QTextCursor.Up                  向上移动一行。
                # QTextCursor.Left                向左移动一个字符。
                # QTextCursor.WordLeft            向左移动一个单词。
                # QTextCursor.End                 移到文档的末尾。
                # QTextCursor.EndOfLine           移动到当前行的末尾。
                # QTextCursor.EndOfWord           移到当前单词的末尾。
                # QTextCursor.EndOfBlock          移动到当前块的末尾。
                # QTextCursor.NextBlock           移动到下一个块的开头。
                # QTextCursor.NextCharacter       移动到下一个角色。
                # QTextCursor.NextWord            转到下一个单词。
                # QTextCursor.Down                向下移动一行。
                # QTextCursor.Right               向右移动一个角色。
                # QTextCursor.WordRight           向右移动一个单词。
                # QTextCursor.NextCell	          移动到当前表中下一个表格单元格的开头。如果当前单元格是行中的最后一个单元格，则光标将移动到下一行中的第一个单元格。
                # QTextCursor.PreviousCell        移动到当前表内的上一个表格单元格的开头。如果当前单元格是行中的第一个单元格，则光标将移动到上一行中的最后一个单元格。
                # QTextCursor.NextRow             移动到当前表中下一行的第一个新单元格。
                # QTextCursor.PreviousRow         移动到当前表中上一行的最后一个单元格。
            
            # tc.movePosition(QTextCursor.StartOfLine,QTextCursor.MoveAnchor) #移动到行首
            # tc.movePosition(QTextCursor.StartOfBlock,QTextCursor.MoveAnchor)  #移动到段首
            # tc.movePosition(QTextCursor.StartOfBlock,QTextCursor.KeepAnchor)  #移动到段首 选中
            # tc.movePosition(QTextCursor.PreviousBlock,QTextCursor.KeepAnchor)  #移动到上一段首 选中
            # tc.movePosition(QTextCursor.Up,QTextCursor.KeepAnchor)  #移动到上一行 选中

            # 2.4 选中 select
                # QTextCursor.Document            选择整个文档。
                # QTextCursor.BlockUnderCursor    选择当前光标的文本段落。
                # QTextCursor.LineUnderCursor     选择当前光标的文本行。
                # QTextCursor.WordUnderCursor     选择当前光标的单词（按空格）。如果光标未定位在可选字符串中，则不选择任何文本。
            tc.select(QTextCursor.WordUnderCursor)

            # 3 将 操作后的光标对象 设置为 当前光标对象          *****
            self.te.setTextCursor(tc)     # 没有这一步，上面的操作都没有结果

            # 4 设置聚焦
            self.te.setFocus() # 没有这一步 看不见 操作效果

        btn.clicked.connect(test)

        pass

    def 内容和格式的获取(self):
        # 获取文本光标对象
        tc=self.te.textCursor()
        # 获取文本块
        # print(tc.block())#<PySide2.QtGui.QTextBlock object at 0x00000297D5CE02C8>
        # 
        # 插入文本列表
        tlf=QTextListFormat()
        tc.insertList(tlf.ListDisc)
     
        # 测试按钮
        btn=QPushButton(self)
        btn.setText('获取内容和格式测试')
        btn.adjustSize()
        btn.move(20,340)
        def test():
            # 获取段落（即光标所在行）文本
            print(self.te.textCursor().block().text())
            
            # 获取是第几段落 段落编号 （从0计算）
            print(self.te.textCursor().blockNumber())

            # 获取文本列表
            # print(self.te.textCursor().currentList()) # pyside2 不支持 只能用pyqt5
            # print(self.te.textCursor().currentList().count()) # 统计列表数量

        btn.clicked.connect(test)
       
        pass

    def 文本格式设置和合并(self):
        
        # 获取文本光标对象
        tc=self.te.textCursor()
        
        # 1 设置 块内字符格式
        # 文本块内的字符格式
        tcf=QTextCharFormat()#z字符格式对象
        tcf.setFontFamily('幼圆')
        tcf.setFontPointSize(30)
        tcf.setFontItalic(True)
        tc.setCharFormat(tcf)
        tc.insertText('光标文本')
        # 代码输入的字体不受光标对象文本格式影响，但会覆盖光标文本格式，导致光标文本格式无用
        # self.te.setText('中文字体') 
        
        # 2 设置 块格式
        # 文本块的格式
        # 一个块就是一个段落 对齐方式、行高、缩进等段落格式
        tbf=QTextBlockFormat()
        tbf.setAlignment(Qt.AlignCenter)#居中
        # tbf.setIndent(2)#设置了两个tab后，就不是居中了
        tc.setBlockFormat(tbf)

        # 3 设置 光标选中字符格式
        # 将光标的当前字符格式设置为给定格式。如果光标有选择，则给定格式应用于当前选择
        ccf=QTextCharFormat()
        ccf.setFontFamily('仿宋')
        ccf.setFontPointSize(50)
        ccf.setFontOverline(True) #上划线
        ccf.setFontUnderline(True) #下划线

        c_btn=QPushButton(self)
        c_btn.setText('设置选中文字的格式')
        c_btn.adjustSize()
        c_btn.move(20,340)
        def set_charFormat():
            # tc.setCharFormat(ccf)#这个是没有效果的 要重新获取光标对象
            self.te.textCursor().setCharFormat(ccf)
           
            
        c_btn.clicked.connect(set_charFormat)
        
        
        # 4 合并 光标选中字符格式
        # 再设置一个文字格式
        ccf2=QTextCharFormat()
        ccf2.setFontStrikeOut(True) #删除线
        
        c_btn2=QPushButton(self)
        c_btn2.setText('合并格式-增加了删除线')
        c_btn2.adjustSize()
        c_btn2.move(150,340)
        def merge_charFormat():
            # 先设置了一个格式
            self.te.textCursor().setCharFormat(ccf)
            # 再把当前格式合并上
            self.te.textCursor().mergeCharFormat(ccf2)
            
        c_btn2.clicked.connect(merge_charFormat)


    def 文本光标插入操作(self):
        # 通过文本光标, 可以操作编辑 文本文档 对象
        # QTextEdit对象就是富文本编辑器可以编辑文本文档=word软件可以编辑doc文档
        # 整个文本编辑器, 其实就是为编辑 这个文本文档 提供了一个可视化的界面
        
        # 获取文档 操作文本对象
        print(self.te.document()) # <PySide2.QtGui.QTextDocument(0x1af1081ba50) at 0x000001AF10C57888>
        
        # QTextDocument 这个文档类上有一堆操作方法
        
        # 获取文本光标 操作文本对象
        print(self.te.textCursor()) #<PySide2.QtGui.QTextCursor object at 0x000002400D1E7948>

        # QTextCursor 这个文本光标类上有一堆操作方法


        # 1 插入文本
        # 获取文本光标 得到文本光标对象
        tc=self.te.textCursor()

        # 设置文本格式对象
        tcf=QTextCharFormat()
        tcf.setToolTip('提示') #放在使用了tcf格式的字符上有提示
        tcf.setFontFamily('微软雅黑')
        tcf.setFontPointSize(66)

        # 插入文本
        
        # 插入普通文本
        tc.insertText("文本1")
        # 插入普通文本带格式
        tc.insertText("文本2",tcf)

        # 插入 富文本（HTML字符串）
        # tc.insertText("<a href='http://www.baidu.com'>百度</a>")
        # self.te.append("<a href='http://www.baidu.com'>百度</a>")
        tc.insertHtml("<a href='http://www.baidu.com'>百度</a>")


        # 2 插入图片
        # tc.insertImage(r'D:\pyj\st\study\pyside2_pyqt\pys2\xxx.png') #老方式可以用不推荐
        # 设置图片格式对象
        icf=QTextImageFormat()
        icf.setName(r'D:\pyj\st\study\pyside2_pyqt\pys2\xxx.png')
        icf.setWidth(60)
        # tc.insertImage(icf)
        tc.insertImage(icf,QTextFrameFormat.FloatRight) # 靠文本框右边


        # 3 插入文本片段
        # 设置对象 用文本片段类静态方法
        # 富文本片段
        # jcf=QTextDocumentFragment.fromHtml("<a href='http://www.itlike.com'> 撩课 </a>")
        # 纯文本片段
        jcf=QTextDocumentFragment.fromPlainText("<a href='http://www.itlike.com'> 撩课 </a>")
        tc.insertFragment(jcf)
        

        # 4 插入列表
            # 两个插入方法
                # 在当前光标位置插入一个新块（或称插入一个制表符），
                # 并使光标右侧成为具有给定格式的新创建列表的第一个列表项，
                # 光标保持不动。返回创建的列表
                    # insertList(QTextListFormat) -> QTextList 
                    # insertList(QTextListFormat.Style) -> QTextList
            	
            # 两个创建方法
                # 在光标所在段首位置创建具有给定格式的新列表（或称在段首创建一个制表符），
                # 光标保持不动。返回创建的列表
                    # createList(QTextListFormat ) -> QTextList 	
                    # createList(QTextListFormat.style ) -> QTextList 
            	
            # 列表对象api QTextListFormat
	            # setIndent(int)
	            # setNumberPrefix(str)
	            # setNumberSuffix(str)
	            # setStyle(QTextListFormat.Style)

            # 列表对象.格式 QTextListFormat.style
                # QTextListFormat.ListDisc            一个圆圈
                # QTextListFormat.ListCircle          一个空的圆圈
                # QTextListFormat.ListSquare          一个方块
                # QTextListFormat.ListDecimal         十进制值按升序排列
                # QTextListFormat.ListLowerAlpha      小写拉丁字符按字母顺序排列
                # QTextListFormat.ListUpperAlpha      大写拉丁字符按字母顺序排列
                # QTextListFormat.ListLowerRoman      小写罗马数字（仅支持最多4999项）
                # QTextListFormat.ListUpperRoman      大写罗马数字（仅支持最多4999项）
       
        #  4.1 用 列表对象.格式 插入或创建
        # ltc=tc.insertList(QTextListFormat.ListDisc) #把光标的右侧当列表的首项 生成的点(制表符)在光标左侧，光标保持原位不动
        # ltc=tc.createList(QTextListFormat.ListDisc) #把光标所在段落当列表的首项 生成的点(制表符)在段首，光标保持原位不动
        # print(ltc.count()) # 1
        #  ltc是QTextList文本列表对象，有很多方法.item

        # 4.2 用 列表对象 插入或创建
        # 定义列表对象
        ltc2=QTextListFormat()
        # ltc2.setStyle(QTextListFormat.ListDisc)#小圆点格式 1. 2. 3.
        ltc2.setStyle(QTextListFormat.ListDecimal)# 前后缀格式
        ltc2.setIndent(2)           #缩进2个Tab键
        # 用前后缀方法 给数字 添加 了 尖括号 形如 <1> <2> ...<n>
        ltc2.setNumberPrefix("<")  #前缀 Style是数字才有用 即 QTextListFormat.ListDecimal才有用
        ltc2.setNumberSuffix(">")  #后缀 
        tc.insertList(ltc2)

        # 5 插入表格
        # 表格：由行和列组成的单元格。
        # 列：字段。行：记录。
        # 5.1 插入(行数,列数)
        # tc.insertTable(5,3)
        # 5.2 插入(行数,列数,表格格式对象)
        # 表格格式对象 QTextTableFormat
            # 设置列宽  setColumnWidthConstraints(self, Iterable, QTextLength=None)
            # 外边距    setCellSpacing(self, p_float)
            # 内边距    setCellPadding(self, p_float)
            # 对齐方式  setAlignment(self, Union, Qt_Alignment=None, Qt_AlignmentFlag=None)
        
        ttf=QTextTableFormat()
        
        ttf.setAlignment(Qt.AlignLeft) #左对齐 是设置整个表格相对于父控件的对齐方式，不是表格的单元格对齐方式
        ttf.setCellPadding(6) #内边距
        ttf.setCellSpacing(3) #外边距 单元格间的距离
        ttf.setColumnWidthConstraints((QTextLength(QTextLength.PercentageLength,30),QTextLength(QTextLength.PercentageLength,30)
        ,QTextLength(QTextLength.PercentageLength,40)))#设置列宽 传递元组() 根据列数决定元组个数
        # QTextLength(QTextLength.PercentageLength,30) 
            # QTextLength.PercentageLength 是说明按整个表格宽度的百分比设置宽度
            # 30 说明该列占整个列表宽度的30%。
        # tc.insertTable(5,3,ttf)

        btn=QPushButton(self)
        btn.setText('插入列表5行3列')
        btn.adjustSize()
        btn.move(20,340)
        def insertTable():
            self.ttb=self.te.textCursor().insertTable(5,3,ttf)# 返回QTextTable文本表格对象
            # ttb 是 QTextTable对象 该对象可以追加行和列
            
        btn.clicked.connect(insertTable)

        a_btn=QPushButton(self)
        a_btn.setText('追加3行2列')
        a_btn.adjustSize()
        a_btn.move(20,370)    
        def append_row_clm():
            self.ttb.appendColumns(2)
            self.ttb.appendRows(3)
        a_btn.clicked.connect(append_row_clm)
        # 插入行 insertRows(p_int,num)、插入列insertColumns(p_int,num)、合并单元格mergeCells(*_args)
        # 移除行removeRows(p_int,num)、移除列removeColumns(p_int,num)、取消合并等


        # 6 插入文本块
       
        # 设置文本块格式对象
        tbf=QTextBlockFormat()
        # tbf.setAlignment(Qt.AlignRight) #右对齐
        tbf.setAlignment(Qt.AlignLeft) #左对齐
        tbf.setRightMargin(100) #右边距
        # tbf.setIndent(1) #缩进1个Tab
        # 
        # 设置字体格式对象
        ccf=QTextCharFormat()
        ccf.setFontFamily('微软雅黑')
        ccf.setFontPointSize(20)


        # 插入文本块
        btn1=QPushButton(self)
        btn1.setText('插入文本块')
        btn1.adjustSize()
        btn1.move(120,340)
        def insertTextBlock():
            # self.te.textCursor().insertBlock(tbf) #带文本块格式
            self.te.textCursor().insertBlock(tbf,ccf) #带文本块格式和字符格式
            # 看不出来
            self.te.setFocus()
            # 
        btn1.clicked.connect(insertTextBlock)


        # 7 插入文本框架
        # 设置文本框架格式对象
        tff=QTextFrameFormat()
        # tff 可以设置边框 宽高 边距等等
        tff.setBorder(3)#设定边框宽度
        tff.setBorderBrush(QColor(255,0,0))#设定边框颜色
        # tff.setRightMargin(150)#设定了外边距 优先于宽度 
        tff.setWidth(300)#如果大于te te会有横向滚动条
        tff.setHeight(20)
        
        # 插入文本框架
        f_btn=QPushButton(self)
        f_btn.setText('插入文本框架')
        f_btn.adjustSize
        f_btn.move(120,370)
        def insertTextFrame():
            self.te.textCursor().insertFrame(tff)
        f_btn.clicked.connect(insertTextFrame)

        # 文档QTextDocument对象的根框架rootFrame就是QTextFrame对象。
        # doc=self.te.document()
        # print(doc.rootFrame()) # <PySide2.QtGui.QTextFrame(0x1b87fc4c150) at 0x000001B8014CE1C8>
        # root_frame=doc.rootFrame()
        # root_frame.setFrameFormat(tff)
        pass
        
        

    def 文本内容的设置(self):
        # 设置普通文本内容
        self.te.setPlainText("<h1>ooo</h1>")      # 代码set文本的 光标 在 最前
        # self.te.insertPlainText("<h1>oooo</h1>")   # 代码 insert 文本的 光标 在 insert文本的 最后
        # print(self.te.toPlainText())

        # 富文本的操作
        # self.te.setHtml("<h1>ooo</h1>")
        # self.te.insertHtml("<h6>社会我顺哥</h6>")
        # print(self.te.toHtml())

        # 自动判定
        # self.te.setText("<h1>ooo</h1>")  # setText(str) 自动判定 普通文本 富文本
        # 追加
        self.te.append("<h3>oooxxx</h3>") # 在老文本最后 另起一行输入append的文本 光标不动 即 append前光标在哪还在哪
    
        print(self.te.toPlainText())
        
        # ooo
        # oooxxx
        # print(self.te.toHtml())
        # <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
        # <html>....</html>

        # 清空
        # self.te.clear()
        pass

if __name__ == "__main__":
    
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
        