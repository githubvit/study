# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'r_1.ui'
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
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.r_bgd_wgt = QWidget(Form)
        self.r_bgd_wgt.setObjectName(u"r_bgd_wgt")
        self.r_bgd_wgt.setMinimumSize(QSize(500, 500))
        self.r_bgd_wgt.setMaximumSize(QSize(500, 500))
        self.r_bgd_wgt.setStyleSheet(u"#r_bgd_wgt{border-image: url(:/r_background/resource/img/background_regsiter.jpg) 0 0 0 310;}")
        self.mn_btn = QPushButton(self.r_bgd_wgt)
        self.mn_btn.setObjectName(u"mn_btn")
        self.mn_btn.setGeometry(QRect(10, 10, 40, 40))
        self.mn_btn.setMinimumSize(QSize(40, 40))
        self.mn_btn.setMaximumSize(QSize(40, 40))
        self.mn_btn.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"    font-size:12pt; \n"
"	background-color: rgb(100, 200, 50);\n"
"	border-radius: 20px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	border:2px solid rgb(62, 105, 223);   \n"
"}\n"
"QPushButton:checked{	\n"
"	background-color: rgb(81, 162, 40);\n"
"\n"
"}\n"
"")
        self.mn_btn.setCheckable(True)
        self.au_btn = QPushButton(self.r_bgd_wgt)
        self.au_btn.setObjectName(u"au_btn")
        self.au_btn.setGeometry(QRect(70, 10, 40, 40))
        self.au_btn.setMinimumSize(QSize(40, 40))
        self.au_btn.setMaximumSize(QSize(40, 40))
        self.au_btn.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"    font-size:12px;\n"
"	background-color: rgb(100, 200, 50);\n"
"	border-radius: 20px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	border:2px solid rgb(62, 105, 223);   \n"
"}\n"
"")
        self.rst_btn = QPushButton(self.r_bgd_wgt)
        self.rst_btn.setObjectName(u"rst_btn")
        self.rst_btn.setGeometry(QRect(60, 60, 40, 40))
        self.rst_btn.setMinimumSize(QSize(40, 40))
        self.rst_btn.setMaximumSize(QSize(40, 40))
        self.rst_btn.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"    font-size:12px;\n"
"	background-color: rgb(100, 200, 50);\n"
"	border-radius: 20px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	border:2px solid rgb(62, 105, 223);   \n"
"}\n"
"")
        self.ex_btn = QPushButton(self.r_bgd_wgt)
        self.ex_btn.setObjectName(u"ex_btn")
        self.ex_btn.setGeometry(QRect(10, 70, 40, 40))
        self.ex_btn.setMinimumSize(QSize(40, 40))
        self.ex_btn.setMaximumSize(QSize(40, 40))
        self.ex_btn.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"    font-size:12px;\n"
"	background-color: rgb(100, 200, 50);\n"
"	border-radius: 20px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	border:2px solid rgb(62, 105, 223);   \n"
"}\n"
"")
        self.widget = QWidget(self.r_bgd_wgt)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(180, 230, 251, 181))
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.u_lb = QLabel(self.widget)
        self.u_lb.setObjectName(u"u_lb")
        self.u_lb.setStyleSheet(u"font:16px '\u5fae\u8f6f\u96c5\u9ed1';\n"
"color: rgb(150, 150, 150);")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.u_lb)

        self.u_le = QLineEdit(self.widget)
        self.u_le.setObjectName(u"u_le")
        self.u_le.setStyleSheet(u"border:none;\n"
"background-color:transparent;\n"
"border-bottom: 1px solid;\n"
"border-color: rgb(188, 188, 188);\n"
"font:12px '\u5fae\u8f6f\u96c5\u9ed1';\n"
"")
        self.u_le.setClearButtonEnabled(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.u_le)

        self.p_lb = QLabel(self.widget)
        self.p_lb.setObjectName(u"p_lb")
        self.p_lb.setStyleSheet(u"font:16px '\u5fae\u8f6f\u96c5\u9ed1';\n"
"color: rgb(150, 150, 150);")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.p_lb)

        self.p_le = QLineEdit(self.widget)
        self.p_le.setObjectName(u"p_le")
        self.p_le.setStyleSheet(u"border:none;\n"
"background-color:transparent;\n"
"border-bottom: 1px solid;\n"
"border-color: rgb(188, 188, 188);\n"
"font:12px '\u5fae\u8f6f\u96c5\u9ed1';\n"
"")
        self.p_le.setClearButtonEnabled(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.p_le)

        self.c_lb = QLabel(self.widget)
        self.c_lb.setObjectName(u"c_lb")
        self.c_lb.setStyleSheet(u"font:16px '\u5fae\u8f6f\u96c5\u9ed1';\n"
"color: rgb(150, 150, 150);")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.c_lb)

        self.c_le = QLineEdit(self.widget)
        self.c_le.setObjectName(u"c_le")
        self.c_le.setStyleSheet(u"border:none;\n"
"background-color:transparent;\n"
"border-bottom: 1px solid;\n"
"border-color: rgb(188, 188, 188);\n"
"font:12px '\u5fae\u8f6f\u96c5\u9ed1';\n"
"")
        self.c_le.setClearButtonEnabled(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.c_le)

        self.reg_btn = QPushButton(self.widget)
        self.reg_btn.setObjectName(u"reg_btn")
        self.reg_btn.setEnabled(False)
        self.reg_btn.setMinimumSize(QSize(0, 45))
        self.reg_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 85, 255);\n"
"	border-radius:10px;\n"
"	font: 12pt \"\u5fae\u8f6f\u96c5\u9ed1 Light\";\n"
"	color: rgb(255, 255, 255);\n"
"	font-weight:500 ;\n"
"	\n"
"}\n"
"QPushButton:disabled{\n"
"	background-color: rgb(124, 175, 252);\n"
"	\n"
"}")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.reg_btn)

        self.au_btn.raise_()
        self.rst_btn.raise_()
        self.ex_btn.raise_()
        self.widget.raise_()
        self.mn_btn.raise_()

        self.horizontalLayout.addWidget(self.r_bgd_wgt)

#if QT_CONFIG(shortcut)
        self.u_lb.setBuddy(self.u_le)
        self.p_lb.setBuddy(self.p_le)
        self.c_lb.setBuddy(self.c_le)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.mn_btn.setText(QCoreApplication.translate("Form", u"\u83dc\u5355", None))
        self.au_btn.setText(QCoreApplication.translate("Form", u"\u5173\u4e8e", None))
        self.rst_btn.setText(QCoreApplication.translate("Form", u"\u91cd\u7f6e", None))
        self.ex_btn.setText(QCoreApplication.translate("Form", u"\u9000\u51fa", None))
        self.u_lb.setText(QCoreApplication.translate("Form", u"\u8d26      \u53f7(&u)\uff1a", None))
        self.u_le.setText("")
        self.p_lb.setText(QCoreApplication.translate("Form", u"\u5bc6      \u7801(&p)\uff1a", None))
        self.p_le.setText("")
        self.c_lb.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4\u5bc6\u7801(&c)\uff1a", None))
        self.c_le.setText("")
        self.reg_btn.setText(QCoreApplication.translate("Form", u"\u6ce8\u518c", None))
    # retranslateUi

