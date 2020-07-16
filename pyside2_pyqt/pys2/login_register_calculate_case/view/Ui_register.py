# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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
        Form.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.bgd_wgt = QWidget(Form)
        self.bgd_wgt.setObjectName(u"bgd_wgt")
        self.bgd_wgt.setStyleSheet(u"#bgd_wgt{border-image: url(:/login/images/background_regsiter.jpg);}")
        self.exit_btn = QPushButton(self.bgd_wgt)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setGeometry(QRect(20, 90, 40, 40))
        self.exit_btn.setMinimumSize(QSize(40, 40))
        self.exit_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"	border-radius:20px;\n"
"	background-color:rgb(0, 170, 127);\n"
"	color:white;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"	border:2px solid rgb(0, 255, 255);\n"
"	border-radius:20px;\n"
"	\n"
"}\n"
"")
        self.exit_btn.setCheckable(False)
        self.Menu_btn = QPushButton(self.bgd_wgt)
        self.Menu_btn.setObjectName(u"Menu_btn")
        self.Menu_btn.setGeometry(QRect(19, 9, 40, 40))
        self.Menu_btn.setMinimumSize(QSize(40, 40))
        self.Menu_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"	border-radius:20px;\n"
"	background-color:rgb(0, 170, 127);\n"
"	color:white;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"	border:2px solid rgb(0, 255, 255);\n"
"	border-radius:20px;\n"
"	\n"
"}\n"
"QPushButton:checked{\n"
"\n"
"	background-color:rgb(63, 126, 31);\n"
"	\n"
"}")
        self.Menu_btn.setCheckable(True)
        self.reset_btn = QPushButton(self.bgd_wgt)
        self.reset_btn.setObjectName(u"reset_btn")
        self.reset_btn.setGeometry(QRect(70, 60, 40, 40))
        self.reset_btn.setMinimumSize(QSize(40, 40))
        self.reset_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"	border-radius:20px;\n"
"	background-color:rgb(0, 170, 127);\n"
"	color:white;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"	border:2px solid rgb(0, 255, 255);\n"
"	border-radius:20px;\n"
"	\n"
"}\n"
"")
        self.reset_btn.setCheckable(False)
        self.about_btn = QPushButton(self.bgd_wgt)
        self.about_btn.setObjectName(u"about_btn")
        self.about_btn.setGeometry(QRect(90, 10, 40, 40))
        self.about_btn.setMinimumSize(QSize(40, 40))
        self.about_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"	border-radius:20px;\n"
"	background-color:rgb(0, 170, 127);\n"
"	color:white;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"	border:2px solid rgb(0, 255, 255);\n"
"	border-radius:20px;\n"
"	\n"
"}\n"
"")
        self.about_btn.setCheckable(False)
        self.layoutWidget = QWidget(self.bgd_wgt)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(310, 130, 245, 248))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.name_lb = QLabel(self.layoutWidget)
        self.name_lb.setObjectName(u"name_lb")
        self.name_lb.setStyleSheet(u"font: 12pt \"\u6977\u4f53\";\n"
"color:rgb(220, 84, 71);\n"
"font-weight: 500;")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.name_lb)

        self.name_le = QLineEdit(self.layoutWidget)
        self.name_le.setObjectName(u"name_le")
        self.name_le.setMinimumSize(QSize(0, 35))
        self.name_le.setStyleSheet(u"border:none;\n"
"border-bottom:2px solid rgb(220, 84, 71);\n"
"background-color: transparent;\n"
"color:rgb(220, 84, 71);\n"
"font-size:12px;\n"
"font-weight:500;\n"
"\n"
"")
        self.name_le.setClearButtonEnabled(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.name_le)

        self.pwd_lb = QLabel(self.layoutWidget)
        self.pwd_lb.setObjectName(u"pwd_lb")
        self.pwd_lb.setStyleSheet(u"font: 12pt \"\u6977\u4f53\";\n"
"color:rgb(220, 84, 71);\n"
"font-weight: 500;")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.pwd_lb)

        self.pwd_le = QLineEdit(self.layoutWidget)
        self.pwd_le.setObjectName(u"pwd_le")
        self.pwd_le.setMinimumSize(QSize(0, 35))
        self.pwd_le.setStyleSheet(u"border:none;\n"
"border-bottom:2px solid rgb(220, 84, 71);\n"
"background-color: transparent;\n"
"color:rgb(220, 84, 71);\n"
"font-size:12px;\n"
"font-weight:500;\n"
"\n"
"")
        self.pwd_le.setClearButtonEnabled(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.pwd_le)

        self.cfm_lb = QLabel(self.layoutWidget)
        self.cfm_lb.setObjectName(u"cfm_lb")
        self.cfm_lb.setStyleSheet(u"font: 12pt \"\u6977\u4f53\";\n"
"color:rgb(220, 84, 71);\n"
"font-weight: 500;")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.cfm_lb)

        self.cfm_le = QLineEdit(self.layoutWidget)
        self.cfm_le.setObjectName(u"cfm_le")
        self.cfm_le.setMinimumSize(QSize(0, 35))
        self.cfm_le.setStyleSheet(u"border:none;\n"
"border-bottom:2px solid rgb(220, 84, 71);\n"
"background-color: transparent;\n"
"color:rgb(220, 84, 71);\n"
"font-size:12px;\n"
"font-weight:500;\n"
"\n"
"")
        self.cfm_le.setClearButtonEnabled(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cfm_le)

        self.register_btn = QPushButton(self.layoutWidget)
        self.register_btn.setObjectName(u"register_btn")
        self.register_btn.setEnabled(False)
        self.register_btn.setMinimumSize(QSize(0, 45))
        self.register_btn.setStyleSheet(u"QPushButton {\n"
"	background-color:rgb(220, 84, 71);\n"
"	color:white;\n"
"	border-radius: 10px;\n"
" \n"
"}\n"
"QPushButton:disabled {\n"
"	background-color:rgb(150, 150, 150);\n"
"	color:rgb(188, 188, 188);\n"
" \n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(255, 96, 82);\n"
" \n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(177, 67, 57);\n"
" \n"
"}\n"
"")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.register_btn)

        self.exit_btn.raise_()
        self.reset_btn.raise_()
        self.about_btn.raise_()
        self.layoutWidget.raise_()
        self.Menu_btn.raise_()

        self.horizontalLayout.addWidget(self.bgd_wgt)

#if QT_CONFIG(shortcut)
        self.name_lb.setBuddy(self.name_le)
        self.pwd_lb.setBuddy(self.pwd_le)
        self.cfm_lb.setBuddy(self.cfm_le)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.exit_btn.setText(QCoreApplication.translate("Form", u"\u9000\u51fa", None))
        self.Menu_btn.setText(QCoreApplication.translate("Form", u"\u83dc\u5355", None))
        self.reset_btn.setText(QCoreApplication.translate("Form", u"\u91cd\u7f6e", None))
        self.about_btn.setText(QCoreApplication.translate("Form", u"\u5173\u4e8e", None))
        self.name_lb.setText(QCoreApplication.translate("Form", u"\u59d3    \u540d(&u)\uff1a", None))
        self.name_le.setText("")
        self.pwd_lb.setText(QCoreApplication.translate("Form", u"\u5bc6    \u7801(&p)\uff1a", None))
        self.pwd_le.setText("")
        self.cfm_lb.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4\u5bc6\u7801(&c)\uff1a", None))
        self.cfm_le.setText("")
        self.register_btn.setText(QCoreApplication.translate("Form", u"\u6ce8\u518c", None))
    # retranslateUi

