# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mark.ui'
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
        Form.resize(526, 300)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.jp_btn = QPushButton(Form)
        self.jp_btn.setObjectName(u"jp_btn")

        self.horizontalLayout.addWidget(self.jp_btn)

        self.line_btn = QPushButton(Form)
        self.line_btn.setObjectName(u"line_btn")

        self.horizontalLayout.addWidget(self.line_btn)

        self.sline_btn = QPushButton(Form)
        self.sline_btn.setObjectName(u"sline_btn")

        self.horizontalLayout.addWidget(self.sline_btn)

        self.ty_btn = QPushButton(Form)
        self.ty_btn.setObjectName(u"ty_btn")

        self.horizontalLayout.addWidget(self.ty_btn)

        self.rect_btn = QPushButton(Form)
        self.rect_btn.setObjectName(u"rect_btn")

        self.horizontalLayout.addWidget(self.rect_btn)

        self.sjx_btn = QPushButton(Form)
        self.sjx_btn.setObjectName(u"sjx_btn")

        self.horizontalLayout.addWidget(self.sjx_btn)

        self.txt_btn = QPushButton(Form)
        self.txt_btn.setObjectName(u"txt_btn")

        self.horizontalLayout.addWidget(self.txt_btn)

        self.image_btn = QPushButton(Form)
        self.image_btn.setObjectName(u"image_btn")

        self.horizontalLayout.addWidget(self.image_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.cx_lb = QLabel(Form)
        self.cx_lb.setObjectName(u"cx_lb")
        self.cx_lb.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.cx_lb)

        self.cx_sld = QSlider(Form)
        self.cx_sld.setObjectName(u"cx_sld")
        self.cx_sld.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.cx_sld)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pic_grv = QGraphicsView(Form)
        self.pic_grv.setObjectName(u"pic_grv")

        self.horizontalLayout_3.addWidget(self.pic_grv)

        self.text_te = QTextEdit(Form)
        self.text_te.setObjectName(u"text_te")

        self.horizontalLayout_3.addWidget(self.text_te)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.jp_btn.setText(QCoreApplication.translate("Form", u"\u622a\u5c4f", None))
        self.line_btn.setText(QCoreApplication.translate("Form", u"\u76f4\u7ebf", None))
        self.sline_btn.setText(QCoreApplication.translate("Form", u"\u7ebf\u6761", None))
        self.ty_btn.setText(QCoreApplication.translate("Form", u"\u692d\u5706", None))
        self.rect_btn.setText(QCoreApplication.translate("Form", u"\u77e9\u5f62", None))
        self.sjx_btn.setText(QCoreApplication.translate("Form", u"\u4e09\u89d2\u5f62", None))
        self.txt_btn.setText(QCoreApplication.translate("Form", u"\u6587\u672c", None))
        self.image_btn.setText(QCoreApplication.translate("Form", u"\u56fe\u7247", None))
        self.cx_lb.setText(QCoreApplication.translate("Form", u"\u7c97\u7ec6", None))
        self.text_te.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">text</p></body></html>", None))
    # retranslateUi

