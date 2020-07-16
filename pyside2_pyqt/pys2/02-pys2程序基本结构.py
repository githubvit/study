# 0. 导包
from PySide2.QtWidgets import QApplication,QWidget,QLabel

# 1. 创建应用程序对象
app=QApplication(['1','3'])
# print(app.arguments())

# 2. 控件操作 界面的内容都在这

# 创建控件,设置控件(大小,位置,样式...),事件,信号的处理
# 没有父控件的控件，就是顶层控件
wd=QWidget()
wd.setWindowTitle('标题')
wd.resize(400,400)
wd.move(400,200)

lb=QLabel('标签',wd)
lb.move(200,200)


# 3. 控件展示
wd.show()

# 4. 应用程序执行 
# 进入消息循环 阻塞
app.exec_()

# 5. 程序结束后操作 如果有
# 程序关闭后 阻塞结束 执行如下代码
if app.arguments()[1]=='2':
    print('xx')
else:
    print('oo')