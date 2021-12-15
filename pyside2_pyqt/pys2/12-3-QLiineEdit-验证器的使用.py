from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

# 规则验证之文本框验证器验证
# 根据验证规则设置验证器 QValidator 
# QValidator 是一个抽象类, 使用前需要进行子类化操作
	# 自定义子类
	# 系统提供子类
		# QIntValidator(bottom, top, parent)
			# 限制整型数据范围
		# QDoubleValidator
			# 浮点类型数据限制范围
			# 经测试, 无效
				# 需要手动实现
		# QRegExpValidator
			# 通过正则表达式限定

# 用定义好的验证器子类 设置文本框验证 实时跟踪验证输入的内容 判断输入的合法性
    # 设置验证器 setValidator(QValidator)
	

    # 验证器的验证方法：
        # validate(self, input_text, pos)
        	# return (QValidator.Acceptable,  input_text, pos)
        		# 验证通过
        	# return (QValidator.Intermediate,  input_text, pos)
        		# 暂不作判定是否通过验证，让继续输入文本框
                # 结束输入时，如果还是该状态，就会调用fixup修复，只调用一次
        	# return (QValidator.Invalid,  input_text, pos)
        		# 输入内容验证不通过
                # 不让显示在文本框 输不进去

    # 如果输入框结束输入后, 上述的验证状态为暂不作判定QValidator.Intermediate,
    # 则会调用修复方法，只会修复一次
    	# fixup(self, input_text)
    		# return 修正后文本

# 系统提供子类
	# QIntValidator(bottom, top, parent)
		# 限制整型数据范围
	# QDoubleValidator
		# 浮点类型数据限制范围
		# 经测试, 无效
		# 需要手动实现
	# QRegExpValidator
		# 通过正则表达式限定

# 自定义限制整型数据范围 CustomIntValidator 类

# 验证器 设置
# 1 子类化 QValidator抽象类
class CustomIntValidator(QValidator):
    # 初始化 整型范围
    def __init__(self,min,max):
        super().__init__()
        self.min=min
        self.max=max
    # 2 实现验证方法
    def validate(self, input_text, pos):#pos光标位置就是指 文本框的第几个字符
        print(input_text,pos)
        try:
            if self.min<=int(input_text)<=self.max:
                return (QValidator.Acceptable,  input_text, pos) #在范围内 验证通过
            elif 1<=int(input_text) <= self.min-1:
                return (QValidator.Intermediate,  input_text, pos) # 暂不作判定是否通过验证 结束时 调用fixup修复方法 只调用一次
            else:
                return (QValidator.Invalid,  input_text, pos) # 验证不通过 不让输入
        except:
            if len(input_text) == 0:
                return (QValidator.Intermediate,  input_text, pos) # 暂不作判定是否通过验证 结束时 调用fixup修复方法 只调用一次
            return (QValidator.Invalid,  input_text, pos) # 验证不通过 不让输入

    # 3 实现修复方法
    def fixup(self,input_text):
        print('调用了修复方法1',input_text)
        if len(input_text) == 0 or int(input_text)<=self.min-1:
            return str(self.min) #返回修复后的字符串数据

# 继承QIntValidator系统类 实现修复
class MyIntValidator(QIntValidator):
    def fixup(self,input_text):
        print('调用了修复方法2',input_text,self.bottom())
        if len(input_text) == 0 or int(input_text)<=self.bottom()-1:
            return str(self.bottom()) #返回修复后的字符串数据
        return str(self.top())

app=QApplication([])
wd=QWidget()
wd.resize(500,500)

le1=QLineEdit(wd)
le1.setPlaceholderText('请输入数字')
le1.adjustSize()
le1.move(50,50)
# 用 自定义限制整型数据范围 验证器 实时验证
# vor=CustomIntValidator(min=18,max=180)
# 用 系统自带的限制整型数据范围 验证器 QIntValidator 实时验证 
# vor=QIntValidator(18,180) # 对于 结束时 暂不作判定状态 
# 继承QIntValidator系统类 实现修复
vor=MyIntValidator(18,180)
le1.setValidator(vor)

le2=QLineEdit(wd)
le2.setPlaceholderText('使le1失去焦点')
le2.move(50,100)

wd.show()

app.exec_()


