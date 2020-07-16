# 描述
	# 展示LCD样式的数字
	# 它可以显示几乎任何大小的数字
	# 它可以显示十进制，十六进制，八进制或二进制数
	# 能够展示的字符
	    # 0/O, 1, 2, 3, 4, 5/S, 6, 7, 8, 9/g
	    # A, B, C, D, E, F, h, H, L, o, P, r, u, U, Y
	    # : ' 空格

# 继承
	# QFrame

# 功能作用
	# 构造函数
		# QLCDNumber(parent: QWidget = None)
		# QLCDNumber(int, parent: QWidget = None)
			# 参数1代表展示的数值位数

	# 设置显示数值
		# display(str)
		# display(float)
		# display(int)
		# intValue() -> int
		# value() -> float

	# 位数限制
		# setDigitCount(int)
		# digitCount() -> int

	# 模式设置
		# setMode(self, QLCDNumber.Mode)
		# mode(self) -> QLCDNumber.Mode
			# QLCDNumber.Hex
				# 十六进制
			# QLCDNumber.Dec
				# 十进制
			# QLCDNumber.Oct
				# 八进制
			# QLCDNumber.Bin
				# 二进制
		# 快捷
			# setHexMode（）
			# setDecMode（）
			# setOctMode（）
			# setBinMode（）

	# 溢出
		# checkOverflow(self, float) -> bool
		# checkOverflow(self, int) -> bool
        
	# 分段样式
		# setSegmentStyle(self, QLCDNumber.SegmentStyle)
		# segmentStyle(self) -> QLCDNumber.SegmentStyle
			# Outline
				# 生成填充了背景颜色的凸起部分
			# Filled
				# 默认值
				# 生成填充前景色的凸起部分。
			# Flat
				# 生成填充前景色的平坦段。

# 信号
	# overflow()
		# 数据溢出时发射

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('LCD数字显示控件QLCDNumber的学习')
        self.setup_ui()

    def setup_ui(self):
        
        # ld=QLCDNumber(self)# 代表显示的位数是2位
        # ld.setDigitCount(5) # 显示位数限制

        ld=QLCDNumber(5,self)# 5 代表显示的位数限制 这种构造函数取代了上面两步
        # ld.adjustSize()
        ld.resize(100,50) #控件越小越淡
        ld.setStyleSheet('background-color:#fff;border:1px solid #ddd')
        ld.move(20,20)
        

        # 1 显示数值 三种方式
        # 显示int数字
        # ld.display(88)
        # ld.display(12345) 
        # ld.display(123456) # 超过位数限制 结果显示0
        

        # 显示float数字
        # 如果整数部分不超过位数，就四舍五入。
        # 整数部分包含负号
        # ld.display(88.885) # 四舍五入 显示 88.89
        # ld.display(88.8849) # 显示 88.88
        

        # 显示str数字或特殊字符
        # ld.display('12345')
        # ld.display('123456') # 操过结果显示 23456 显示后5位

        # 特殊字符
            # 0/O, 1, 2, 3, 4, 5/S, 6, 7, 8, 9/g
            # A, B, C, D, E, F, h, H, L, o, P, r, u, U, Y
            # : ' 空格
        # ld.setDigitCount(30)
        # ld.resize(400,50)
        # ld.display('ABCDEFghHLoOPruUY') #AbCdEF9hHLo0PruUy
        '''
         _     _     _  _  _              _  _             
        |_||_ |   _||_ |_ |_||_ |_||   _ | ||_| _    | ||_|
        | ||_||_ |_||_ |   _|| || ||_ |_||_||  |  |_||_| _|

         _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _ 
        |_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_|
        |_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_|
        
        '''

        # 2 获取数值 两种方式 
        
        # ld.display(88854.66) # 显示 88855
        # 获取浮点数
        # print(ld.value()) # 浮点展示结果 88854.66
        # 获取整型数
        # print(ld.intValue()) # 整型展示结果 88855

        # ld.display(-88854.66) # 整型部分已经超出 显示0
        # print(ld.value()) # 浮点展示结果 -88854.66
        # print(ld.intValue()) # 整型展示结果 -88855

        # ld.display(-8854.66) # 显示-8855 
        
        # 3 数字模式  显示不同进制数
        ld.display(12)
        # ld.setHexMode() #十六进制 显示 c
        # ld.setOctMode() #八进制 14
        # ld.setBinMode() #二进制1100
        # ld.setDecMode() #默认十进制 12

        # 4 信号 溢出 
        # 判断是否溢出
        print(ld.checkOverflow(99999)) #False
        print(ld.checkOverflow(100000)) #True 产生溢出 展示 结果就会是0 并且会产生溢出信号overflow
        ld.overflow.connect(lambda : print('溢出')) 
        ld.display(100000) # 如果前面有非溢出的显示 该display就不会展示0，会展示前面非溢出的数字，但是会发射信号，打印溢出。


        


      



        pass


if __name__ == "__main__":
    app = QApplication([])
    wd=Window()
    wd.show()
    app.exec_()