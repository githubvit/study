# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bqsk_kj.ui'
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
        MainWindow.resize(800, 615)
        self.action_onoff_tl = QAction(MainWindow)
        self.action_onoff_tl.setObjectName(u"action_onoff_tl")
        self.action_Learning_situation = QAction(MainWindow)
        self.action_Learning_situation.setObjectName(u"action_Learning_situation")
        self.action_setting = QAction(MainWindow)
        self.action_setting.setObjectName(u"action_setting")
        self.action_login = QAction(MainWindow)
        self.action_login.setObjectName(u"action_login")
        self.action_onoff_mark = QAction(MainWindow)
        self.action_onoff_mark.setObjectName(u"action_onoff_mark")
        self.action_start_page = QAction(MainWindow)
        self.action_start_page.setObjectName(u"action_start_page")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.text_twgt = QTabWidget(self.centralwidget)
        self.text_twgt.setObjectName(u"text_twgt")
        self.text_twgt.setTabsClosable(True)
        self.text_twgt.setMovable(True)
        self.text_twgt.setTabBarAutoHide(True)
        self.text_start_wgt = QWidget()
        self.text_start_wgt.setObjectName(u"text_start_wgt")
        self.text_twgt.addTab(self.text_start_wgt, "")

        self.horizontalLayout.addWidget(self.text_twgt)

        MainWindow.setCentralWidget(self.centralwidget)
        self.tl_dwgt = QDockWidget(MainWindow)
        self.tl_dwgt.setObjectName(u"tl_dwgt")
        self.tl_dwgt.setFeatures(QDockWidget.DockWidgetMovable)
        self.tl_wgt = QWidget()
        self.tl_wgt.setObjectName(u"tl_wgt")
        self.tl_dwgt.setWidget(self.tl_wgt)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.tl_dwgt)
        self.media_dwgt = QDockWidget(MainWindow)
        self.media_dwgt.setObjectName(u"media_dwgt")
        self.media_wgt = QWidget()
        self.media_wgt.setObjectName(u"media_wgt")
        self.media_dwgt.setWidget(self.media_wgt)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.media_dwgt)
        self.mark_dwgt = QDockWidget(MainWindow)
        self.mark_dwgt.setObjectName(u"mark_dwgt")
        self.mark_wgt = QWidget()
        self.mark_wgt.setObjectName(u"mark_wgt")
        self.mark_dwgt.setWidget(self.mark_wgt)
        MainWindow.addDockWidget(Qt.BottomDockWidgetArea, self.mark_dwgt)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.action_onoff_tl)
        self.toolBar.addAction(self.action_start_page)
        self.toolBar.addAction(self.action_onoff_mark)
        self.toolBar.addAction(self.action_Learning_situation)
        self.toolBar.addAction(self.action_setting)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_login)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u535a\u9a9e\u4e0a\u8bfe", None))
        self.action_onoff_tl.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00/\u5173\u95ed\u76ee\u5f55", None))
#if QT_CONFIG(tooltip)
        self.action_onoff_tl.setToolTip(QCoreApplication.translate("MainWindow", u"\u6253\u5f00/\u5173\u95ed\u76ee\u5f55", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_onoff_tl.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
        self.action_Learning_situation.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u60c5", None))
#if QT_CONFIG(tooltip)
        self.action_Learning_situation.setToolTip(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u5b66\u60c5\u62a5\u544a", None))
#endif // QT_CONFIG(tooltip)
        self.action_setting.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
#if QT_CONFIG(tooltip)
        self.action_setting.setToolTip(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
#endif // QT_CONFIG(tooltip)
        self.action_login.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55/\u6ce8\u9500", None))
#if QT_CONFIG(tooltip)
        self.action_login.setToolTip(QCoreApplication.translate("MainWindow", u"\u767b\u5f55/\u6ce8\u9500", None))
#endif // QT_CONFIG(tooltip)
        self.action_onoff_mark.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00/\u5173\u95ed\u7b14\u8bb0", None))
#if QT_CONFIG(tooltip)
        self.action_onoff_mark.setToolTip(QCoreApplication.translate("MainWindow", u"\u6253\u5f00/\u5173\u95ed\u7b14\u8bb0", None))
#endif // QT_CONFIG(tooltip)
        self.action_start_page.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00/\u5173\u95ed\u5f00\u59cb\u9875", None))
#if QT_CONFIG(tooltip)
        self.action_start_page.setToolTip(QCoreApplication.translate("MainWindow", u"\u6253\u5f00/\u5173\u95ed\u5f00\u59cb\u9875", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_start_page.setShortcut(QCoreApplication.translate("MainWindow", u"S", None))
#endif // QT_CONFIG(shortcut)
        self.text_twgt.setTabText(self.text_twgt.indexOf(self.text_start_wgt), QCoreApplication.translate("MainWindow", u"start", None))
#if QT_CONFIG(tooltip)
        self.text_twgt.setTabToolTip(self.text_twgt.indexOf(self.text_start_wgt), QCoreApplication.translate("MainWindow", u"start", None))
#endif // QT_CONFIG(tooltip)
        self.tl_dwgt.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u76ee\u5f55", None))
        self.media_dwgt.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u64ad\u653e\u5668", None))
        self.mark_dwgt.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u7b14\u8bb0", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

