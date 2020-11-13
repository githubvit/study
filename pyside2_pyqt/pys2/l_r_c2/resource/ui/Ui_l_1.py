# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'l_1.ui'
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

import r_l_c_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(500, 500)
        Form.setMinimumSize(QSize(500, 500))
        Form.setMaximumSize(QSize(500, 500))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ant_wgt = QWidget(Form)
        self.ant_wgt.setObjectName(u"ant_wgt")
        self.ant_wgt.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.ant_wgt)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.an_lb = QLabel(self.ant_wgt)
        self.an_lb.setObjectName(u"an_lb")
        self.an_lb.setMaximumSize(QSize(16777215, 250))

        self.horizontalLayout_2.addWidget(self.an_lb)


        self.verticalLayout.addWidget(self.ant_wgt)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_wgt = QWidget(self.widget_2)
        self.left_wgt.setObjectName(u"left_wgt")
        self.left_wgt.setStyleSheet(u"")
        self.r_btn = QPushButton(self.left_wgt)
        self.r_btn.setObjectName(u"r_btn")
        self.r_btn.setGeometry(QRect(10, 200, 80, 23))
        self.r_btn.setMinimumSize(QSize(60, 0))
        self.r_btn.setMaximumSize(QSize(80, 16777215))
        self.r_btn.setStyleSheet(u"QPushButton {\n"
"	font: 15px \"\u5fae\u8f6f\u96c5\u9ed1 Light\";\n"
"	font-weight:500;\n"
"}\n"
"")
        self.r_btn.setFlat(True)

        self.horizontalLayout.addWidget(self.left_wgt)

        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 20, -1, -1)
        self.pw_le = QLineEdit(self.widget)
        self.pw_le.setObjectName(u"pw_le")
        self.pw_le.setMinimumSize(QSize(0, 30))
        self.pw_le.setStyleSheet(u"QLineEdit {\n"
"    border:none;\n"
"	background: transparent;\n"
"	border-bottom:2px solid rgb(138, 138, 138);\n"
"	\n"
"	font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    \n"
"   \n"
"}\n"
"QLineEdit:hover{\n"
"    border-bottom:2px solid rgb(95, 95, 95);\n"
"}\n"
"QLineEdit:focus{\n"
"    border-bottom:2px solid rgb(82, 209, 255);\n"
"}")
        self.pw_le.setEchoMode(QLineEdit.Password)
        self.pw_le.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.pw_le, 1, 0, 1, 2)

        self.rp_cbx = QCheckBox(self.widget)
        self.rp_cbx.setObjectName(u"rp_cbx")

        self.gridLayout.addWidget(self.rp_cbx, 2, 0, 1, 1)

        self.user_cmbx = QComboBox(self.widget)
        icon = QIcon()
        icon.addFile(u":/l_1/resource/img/safe1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.user_cmbx.addItem(icon, "")
        icon1 = QIcon()
        icon1.addFile(u":/l_1/resource/img/safe2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.user_cmbx.addItem(icon1, "")
        self.user_cmbx.setObjectName(u"user_cmbx")
        self.user_cmbx.setMinimumSize(QSize(0, 30))
        self.user_cmbx.setStyleSheet(u"\n"
"QComboBox {\n"
"	border:none;\n"
"	background: transparent;\n"
"	border-bottom:2px solid rgb(138, 138, 138);\n"
"    selection-background-color: orange;\n"
"	\n"
"	font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}\n"
"QComboBox::drop-down {\n"
"	background-color: transparent;\n"
"	width: 30px;\n"
"    height: 30px;\n"
"} \n"
" \n"
"QComboBox:down-arrow {\n"
"    image: url(:/l_1/resource/img/bottom_btn.png);\n"
"    \n"
"} \n"
"\n"
"QComboBox:hover{\n"
"    border-bottom:2px solid rgb(95, 95, 95);\n"
"}\n"
"QComboBox:focus{\n"
"    border-bottom:2px solid rgb(82, 209, 255);\n"
"}")
        self.user_cmbx.setEditable(True)

        self.gridLayout.addWidget(self.user_cmbx, 0, 0, 1, 2)

        self.alg_cbx = QCheckBox(self.widget)
        self.alg_cbx.setObjectName(u"alg_cbx")

        self.gridLayout.addWidget(self.alg_cbx, 2, 1, 1, 1, Qt.AlignRight)

        self.lg_btn = QPushButton(self.widget)
        self.lg_btn.setObjectName(u"lg_btn")
        self.lg_btn.setEnabled(False)
        self.lg_btn.setMinimumSize(QSize(0, 40))
        self.lg_btn.setStyleSheet(u"QPushButton{\n"
"    \n"
"    border-radius: 10px;\n"
"	\n"
"	background-color: rgb(0, 0, 127);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"    \n"
"}\n"
"QPushButton:disabled{\n"
"    \n"
"    color:gray;\n"
"	background-color: rgb(98, 92, 127);\n"
"    \n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"	background-color: rgb(0, 0, 184);\n"
"    \n"
"    \n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/l_1/resource/img/captain_america.png", QSize(), QIcon.Normal, QIcon.Off)
        self.lg_btn.setIcon(icon2)
        self.lg_btn.setIconSize(QSize(22, 22))

        self.gridLayout.addWidget(self.lg_btn, 3, 0, 1, 2)


        self.horizontalLayout.addWidget(self.widget)

        self.right_wgt = QWidget(self.widget_2)
        self.right_wgt.setObjectName(u"right_wgt")
        self.right_wgt.setEnabled(True)
        self.right_wgt.setStyleSheet(u"")
        self.url_btn = QPushButton(self.right_wgt)
        self.url_btn.setObjectName(u"url_btn")
        self.url_btn.setEnabled(True)
        self.url_btn.setGeometry(QRect(16, 120, 100, 100))
        self.url_btn.setMinimumSize(QSize(100, 100))
        self.url_btn.setMaximumSize(QSize(100, 100))
        self.url_btn.setStyleSheet(u"border-image: url(:/l_1/resource/img/bd.png);")

        self.horizontalLayout.addWidget(self.right_wgt)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout.addWidget(self.widget_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.an_lb.setText(QCoreApplication.translate("Form", u"\u52a8\u753b\u6807\u7b7e", None))
        self.r_btn.setText(QCoreApplication.translate("Form", u"\u7acb\u5373\u6ce8\u518c", None))
        self.rp_cbx.setText(QCoreApplication.translate("Form", u"\u8bb0\u4f4f\u5bc6\u7801", None))
        self.user_cmbx.setItemText(0, QCoreApplication.translate("Form", u"123465", None))
        self.user_cmbx.setItemText(1, QCoreApplication.translate("Form", u"7897987", None))

        self.alg_cbx.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u767b\u5f55", None))
        self.lg_btn.setText(QCoreApplication.translate("Form", u"\u5b89\u5168\u767b\u5f55", None))
        self.url_btn.setText("")
    # retranslateUi

