from PySide2.QtWidgets import *
from PySide2.QtCore import *
app=QApplication([])

window=QMainWindow()

window.setWindowTitle('信息提示')
window.resize(500,500)

# 1 状态提示

# 加载或称启动状态栏 
window.statusBar() #一定要有这行 状态提示才有用
# 设置状态提示 是懒加载方式 在窗口里才会显示
window.setStatusTip('状态栏提示')

# 2 工具提示
lb=QLabel(window)
lb.setText('这是一个标签')
lb.move(50,50)
lb.setToolTip('工具提示')
lb.setStatusTip('标签状态栏提示')
# 工具提示时长 2秒
lb.setToolTipDuration(2000)

# 3 帮助提示 这是啥提示
window.setWindowFlags(Qt.WindowContextHelpButtonHint)
lb.setWhatsThis('帮助提示')
window.show()

app.exec_()