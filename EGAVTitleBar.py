"""
EGAVTitleBar.py :=> This file provides Title Bar UI for all windows in EG ClamNet Antivirus
"""

import sys
from PySide6 import QtGui, QtCore, QtWidgets
from pyUIClasses.title_bar import Ui_Form as title_bar
from EGAVResources import EGAVTheme
from EGAVMsgNPopup import EGAVInfoPopup
from custom import print_v1


class EGAVTitleBar(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(EGAVTitleBar, self).__init__()

        self.parent = parent
        print(self.parent.width())
        self.pressing = False
        self.start = QtCore.QPoint(0, 0)
        self.end = None
        self.movement = None
        self.close = True
        self.ui = title_bar()

        self.setupUi()
        self.resetUi()
        self.setEvents()

    def setupUi(self):
        self.ui.setupUi(self)

    def resetUi(self):
        self.parent.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        height = 25
        self.ui.label.setFixedHeight(height)
        self.ui.label_2.setFixedHeight(height)
        self.ui.label_5.setFixedHeight(height)
        self.ui.label_7.setFixedHeight(height)
        self.ui.label_8.setFixedHeight(height)

        self.ui.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ui.pushButton_23.setText("         ")
        self.ui.pushButton_23.setStyleSheet(EGAVTheme.MainWindow.style_close_button_with_image)
        self.ui.label_5.setText("             ")
        self.ui.label_5.setStyleSheet(EGAVTheme.MainWindow.style_icon_titleBar_label)
        self.ui.label_5.setMaximumSize(EGAVTheme.MainWindow.style_icon_titleBar_label_size)
        self.ui.pushButton_22.setText("         ")
        self.ui.pushButton_22.setStyleSheet(EGAVTheme.MainWindow.style_minimize_button_with_image)
        self.ui.label_2.setStyleSheet(EGAVTheme.MainWindow.style_label_Title_EG)
        self.ui.label_4.setStyleSheet(EGAVTheme.MainWindow.style_label_Title_ClamNet)
        self.ui.label.setStyleSheet(EGAVTheme.MainWindow.style_label_Title_Antivirus)

        self.ui.label_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ui.label_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.ui.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.setLayout(self.ui.horizontalLayout_3)
        # self.ui.groupBox_15.setStyleSheet(EGAVTheme.MainWindow.style_titleBar_box)
        # self.ui.horizontalLayoutWidget.setStyleSheet(EGAVTheme.MainWindow.style_titleBar_widget)
        # self.setStyleSheet("""background-color: rgb(64, 69, 74); color: white; """)
        self.setStyleSheet(EGAVTheme.MainWindow.style_titleBar_widget)
        # self.ui.groupBox_15.setStyleSheet("""background-color: rgb(64, 69, 74);""")

    def setEvents(self):
        # self.ui.label.mousePressEvent = self.on_label_EG
        self.ui.label_2.mousePressEvent = self.on_label_EG
        self.ui.label_5.mousePressEvent = self.on_label_EG

        self.ui.pushButton_22.clicked.connect(self.onTitleBarMinimizeButton)
        self.ui.pushButton_23.clicked.connect(self.onTitleBarCloseButton)

    def on_label_EG(self, e):
        globalPos = e.globalPosition()
        label_2_lower_size_x = self.ui.label_2.size().width()
        label_2_lower_size_y = self.ui.label_2.size().height()
        globalPos_x = globalPos.x()
        globalPos_y = globalPos.y()
        move_x = globalPos_x + label_2_lower_size_x / 2
        move_y = globalPos_y + label_2_lower_size_y / 2
        popup = EGAVInfoPopup(eg_label_lower_point=QtCore.QPoint(move_x, move_y))
        popup.show()
        print_v1("EG Antivirus popup")

    def resizeEvent(self, QResizeEvent):
        super(EGAVTitleBar, self).resizeEvent(QResizeEvent)
        # self.title.setFixedWidth(self.parent.width())

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end - self.start
            self.parent.setGeometry(self.mapToGlobal(self.movement).x(),
                                    self.mapToGlobal(self.movement).y(),
                                    self.parent.width(),
                                    self.parent.height())
            self.start = self.end

    def onTitleBarMinimizeButton(self):
        print_v1("Button Clicked: minimize MainWindow")
        self.parent.showMinimized()

    def onTitleBarCloseButton(self):
        print_v1("Button Clicked: close MainWindow")
        if self.close:
            self.parent.close()
        else:
            pass

    def setClose(self, bEnable=True):
        self.close = bEnable


class MyWidjet(QtWidgets.QWidget):
    def __init__(self):
        super(MyWidjet, self).__init__()
        self.setStyleSheet("QWidget { background-color: black; border: 1px solid white; }")
        self.layout = QtWidgets.QVBoxLayout()
        self.title_bar = EGAVTitleBar(self)
        self.layout.addWidget(self.title_bar)
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addStretch(-1)
        self.setMinimumSize(970, 700)
        self.title_bar.setFixedWidth(self.width())
        self.pressing = False


if __name__ == "__main__":
    # test any code here
    pass
