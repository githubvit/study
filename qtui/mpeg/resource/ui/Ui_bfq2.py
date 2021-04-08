# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bfq2.ui'
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

import bfq_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(930, 686)
        MainWindow.setStyleSheet(u"")
        MainWindow.setDockNestingEnabled(False)
        self.list_onoff_act = QAction(MainWindow)
        self.list_onoff_act.setObjectName(u"list_onoff_act")
        self.setting_act = QAction(MainWindow)
        self.setting_act.setObjectName(u"setting_act")
        self.login_act = QAction(MainWindow)
        self.login_act.setObjectName(u"login_act")
        self.study_act = QAction(MainWindow)
        self.study_act.setObjectName(u"study_act")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.right_wgt = QWidget(self.centralwidget)
        self.right_wgt.setObjectName(u"right_wgt")
        self.right_wgt.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.right_wgt)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.cnt_wgt = QWidget(self.right_wgt)
        self.cnt_wgt.setObjectName(u"cnt_wgt")
        self.cnt_wgt.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.cnt_wgt)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.cnt_tab_tbwgt = QTabWidget(self.cnt_wgt)
        self.cnt_tab_tbwgt.setObjectName(u"cnt_tab_tbwgt")
        self.cnt_tab_tbwgt.setStyleSheet(u"")
        self.cnt_tab_tbwgt.setElideMode(Qt.ElideRight)
        self.cnt_tab_tbwgt.setDocumentMode(False)
        self.cnt_tab_tbwgt.setTabsClosable(True)
        self.cnt_tab_tbwgt.setMovable(True)
        self.cnt_tab_tbwgt.setTabBarAutoHide(False)
        self.start_tab_wgt = QWidget()
        self.start_tab_wgt.setObjectName(u"start_tab_wgt")
        self.start_tab_wgt.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.start_tab_wgt)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.textEdit = QTextEdit(self.start_tab_wgt)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(True)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.textEdit)

        self.cnt_tab_tbwgt.addTab(self.start_tab_wgt, "")

        self.verticalLayout_2.addWidget(self.cnt_tab_tbwgt)


        self.horizontalLayout.addWidget(self.cnt_wgt)

        self.horizontalLayout.setStretch(0, 1)

        self.verticalLayout_4.addWidget(self.right_wgt)

        MainWindow.setCentralWidget(self.centralwidget)
        self.lst_dwgt = QDockWidget(MainWindow)
        self.lst_dwgt.setObjectName(u"lst_dwgt")
        self.lst_dwgt.setStyleSheet(u"margin: 0 0 0 0;\n"
"padding: 0 0 0 0;\n"
"")
        self.lst_dwgt.setFeatures(QDockWidget.DockWidgetMovable)
        self.lst_dwgt.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.lst_wgt = QWidget()
        self.lst_wgt.setObjectName(u"lst_wgt")
        self.lst_wgt.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.lst_wgt)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.sch_lst_le = QLineEdit(self.lst_wgt)
        self.sch_lst_le.setObjectName(u"sch_lst_le")

        self.verticalLayout.addWidget(self.sch_lst_le)

        self.lst_tv = QTreeView(self.lst_wgt)
        self.lst_tv.setObjectName(u"lst_tv")

        self.verticalLayout.addWidget(self.lst_tv)

        self.lst_dwgt.setWidget(self.lst_wgt)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.lst_dwgt)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMovable(True)
        self.toolBar.setAllowedAreas(Qt.LeftToolBarArea|Qt.RightToolBarArea|Qt.TopToolBarArea)
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.toolBar.setFloatable(False)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.media_dwgt = QDockWidget(MainWindow)
        self.media_dwgt.setObjectName(u"media_dwgt")
        self.media_dwgt.setFloating(False)
        self.media_dwgt.setFeatures(QDockWidget.AllDockWidgetFeatures)
        self.media_dwgt.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.mdeia_cnt_wgt = QWidget()
        self.mdeia_cnt_wgt.setObjectName(u"mdeia_cnt_wgt")
        self.verticalLayout_5 = QVBoxLayout(self.mdeia_cnt_wgt)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.play_wgt = QWidget(self.mdeia_cnt_wgt)
        self.play_wgt.setObjectName(u"play_wgt")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.play_wgt.sizePolicy().hasHeightForWidth())
        self.play_wgt.setSizePolicy(sizePolicy)
        self.play_wgt.setMinimumSize(QSize(500, 300))
        self.play_wgt.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.verticalLayout_5.addWidget(self.play_wgt)

        self.process_sdr = QSlider(self.mdeia_cnt_wgt)
        self.process_sdr.setObjectName(u"process_sdr")
        self.process_sdr.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.process_sdr)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.left_lb = QLabel(self.mdeia_cnt_wgt)
        self.left_lb.setObjectName(u"left_lb")

        self.horizontalLayout_3.addWidget(self.left_lb)

        self.right_lb = QLabel(self.mdeia_cnt_wgt)
        self.right_lb.setObjectName(u"right_lb")
        self.right_lb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.right_lb)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.play_btn = QPushButton(self.mdeia_cnt_wgt)
        self.play_btn.setObjectName(u"play_btn")

        self.horizontalLayout_4.addWidget(self.play_btn)

        self.mtu_btn = QPushButton(self.mdeia_cnt_wgt)
        self.mtu_btn.setObjectName(u"mtu_btn")

        self.horizontalLayout_4.addWidget(self.mtu_btn)

        self.voice_sdr = QSlider(self.mdeia_cnt_wgt)
        self.voice_sdr.setObjectName(u"voice_sdr")
        self.voice_sdr.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.voice_sdr)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.media_dwgt.setWidget(self.mdeia_cnt_wgt)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.media_dwgt)
        self.mark_dwgt = QDockWidget(MainWindow)
        self.mark_dwgt.setObjectName(u"mark_dwgt")
        self.mark_dwgt.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.mark_cnt_wgt = QWidget()
        self.mark_cnt_wgt.setObjectName(u"mark_cnt_wgt")
        self.mark_dwgt.setWidget(self.mark_cnt_wgt)
        MainWindow.addDockWidget(Qt.BottomDockWidgetArea, self.mark_dwgt)

        self.toolBar.addAction(self.list_onoff_act)
        self.toolBar.addAction(self.study_act)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.login_act)
        self.toolBar.addAction(self.setting_act)

        self.retranslateUi(MainWindow)

        self.cnt_tab_tbwgt.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.list_onoff_act.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00/\u5173\u95ed\u76ee\u5f55", None))
#if QT_CONFIG(tooltip)
        self.list_onoff_act.setToolTip(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6216\u5173\u95ed\u76ee\u5f55", None))
#endif // QT_CONFIG(tooltip)
        self.setting_act.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
#if QT_CONFIG(tooltip)
        self.setting_act.setToolTip(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
#endif // QT_CONFIG(tooltip)
        self.login_act.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55/\u6ce8\u9500", None))
#if QT_CONFIG(tooltip)
        self.login_act.setToolTip(QCoreApplication.translate("MainWindow", u"\u767b\u5f55/\u6ce8\u9500", None))
#endif // QT_CONFIG(tooltip)
        self.study_act.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u60c5\u5206\u6790", None))
#if QT_CONFIG(tooltip)
        self.study_act.setToolTip(QCoreApplication.translate("MainWindow", u"\u5b66\u60c5\u5206\u6790", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.start_tab_wgt.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/start_fm/resource/img/fm1.png\" /></p></body></html>", None))
        self.cnt_tab_tbwgt.setTabText(self.cnt_tab_tbwgt.indexOf(self.start_tab_wgt), QCoreApplication.translate("MainWindow", u"start_page", None))
#if QT_CONFIG(tooltip)
        self.cnt_tab_tbwgt.setTabToolTip(self.cnt_tab_tbwgt.indexOf(self.start_tab_wgt), QCoreApplication.translate("MainWindow", u"start_page", None))
#endif // QT_CONFIG(tooltip)
        self.lst_dwgt.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u76ee\u5f55", None))
        self.sch_lst_le.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filter File", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.media_dwgt.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u64ad\u653e\u5668", None))
        self.left_lb.setText(QCoreApplication.translate("MainWindow", u"0:00:00", None))
        self.right_lb.setText(QCoreApplication.translate("MainWindow", u"0:00:00", None))
        self.play_btn.setText(QCoreApplication.translate("MainWindow", u"\u64ad\u653e", None))
        self.mtu_btn.setText(QCoreApplication.translate("MainWindow", u"\u5587\u53ed", None))
        self.mark_dwgt.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u7b14\u8bb0", None))
    # retranslateUi

