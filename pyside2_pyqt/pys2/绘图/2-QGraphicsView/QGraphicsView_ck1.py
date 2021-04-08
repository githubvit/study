from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap,QRadialGradient,QPen,QPainterPath)
from PySide2.QtWidgets import *

# 用QGraphicsView，QGraphicsScene加各样的item实现，可以留下更多功能实现的余地，
# UI使用设计器生成，后面又修改一点.
class MyScene(QGraphicsScene):#自定场景
    pen_color=Qt.black #预设笔的颜色
    pen_width=5 #预设笔的宽度
    def __init__(self):#初始函数
        super(MyScene, self).__init__() #实例化QGraphicsScene
        self.setSceneRect(0,0,800,600) #设置场景起始及大小，默认场景是中心为起始，不方便后面的代码

    def mousePressEvent(self, event):#重载鼠标事件
        if event.button() == Qt.LeftButton:#仅左键事件触发
            self.QGraphicsPath = QGraphicsPathItem() #实例QGraphicsPathItem
            self.path1 = QPainterPath()#实例路径函数
            self.path1.moveTo(event.scenePos()) #路径开始于
            pp=QPen() #实例QPen
            pp.setColor(self.pen_color) #设置颜色
            pp.setWidth(self.pen_width)#设置宽度
            self.QGraphicsPath.setPen(pp) #应用笔
            self.addItem(self.QGraphicsPath) #场景添加图元


    def mouseMoveEvent(self, event):#重载鼠标移动事件
        if event.buttons() & Qt.LeftButton: #仅左键时触发，event.button返回notbutton，需event.buttons()判断，这应是对象列表，用&判断
            if self.path1:#判断self.path1
                self.path1.lineTo(event.scenePos()) #移动并连接点
            
                self.QGraphicsPath.setPath(self.path1) #self.QGraphicsPath添加路径，如果写在上面的函数，是没线显示的，写在下面则在松键才出现线


    def mouseReleaseEvent(self, event):#重载鼠标松开事件
        if event.button() == Qt.LeftButton:#判断左键松开
            if self.path1:
                self.path1.closeSubpath() #结束路径


class Ui_Form(QWidget):
    def __init__(self):
        super(Ui_Form,self).__init__()
        self.formLayout = QFormLayout(self)
        self.formLayout.setObjectName(u"formLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.graphicsView = QGraphicsView(self)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setRenderHint(QPainter.Antialiasing) #设置反锯齿，注释掉曲线不平滑
        self.scene=MyScene()
        self.horizontalLayout.addWidget(self.graphicsView)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(self.verticalSpacer)
        self.pushButton = QPushButton(self)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QPushButton(self)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QPushButton(self)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.QSlider_1 = QSlider(self)
        self.QSlider_1.setMaximum(21)
        self.QSlider_1.setMinimum(1)
        self.QSlider_1.setSingleStep(2)
        self.QSlider_1.setValue(5)
        self.QSlider_1.setTickPosition(self.QSlider_1.TicksRight)
        self.QSlider_1.setObjectName(u"QSlider_1")
        self.verticalLayout.addWidget(self.QSlider_1)
        self.label1=QLabel()
        self.verticalLayout.addWidget(self.label1)
        self.pushButton_6 = QPushButton(self)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(self.verticalSpacer_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.formLayout.setLayout(0, QFormLayout.SpanningRole, self.horizontalLayout)
        self.retranslateUi(self)
        QMetaObject.connectSlotsByName(self) #UI工具生成代码，注释看好像也没影响

        self.graphicsView.setScene(self.scene)

        self.QSlider_1.valueChanged.connect(self.change_pen_width)
        self.pushButton.clicked.connect(self.change_color_black)
        self.pushButton_2.clicked.connect(self.change_color_blue)
        self.pushButton_3.clicked.connect(self.change_color_magenta)
        self.pushButton_6.clicked.connect(self.clean_all)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Design By xxxx", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u9ed1\u8272", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u84dd\u8272", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u54c1\u7ea2", None))
        self.label1.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u7b14\u8ff9\u5bbd\u5ea6", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"\u6e05\u9664\u5185\u5bb9", None))
    # retranslateUi

    def change_pen_width(self): #改变画符宽度，其实应该直接信号槽写临函也可以
        self.scene.pen_width=self.QSlider_1.value()

    def change_color_blue(self): #换画笔颜色
        self.scene.pen_color=Qt.blue
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(True)

    def change_color_black(self):#换画笔颜色
        self.scene.pen_color=Qt.black
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(True)

    def change_color_magenta(self):#换画笔颜色
        self.scene.pen_color=Qt.magenta
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(False)

    def clean_all(self):#清除图元
        self.scene.clear()


if __name__=='__main__':
    import sys
    app=QApplication(sys.argv)
    MyWin=Ui_Form()
    MyWin.show()
    sys.exit(app.exec_())