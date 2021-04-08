# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qv1.ui'
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
        Form.resize(1067, 496)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.hw_btn = QPushButton(Form)
        self.hw_btn.setObjectName(u"hw_btn")

        self.horizontalLayout.addWidget(self.hw_btn)

        self.lint_btn = QPushButton(Form)
        self.lint_btn.setObjectName(u"lint_btn")

        self.horizontalLayout.addWidget(self.lint_btn)

        self.cubic_btn = QPushButton(Form)
        self.cubic_btn.setObjectName(u"cubic_btn")

        self.horizontalLayout.addWidget(self.cubic_btn)

        self.rect_btn = QPushButton(Form)
        self.rect_btn.setObjectName(u"rect_btn")

        self.horizontalLayout.addWidget(self.rect_btn)

        self.roundrect_btn = QPushButton(Form)
        self.roundrect_btn.setObjectName(u"roundrect_btn")

        self.horizontalLayout.addWidget(self.roundrect_btn)

        self.ellipse_btn = QPushButton(Form)
        self.ellipse_btn.setObjectName(u"ellipse_btn")

        self.horizontalLayout.addWidget(self.ellipse_btn)

        self.polygon_btn = QPushButton(Form)
        self.polygon_btn.setObjectName(u"polygon_btn")

        self.horizontalLayout.addWidget(self.polygon_btn)

        self.triangle_btn = QPushButton(Form)
        self.triangle_btn.setObjectName(u"triangle_btn")

        self.horizontalLayout.addWidget(self.triangle_btn)

        self.pie_btn = QPushButton(Form)
        self.pie_btn.setObjectName(u"pie_btn")

        self.horizontalLayout.addWidget(self.pie_btn)

        self.arc_btn = QPushButton(Form)
        self.arc_btn.setObjectName(u"arc_btn")

        self.horizontalLayout.addWidget(self.arc_btn)

        self.chord_btn = QPushButton(Form)
        self.chord_btn.setObjectName(u"chord_btn")

        self.horizontalLayout.addWidget(self.chord_btn)

        self.text_btn = QPushButton(Form)
        self.text_btn.setObjectName(u"text_btn")

        self.horizontalLayout.addWidget(self.text_btn)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.earse_btn = QPushButton(Form)
        self.earse_btn.setObjectName(u"earse_btn")

        self.horizontalLayout_2.addWidget(self.earse_btn)

        self.background_btn = QPushButton(Form)
        self.background_btn.setObjectName(u"background_btn")

        self.horizontalLayout_2.addWidget(self.background_btn)

        self.pen_color_btn = QPushButton(Form)
        self.pen_color_btn.setObjectName(u"pen_color_btn")

        self.horizontalLayout_2.addWidget(self.pen_color_btn)

        self.tkness_lb = QLabel(Form)
        self.tkness_lb.setObjectName(u"tkness_lb")
        self.tkness_lb.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.tkness_lb)

        self.tkness_sld = QSlider(Form)
        self.tkness_sld.setObjectName(u"tkness_sld")
        self.tkness_sld.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.tkness_sld)

        self.state_lb = QLabel(Form)
        self.state_lb.setObjectName(u"state_lb")
        self.state_lb.setMinimumSize(QSize(200, 0))
        self.state_lb.setStyleSheet(u"color: rgb(255, 133, 26);")
        self.state_lb.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.state_lb)

        self.screenshot_btn = QPushButton(Form)
        self.screenshot_btn.setObjectName(u"screenshot_btn")

        self.horizontalLayout_2.addWidget(self.screenshot_btn)

        self.media_btn = QPushButton(Form)
        self.media_btn.setObjectName(u"media_btn")

        self.horizontalLayout_2.addWidget(self.media_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.clear_btn = QPushButton(Form)
        self.clear_btn.setObjectName(u"clear_btn")

        self.horizontalLayout_2.addWidget(self.clear_btn)

        self.save_btn = QPushButton(Form)
        self.save_btn.setObjectName(u"save_btn")

        self.horizontalLayout_2.addWidget(self.save_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.handwrite_grv = QGraphicsView(Form)
        self.handwrite_grv.setObjectName(u"handwrite_grv")

        self.verticalLayout.addWidget(self.handwrite_grv)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.hw_btn.setText(QCoreApplication.translate("Form", u"\u624b\u5199", None))
        self.lint_btn.setText(QCoreApplication.translate("Form", u"\u76f4\u7ebf", None))
        self.cubic_btn.setText(QCoreApplication.translate("Form", u"\u66f2\u7ebf", None))
        self.rect_btn.setText(QCoreApplication.translate("Form", u"\u77e9\u5f62", None))
        self.roundrect_btn.setText(QCoreApplication.translate("Form", u"\u5706\u89d2\u77e9\u5f62", None))
        self.ellipse_btn.setText(QCoreApplication.translate("Form", u"\u692d\u5706", None))
        self.polygon_btn.setText(QCoreApplication.translate("Form", u"\u591a\u8fb9\u5f62", None))
        self.triangle_btn.setText(QCoreApplication.translate("Form", u"\u4e09\u89d2\u5f62", None))
        self.pie_btn.setText(QCoreApplication.translate("Form", u"\u6247\u5f62", None))
        self.arc_btn.setText(QCoreApplication.translate("Form", u"\u5f27", None))
        self.chord_btn.setText(QCoreApplication.translate("Form", u"\u5f26", None))
        self.text_btn.setText(QCoreApplication.translate("Form", u"\u6587\u672c", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u56fe\u7247", None))
        self.earse_btn.setText(QCoreApplication.translate("Form", u"\u6a61\u76ae\u64e6", None))
        self.background_btn.setText(QCoreApplication.translate("Form", u"\u80cc\u666f", None))
        self.pen_color_btn.setText(QCoreApplication.translate("Form", u"\u7b14\u8272", None))
        self.tkness_lb.setText(QCoreApplication.translate("Form", u"\u7c97\u7ec6", None))
        self.state_lb.setText(QCoreApplication.translate("Form", u"\u624b\u5199", None))
        self.screenshot_btn.setText(QCoreApplication.translate("Form", u"\u622a\u56fe", None))
        self.media_btn.setText(QCoreApplication.translate("Form", u"\u591a\u5a92\u4f53", None))
        self.clear_btn.setText(QCoreApplication.translate("Form", u"\u6e05\u9664", None))
        self.save_btn.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58", None))
    # retranslateUi

