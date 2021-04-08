# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nobk.ui'
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

import nobk_ico_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1000, 500)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btl_wgt = QWidget(Form)
        self.btl_wgt.setObjectName(u"btl_wgt")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btl_wgt.sizePolicy().hasHeightForWidth())
        self.btl_wgt.setSizePolicy(sizePolicy)
        self.btl_wgt.setMinimumSize(QSize(0, 30))
        self.btl_wgt.setMaximumSize(QSize(16777215, 30))
        self.btl_wgt.setStyleSheet(u"QWidget#btl_wgt{background-color: rgb(50, 50, 50);}")
        self.horizontalLayout_5 = QHBoxLayout(self.btl_wgt)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.logo_wgt = QWidget(self.btl_wgt)
        self.logo_wgt.setObjectName(u"logo_wgt")
        self.logo_wgt.setMinimumSize(QSize(60, 0))
        self.horizontalLayout_3 = QHBoxLayout(self.logo_wgt)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.logo_lb = QLabel(self.logo_wgt)
        self.logo_lb.setObjectName(u"logo_lb")
        self.logo_lb.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.logo_lb.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.logo_lb)


        self.horizontalLayout_5.addWidget(self.logo_wgt)

        self.dx_wgt = QWidget(self.btl_wgt)
        self.dx_wgt.setObjectName(u"dx_wgt")
        self.horizontalLayout_2 = QHBoxLayout(self.dx_wgt)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.fd_btn = QPushButton(self.dx_wgt)
        self.fd_btn.setObjectName(u"fd_btn")
        self.fd_btn.setMaximumSize(QSize(30, 16777215))
        self.fd_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"	border: 1px solid gray;\n"
"}")

        self.horizontalLayout_2.addWidget(self.fd_btn)

        self.bk_btn = QPushButton(self.dx_wgt)
        self.bk_btn.setObjectName(u"bk_btn")
        self.bk_btn.setMaximumSize(QSize(30, 16777215))
        self.bk_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"	border: 1px solid gray;\n"
"}")

        self.horizontalLayout_2.addWidget(self.bk_btn)


        self.horizontalLayout_5.addWidget(self.dx_wgt)

        self.sercher_le = QLineEdit(self.btl_wgt)
        self.sercher_le.setObjectName(u"sercher_le")

        self.horizontalLayout_5.addWidget(self.sercher_le)

        self.horizontalSpacer = QSpacerItem(262, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.widget = QWidget(self.btl_wgt)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.logo_btn_2 = QPushButton(self.widget)
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

        self.vip_btn = QPushButton(self.widget)
        self.vip_btn.setObjectName(u"vip_btn")
        self.vip_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: orange;\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {\n"
"  	color: white;\n"
"   	\n"
"}")

        self.horizontalLayout_4.addWidget(self.vip_btn)


        self.horizontalLayout_5.addWidget(self.widget)

        self.th_btn = QPushButton(self.btl_wgt)
        self.th_btn.setObjectName(u"th_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.th_btn.sizePolicy().hasHeightForWidth())
        self.th_btn.setSizePolicy(sizePolicy1)
        self.th_btn.setMinimumSize(QSize(50, 0))
        self.th_btn.setMaximumSize(QSize(50, 16777215))
        self.th_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    \n"
"	color: rgb(200, 200, 200);\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(100, 100, 100);\n"
"}")

        self.horizontalLayout_5.addWidget(self.th_btn)

        self.email_btn = QPushButton(self.btl_wgt)
        self.email_btn.setObjectName(u"email_btn")
        sizePolicy1.setHeightForWidth(self.email_btn.sizePolicy().hasHeightForWidth())
        self.email_btn.setSizePolicy(sizePolicy1)
        self.email_btn.setMinimumSize(QSize(50, 0))
        self.email_btn.setMaximumSize(QSize(50, 16777215))
        self.email_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    \n"
"	color: rgb(200, 200, 200);\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(100, 100, 100);\n"
"}")

        self.horizontalLayout_5.addWidget(self.email_btn)

        self.set_btn = QPushButton(self.btl_wgt)
        self.set_btn.setObjectName(u"set_btn")
        sizePolicy1.setHeightForWidth(self.set_btn.sizePolicy().hasHeightForWidth())
        self.set_btn.setSizePolicy(sizePolicy1)
        self.set_btn.setMinimumSize(QSize(50, 0))
        self.set_btn.setMaximumSize(QSize(50, 16777215))
        self.set_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    \n"
"	color: rgb(200, 200, 200);\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(100, 100, 100);\n"
"}")

        self.horizontalLayout_5.addWidget(self.set_btn)

        self.min_btn = QPushButton(self.btl_wgt)
        self.min_btn.setObjectName(u"min_btn")
        sizePolicy1.setHeightForWidth(self.min_btn.sizePolicy().hasHeightForWidth())
        self.min_btn.setSizePolicy(sizePolicy1)
        self.min_btn.setMinimumSize(QSize(45, 0))
        self.min_btn.setMaximumSize(QSize(50, 16777215))
        self.min_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(100, 100, 100);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/resource/img/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.min_btn.setIcon(icon)
        self.min_btn.setFlat(True)

        self.horizontalLayout_5.addWidget(self.min_btn)

        self.max_btn = QPushButton(self.btl_wgt)
        self.max_btn.setObjectName(u"max_btn")
        sizePolicy1.setHeightForWidth(self.max_btn.sizePolicy().hasHeightForWidth())
        self.max_btn.setSizePolicy(sizePolicy1)
        self.max_btn.setMinimumSize(QSize(45, 0))
        self.max_btn.setMaximumSize(QSize(50, 16777215))
        self.max_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(100, 100, 100);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/resource/img/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.max_btn.setIcon(icon1)
        self.max_btn.setFlat(True)

        self.horizontalLayout_5.addWidget(self.max_btn)

        self.cls_btn = QPushButton(self.btl_wgt)
        self.cls_btn.setObjectName(u"cls_btn")
        sizePolicy1.setHeightForWidth(self.cls_btn.sizePolicy().hasHeightForWidth())
        self.cls_btn.setSizePolicy(sizePolicy1)
        self.cls_btn.setMinimumSize(QSize(45, 0))
        self.cls_btn.setMaximumSize(QSize(50, 16777215))
        self.cls_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(122, 0, 0);\n"
"\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/resource/img/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cls_btn.setIcon(icon2)
        self.cls_btn.setFlat(True)

        self.horizontalLayout_5.addWidget(self.cls_btn)


        self.verticalLayout.addWidget(self.btl_wgt)

        self.cnt_wgt = QWidget(Form)
        self.cnt_wgt.setObjectName(u"cnt_wgt")
        self.horizontalLayout = QHBoxLayout(self.cnt_wgt)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_wgt = QWidget(self.cnt_wgt)
        self.left_wgt.setObjectName(u"left_wgt")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.left_wgt.sizePolicy().hasHeightForWidth())
        self.left_wgt.setSizePolicy(sizePolicy2)
        self.left_wgt.setMinimumSize(QSize(50, 0))
        self.left_wgt.setMaximumSize(QSize(50, 16777215))
        self.left_wgt.setStyleSheet(u"background-color: rgb(45, 45, 45);")

        self.horizontalLayout.addWidget(self.left_wgt)

        self.list_wgt = QWidget(self.cnt_wgt)
        self.list_wgt.setObjectName(u"list_wgt")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.list_wgt.sizePolicy().hasHeightForWidth())
        self.list_wgt.setSizePolicy(sizePolicy3)
        self.list_wgt.setMinimumSize(QSize(200, 0))
        self.list_wgt.setMaximumSize(QSize(16777215, 16777215))
        self.list_wgt.setBaseSize(QSize(0, 0))
        self.list_wgt.setMouseTracking(False)
        self.list_wgt.setStyleSheet(u"background-color: rgb(40, 40, 40);")

        self.horizontalLayout.addWidget(self.list_wgt)

        self.right_wgt = QWidget(self.cnt_wgt)
        self.right_wgt.setObjectName(u"right_wgt")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.right_wgt.sizePolicy().hasHeightForWidth())
        self.right_wgt.setSizePolicy(sizePolicy4)
        self.right_wgt.setMinimumSize(QSize(300, 0))
        self.right_wgt.setStyleSheet(u"background-color: rgb(35, 35, 35);")

        self.horizontalLayout.addWidget(self.right_wgt)


        self.verticalLayout.addWidget(self.cnt_wgt)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.logo_lb.setText(QCoreApplication.translate("Form", u"logo", None))
        self.fd_btn.setText(QCoreApplication.translate("Form", u"<", None))
        self.bk_btn.setText(QCoreApplication.translate("Form", u">", None))
        self.sercher_le.setPlaceholderText(QCoreApplication.translate("Form", u"\u641c\u7d22\u89c6\u9891\u3001\u97f3\u4e50\u3001\u7535\u53f0", None))
        self.logo_btn_2.setText(QCoreApplication.translate("Form", u"\u767b\u5f55", None))
        self.vip_btn.setText(QCoreApplication.translate("Form", u"\u5347\u7ea7\u4e3aVIP", None))
        self.th_btn.setText(QCoreApplication.translate("Form", u"\u4e3b\u9898", None))
        self.email_btn.setText(QCoreApplication.translate("Form", u"\u90ae\u7bb1", None))
        self.set_btn.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
        self.min_btn.setText("")
        self.max_btn.setText("")
        self.cls_btn.setText("")
    # retranslateUi

