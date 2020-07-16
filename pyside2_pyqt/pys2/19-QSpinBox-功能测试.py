from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# 用自定义展示格式 展示星期
class MySpinBox(QSpinBox):
    # 重写 textFromValue(self, p_int)
    # 不同的value 展示不同的text
    def textFromValue(self, p_int):
        # print(p_int)
        if p_int==1:
            return '周一'
        elif p_int==2:
            return '周二'
        elif p_int==3:
            return '周三'
        elif p_int==4:
            return '周四'
        elif p_int==5:
            return '周五'
        elif p_int==6:
            return '周六'
        else:
            return '周日'


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('整型和离散调节QSpinBox的学习')
        self.setup_ui()

    def setup_ui(self):
        self.sb=QSpinBox(self)
        self.sb.resize(100,25)
        self.sb.move(50,50)
        # 默认最大99 最小0 步长1

        #步长设置
        # self.sb.setSingleStep(3)
        #进制设置
        # print(self.sb.displayIntegerBase()) #10
        # self.sb.setDisplayIntegerBase(2)#二进制最大1100011 还是10进制的99 
        
        # self.最大值最小值()
        # self. 数值循环()
        # self.前缀和后缀()
        self.设置以及获取数值()
        self.星期展示案例()
        
        pass
        # 自定义展示格式
	        # API
	        	# 重写
	        		# textFromValue(self, p_int) -> format_str
	        # 应用场景
	        	# 展示数值之前, 调用此方法, 转换成对应的格式字符串进行展示
	        # 案例
	        	# 测试以上API

    def 星期展示案例(self):
        # 用自定义展示格式
        self.sb1=MySpinBox(self)
        self.sb1.resize(100,25)
        self.sb1.move(100,100)
        # 设置范围
        self.sb1.setRange(0,6)
        # 设置循环
        self.sb1.setWrapping(True)

        # 信号 valueChanged 参数可以是value也可以是text 
        # 同一个信号 当有不同的参数类型可以选择，用[type]选择
        # 取值 value 默认
        self.sb1.valueChanged.connect(lambda arg: print(type(arg), arg)) #<class 'int'> 1
        # self.sb1.valueChanged[int].connect(lambda arg: print(type(arg), arg)) #<class 'int'> 1
        # 取显示的文本 text
        # self.sb1.valueChanged[str].connect(lambda arg: print(type(arg), arg)) #<class 'str'> 周一

        pass
    
   
    def 设置以及获取数值(self):
        # value 和 str
        self.sb.setRange(0, 9)
        self.sb.setPrefix("撩课")
        self.sb.setValue(66) # 超出了范围，取最大值或最小值
        print(self.sb.value())  # int 9
        print(self.sb.text())   # str  撩课9
        print(self.sb.lineEdit().text()) # str 撩课9
        pass

    def 前缀和后缀(self):
        # 设定循环
        self.sb.setWrapping(True)
        # 设置月份
        # self.sb.setRange(1, 12)
        # 后缀
        # self.sb.setSuffix("月")

        # 设置星期
        self.sb.setRange(0, 6)
        # 前缀
        self.sb.setPrefix("周")
        # 当数据到达最小值时, 会显示此字符串
        self.sb.setSpecialValueText("周日")
        pass
        
    def 数值循环(self):
        #  当最小时，按向下，会跳到最大。
        #  当最大时，按向上，会跳到最小。
        #  转圈圈
        #  默认是没有的
        print(self.sb.wrapping())#False
        self.sb.setWrapping(True)
        print(self.sb.wrapping())#True

    def 最大值最小值(self):
        # self.sb.setMaximum(180)
        # print(self.sb.maximum())
        #
        # self.sb.setMinimum(18)
        # print(self.sb.minimum())

        # 设置范围
        self.sb.setRange(18, 180) # 注意可以取到180 
        
if __name__ == "__main__":
    from PySide2.QtWidgets import *
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()