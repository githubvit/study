# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'c_1.ui'
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

from ca_btn import CaBtn


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(336, 427)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ca_le = QLineEdit(Form)
        self.ca_le.setObjectName(u"ca_le")
        self.ca_le.setEnabled(True)
        self.ca_le.setMinimumSize(QSize(0, 30))
        self.ca_le.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(16)
        self.ca_le.setFont(font)
        self.ca_le.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ca_le.setReadOnly(True)

        self.gridLayout.addWidget(self.ca_le, 0, 0, 1, 4)

        self.ac_btn = CaBtn(Form)
        self.ac_btn.setObjectName(u"ac_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ac_btn.sizePolicy().hasHeightForWidth())
        self.ac_btn.setSizePolicy(sizePolicy)
        self.ac_btn.setCheckable(True)
        self.ac_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.ac_btn, 1, 0, 1, 1)

        self.zf_btn = CaBtn(Form)
        self.zf_btn.setObjectName(u"zf_btn")
        sizePolicy.setHeightForWidth(self.zf_btn.sizePolicy().hasHeightForWidth())
        self.zf_btn.setSizePolicy(sizePolicy)
        self.zf_btn.setCheckable(True)
        self.zf_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.zf_btn, 1, 1, 1, 1)

        self.bf_btn = CaBtn(Form)
        self.bf_btn.setObjectName(u"bf_btn")
        sizePolicy.setHeightForWidth(self.bf_btn.sizePolicy().hasHeightForWidth())
        self.bf_btn.setSizePolicy(sizePolicy)
        self.bf_btn.setCheckable(True)
        self.bf_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.bf_btn, 1, 2, 1, 1)

        self.o4_btn = CaBtn(Form)
        self.o4_btn.setObjectName(u"o4_btn")
        sizePolicy.setHeightForWidth(self.o4_btn.sizePolicy().hasHeightForWidth())
        self.o4_btn.setSizePolicy(sizePolicy)
        self.o4_btn.setCheckable(True)
        self.o4_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.o4_btn, 1, 3, 1, 1)

        self.n7_btn = CaBtn(Form)
        self.n7_btn.setObjectName(u"n7_btn")
        sizePolicy.setHeightForWidth(self.n7_btn.sizePolicy().hasHeightForWidth())
        self.n7_btn.setSizePolicy(sizePolicy)
        self.n7_btn.setCheckable(True)
        self.n7_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.n7_btn, 2, 0, 1, 1)

        self.n8_btn = CaBtn(Form)
        self.n8_btn.setObjectName(u"n8_btn")
        sizePolicy.setHeightForWidth(self.n8_btn.sizePolicy().hasHeightForWidth())
        self.n8_btn.setSizePolicy(sizePolicy)
        self.n8_btn.setCheckable(True)
        self.n8_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.n8_btn, 2, 1, 1, 1)

        self.n9_btn = CaBtn(Form)
        self.n9_btn.setObjectName(u"n9_btn")
        sizePolicy.setHeightForWidth(self.n9_btn.sizePolicy().hasHeightForWidth())
        self.n9_btn.setSizePolicy(sizePolicy)
        self.n9_btn.setCheckable(True)
        self.n9_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.n9_btn, 2, 2, 1, 1)

        self.o3_btn = CaBtn(Form)
        self.o3_btn.setObjectName(u"o3_btn")
        sizePolicy.setHeightForWidth(self.o3_btn.sizePolicy().hasHeightForWidth())
        self.o3_btn.setSizePolicy(sizePolicy)
        self.o3_btn.setCheckable(True)
        self.o3_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.o3_btn, 2, 3, 1, 1)

        self.n4_btn = CaBtn(Form)
        self.n4_btn.setObjectName(u"n4_btn")
        sizePolicy.setHeightForWidth(self.n4_btn.sizePolicy().hasHeightForWidth())
        self.n4_btn.setSizePolicy(sizePolicy)
        self.n4_btn.setCheckable(True)
        self.n4_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.n4_btn, 3, 0, 1, 1)

        self.n5_btn = CaBtn(Form)
        self.n5_btn.setObjectName(u"n5_btn")
        sizePolicy.setHeightForWidth(self.n5_btn.sizePolicy().hasHeightForWidth())
        self.n5_btn.setSizePolicy(sizePolicy)
        self.n5_btn.setCheckable(True)
        self.n5_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.n5_btn, 3, 1, 1, 1)

        self.n6_btn = CaBtn(Form)
        self.n6_btn.setObjectName(u"n6_btn")
        sizePolicy.setHeightForWidth(self.n6_btn.sizePolicy().hasHeightForWidth())
        self.n6_btn.setSizePolicy(sizePolicy)
        self.n6_btn.setCheckable(True)
        self.n6_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.n6_btn, 3, 2, 1, 1)

        self.o1_btn = CaBtn(Form)
        self.o1_btn.setObjectName(u"o1_btn")
        sizePolicy.setHeightForWidth(self.o1_btn.sizePolicy().hasHeightForWidth())
        self.o1_btn.setSizePolicy(sizePolicy)
        self.o1_btn.setCheckable(True)
        self.o1_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.o1_btn, 3, 3, 1, 1)

        self.n1_btn = CaBtn(Form)
        self.n1_btn.setObjectName(u"n1_btn")
        sizePolicy.setHeightForWidth(self.n1_btn.sizePolicy().hasHeightForWidth())
        self.n1_btn.setSizePolicy(sizePolicy)
        self.n1_btn.setCheckable(True)
        self.n1_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.n1_btn, 4, 0, 1, 1)

        self.n2_btn = CaBtn(Form)
        self.n2_btn.setObjectName(u"n2_btn")
        sizePolicy.setHeightForWidth(self.n2_btn.sizePolicy().hasHeightForWidth())
        self.n2_btn.setSizePolicy(sizePolicy)
        self.n2_btn.setCheckable(True)
        self.n2_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.n2_btn, 4, 1, 1, 1)

        self.n3_btn = CaBtn(Form)
        self.n3_btn.setObjectName(u"n3_btn")
        sizePolicy.setHeightForWidth(self.n3_btn.sizePolicy().hasHeightForWidth())
        self.n3_btn.setSizePolicy(sizePolicy)
        self.n3_btn.setCheckable(True)
        self.n3_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.n3_btn, 4, 2, 1, 1)

        self.o2_btn = CaBtn(Form)
        self.o2_btn.setObjectName(u"o2_btn")
        sizePolicy.setHeightForWidth(self.o2_btn.sizePolicy().hasHeightForWidth())
        self.o2_btn.setSizePolicy(sizePolicy)
        self.o2_btn.setCheckable(True)
        self.o2_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.o2_btn, 4, 3, 1, 1)

        self.nd_btn = CaBtn(Form)
        self.nd_btn.setObjectName(u"nd_btn")
        sizePolicy.setHeightForWidth(self.nd_btn.sizePolicy().hasHeightForWidth())
        self.nd_btn.setSizePolicy(sizePolicy)
        self.nd_btn.setCheckable(True)
        self.nd_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.nd_btn, 5, 2, 1, 1)

        self.ca_btn = CaBtn(Form)
        self.ca_btn.setObjectName(u"ca_btn")
        sizePolicy.setHeightForWidth(self.ca_btn.sizePolicy().hasHeightForWidth())
        self.ca_btn.setSizePolicy(sizePolicy)
        self.ca_btn.setCheckable(True)
        self.ca_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.ca_btn, 5, 3, 1, 1)

        self.n0_btn = CaBtn(Form)
        self.n0_btn.setObjectName(u"n0_btn")
        sizePolicy.setHeightForWidth(self.n0_btn.sizePolicy().hasHeightForWidth())
        self.n0_btn.setSizePolicy(sizePolicy)
        self.n0_btn.setCheckable(True)
        self.n0_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.n0_btn, 5, 0, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.ca_le.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.ac_btn.setText(QCoreApplication.translate("Form", u"AC", None))
        self.ac_btn.setProperty("bg", QCoreApplication.translate("Form", u"lightgray", None))
        self.ac_btn.setProperty("role", QCoreApplication.translate("Form", u"ac", None))
        self.zf_btn.setText(QCoreApplication.translate("Form", u"+/-", None))
        self.zf_btn.setProperty("bg", QCoreApplication.translate("Form", u"lightgray", None))
        self.zf_btn.setProperty("role", QCoreApplication.translate("Form", u"zf", None))
        self.bf_btn.setText(QCoreApplication.translate("Form", u"%", None))
        self.bf_btn.setProperty("bg", QCoreApplication.translate("Form", u"lightgray", None))
        self.bf_btn.setProperty("role", QCoreApplication.translate("Form", u"bf", None))
        self.o4_btn.setText(QCoreApplication.translate("Form", u"/", None))
        self.o4_btn.setProperty("bg", QCoreApplication.translate("Form", u"orange", None))
        self.o4_btn.setProperty("role", QCoreApplication.translate("Form", u"op", None))
        self.n7_btn.setText(QCoreApplication.translate("Form", u"7", None))
        self.n7_btn.setProperty("bg", QCoreApplication.translate("Form", u"gray", None))
        self.n7_btn.setProperty("role", QCoreApplication.translate("Form", u"num", None))
        self.n8_btn.setText(QCoreApplication.translate("Form", u"8", None))
        self.n8_btn.setProperty("bg", QCoreApplication.translate("Form", u"gray", None))
        self.n8_btn.setProperty("role", QCoreApplication.translate("Form", u"num", None))
        self.n9_btn.setText(QCoreApplication.translate("Form", u"9", None))
        self.n9_btn.setProperty("bg", QCoreApplication.translate("Form", u"gray", None))
        self.n9_btn.setProperty("role", QCoreApplication.translate("Form", u"num", None))
        self.o3_btn.setText(QCoreApplication.translate("Form", u"*", None))
        self.o3_btn.setProperty("bg", QCoreApplication.translate("Form", u"orange", None))
        self.o3_btn.setProperty("role", QCoreApplication.translate("Form", u"op", None))
        self.n4_btn.setText(QCoreApplication.translate("Form", u"4", None))
        self.n4_btn.setProperty("bg", QCoreApplication.translate("Form", u"gray", None))
        self.n4_btn.setProperty("role", QCoreApplication.translate("Form", u"num", None))
        self.n5_btn.setText(QCoreApplication.translate("Form", u"5", None))
        self.n5_btn.setProperty("bg", QCoreApplication.translate("Form", u"gray", None))
        self.n5_btn.setProperty("role", QCoreApplication.translate("Form", u"num", None))
        self.n6_btn.setText(QCoreApplication.translate("Form", u"6", None))
        self.n6_btn.setProperty("bg", QCoreApplication.translate("Form", u"gray", None))
        self.n6_btn.setProperty("role", QCoreApplication.translate("Form", u"num", None))
        self.o1_btn.setText(QCoreApplication.translate("Form", u"+", None))
        self.o1_btn.setProperty("bg", QCoreApplication.translate("Form", u"orange", None))
        self.o1_btn.setProperty("role", QCoreApplication.translate("Form", u"op", None))
        self.n1_btn.setText(QCoreApplication.translate("Form", u"1", None))
        self.n1_btn.setProperty("bg", QCoreApplication.translate("Form", u"gray", None))
        self.n1_btn.setProperty("role", QCoreApplication.translate("Form", u"num", None))
        self.n2_btn.setText(QCoreApplication.translate("Form", u"2", None))
        self.n2_btn.setProperty("bg", QCoreApplication.translate("Form", u"gray", None))
        self.n2_btn.setProperty("role", QCoreApplication.translate("Form", u"num", None))
        self.n3_btn.setText(QCoreApplication.translate("Form", u"3", None))
        self.n3_btn.setProperty("bg", QCoreApplication.translate("Form", u"gray", None))
        self.n3_btn.setProperty("role", QCoreApplication.translate("Form", u"num", None))
        self.o2_btn.setText(QCoreApplication.translate("Form", u"-", None))
        self.o2_btn.setProperty("bg", QCoreApplication.translate("Form", u"orange", None))
        self.o2_btn.setProperty("role", QCoreApplication.translate("Form", u"op", None))
        self.nd_btn.setText(QCoreApplication.translate("Form", u".", None))
        self.nd_btn.setProperty("bg", QCoreApplication.translate("Form", u"gray", None))
        self.nd_btn.setProperty("role", QCoreApplication.translate("Form", u"num", None))
        self.ca_btn.setText(QCoreApplication.translate("Form", u"=", None))
        self.ca_btn.setProperty("bg", QCoreApplication.translate("Form", u"orange", None))
        self.ca_btn.setProperty("role", QCoreApplication.translate("Form", u"ca", None))
        self.n0_btn.setText(QCoreApplication.translate("Form", u"0", None))
        self.n0_btn.setProperty("bg", QCoreApplication.translate("Form", u"gray", None))
        self.n0_btn.setProperty("role", QCoreApplication.translate("Form", u"num", None))
    # retranslateUi

