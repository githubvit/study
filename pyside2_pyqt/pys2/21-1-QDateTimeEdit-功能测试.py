from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('日期时间编辑器QDateTimeEdit的学习')
        self.setup_ui()

    def setup_ui(self):
        # 构造函数
        dte = QDateTimeEdit(self)
        # dte = QDateTimeEdit(QDateTime.currentDateTime(), self)
        # dte = QDateTimeEdit(QDate.currentDate(), self)
        # dte = QDateTimeEdit(QTime.currentTime(), self)
        dte.move(100, 100)
        # 设置日期时间格式
            # 日期
	            # d       没有前导零的数字的日期（1到31）
	            # dd      有前导零的数字的日期（01到31）
	            # ddd     缩写的本地化日期名称（例如'Mon'到'Sun'
	            # dddd    完整本地化的日期名称（例如“星期一”到“星期日”）
	            # 
                # M       没有前导零的数字的月份（1-12）
	            # MM      月份为前导零的数字（01-12）
	            # MMM     缩写的本地化月份名称（例如'Jan'到'Dec'）
	            # MMMM    完整的本地化月份名称（例如“1月”到“12月”）
	            # 
                # yy      年份为两位数字（00-99）
	            # yyyy    年份为四位数字
            # 时间
	            # h       没有前导零的小时（如果显示AM / PM，则为0到23或1到12）
	            # hh      前导零的小时（如果AM / PM显示，则为00到23或01到12）
	            # 
                # H       没有前导零的小时（0到23，即使有AM / PM显示）
	            # HH      前导零的小时（00到23，即使有AM / PM显示）
	            # 
                # m       没有前导零的分钟（0到59）
	            # mm      前导零（00到59）的分钟
	            # 
                # s       整个秒没有前导零（0到59）
	            # ss      带有前导零（00到59）
	            # 
                # z       第二个小数部分, 没有尾随零的毫秒（0到999）
	            # zzz     第二个小数部分, 有尾随零的毫秒（000到999）
	            # 
                # AP / A  使用AM / PM显示
	            # ap / a  使用am / pm显示
	            # 
                # t       时区
        dte.setDisplayFormat("yy-MM-dd $ m: ss: zzz")

        btn = QPushButton(self)
        btn.move(200, 200)
        btn.setText("测试")
        def test():
            # print("xxx")
            # 获取当前 Section 索引值（从0计算） 
            print(dte.currentSectionIndex())

            # 小技巧：先把光标锁定在文本框 
            # 避免后面 setCurrentSectionIndex(3) 看不出来
            dte.setFocus()

            # 根据Section索引设置当前Section
            # 设定3号Section为当前Section
            # dte.setCurrentSectionIndex(3)

            # 根据Section类别设置当前Section
            # 设定 日 Section 为 当前Section 
                # 各种Section
                    # QDateTimeEdit.NoSection
                    # QDateTimeEdit.AmPmSection
                    # QDateTimeEdit.MSecSection
                    # QDateTimeEdit.SecondSection
                    # QDateTimeEdit.MinuteSection
                    # QDateTimeEdit.HourSection
                    # QDateTimeEdit.DaySection
                    # QDateTimeEdit.MonthSection
                    # QDateTimeEdit.YearSection
            # dte.setCurrentSection(QDateTimeEdit.DaySection)
            # 获取 日Section 的文本
            # print(dte.sectionText(QDateTimeEdit.DaySection))
            
            # 设定最大日期时间
            # dte.setMaximumDateTime(QDateTime(2022, 8, 15, 12, 30))
            # dte.clearMaximumDateTime() #清除最大日期时间
            # 日期和时间都可以单独设置或清除最大最小
            # #dte.setMaximumDate(QDate(y,m,d))
            # #dte.setMaximumTime(QTime(h,m,s))
            # 设定最小日期时间
            # dte.setMinimumDateTime(QDateTime.currentDateTime())
            # dte.clearMinimumDateTime() #清除最小日期时间

            # 设定日期范围
            dte.setDateTimeRange(QDateTime.currentDateTime().addDays(-3), QDateTime.currentDateTime().addDays(3))
            
            # print(dte.dateTime())
            print(dte.date())
            print(dte.time())

        btn.clicked.connect(test)
        # 获取总共几段
        print(dte.sectionCount())

        # 上下按钮 变为 弹出 日历控件 
        dte.setCalendarPopup(True)
        # 信号
        dte.dateTimeChanged.connect(lambda val:print(val))
        dte.dateChanged.connect(lambda val: print("日期发生改变", val))
        dte.timeChanged.connect(lambda val: print("时间发生改变", val))

        pass

if __name__ == "__main__":
    from PySide2.QtWidgets import *
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()