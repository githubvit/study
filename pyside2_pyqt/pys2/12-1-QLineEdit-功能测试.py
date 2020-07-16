from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

app=QApplication([])
wd=QWidget()
wd.setWindowTitle('单行文本框QLineEdit功能')
wd.resize(500,500)

le=QLineEdit(wd)
le.setPlaceholderText('文本框')
le.move(50,50)
le2=QLineEdit(wd)
le2.move(50,100)
# 一 文本的设置和获取
# 1 setText(str)
	# 设置内容文本 覆盖原内容
# 2 insert(newText)
	# 在光标处插入文本
# 3 text()
	#针对密文而言 获取真实内容文本 
# 4 displayText()
	#针对密文而言 获取用户能看到的内容文本 

# 在文本框1，2中设置内容文本，点击插入按钮在文本框1插入文本框2中输入的内容
le.setText('只在此山中')
le2.setText('云深不知处')
c_btn=QPushButton('插入1',wd)
c_btn.move(200,100)
c_btn.clicked.connect(lambda : le.insert(le2.text()))

# 清空文本框
q_btn=QPushButton('清空1',wd)
q_btn.move(200,50)
# q_btn.clicked.connect(lambda : le.setText('')) # 设置空字符串 即可
q_btn.clicked.connect(lambda : le.clear()) # 正统方法

# 二 文本的输出模式

# setEchoMode(QLineEdit.EchoMode)
	# NoEcho = 1
	    # 不输出 设置为不输出，依然能够获取输入的text
        # 用按钮和鼠标无法删除文本框的内容
        # 输入的内容永远在最前
	# Normal = 0
	    # 正常输出
	# Password = 2
	    # 密文形式
	# PasswordEchoOnEdit = 3
	    # 编辑时明文, 结束后密文
# 设置le2的输出模式
s_btn1=QPushButton('不输出',wd)
s_btn1.setToolTip('设置le2的输出模式 NoEcho = 1')
s_btn1.move(50,150)
def Set_NoEcho():
    le2.setEchoMode(QLineEdit.NoEcho)
    print(le2.echoMode())
s_btn1.clicked.connect(Set_NoEcho)

s_btn2=QPushButton('正常输出',wd)
s_btn2.setToolTip('设置le2的输出模式 Normal = 0')
s_btn2.move(150,150)
def Set_Normal():
    le2.setEchoMode(QLineEdit.Normal)
    print(le2.echoMode())
s_btn2.clicked.connect(Set_Normal)

s_btn3=QPushButton('密文形式',wd)
s_btn3.setToolTip('设置le2的输出模式 Password = 2')
s_btn3.move(250,150)
def Set_Password():
    le2.setEchoMode(QLineEdit.Password)
    print(le2.echoMode())
s_btn3.clicked.connect(Set_Password)

s_btn4=QPushButton('编辑时明文, 结束后密文',wd)
s_btn4.setToolTip('设置le2的输出模式 PasswordEchoOnEdit = 3')
s_btn4.move(350,150)
def Set_PasswordEchoOnEdit():
    le2.setEchoMode(QLineEdit.PasswordEchoOnEdit)
    print(le2.echoMode())
s_btn4.clicked.connect(Set_PasswordEchoOnEdit)

# 三 输入限制
# 1 长度限制
	# setMaxLength(int)
		# 设置限制输入的长度 字符个数
	# maxLength()
		# 获取输入长度

le3=QLineEdit(wd)
le3.setPlaceholderText('输入长度限制3字符')
le3.move(50,200)
le3.adjustSize()
le3.setMaxLength(3) #最长只能3个英文或中文字符。
le3.setText('4个字符') #只能显示 4个字，符 字不能显示 通过代码不能改变
print('长度限制',le3.text())# 获取的文本也就是 4个字。

# 2 只读限制 
	# setReadOnly(bool)
	# isReadOnly()
le4=QLineEdit(wd)
le4.setPlaceholderText('只读限制')
le4.move(200,200)
le4.adjustSize()
print('是否只读',le4.isReadOnly())
le4.setText('只读限制123')
le4.setReadOnly(True)
le4.setText('改变只读限制') # 通过代码可以改变

# 3 规则限制之掩码验证
# 用来控制输入的格式
# 掩码由 一串掩码字符和分隔符组成 + 可选的分号; 和 空白占位字符
# 例如 座机号码 四位区号-七位电话  IP地址 XXX.XXX.XXX.XXX
# 
le5=QLineEdit(wd)
le5.setPlaceholderText('规则验证之掩码限制')
le5.move(50,250)
le5.adjustSize()
# 设置 两位大写字母+'-'分隔符+两位数字 掩码 这样 不符合掩码规则的就输入不了
# le5.setInputMask('>AA-99')
# le5.setInputMask('>AA-99;#') # 分号后是空白占位符
# 设置座机号码掩码
# le5.setInputMask('9999-9999999;0')
# 设置Ip地址
le5.setInputMask('999.999.999.999;x')#可以结合验证器限制每段在255以内
# le5.setInputMask('000.000.000.000;_')  #"数字掩码"
# 
# le5.setInputMask('HH:HH:HH:HH:HH:HH;_') #"MAC掩码" 
# 
# le5.setInputMask('0000-00-00')       # "日期掩码“
# 
# le5.setInputMask('>AAAA-AAAA-AAAA-AAAA-AAAA;#') #"许可证掩码",

# 掩码字符表
	# 字符	含义
	# A	ASCII字母字符是必须输入的（A-Z，a-z）
	# a	ASCII字母字符是允许输入的，但不是必须输入的
	# N	ASCII字母字符是必须输入的（A-Z，a-z，0-9）
	# n	ASCII字母字符是允许输入的，但不是必须输入的
	# X	任何字符都是必须输入
	# x	任何字符都是允许输入的，但不是必须输入的
	# 9	ASCII数字字符是必须输入的（0-9）
	# 0	ASCII数字字符是允许输入的，但不是必须输入的
	# D	ASCII数字字符是必须输入的（1-9）
	# d	ASCII数字字符是允许输入的，但不是必须的（1-9）
	# # ASCII数字字符与加减字符是允许输入的，但不是必须的
	# H	十六进制格式字符是必须输入的（A-F，a-f，0-9）
	# h	十六进制格式字符允许输入，但不是必须的
	# B	二进制格式字符是必须输入的（0,1）
	# b	二进制格式字符是允许输入的，但不是必须的
	# >	所有字母字符都大写
	# <	所有字母字符都小写
	# !	关闭大小写转换
	# \	使用‘\’转义上面列出的字符


wd.show()

app.exec_()