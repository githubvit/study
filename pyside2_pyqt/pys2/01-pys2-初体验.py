from PySide2.QtWidgets import QApplication,QWidget,QLabel

app=QApplication([])

wd=QWidget()
wd.setWindowTitle('标题')
wd.resize(500,500)
wd.move(400,200)

# lb=QLabel(wd)
# lb.resize(50,30)
# lb.setText('标签1')
lb=QLabel('标签',wd)
lb.move(200,200)

wd.show()

app.exec_()

