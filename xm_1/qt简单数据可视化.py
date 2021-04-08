# Qt数据可视化 https://doc.qt.io/qt-5/qtcharts-overview.html
from PySide2 import QtGui, QtWidgets
from PySide2.QtCharts import QtCharts

# 在Qt5.7版本后将Qt Charts加入到了Qt模块中。
# 我们可以方便的使用这个模块，绘制很多样式的图形，比如折线、饼图等，快速实现数据可视化。
# 用Qt Charts绘制，大概分为四个部分：
    # 数据（QXYSeries）、QChart(不知怎么称呼)、坐标轴（QAbstractAXis）和视图（QChartView）。
    # 要注意的是 QChart要先添加数据（QXYSeries）

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        series = QtCharts.QLineSeries()#定义线条 连续折线图
        # 加点 添加数据 
        series.append(0,0)
        series.append(1,7)
        series.append(1.2,14)
        series.append(1.3,21)
        series.append(1.4,28)
        series.append(1.5,35)

        self.chartView = QtCharts.QChartView() # 定义ui
        self.chartView.chart().addSeries(series) # 添加 线条 即 数据
        self.chartView.chart().createDefaultAxes() # 创建 坐标轴
        series.setColor(QtGui.QColor("salmon")) # 给线条设置颜色 salmon 橙红色，粉橙色

        self.setCentralWidget(self.chartView) # 给QMainWindow窗口设置中心部件，必须的

        

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())