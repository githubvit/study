from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

app=QApplication([])
wd=QWidget()
wd.setWindowTitle('单行文本框QLineEdit功能')
wd.resize(500,500)


# 四 其他
# 1 是否被编辑 
    # 标识文本框内容是否被修改
le=QLineEdit(wd)
le.setPlaceholderText('验证是否编辑')
le.adjustSize()
le.move(50,50)

def check_modify():
	# 先获取 编辑状态
	print('le的编辑状态',le.isModified())
	# 再还原 编辑状态 即设置编辑状态为False
	# le.setModified(False)
# 有输入 就为True 
# le.textChanged.connect(check_modify)
# 没有输入 则为False
m_btn=QPushButton(wd)
m_btn.setText('验证编辑')
m_btn.adjustSize()
m_btn.move(200,50)
m_btn.clicked.connect(check_modify)

# 2 光标控制
# 控制光标, 以及文本选中操作
    # 向前、向后移动  mark：是否带选中字符 step：移动多个步
        # cursorForward(bool mark，int steps = 1)
        # cursorBackward(bool mark，int steps = 1)

    # 向前、向后移动一个单词  mark：是否带选中字符
        # cursorWordForward(bool mark)
        # cursorWordBackward(bool mark)

    # 移动到行首 True 带选中字符 home(bool)
    # 移动到行尾 True 带选中字符 end(bool)

    # 设置光标位置 setCursorPosition(int)
    # 获取光标位置 cursorPosition()
    # 获取指定坐标位置对应文本光标位置 cursorPositionAt(const QPoint＆ pos)
    # 注意区分 光标 鼠标 坐标
le2=QLineEdit(wd)
le2.setPlaceholderText('光标移动')
le2.adjustSize()
le2.move(50,100)

# 控制光标移动
c_btn=QPushButton(wd)
c_btn.setText('控制光标')
c_btn.adjustSize()
c_btn.move(200,100)
def control_cursor():
    # 向后移动
    # le2.cursorBackward(False,2) #无光标闪动

    # 要看到光标 需要设置焦点
    le2.setFocus() #看到光标闪动，文本框周围有选中光圈作为当前活动控件 ******

    # le2.cursorBackward(True,2) #向后选中两个文本字符 变蓝 无光标闪动
    # le2.cursorBackward(False,2) #向后移动两个光标 光标闪动
    
    # 向后移动一个单词(按空格算单词),即向后移动到一个空格 不选中到空格
    # le2.cursorWordBackward(False)

    # 移动到行首 从当前光标到行首全选中
    # le2.home(True)

    le2.setText('0123456789')
    # 设置光标在第三个位置闪烁 初始状态是无法成功的
    le2.setCursorPosition(2)

    # 获取当前光标位置 文本框光标位置是从0开始的
    print('文本框le2当前光标位置',le2.cursorPosition())

    # 获取 相对文本框的坐标位置 对应的 文本框光标位置 的值
    
    # le2.setText('abc defg')

    # 针对 数字 英文 光标文字一个字符约为 5px 中文不一样
    # print(le2.cursorPositionAt(QPoint(10,10)))  #获取文本框相对坐标为10px,10px的光标位置 1
    # print(le2.cursorPositionAt(QPoint(11,10)))  #获取文本框相对坐标为10px,10px的光标位置 1
    # print(le2.cursorPositionAt(QPoint(14,10)))  #获取文本框相对坐标为10px,10px的光标位置 2
    # print(le2.cursorPositionAt(QPoint(15,10)))  #获取文本框相对坐标为15px,10px的光标位置 2
    # print(le2.cursorPositionAt(QPoint(20,10)))  #获取文本框相对坐标为15px,10px的光标位置 3
    # print(le2.cursorPositionAt(QPoint(25,10)))  #获取文本框相对坐标为15px,10px的光标位置 4
    # print(le2.cursorPositionAt(QPoint(30,10)))  #获取文本框相对坐标为15px,10px的光标位置 4
    # print(le2.cursorPositionAt(QPoint(31,10))) #获取文本框相对坐标为31px,10px的光标位置 5
    # print(le2.cursorPositionAt(QPoint(35,10))) #获取文本框相对坐标为31px,10px的光标位置 5

    # print(le2.cursorPositionAt(QPoint(10,100))) #y的坐标到外面了，还是可以获取到 1
    # print(le2.cursorPositionAt(QPoint(1000,100))) #x\y的坐标都到外面了，还是可以获取到 10 这就是光标结尾的位置

    # 小案例
    # 输入一堆文本结束时，让光标停在左侧起始位置
    # le2.setText('0123456789'*3)
    # le2.home(True) # 全选
    # le2.home(False) # 光标 在行首
c_btn.clicked.connect(control_cursor)

# 3 文本边距 
    # 设置 setTextMargins(int left，int top，int right，int bottom)
    # 获取 getTextMargins()
le3=QLineEdit(wd)
le3.setPlaceholderText('文本边距')
le3.resize(le2.width(),le2.width())
le3.move(50,150)
# 用QWidget内容边距 会改变输入框的外形大小
# le3.setContentsMargins(100,100,0,0)
# 用文本边距 
b_btn=QPushButton(wd)
b_btn.setText('文本边距')
b_btn.adjustSize()
b_btn.move(200,150)
def text_margin():
    # 设置文本边距 会依据光标位置裁剪
    le3.setTextMargins(50,50,10,10)
    # 获取文本边距
    print(le3.getTextMargins())
    
b_btn.clicked.connect(text_margin)

# 4 光标对齐
    # 设置 setAlignment(Qt.Alignment) 
		# 水平
			# Qt.AlignLeft
			# Qt.AlignRight
			# Qt.AlignHCenter
			# Qt.AlignJustify # 此处同左对齐

		# 垂直
			# Qt.AlignTop
			# Qt.AlignBottom
			# Qt.AlignVCenter
			# Qt.AlignBaseline

        # 垂直和水平都居中
		    # Qt.AlignCenter 等同于 Qt.AlignHCenter | Qt.AlignVCenter
			
# 设置le3 光标对齐方式为右下
a_btn=QPushButton(wd)
a_btn.setText('右下对齐')
a_btn.adjustSize()
a_btn.move(200,200)
def cursor_align():
    # 设置 右下对齐 
    le3.setAlignment(Qt.AlignRight | Qt.AlignBottom)
    # 获取光标
    le3.setFocus()
    # 获取
    print(le3.alignment())
    
a_btn.clicked.connect(cursor_align)
# 如果先按文本边距按钮，再按右下对齐，光标离右下角 就有文本按钮产生的边距 不会紧贴右下角

# 5 常用编辑功能
le5=QLineEdit(wd)
le5.setPlaceholderText('常用功能测试')
le5.adjustSize()
le5.move(50,300)
    # QLineEdit文本框的右键菜单提供撤销、重复、复制、剪切、拷贝等常用功能，并支持快捷键的操作。
    # 退格
    	# backspace() 删除选中文本（如果有）或 删除光标 左侧 一个字符 
btn1=QPushButton(wd)
btn1.setText('退格 backspace')	
btn1.adjustSize()
btn1.move(200,300)
btn1.clicked.connect(lambda :(le5.backspace(),le5.setFocus())) # lambda :(语句1,语句2)
    # 删除
    	# del_() 删除选中文本（如果有）或 删除光标 右侧 一个字符 
btn2=QPushButton(wd)
btn2.setText('删除 del')	
btn2.adjustSize()
btn2.move(300,300)
btn2.clicked.connect(lambda :(le5.del_(),le5.setFocus()))

    # 清空 clear() 删除所有文本框内容
btn3=QPushButton(wd)
btn3.setText('清空 clear')	
btn3.adjustSize()
btn3.move(400,300)
btn3.clicked.connect(lambda : (le5.clear(),le5.setFocus()))
    # 复制 copy()
btn4=QPushButton(wd)
btn4.setText('复制 copy')	
btn4.adjustSize()
btn4.move(50,350)
btn4.clicked.connect(lambda : (le5.cursorBackward(True,4),print(le5.copy())))
    # 剪切 cut()
btn5=QPushButton(wd)
btn5.setText('剪切 cut')	
btn5.adjustSize()
btn5.move(150,350)
btn5.clicked.connect(lambda : (le5.setFocus(),le5.cursorBackward(True,2),le5.cut()))
    # 粘贴 paste()
btn6=QPushButton(wd)
btn6.setText('粘贴 paste')	
btn6.adjustSize()
btn6.move(250,350)
btn6.clicked.connect(lambda : le3.paste())
    # 撤消 undo()
        # isUndoAvailable() 
btn7=QPushButton(wd)
btn7.setText('撤消 undo')	
btn7.adjustSize()
btn7.move(50,400)
btn7.clicked.connect(lambda : le5.undo())
    # 重做 redo()
    	# isRedoAvailable()
btn8=QPushButton(wd)
btn8.setText('重做 redo')	
btn8.adjustSize()
btn8.move(150,400)
btn8.clicked.connect(lambda : le5.redo())
    # 拖放
    	# 设置是否可以拖拽 setDragEnabled(bool)
        # 用法 
            # 先设置可以拖拽
            # 再选中字符 变蓝

btn9=QPushButton(wd)
btn9.setText('设置拖放')	
btn9.adjustSize()
btn9.move(250,400)
btn9.clicked.connect(lambda : le5.setDragEnabled(True))

btn10=QPushButton(wd)
btn10.setText('取消拖放')	
btn10.adjustSize()
btn10.move(350,400)
btn10.clicked.connect(lambda : le5.setDragEnabled(False))

    # 文本选择 
        # 选中指定区间的文本      setSelection(start_pos, length)
btn11=QPushButton(wd)
btn11.setText('选择文本位置2长度5')	
btn11.adjustSize()
btn11.move(50,450)
btn11.clicked.connect(lambda : le5.setSelection(2, 5))
        # 选中所有文本            selectAll()
btn12=QPushButton(wd)
btn12.setText('选择所有文本')	
btn12.adjustSize()
btn12.move(200,450)
btn12.clicked.connect(lambda : le5.selectAll())
        # 取消选中已选择文本      deselect()
btn13=QPushButton(wd)
btn13.setText('取消选中文本')	
btn13.adjustSize()
btn13.move(300,450)
btn13.clicked.connect(lambda :le5.deselect())
        # 是否有选中文本          hasSelectedText()
        # 获取选中的文本          selectedText()
        # 选中的开始位置          selectionStart()
        # 选中的结束位置          selectionEnd()
        # 选中的长度              selectionLength()

# 6 信号
    # 文本编辑时发射的信号               textEdited(text)
    # 文本框文本发生改变时发出的信号      textChanged(text)
    # 按下回车键时发出的信号             returnPressed()不传递参数
    # 结束编辑时发出的信号               editingFinished()
    # 光标位置发生改变时发出的信号        cursorPositionChanged(int oldPos，int newPos)
    # 选中的文本发生改变时发出的信号      selectionChanged()

# textEdited(text)与textChanged(text)的区别
le5.textEdited.connect(lambda text:print('触发了textEdited',text))
le5.textChanged.connect(lambda text:print('触发了textChanged',text))
# 当采用代码方式输入的时候，textEdited是无法响应的
le5.setText('只触发了textChanged')
def change_select():
    print('改变了选中的文字,获取选中的文本',le5.selectedText())
le5.selectionChanged.connect(change_select)
wd.show()

app.exec_()