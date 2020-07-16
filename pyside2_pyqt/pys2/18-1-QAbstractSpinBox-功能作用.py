# 步长调节 输入控件
# 是组合控件 由一个步长调节器和单行文本框来调节和显示数据
# QAbstractSpinBox是这类控件的抽象类，要使用该类就要子类化
# 系统子类化的有 离散数和整型变量调节 QSpinBox、浮点数调节 QDoubleSpinBox、日期调节 QDateTimeEdit

# QAbstractSpinBox的使用
	# 1. 子类化此类
	# 2. 实现控制上下能用的方法
		# stepEnabled(self) -> QAbstractSpinBox.StepEnabled
			# QAbstractSpinBox.StepNone
				# 都不能用
			# QAbstractSpinBox.StepUpEnabled
				# 上可用
			# QAbstractSpinBox.StepDownEnabled
				# 下可用
	# 3. 实现步长调整方法
		# stepBy(self, p_int)

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
class MyAbs(QAbstractSpinBox):
    def __init__(self,parent,num=0):
        super().__init__(parent)
        self.lineEdit().setText(str(num)) # 初始化，默认数字为0
        
    # 实现控制上下按钮
    def stepEnabled(self):
        # 如果为空
        if not len(self.text().strip()):
            return  QAbstractSpinBox.StepNone #上下都不可用
        # 设置自然数
        if int(self.text())<=0:
            return QAbstractSpinBox.StepUpEnabled #上可用
        # 其余 上下都可用
        return QAbstractSpinBox.StepUpEnabled | QAbstractSpinBox.StepDownEnabled
        pass

    # 实现步长变化
    def stepBy(self,p_int):
        # print(p_int)
        # current_num=int(self.text())+p_int
        current_num=int(self.text())+p_int*2 # 改变步长
        # 反向设置
        # 步长调节器本身没有setText方法，步长调节器中有一个文本输入框，这个文本输入框有setText.
        self.lineEdit().setText(str(current_num))
        
        pass

    # 实现验证器 避免输入非数字字符
    def validate(self, input_text, pos):
        print(input_text)
        # 保证输入的是数字 并且 大于等于0
        if input_text.isdigit() and int(input_text) >= 0:
            return (QValidator.Acceptable,  input_text, pos) #在范围内 验证通过 
        elif not len(input_text.strip()): #如果清空
            return (QValidator.Intermediate,  input_text, pos) # 暂不作判定是否通过验证 结束时 调用fixup修复方法 只调用一次
        else:
            return (QValidator.Invalid,  input_text, pos) # 验证不通过 不让输入

    def fixup(self,input_text):
        print('清空则改为0')
        self.lineEdit().setText('0') #直接改
        return '18' #这个并没有输入进文本框 说明有bug 改用上面的输入方式 直接输入文本框

    pass

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('步长调节器QAbstractSpinBox的学习')
        self.setup_ui()

    def setup_ui(self):
        abs=MyAbs(self,6)
        abs.move(50,50)
        abs.resize(100,30)

        le=QLineEdit(self)
        le.move(200,50)
        le.resize(100,30)
        le.setPlaceholderText('让步长调节器失去焦点')


        # 设置加速 如果按住上或下不放，那么增加或减少的速度 会不断增加。否则，保持匀速增减。
        # print(abs.isAccelerated()) # False
        abs.setAccelerated(True)

        # 只读 指不能通过键盘 只能通过上下按钮调节
        print(abs.isReadOnly()) # False
        # abs.setReadOnly(True)

        # 输入文本
        # 步长调节器本身没有setText方法，步长调节器中有一个文本输入框，这个文本输入框有setText.
        abs.lineEdit().setText('88')
        
        # 设置对齐 默认是左对齐
        # abs.setAlignment(Qt.AlignCenter) 

        # 设置周边框架 默认是有的
        print(abs.hasFrame()) # True
        # abs.setFrame(False)

        # 清空
        # abs.clear()

        # 设置上下按钮
        # 不显示        QAbstractSpinBox.NoButtons ,
        # '+' '-'显示   QAbstractSpinBox.PlusMinus , 没有用
        # 上下箭头      QAbstractSpinBox.UpDownArrows  默认。
        # abs.setButtonSymbols(QAbstractSpinBox.NoButtons)
        # 可用键盘上下键，或鼠标滚轮调节。

        pass

if __name__ == "__main__":
    from PySide2.QtWidgets import *
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()