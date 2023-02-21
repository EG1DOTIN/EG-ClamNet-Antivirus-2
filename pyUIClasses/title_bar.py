# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'title_bar.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1029, 40)
        Form.setMinimumSize(QSize(1024, 40))
        Form.setMaximumSize(QSize(16777215, 40))
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 1031, 40))
        self.groupBox.setMinimumSize(QSize(0, 40))
        self.groupBox.setMaximumSize(QSize(16777215, 40))
        self.groupBox.setStyleSheet(u"background-color: rgb(64, 69, 74);")
        self.horizontalLayoutWidget = QWidget(self.groupBox)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 0, 991, 42))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_5 = QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.label_5)

        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        self.label_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_2, 0, Qt.AlignLeft)

        self.label_4 = QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(20)
        self.label_4.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_21)

        self.pushButton_22 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_22.setObjectName(u"pushButton_22")

        self.horizontalLayout_3.addWidget(self.pushButton_22)

        self.label_8 = QLabel(self.horizontalLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)

        self.pushButton_23 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_23.setObjectName(u"pushButton_23")

        self.horizontalLayout_3.addWidget(self.pushButton_23)

        self.label_7 = QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle("")
        self.label_3.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"EG", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"ClamNet", None))
        self.label.setText(QCoreApplication.translate("Form", u"Antivirus", None))
        self.pushButton_22.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_8.setText("")
        self.pushButton_23.setText(QCoreApplication.translate("Form", u"X", None))
        self.label_7.setText("")
    # retranslateUi

