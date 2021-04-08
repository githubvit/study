# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test2.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 756)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_wgt = QWidget(self.centralwidget)
        self.top_wgt.setObjectName(u"top_wgt")
        self.top_wgt.setMinimumSize(QSize(0, 30))
        self.top_wgt.setMaximumSize(QSize(16777215, 30))
        self.top_wgt.setStyleSheet(u"QWidget#top_wgt{background-color: rgb(170, 0, 0);}")
        self.horizontalLayout_5 = QHBoxLayout(self.top_wgt)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_9 = QWidget(self.top_wgt)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(200, 0))
        self.widget_9.setMaximumSize(QSize(200, 16777215))
        self.logo_lb = QLabel(self.widget_9)
        self.logo_lb.setObjectName(u"logo_lb")
        self.logo_lb.setGeometry(QRect(70, 8, 24, 16))
        self.logo_lb.setStyleSheet(u"color:white;")
        self.logo_lb.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.widget_9)

        self.widget = QWidget(self.top_wgt)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 0, 6, 0)
        self.fd_btn = QPushButton(self.widget)
        self.fd_btn.setObjectName(u"fd_btn")
        self.fd_btn.setMaximumSize(QSize(30, 16777215))
        self.fd_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"	border: 1px solid gray;\n"
"}")

        self.horizontalLayout.addWidget(self.fd_btn)

        self.bk_btn = QPushButton(self.widget)
        self.bk_btn.setObjectName(u"bk_btn")
        self.bk_btn.setMaximumSize(QSize(30, 16777215))
        self.bk_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"	border: 1px solid gray;\n"
"}")

        self.horizontalLayout.addWidget(self.bk_btn)


        self.horizontalLayout_5.addWidget(self.widget)

        self.lineEdit = QLineEdit(self.top_wgt)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_5.addWidget(self.lineEdit)

        self.horizontalSpacer = QSpacerItem(249, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.widget_4 = QWidget(self.top_wgt)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setSpacing(9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 9, 0)
        self.logo_btn_2 = QPushButton(self.widget_4)
        self.logo_btn_2.setObjectName(u"logo_btn_2")
        self.logo_btn_2.setMaximumSize(QSize(50, 16777215))
        self.logo_btn_2.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"	color:orange;\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {\n"
"    color: white;\n"
"}")

        self.horizontalLayout_4.addWidget(self.logo_btn_2)

        self.logo_btn_3 = QPushButton(self.widget_4)
        self.logo_btn_3.setObjectName(u"logo_btn_3")
        self.logo_btn_3.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: orange;\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {\n"
"  	color: white;\n"
"   	\n"
"}")

        self.horizontalLayout_4.addWidget(self.logo_btn_3)


        self.horizontalLayout_5.addWidget(self.widget_4)

        self.widget_2 = QWidget(self.top_wgt)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.email_btn = QPushButton(self.widget_2)
        self.email_btn.setObjectName(u"email_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.email_btn.sizePolicy().hasHeightForWidth())
        self.email_btn.setSizePolicy(sizePolicy)
        self.email_btn.setMinimumSize(QSize(50, 0))
        self.email_btn.setMaximumSize(QSize(50, 16777215))
        self.email_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(142, 32, 32);\n"
"}")

        self.horizontalLayout_2.addWidget(self.email_btn)

        self.th_btn = QPushButton(self.widget_2)
        self.th_btn.setObjectName(u"th_btn")
        sizePolicy.setHeightForWidth(self.th_btn.sizePolicy().hasHeightForWidth())
        self.th_btn.setSizePolicy(sizePolicy)
        self.th_btn.setMinimumSize(QSize(50, 0))
        self.th_btn.setMaximumSize(QSize(50, 16777215))
        self.th_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(142, 32, 32);\n"
"}")

        self.horizontalLayout_2.addWidget(self.th_btn)

        self.set_btn = QPushButton(self.widget_2)
        self.set_btn.setObjectName(u"set_btn")
        sizePolicy.setHeightForWidth(self.set_btn.sizePolicy().hasHeightForWidth())
        self.set_btn.setSizePolicy(sizePolicy)
        self.set_btn.setMinimumSize(QSize(50, 0))
        self.set_btn.setMaximumSize(QSize(50, 16777215))
        self.set_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(142, 32, 32);\n"
"}")

        self.horizontalLayout_2.addWidget(self.set_btn)


        self.horizontalLayout_5.addWidget(self.widget_2)

        self.line = QFrame(self.top_wgt)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line)

        self.widget_3 = QWidget(self.top_wgt)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.min_btn = QPushButton(self.widget_3)
        self.min_btn.setObjectName(u"min_btn")
        sizePolicy.setHeightForWidth(self.min_btn.sizePolicy().hasHeightForWidth())
        self.min_btn.setSizePolicy(sizePolicy)
        self.min_btn.setMinimumSize(QSize(45, 0))
        self.min_btn.setMaximumSize(QSize(50, 16777215))
        self.min_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(142, 32, 32);\n"
"}")
        self.min_btn.setFlat(True)

        self.horizontalLayout_3.addWidget(self.min_btn)

        self.max_btn = QPushButton(self.widget_3)
        self.max_btn.setObjectName(u"max_btn")
        sizePolicy.setHeightForWidth(self.max_btn.sizePolicy().hasHeightForWidth())
        self.max_btn.setSizePolicy(sizePolicy)
        self.max_btn.setMinimumSize(QSize(45, 0))
        self.max_btn.setMaximumSize(QSize(50, 16777215))
        self.max_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(142, 32, 32);\n"
"}")
        self.max_btn.setFlat(True)

        self.horizontalLayout_3.addWidget(self.max_btn)

        self.cls_btn = QPushButton(self.widget_3)
        self.cls_btn.setObjectName(u"cls_btn")
        sizePolicy.setHeightForWidth(self.cls_btn.sizePolicy().hasHeightForWidth())
        self.cls_btn.setSizePolicy(sizePolicy)
        self.cls_btn.setMinimumSize(QSize(45, 0))
        self.cls_btn.setMaximumSize(QSize(50, 16777215))
        self.cls_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(122, 0, 0);\n"
"}")
        self.cls_btn.setFlat(True)

        self.horizontalLayout_3.addWidget(self.cls_btn)


        self.horizontalLayout_5.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.top_wgt)

        self.main_wgt = QWidget(self.centralwidget)
        self.main_wgt.setObjectName(u"main_wgt")
        self.horizontalLayout_6 = QHBoxLayout(self.main_wgt)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.left_wgt = QWidget(self.main_wgt)
        self.left_wgt.setObjectName(u"left_wgt")
        self.left_wgt.setMinimumSize(QSize(200, 0))
        self.left_wgt.setMaximumSize(QSize(200, 16777215))
        self.left_wgt.setStyleSheet(u"QWidget#left_wgt{\n"
"	background-color: rgb(217, 217, 217);\n"
"}\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.left_wgt)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_5 = QWidget(self.left_wgt)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_2 = QVBoxLayout(self.widget_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget_5)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_2.addWidget(self.label)

        self.pushButton_4 = QPushButton(self.widget_5)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	text-align:left;\n"
"}")

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.widget_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"	text-align:left;\n"
"}")

        self.verticalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_7 = QPushButton(self.widget_5)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"	text-align:left;\n"
"}")

        self.verticalLayout_2.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.widget_5)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
"	text-align:left;\n"
"}")

        self.verticalLayout_2.addWidget(self.pushButton_8)

        self.pushButton_6 = QPushButton(self.widget_5)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"	text-align:left;\n"
"}")

        self.verticalLayout_2.addWidget(self.pushButton_6)


        self.verticalLayout_4.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.left_wgt)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_3 = QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.widget_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_3.addWidget(self.label_2)

        self.pushButton_9 = QPushButton(self.widget_6)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
"	text-align:left;\n"
"}")

        self.verticalLayout_3.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.widget_6)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"QPushButton{\n"
"	text-align:left;\n"
"}")

        self.verticalLayout_3.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.widget_6)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setStyleSheet(u"QPushButton{\n"
"	text-align:left;\n"
"}")

        self.verticalLayout_3.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.widget_6)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setStyleSheet(u"QPushButton{\n"
"	text-align:left;\n"
"}")

        self.verticalLayout_3.addWidget(self.pushButton_12)


        self.verticalLayout_4.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.left_wgt)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_5 = QVBoxLayout(self.widget_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.widget_7)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.listView = QListView(self.widget_7)
        self.listView.setObjectName(u"listView")

        self.verticalLayout_5.addWidget(self.listView)


        self.verticalLayout_4.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.left_wgt)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_6 = QVBoxLayout(self.widget_8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.widget_8)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_6.addWidget(self.label_4)

        self.listView_2 = QListView(self.widget_8)
        self.listView_2.setObjectName(u"listView_2")

        self.verticalLayout_6.addWidget(self.listView_2)


        self.verticalLayout_4.addWidget(self.widget_8)


        self.horizontalLayout_6.addWidget(self.left_wgt)

        self.right_wgt = QWidget(self.main_wgt)
        self.right_wgt.setObjectName(u"right_wgt")
        self.right_wgt.setStyleSheet(u"QWidget#right_wgt{\n"
"	\n"
"	background-color: rgb(227, 227, 227);\n"
"}\n"
"")
        self.verticalLayout_7 = QVBoxLayout(self.right_wgt)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tabWidget = QTabWidget(self.right_wgt)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabWidget::pane{\n"
"    border-top: 1px solid rgba(69,104,220,0.3);\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::tab{\n"
"    min-width: 70px;\n"
"    min-height: 30px;\n"
"    background: transparent;\n"
"	color:blank;\n"
"}\n"
"QTabBar::tab:selected{\n"
"    color:rgb(69,104,220);\n"
"    background-color:rgba(240,245,255,0.8) ;\n"
"}\n"
"\n"
"QTabBar::tab:hover{\n"
"    background-color:rgba(240,245,255,0.8) ;\n"
"}\n"
"")
        self.tabWidget.setTabBarAutoHide(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tabWidget.addTab(self.tab_6, "")

        self.verticalLayout_7.addWidget(self.tabWidget)


        self.horizontalLayout_6.addWidget(self.right_wgt)


        self.verticalLayout.addWidget(self.main_wgt)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_lb.setText(QCoreApplication.translate("MainWindow", u"logo", None))
        self.fd_btn.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.bk_btn.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u89c6\u9891\u3001\u97f3\u4e50\u3001\u7535\u53f0", None))
        self.logo_btn_2.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55", None))
        self.logo_btn_3.setText(QCoreApplication.translate("MainWindow", u"\u5347\u7ea7\u4e3aVIP", None))
        self.email_btn.setText(QCoreApplication.translate("MainWindow", u"\u90ae\u7bb1", None))
        self.th_btn.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u9898", None))
        self.set_btn.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.min_btn.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.max_btn.setText(QCoreApplication.translate("MainWindow", u"max", None))
        self.cls_btn.setText(QCoreApplication.translate("MainWindow", u"close", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u63a8\u8350", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u73b0\u97f3\u4e50", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u79c1\u4ebaFM", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"LOOK\u76f4\u64ad", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u670b\u53cb", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6536\u85cf", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u73b0\u97f3\u4e50", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u79c1\u4ebaFM", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"LOOK\u76f4\u64ad", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u521b\u5efa\u7684\u6b4c\u5355", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u6536\u85cf\u7684\u6b4c\u5355", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u4e2a\u6027\u63a8\u8350", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u6b4c\u5355", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u6392\u884c\u699c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u4e3b\u64ad\u7535\u53f0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u6b4c\u624b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"\u6700\u65b0\u97f3\u4e50", None))
    # retranslateUi

