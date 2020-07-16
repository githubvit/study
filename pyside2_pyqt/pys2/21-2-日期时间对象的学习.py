from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('日期时间对象的学习')
        self.setup_ui()

    def setup_ui(self):
        # 设置QDateTime对象
        # dt = QDateTime(2018, 12, 12, 12, 30) #（年，月，日，小时，分钟、秒）
        dt = QDateTime.currentDateTime()#直接用当前时间作为QDateTime对象
        # 可以为QDateTime对象单独改变年，月，日，小时，分钟、秒、毫秒等。
        # dt = dt.addYears(-2)
        # 获取QDateTime对象与当前世界标准时间Utc的差：dt.offsetFromUtc()
        # 结果是秒除以3600转换成小时，如果dt是当前时间，则结果为8.
        # print(dt.offsetFromUtc() // 3600)
        # # print(dt)
        # 在日期时间编辑器中看到设置的日期时间对象的结果
        QDateTimeEdit(dt, self)
        # QDate
        # QTime
        # 计时器 
        time = QTime.currentTime()
        time.start()
        btn = QPushButton(self)
        btn.setText("测试")
        btn.move(200, 200)
        # elapsed() 输出是毫秒
	    # start()和restart()两个方法启动后, 至此方法调用时, 经历的毫秒数
        btn.clicked.connect(lambda :(print(time.elapsed() / 1000,time.restart())))
        pass

if __name__ == "__main__":
    from PySide2.QtWidgets import *
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()