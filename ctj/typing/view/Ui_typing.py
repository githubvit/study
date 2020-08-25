# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'typing.ui'
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


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(509, 100)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_wgt = QWidget(Form)
        self.menu_wgt.setObjectName(u"menu_wgt")
        self.menu_wgt.setMinimumSize(QSize(0, 100))
        self.menu_wgt.setMaximumSize(QSize(16777215, 100))
        self.menu_wgt.setStyleSheet(u"#menu_wgt{background-color: rgb(255, 170, 127);}")
        self.select_btn = QPushButton(self.menu_wgt)
        self.select_btn.setObjectName(u"select_btn")
        self.select_btn.setGeometry(QRect(30, 20, 75, 23))
        self.gopause_btn = QPushButton(self.menu_wgt)
        self.gopause_btn.setObjectName(u"gopause_btn")
        self.gopause_btn.setGeometry(QRect(430, 10, 61, 41))
        self.countdown_lb = QLabel(self.menu_wgt)
        self.countdown_lb.setObjectName(u"countdown_lb")
        self.countdown_lb.setGeometry(QRect(150, 20, 54, 12))
        self.countdown_le = QLineEdit(self.menu_wgt)
        self.countdown_le.setObjectName(u"countdown_le")
        self.countdown_le.setGeometry(QRect(210, 10, 71, 20))
        self.timer_le = QLineEdit(self.menu_wgt)
        self.timer_le.setObjectName(u"timer_le")
        self.timer_le.setGeometry(QRect(210, 40, 71, 20))
        self.timer_lb = QLabel(self.menu_wgt)
        self.timer_lb.setObjectName(u"timer_lb")
        self.timer_lb.setGeometry(QRect(150, 50, 54, 12))
        self.speed_le = QLineEdit(self.menu_wgt)
        self.speed_le.setObjectName(u"speed_le")
        self.speed_le.setGeometry(QRect(210, 70, 71, 20))
        self.speed_lb = QLabel(self.menu_wgt)
        self.speed_lb.setObjectName(u"speed_lb")
        self.speed_lb.setGeometry(QRect(150, 80, 54, 12))
        self.accuracy_le = QLineEdit(self.menu_wgt)
        self.accuracy_le.setObjectName(u"accuracy_le")
        self.accuracy_le.setGeometry(QRect(350, 10, 71, 20))
        self.accuracy_lb = QLabel(self.menu_wgt)
        self.accuracy_lb.setObjectName(u"accuracy_lb")
        self.accuracy_lb.setGeometry(QRect(290, 20, 54, 12))
        self.errnum_le = QLineEdit(self.menu_wgt)
        self.errnum_le.setObjectName(u"errnum_le")
        self.errnum_le.setGeometry(QRect(350, 40, 71, 20))
        self.errnum_lb = QLabel(self.menu_wgt)
        self.errnum_lb.setObjectName(u"errnum_lb")
        self.errnum_lb.setGeometry(QRect(290, 50, 54, 12))
        self.bsnum_le = QLineEdit(self.menu_wgt)
        self.bsnum_le.setObjectName(u"bsnum_le")
        self.bsnum_le.setGeometry(QRect(350, 70, 71, 20))
        self.bsnum_lb = QLabel(self.menu_wgt)
        self.bsnum_lb.setObjectName(u"bsnum_lb")
        self.bsnum_lb.setGeometry(QRect(290, 80, 54, 12))
        self.up_btn = QPushButton(self.menu_wgt)
        self.up_btn.setObjectName(u"up_btn")
        self.up_btn.setGeometry(QRect(30, 60, 75, 23))
        self.reset_btn = QPushButton(self.menu_wgt)
        self.reset_btn.setObjectName(u"reset_btn")
        self.reset_btn.setGeometry(QRect(430, 60, 61, 23))

        self.verticalLayout.addWidget(self.menu_wgt)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.select_btn.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u7a3f", None))
        self.gopause_btn.setText(QCoreApplication.translate("Form", u"\u7ee7\u7eed/\u6682\u505c", None))
        self.countdown_lb.setText(QCoreApplication.translate("Form", u"\u5012\u8ba1\u65f6", None))
        self.timer_lb.setText(QCoreApplication.translate("Form", u"\u8bbe\u5b9a\u65f6\u95f4", None))
        self.speed_lb.setText(QCoreApplication.translate("Form", u"\u901f\u5ea6", None))
        self.accuracy_lb.setText(QCoreApplication.translate("Form", u"\u6b63\u786e\u7387", None))
        self.errnum_lb.setText(QCoreApplication.translate("Form", u"\u9519\u8bef\u5b57\u6570", None))
        self.bsnum_lb.setText(QCoreApplication.translate("Form", u"\u9000\u683c\u6b21\u6570", None))
        self.up_btn.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u6587\u7a3f", None))
        self.reset_btn.setText(QCoreApplication.translate("Form", u"\u590d\u4f4d", None))
    # retranslateUi

