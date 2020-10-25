from PySide2.QtWidgets import *

app=QApplication([])
wd=QWidget()
wd.setWindowTitle('框架QFrame的学习')
wd.resize(500,500)

# 是一个基类, 可以选择直接使用
# 主要是用来控制一些边框样式 例如凸起、凹下、阴影、线宽
frame=QFrame(wd)
frame.resize(300,300)
frame.move(50,50)
# 形状 阴影 线宽
# 形状类别  
    # QFrame.NoFrame    QFrame什么都没画
    # QFrame.Box	    QFrame围绕其内容绘制一个框
    # QFrame.Panel      QFrame绘制一个面板，使内容显得凸起或凹陷
    # QFrame.HLine      QFrame绘制一条没有框架的水平线（用作分隔符）
    # QFrame.VLine      QFrame绘制一条无框架的垂直线（用作分隔符）
    # QFrame.StyledPanel
        # 绘制一个矩形面板，其外观取决于当前的GUI样式。它可以升起或凹陷。
        # 绘制一个可以像Windows 2000中那样凸起或凹陷的矩形面板。
    # QFrame.WinPanel
        # 指定此形状可将线宽设置为2像素。WinPanel是为了兼容性而提供的。
        # 对于GUI样式独立性，建议使用StyledPanel。
# 设置形状
# frame.setFrameShape(QFrame.Box)
# frame.setFrameShape(QFrame.Panel)
# frame.setFrameShape(QFrame.HLine)

# 设置框架边框阴影
# frame.setFrameShadow(QFrame.Raised)
# 阴影类别
	# QFrame.Plain    框架和内容与周围环境呈现水平;（没有任何3D效果）
	# QFrame.Raised   框架和内容出现; 使用当前颜色组的浅色和深色绘制3D凸起线
	# QFrame.Sunken   框架和内容出现凹陷; 使用当前颜色组的浅色和深色绘制3D凹陷线
frame.setStyleSheet('background-color:cyan')		
 
# 框架样式
    # 上方的形状和阴影的组合设置  setFrameStyle(shape | shadow)
# frame.setFrameStyle(QFrame.Box | QFrame.Raised)	

# 线宽
    # 通过控制线宽, 来达到不同的组合效果

	# 外线宽度 setLineWidth(int width)  lineWidth()
	# 中线宽度 setMidLineWidth(int width)  midLineWidth()
	# 总宽度 frameWidth()   
# frame.setLineWidth(10)
# frame.setMidLineWidth(12)
# print(frame.frameWidth()) # 32=10+12+10
 
# 框架矩形
from PySide2.QtCore import QRect 
frame.setFrameRect(QRect(20, 20, 60, 60))

# frame.setFrameStyle(QFrame.Panel | QFrame.Sunken)	# 面板类型就没有中线
# frame.setFrameStyle(QFrame.Panel | QFrame.Raised)	# 面板类型就没有中线
# frame.setFrameStyle(QFrame.Box | QFrame.Raised)	# 面板类型就没有中线
frame.setFrameStyle(QFrame.Box | QFrame.Sunken)	# 面板类型就没有中线
frame.setLineWidth(5)


wd.show()
app.exec_()