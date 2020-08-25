# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'selectpage.ui'
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
        Form.resize(709, 556)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.items_lst = QListWidget(Form)
        QListWidgetItem(self.items_lst)
        QListWidgetItem(self.items_lst)
        QListWidgetItem(self.items_lst)
        self.items_lst.setObjectName(u"items_lst")

        self.horizontalLayout.addWidget(self.items_lst)

        self.pages_skt = QStackedWidget(Form)
        self.pages_skt.setObjectName(u"pages_skt")
        self.word_page_wgt = QWidget()
        self.word_page_wgt.setObjectName(u"word_page_wgt")
        self.word_page_wgt.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(100, 200, 50);\n"
"}")
        self.pages_skt.addWidget(self.word_page_wgt)
        self.text_page_wgt = QWidget()
        self.text_page_wgt.setObjectName(u"text_page_wgt")
        self.text_page_wgt.setStyleSheet(u"QWidget{background-color: rgb(190, 143, 78);}\n"
"")
        self.pages_skt.addWidget(self.text_page_wgt)
        self.chinese_page_wgt = QWidget()
        self.chinese_page_wgt.setObjectName(u"chinese_page_wgt")
        self.pages_skt.addWidget(self.chinese_page_wgt)

        self.horizontalLayout.addWidget(self.pages_skt)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.retranslateUi(Form)

        self.pages_skt.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))

        __sortingEnabled = self.items_lst.isSortingEnabled()
        self.items_lst.setSortingEnabled(False)
        ___qlistwidgetitem = self.items_lst.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"\u9879\u76ee1", None));
        ___qlistwidgetitem1 = self.items_lst.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form", u"\u9879\u76ee2", None));
        ___qlistwidgetitem2 = self.items_lst.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Form", u"\u9879\u76ee3", None));
        self.items_lst.setSortingEnabled(__sortingEnabled)

    # retranslateUi

