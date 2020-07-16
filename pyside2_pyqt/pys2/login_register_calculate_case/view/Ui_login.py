# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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

import login_register_calculate_case_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(600, 400)
        Form.setMinimumSize(QSize(600, 400))
        Form.setMaximumSize(QSize(600, 400))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.animation_lb = QLabel(self.widget)
        self.animation_lb.setObjectName(u"animation_lb")

        self.horizontalLayout.addWidget(self.animation_lb)


        self.verticalLayout.addWidget(self.widget)

        self.login_bottom = QWidget(Form)
        self.login_bottom.setObjectName(u"login_bottom")
        self.login_bottom.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.login_bottom)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_4 = QWidget(self.login_bottom)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.register_btn = QPushButton(self.widget_4)
        self.register_btn.setObjectName(u"register_btn")
        self.register_btn.setMinimumSize(QSize(100, 0))
        self.register_btn.setMaximumSize(QSize(100, 16777215))
        self.register_btn.setStyleSheet(u"font: 12pt \"\u9ed1\u4f53\";\n"
"")
        self.register_btn.setFlat(True)

        self.horizontalLayout_3.addWidget(self.register_btn, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.widget_4)

        self.widget_3 = QWidget(self.login_bottom)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pwd_le = QLineEdit(self.widget_3)
        self.pwd_le.setObjectName(u"pwd_le")
        self.pwd_le.setMinimumSize(QSize(0, 35))
        self.pwd_le.setStyleSheet(u"QLineEdit {\n"
"	border:none;\n"
"	border-bottom:2px solid darkgray;\n"
"	background-color:transparent;\n"
"	font: 25 12pt \"\u5fae\u8f6f\u96c5\u9ed1 Light\";\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"    border-bottom:2px solid gray;\n"
"}\n"
"QLineEdit:focus{\n"
"    border-bottom:2px solid rgb(90, 242, 255);\n"
"}\n"
"")
        self.pwd_le.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.pwd_le.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.pwd_le, 1, 0, 1, 2)

        self.username_cmbx = QComboBox(self.widget_3)
        icon = QIcon()
        icon.addFile(u":/login/images/safe1.png", QSize(), QIcon.Selected, QIcon.On)
        self.username_cmbx.addItem(icon, "")
        icon1 = QIcon()
        icon1.addFile(u":/login/images/safe2.png", QSize(), QIcon.Selected, QIcon.On)
        self.username_cmbx.addItem(icon1, "")
        self.username_cmbx.setObjectName(u"username_cmbx")
        self.username_cmbx.setMinimumSize(QSize(0, 35))
        self.username_cmbx.setStyleSheet(u"QComboBox{\n"
"	border:none;\n"
"	border-bottom:2px solid darkgray;\n"
"	background-color:transparent;\n"
"	\n"
"	font: 25 12pt \"\u5fae\u8f6f\u96c5\u9ed1 Light\";\n"
"}\n"
"QComboBox::drop-down {\n"
"	margin-top: 10px;\n"
"   	border-image: url(:/login/images/bottom_btn.png);\n"
"	background-color: transparent;\n"
"	width:30px;\n"
"	height:20px;\n"
"}\n"
"QComboBox:hover{\n"
"    border-bottom:2px solid gray;\n"
"}\n"
"QComboBox:focus{\n"
"    border-bottom:2px solid rgb(90, 242, 255);\n"
"}\n"
"")
        self.username_cmbx.setEditable(True)

        self.gridLayout.addWidget(self.username_cmbx, 0, 0, 1, 2)

        self.auto_login_cbx = QCheckBox(self.widget_3)
        self.auto_login_cbx.setObjectName(u"auto_login_cbx")

        self.gridLayout.addWidget(self.auto_login_cbx, 2, 0, 1, 1)

        self.login_btn = QPushButton(self.widget_3)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setEnabled(False)
        self.login_btn.setMinimumSize(QSize(200, 40))
        self.login_btn.setMaximumSize(QSize(16777215, 40))
        self.login_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(220, 84, 71);\n"
"    border-radius: 15px;\n"
"	color:white;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(254, 96, 81);\n"
"    	\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(157, 59, 50);\n"
"    	\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color:gray;\n"
"	color:rgb(179, 179, 179);\n"
"    	\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/login/images/captain_america.png", QSize(), QIcon.Selected, QIcon.On)
        self.login_btn.setIcon(icon2)
        self.login_btn.setIconSize(QSize(22, 22))

        self.gridLayout.addWidget(self.login_btn, 3, 0, 1, 2)

        self.remember_cbx = QCheckBox(self.widget_3)
        self.remember_cbx.setObjectName(u"remember_cbx")

        self.gridLayout.addWidget(self.remember_cbx, 2, 1, 1, 1, Qt.AlignRight)


        self.horizontalLayout_2.addWidget(self.widget_3)

        self.widget_5 = QWidget(self.login_bottom)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.url_btn = QPushButton(self.widget_5)
        self.url_btn.setObjectName(u"url_btn")
        self.url_btn.setMinimumSize(QSize(100, 100))
        self.url_btn.setMaximumSize(QSize(100, 100))
        self.url_btn.setStyleSheet(u"border-image: url(:/login/images/bd.png);")

        self.horizontalLayout_4.addWidget(self.url_btn, 0, Qt.AlignRight|Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.widget_5)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout.addWidget(self.login_bottom)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 3)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.animation_lb.setText(QCoreApplication.translate("Form", u"\u52a8\u753b\u6807\u7b7e", None))
        self.register_btn.setText(QCoreApplication.translate("Form", u"\u7acb\u5373\u6ce8\u518c", None))
        self.username_cmbx.setItemText(0, QCoreApplication.translate("Form", u"695989545", None))
        self.username_cmbx.setItemText(1, QCoreApplication.translate("Form", u"7981146", None))

        self.auto_login_cbx.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u767b\u5f55", None))
        self.login_btn.setText(QCoreApplication.translate("Form", u"\u5b89\u5168\u767b\u5f55", None))
        self.remember_cbx.setText(QCoreApplication.translate("Form", u"\u8bb0\u4f4f\u5bc6\u7801", None))
        self.url_btn.setText("")
    # retranslateUi

