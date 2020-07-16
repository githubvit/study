# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculate.ui'
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
# from PyQt5.Qt import *

from calculate_btn_class import CalculateBtn


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(367, 436)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 4)

        self.ac_btn = CalculateBtn(Form)
        self.ac_btn.setObjectName(u"ac_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ac_btn.sizePolicy().hasHeightForWidth())
        self.ac_btn.setSizePolicy(sizePolicy)
        self.ac_btn.setCheckable(True)
        self.ac_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.ac_btn, 1, 0, 1, 1)

        self.plus_minus_btn = CalculateBtn(Form)
        self.plus_minus_btn.setObjectName(u"plus_minus_btn")
        sizePolicy.setHeightForWidth(self.plus_minus_btn.sizePolicy().hasHeightForWidth())
        self.plus_minus_btn.setSizePolicy(sizePolicy)
        self.plus_minus_btn.setCheckable(True)
        self.plus_minus_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.plus_minus_btn, 1, 1, 1, 1)

        self.percent_btn = CalculateBtn(Form)
        self.percent_btn.setObjectName(u"percent_btn")
        sizePolicy.setHeightForWidth(self.percent_btn.sizePolicy().hasHeightForWidth())
        self.percent_btn.setSizePolicy(sizePolicy)
        self.percent_btn.setCheckable(True)
        self.percent_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.percent_btn, 1, 2, 1, 1)

        self.division_btn = CalculateBtn(Form)
        self.division_btn.setObjectName(u"division_btn")
        sizePolicy.setHeightForWidth(self.division_btn.sizePolicy().hasHeightForWidth())
        self.division_btn.setSizePolicy(sizePolicy)
        self.division_btn.setCheckable(True)
        self.division_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.division_btn, 1, 3, 1, 1)

        self.n7_btn = CalculateBtn(Form)
        self.n7_btn.setObjectName(u"n7_btn")
        sizePolicy.setHeightForWidth(self.n7_btn.sizePolicy().hasHeightForWidth())
        self.n7_btn.setSizePolicy(sizePolicy)
        self.n7_btn.setCheckable(True)
        self.n7_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.n7_btn, 2, 0, 1, 1)

        self.n8_btn = CalculateBtn(Form)
        self.n8_btn.setObjectName(u"n8_btn")
        sizePolicy.setHeightForWidth(self.n8_btn.sizePolicy().hasHeightForWidth())
        self.n8_btn.setSizePolicy(sizePolicy)
        self.n8_btn.setCheckable(True)
        self.n8_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.n8_btn, 2, 1, 1, 1)

        self.n9_btn = CalculateBtn(Form)
        self.n9_btn.setObjectName(u"n9_btn")
        sizePolicy.setHeightForWidth(self.n9_btn.sizePolicy().hasHeightForWidth())
        self.n9_btn.setSizePolicy(sizePolicy)
        self.n9_btn.setCheckable(True)
        self.n9_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.n9_btn, 2, 2, 1, 1)

        self.multiplication_btn = CalculateBtn(Form)
        self.multiplication_btn.setObjectName(u"multiplication_btn")
        sizePolicy.setHeightForWidth(self.multiplication_btn.sizePolicy().hasHeightForWidth())
        self.multiplication_btn.setSizePolicy(sizePolicy)
        self.multiplication_btn.setCheckable(True)
        self.multiplication_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.multiplication_btn, 2, 3, 1, 1)

        self.n4_btn = CalculateBtn(Form)
        self.n4_btn.setObjectName(u"n4_btn")
        sizePolicy.setHeightForWidth(self.n4_btn.sizePolicy().hasHeightForWidth())
        self.n4_btn.setSizePolicy(sizePolicy)
        self.n4_btn.setCheckable(True)
        self.n4_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.n4_btn, 3, 0, 1, 1)

        self.n5_btn = CalculateBtn(Form)
        self.n5_btn.setObjectName(u"n5_btn")
        sizePolicy.setHeightForWidth(self.n5_btn.sizePolicy().hasHeightForWidth())
        self.n5_btn.setSizePolicy(sizePolicy)
        self.n5_btn.setCheckable(True)
        self.n5_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.n5_btn, 3, 1, 1, 1)

        self.n6_btn = CalculateBtn(Form)
        self.n6_btn.setObjectName(u"n6_btn")
        sizePolicy.setHeightForWidth(self.n6_btn.sizePolicy().hasHeightForWidth())
        self.n6_btn.setSizePolicy(sizePolicy)
        self.n6_btn.setCheckable(True)
        self.n6_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.n6_btn, 3, 2, 1, 1)

        self.sub_btn = CalculateBtn(Form)
        self.sub_btn.setObjectName(u"sub_btn")
        sizePolicy.setHeightForWidth(self.sub_btn.sizePolicy().hasHeightForWidth())
        self.sub_btn.setSizePolicy(sizePolicy)
        self.sub_btn.setCheckable(True)
        self.sub_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.sub_btn, 3, 3, 1, 1)

        self.n1_btn = CalculateBtn(Form)
        self.n1_btn.setObjectName(u"n1_btn")
        sizePolicy.setHeightForWidth(self.n1_btn.sizePolicy().hasHeightForWidth())
        self.n1_btn.setSizePolicy(sizePolicy)
        self.n1_btn.setCheckable(True)
        self.n1_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.n1_btn, 4, 0, 1, 1)

        self.n2_btn = CalculateBtn(Form)
        self.n2_btn.setObjectName(u"n2_btn")
        sizePolicy.setHeightForWidth(self.n2_btn.sizePolicy().hasHeightForWidth())
        self.n2_btn.setSizePolicy(sizePolicy)
        self.n2_btn.setCheckable(True)
        self.n2_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.n2_btn, 4, 1, 1, 1)

        self.n3_btn = CalculateBtn(Form)
        self.n3_btn.setObjectName(u"n3_btn")
        sizePolicy.setHeightForWidth(self.n3_btn.sizePolicy().hasHeightForWidth())
        self.n3_btn.setSizePolicy(sizePolicy)
        self.n3_btn.setCheckable(True)
        self.n3_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.n3_btn, 4, 2, 1, 1)

        self.add_btn = CalculateBtn(Form)
        self.add_btn.setObjectName(u"add_btn")
        sizePolicy.setHeightForWidth(self.add_btn.sizePolicy().hasHeightForWidth())
        self.add_btn.setSizePolicy(sizePolicy)
        self.add_btn.setCheckable(True)
        self.add_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.add_btn, 4, 3, 1, 1)

        self.zero_btn = CalculateBtn(Form)
        self.zero_btn.setObjectName(u"zero_btn")
        sizePolicy.setHeightForWidth(self.zero_btn.sizePolicy().hasHeightForWidth())
        self.zero_btn.setSizePolicy(sizePolicy)
        self.zero_btn.setCheckable(True)
        self.zero_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.zero_btn, 5, 0, 1, 2)

        self.point_btn = CalculateBtn(Form)
        self.point_btn.setObjectName(u"point_btn")
        sizePolicy.setHeightForWidth(self.point_btn.sizePolicy().hasHeightForWidth())
        self.point_btn.setSizePolicy(sizePolicy)
        self.point_btn.setCheckable(True)
        self.point_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.point_btn, 5, 2, 1, 1)

        self.equal_btn = CalculateBtn(Form)
        self.equal_btn.setObjectName(u"equal_btn")
        sizePolicy.setHeightForWidth(self.equal_btn.sizePolicy().hasHeightForWidth())
        self.equal_btn.setSizePolicy(sizePolicy)
        self.equal_btn.setCheckable(True)
        self.equal_btn.setAutoExclusive(True)

        self.gridLayout.addWidget(self.equal_btn, 5, 3, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.ac_btn.setText(QCoreApplication.translate("Form", u"AC", None))
        self.ac_btn.setProperty("bg", QCoreApplication.translate("Form", u"lightgray", None))
        self.ac_btn.setProperty("role", QCoreApplication.translate("Form", u"clear", None))
        self.plus_minus_btn.setText(QCoreApplication.translate("Form", u"+/-", None))
        self.plus_minus_btn.setProperty("bg", QCoreApplication.translate("Form", u"lightgray", None))
        self.plus_minus_btn.setProperty("role", QCoreApplication.translate("Form", u"num", None))
        self.percent_btn.setText(QCoreApplication.translate("Form", u"%", None))
        self.percent_btn.setProperty("bg", QCoreApplication.translate("Form", u"lightgray", None))
        self.percent_btn.setProperty("role", QCoreApplication.translate("Form", u"num", None))
        self.division_btn.setText(QCoreApplication.translate("Form", u"/", None))
        self.division_btn.setProperty("bg", QCoreApplication.translate("Form", u"orange", None))
        self.division_btn.setProperty("role", QCoreApplication.translate("Form", u"operator", None))
        self.n7_btn.setText(QCoreApplication.translate("Form", u"7", None))
        self.n7_btn.setProperty("bg", QCoreApplication.translate("Form", u"gray", None))
        self.n7_btn.setProperty("role", QCoreApplication.translate("Form", u"num", None))
        self.n8_btn.setText(QCoreApplication.translate("Form", u"8", None))
        self.n8_btn.setProperty("bg", QCoreApplication.translate("Form", u"gray", None))
        self.n8_btn.setProperty("role", QCoreApplication.translate("Form", u"num", None))
        self.n9_btn.setText(QCoreApplication.translate("Form", u"9", None))
        self.n9_btn.setProperty("bg", QCoreApplication.translate("Form", u"gray", None))
        self.n9_btn.setProperty("role", QCoreApplication.translate("Form", u"num", None))
        self.multiplication_btn.setText(QCoreApplication.translate("Form", u"*", None))
        self.multiplication_btn.setProperty("bg", QCoreApplication.translate("Form", u"orange", None))
        self.multiplication_btn.setProperty("role", QCoreApplication.translate("Form", u"operator", None))
        self.n4_btn.setText(QCoreApplication.translate("Form", u"4", None))
        self.n4_btn.setProperty("bg", QCoreApplication.translate("Form", u"gray", None))
        self.n4_btn.setProperty("role", QCoreApplication.translate("Form", u"num", None))
        self.n5_btn.setText(QCoreApplication.translate("Form", u"5", None))
        self.n5_btn.setProperty("bg", QCoreApplication.translate("Form", u"gray", None))
        self.n5_btn.setProperty("role", QCoreApplication.translate("Form", u"num", None))
        self.n6_btn.setText(QCoreApplication.translate("Form", u"6", None))
        self.n6_btn.setProperty("bg", QCoreApplication.translate("Form", u"gray", None))
        self.n6_btn.setProperty("role", QCoreApplication.translate("Form", u"num", None))
        self.sub_btn.setText(QCoreApplication.translate("Form", u"-", None))
        self.sub_btn.setProperty("bg", QCoreApplication.translate("Form", u"orange", None))
        self.sub_btn.setProperty("role", QCoreApplication.translate("Form", u"operator", None))
        self.n1_btn.setText(QCoreApplication.translate("Form", u"1", None))
        self.n1_btn.setProperty("bg", QCoreApplication.translate("Form", u"gray", None))
        self.n1_btn.setProperty("role", QCoreApplication.translate("Form", u"num", None))
        self.n2_btn.setText(QCoreApplication.translate("Form", u"2", None))
        self.n2_btn.setProperty("bg", QCoreApplication.translate("Form", u"gray", None))
        self.n2_btn.setProperty("role", QCoreApplication.translate("Form", u"num", None))
        self.n3_btn.setText(QCoreApplication.translate("Form", u"3", None))
        self.n3_btn.setProperty("bg", QCoreApplication.translate("Form", u"gray", None))
        self.n3_btn.setProperty("role", QCoreApplication.translate("Form", u"num", None))
        self.add_btn.setText(QCoreApplication.translate("Form", u"+", None))
        self.add_btn.setProperty("bg", QCoreApplication.translate("Form", u"orange", None))
        self.add_btn.setProperty("role", QCoreApplication.translate("Form", u"operator", None))
        self.zero_btn.setText(QCoreApplication.translate("Form", u"0", None))
        self.zero_btn.setProperty("bg", QCoreApplication.translate("Form", u"gray", None))
        self.zero_btn.setProperty("role", QCoreApplication.translate("Form", u"num", None))
        self.point_btn.setText(QCoreApplication.translate("Form", u".", None))
        self.point_btn.setProperty("bg", QCoreApplication.translate("Form", u"gray", None))
        self.point_btn.setProperty("role", QCoreApplication.translate("Form", u"num", None))
        self.equal_btn.setText(QCoreApplication.translate("Form", u"=", None))
        self.equal_btn.setProperty("bg", QCoreApplication.translate("Form", u"equal", None))
        self.equal_btn.setProperty("role", QCoreApplication.translate("Form", u"calculate", None))
    # retranslateUi

