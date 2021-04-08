# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'short_screen.ui'
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
        MainWindow.resize(800, 600)
        self.actionopen = QAction(MainWindow)
        self.actionopen.setObjectName(u"actionopen")
        self.actionsave = QAction(MainWindow)
        self.actionsave.setObjectName(u"actionsave")
        self.actionnew = QAction(MainWindow)
        self.actionnew.setObjectName(u"actionnew")
        self.actionquite = QAction(MainWindow)
        self.actionquite.setObjectName(u"actionquite")
        self.actionproperty = QAction(MainWindow)
        self.actionproperty.setObjectName(u"actionproperty")
        self.actionsize = QAction(MainWindow)
        self.actionsize.setObjectName(u"actionsize")
        self.actionapi = QAction(MainWindow)
        self.actionapi.setObjectName(u"actionapi")
        self.actionabout_this = QAction(MainWindow)
        self.actionabout_this.setObjectName(u"actionabout_this")
        self.actionocr = QAction(MainWindow)
        self.actionocr.setObjectName(u"actionocr")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.img_lb = QLabel(self.centralwidget)
        self.img_lb.setObjectName(u"img_lb")
        self.img_lb.setWordWrap(True)
        self.img_lb.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.horizontalLayout.addWidget(self.img_lb)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        self.menufile = QMenu(self.menubar)
        self.menufile.setObjectName(u"menufile")
        self.menusetting = QMenu(self.menubar)
        self.menusetting.setObjectName(u"menusetting")
        self.menuhelp = QMenu(self.menubar)
        self.menuhelp.setObjectName(u"menuhelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menusetting.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())
        self.menufile.addAction(self.actionnew)
        self.menufile.addAction(self.actionopen)
        self.menufile.addSeparator()
        self.menufile.addAction(self.actionsave)
        self.menufile.addSeparator()
        self.menufile.addAction(self.actionquite)
        self.menusetting.addAction(self.actionproperty)
        self.menusetting.addSeparator()
        self.menusetting.addAction(self.actionsize)
        self.menusetting.addAction(self.actionapi)
        self.menusetting.addSeparator()
        self.menusetting.addAction(self.actionocr)
        self.menuhelp.addAction(self.actionabout_this)
        self.toolBar.addAction(self.actionnew)
        self.toolBar.addAction(self.actionopen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionocr)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionproperty)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionopen.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u622a\u56fe", None))
#if QT_CONFIG(tooltip)
        self.actionopen.setToolTip(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u622a\u56fe", None))
#endif // QT_CONFIG(tooltip)
        self.actionsave.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.actionnew.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u622a\u56fe", None))
#if QT_CONFIG(tooltip)
        self.actionnew.setToolTip(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u622a\u56fe", None))
#endif // QT_CONFIG(tooltip)
        self.actionquite.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
#if QT_CONFIG(tooltip)
        self.actionquite.setToolTip(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
#endif // QT_CONFIG(tooltip)
        self.actionproperty.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.actionsize.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u56fe\u5927\u5c0f", None))
        self.actionapi.setText(QCoreApplication.translate("MainWindow", u"ocr\u63a5\u53e3", None))
        self.actionabout_this.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.actionocr.setText(QCoreApplication.translate("MainWindow", u"\u6587\u5b57\u8bc6\u522b", None))
#if QT_CONFIG(tooltip)
        self.actionocr.setToolTip(QCoreApplication.translate("MainWindow", u"\u6587\u5b57\u8bc6\u522b", None))
#endif // QT_CONFIG(tooltip)
        self.img_lb.setText(QCoreApplication.translate("MainWindow", u"1. \u53ef\u4ee5 \u622a\u56fe \u8fdb\u884c\u8bc6\u522b   2.\u53ef\u4ee5 \u6253\u5f00\u73b0\u6709\u7684\u56fe\u7247 \u8fdb\u884c\u8bc6\u522b                                                                              ", None))
        self.menufile.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menusetting.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.menuhelp.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

