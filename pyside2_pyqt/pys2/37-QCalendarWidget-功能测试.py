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
        btn=QPushButton(self)
        btn.setText('弹出日历')
        btn.move(50,50)

        btn2=QPushButton(self)
        btn2.setText('测试常用方法')
        btn2.adjustSize()
        btn2.move(200,50)
        btn2.setEnabled(False)

        def calendarWidget_handel():
            cal=QCalendarWidget(self)
            cal.move(100,100)
            
            # 范围
            # cal.setMaximumDate(QDate(2222,2,22))
            # cal.setMinimumDate(QDate(1990,2,22))
            # cal.setDateRange(QDate(1990,2,22),QDate(2222,2,22))
            
            # print(cal.isDateEditEnabled()) #True 默认可编辑
            # cal.setDateEditEnabled(False) # 这里的不能编辑，仅仅指键盘，鼠标和滚轮不受影响，可以改变日期。

            # cal.setDateEditAcceptDelay(30000) # 延时生效 无效
            # 设置无法选中日期 
            # cal.setSelectionMode(QCalendarWidget.NoSelection) #年、月可以更改 选中的日期不能更改 用代码可以改
            # 设置默认
            # cal.setSelectedDate(QDate(2019,6,12))
            

            # 设置导航条
            # cal.setNavigationBarVisible(False) # 设置导航条不可见 无法调整年月
            # 设置一周的第一天 设为 周日 默认周一
            cal.setFirstDayOfWeek(Qt.Sunday)
            cal.setGridVisible(True) #网格可见
            
            # 设置文本格式
            tcf=QTextCharFormat()
            tcf.setFontFamily('隶书')
            tcf.setFontPointSize(16)
            cal.setHeaderTextFormat(tcf)        # 设置水平头和垂直头文件格式 即 星期 和 
            # 单独设置水平头中文显示星期几
            cal.setHorizontalHeaderFormat(QCalendarWidget.LongDayNames)
            # 隐藏水平头或垂直头
            # cal.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)#隐藏垂直头

            # 设置每周中的某一天文本格式
            tcf2=QTextCharFormat()
            tcf2.setFontFamily('幼圆')
            tcf2.setFontPointSize(24)
            tcf2.setFontWeight(100)
            tcf2.setToolTip('星期二 该收账了')
            # cal.setWeekdayTextFormat(Qt.Tuesday,tcf2)
           
            # 设置某一天的文本格式
            tcf3=QTextCharFormat()
            tcf3.setFontFamily('幼圆')
            tcf3.setFontPointSize(24)
            # tcf3.setFontItalic(True)
            tcf3.setFontWeight(100)
            tcf3.setToolTip('博骞考试日')
            cal.setDateTextFormat(QDate(2020,6,27),tcf3)#就这一天的字体变大了
            cal.show()

            # 获取 展示
            print(cal.yearShown())
            print(cal.monthShown())
            # 获取 选中 按回车后的日期
            print(cal.selectedDate())

            # 日历滚动常用方法
            # showToday()
            # showSelectedDate()
            # showNextYear()
            # showPreviousYear()
            # showNextMonth()
            # showPreviousMonth()
            # setCurrentPage(int year, int month)
            btn2.setEnabled(True)
            # btn2.clicked.connect(lambda:(cal.showToday(),cal.setFocus()))        #滚动到今天
            # btn2.clicked.connect(lambda:(cal.showSelectedDate(),cal.setFocus()))   #滚动到选中的那一天
            # btn2.clicked.connect(cal.showNextYear) #跳转到下一年，点击一次加一年
            # btn2.clicked.connect(cal.showPreviousYear) 
            # btn2.clicked.connect(cal.showNextMonth) #跳转到下一月，点击一次加一月
            # btn2.clicked.connect(cal.PreviousMonth)
            btn2.clicked.connect(lambda:(cal.setCurrentPage(2020,8),cal.setFocus())) # 滚到设定的某年某月的那一页
           
         

            # 信号
            # activated(QDate date)
            	# 只要用户按下Return或Enter键或双击日历小部件中的日期，就会发出此信号。
            cal.activated.connect(lambda date: print('双击或回车',date))
           
            # clicked(QDate date)
            	# 单击有效日期时才会发出信号
            cal.clicked.connect(lambda date: print('单击日期',date))
            
            # currentPageChanged(int year, int month)
            	# 当前显示的月份更改时会发出此信号。新的一年和一个月作为参数传递。
            cal.currentPageChanged.connect(lambda y,m: print('导航条变化了年或月',y,m))  
           
            # selectionChanged() 无参
            	# 当前选择的日期更改时会发出此信号
            		# 鼠标
            		# 代码 
            cal.selectionChanged.connect(lambda : print('选中的日期变化'))


        btn.clicked.connect(calendarWidget_handel)    
        

        pass
if __name__ == "__main__":
    app = QApplication([])
    wd=Window()
    wd.show()
    app.exec_()