"""
EGAVMsgNPopup.py :=> This file is used for showing Messages, Custom Dialogs, Notification Popups
"""

import sys
from webbrowser import open as open_browser
from webbrowser import open_new as web_open_link

from PySide6 import QtGui, QtCore, QtWidgets

from EGAVResources import EGAVTheme
from config import OtherLinks
from custom import print_v1, run_command_async_and_get_output
from singleObj import clamav_commands


class CustomQDialog(QtWidgets.QDialog):
    def __init__(self):
        super(CustomQDialog, self).__init__()
        self.pressing = False
        self.start = QtCore.QPoint(0, 0)
        self.end = None
        self.movement = None

    def resizeEvent(self, QResizeEvent):
        super(QtWidgets.QDialog, self).resizeEvent(QResizeEvent)
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
            self.setGeometry(self.mapToGlobal(self.movement).x(),
                             self.mapToGlobal(self.movement).y(),
                             self.width(),
                             self.height())
            self.start = self.end


class EGAVInfoPopup(QtWidgets.QDialog):
    def __init__(self, eg_label_lower_point):
        from pyUIClasses.info_popup import Ui_Dialog
        super(EGAVInfoPopup, self).__init__()
        self.ui = Ui_Dialog()
        self.setUi()
        self.resetUi()
        self.setEvents()
        self.initUi()
        self.move(eg_label_lower_point)

    def initUi(self):
        pass

    def setUi(self):
        self.ui.setupUi(self)

    def resetUi(self):
        self.setWindowFlags(QtCore.Qt.Popup | QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet(EGAVTheme.InfoPopup.style_dialog)
        self.ui.label.setStyleSheet(EGAVTheme.InfoPopup.style_label_eg)
        self.ui.label_15.setStyleSheet(EGAVTheme.InfoPopup.style_label_ClamNet)
        self.ui.label_2.setStyleSheet(EGAVTheme.InfoPopup.style_label_antivirus)
        self.ui.label_3.setStyleSheet(EGAVTheme.InfoPopup.style_label_year)
        version = "ClamAV"
        egav_version = "Version: 2.0.x"
        try:
            version = run_command_async_and_get_output(clamav_commands.clamscan_exe + " -V")
            egav_version = version.replace("ClamAV", "  Version:2.0.")
            egav_version = egav_version.replace(" ", "")
        except Exception as e:
            print_v1("error: " + e.__str__())
            pass
        self.ui.label_3.setText(egav_version)
        self.ui.label.setStyleSheet(EGAVTheme.InfoPopup.style_label_eg)
        self.ui.label_2.setStyleSheet(EGAVTheme.InfoPopup.style_label_antivirus)
        self.ui.label_3.setStyleSheet(EGAVTheme.InfoPopup.style_label_year)

        self.ui.label_10.setText("")
        self.ui.label_10.setStyleSheet(EGAVTheme.InfoPopup.style_label_image_egav)

        self.ui.label_4.setStyleSheet(EGAVTheme.InfoPopup.style_label_copyright_website_email)
        self.ui.label_6.setStyleSheet(EGAVTheme.InfoPopup.style_label_copyright_website_email)
        self.ui.label_8.setStyleSheet(EGAVTheme.InfoPopup.style_label_copyright_website_email)

        self.ui.label_5.setStyleSheet(EGAVTheme.InfoPopup.style_label_copyright_text)
        self.ui.label_7.setStyleSheet(EGAVTheme.InfoPopup.style_label_website_email_text)
        self.ui.label_9.setStyleSheet(EGAVTheme.InfoPopup.style_label_website_email_text)

        self.ui.label_11.setStyleSheet(EGAVTheme.InfoPopup.style_label_poweredBy_GuiBy)
        self.ui.label_13.setStyleSheet(EGAVTheme.InfoPopup.style_label_poweredBy_GuiBy)

        self.ui.label_12.setText("")
        self.ui.label_14.setText("")
        self.ui.label_12.setStyleSheet(EGAVTheme.InfoPopup.style_label_image_clamAV)
        self.ui.label_14.setStyleSheet(EGAVTheme.InfoPopup.style_label_image_QtPyside6)

        self.ui.label_12.setMinimumSize(EGAVTheme.InfoPopup.size_label_image_clamAV)
        self.ui.label_12.setMaximumSize(EGAVTheme.InfoPopup.size_label_image_clamAV)
        self.ui.label_14.setMinimumSize(EGAVTheme.InfoPopup.size_label_image_QtPyside6)
        self.ui.label_14.setMaximumSize(EGAVTheme.InfoPopup.size_label_image_QtPyside6)

        # self.setToolTip("<b> Double Click on window to close...</b>")
        self.ui.label_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ui.label_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ui.label_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ui.label_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ui.label_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        try:
            self.ui.label_11.setText(self.ui.label_11.text() + " " + version)
            self.ui.label_13.setText(self.ui.label_13.text() + " " + "PySide6")
        except Exception as e:
            print_v1("error: " + e.__str__())
            pass

    def setEvents(self):
        self.ui.label_7.mousePressEvent = self.on_eg1_website_click
        self.ui.label_10.mousePressEvent = self.on_egav_label_image_click
        self.ui.label_12.mousePressEvent = self.on_clamAV_label_image_click
        self.ui.label_14.mousePressEvent = self.on_pyside6_label_image_click
        self.ui.label_9.mousePressEvent = self.on_eg1email_click

    def on_eg1email_click(self, e):
        email_link = 'mailto:' + self.ui.label_9.text()[1:-1]
        print(email_link)
        web_open_link(email_link)
        pass

    def on_eg1_website_click(self, e):
        open_browser(url=self.ui.label_7.text())

    def on_egav_label_image_click(self, e):
        open_browser(url="")

    def on_clamAV_label_image_click(self, e):
        open_browser(url=OtherLinks.CLAMAV_WEBSITE_LINK)

    def on_pyside6_label_image_click(self, e):
        open_browser(url=OtherLinks.PYSIDE6_WIKI_LINK)

    def mouseDoubleClickEvent(self, e):
        # e.accept()
        self.accept()
        self.done(0)
        # self.hide()


class EGAVInputPopup(CustomQDialog):
    def __init__(self, editItem=False, itemText=None):
        from pyUIClasses.input_popup import Ui_Dialog
        super(EGAVInputPopup, self).__init__()
        self.inputText = ""
        self.bAccepted = False
        self.bEditItem = editItem
        self.ui = Ui_Dialog()

        if self.bEditItem:
            if itemText is None:
                self.itemText = " "
            else:
                self.itemText = itemText

        self.setUi()
        self.resetUi()
        self.setEvents()

    def setUi(self):
        self.ui.setupUi(self)

    def resetUi(self):
        if self.bEditItem:
            self.ui.label.setText("Edit Dialog")
            self.ui.label_2.setText("Edit Item")
            self.ui.lineEdit.setText(self.itemText)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet(EGAVTheme.InputPopup.style_dialog)
        self.ui.label.setStyleSheet(EGAVTheme.InputPopup.style_label)
        self.ui.label_2.setStyleSheet(EGAVTheme.InputPopup.style_label)
        self.ui.lineEdit.setStyleSheet(EGAVTheme.InputPopup.style_lineEdit)
        self.ui.pushButton.setStyleSheet(EGAVTheme.InputPopup.style_pushButton)
        self.ui.pushButton_2.setStyleSheet(EGAVTheme.InputPopup.style_pushButton1)
        self.ui.pushButton_3.setStyleSheet(EGAVTheme.InputPopup.style_pushButton1)
        self.ui.groupBox.setStyleSheet(EGAVTheme.InputPopup.style_groupBox)
        self.ui.groupBox_2.setStyleSheet(EGAVTheme.InputPopup.style_groupBox1)

    def setEvents(self):
        self.ui.pushButton.clicked.connect(self.onCloseDialog)
        self.ui.pushButton_2.clicked.connect(self.onOk)
        self.ui.pushButton_3.clicked.connect(self.onCancel)

    def onCloseDialog(self):
        print_v1("Button Clicked: EGAVInputPopup -> Close")
        self.inputText = ""
        self.bAccepted = False
        self.close()

    def onOk(self):
        lineEditText = self.ui.lineEdit.text()
        if lineEditText == "" or lineEditText.__contains__(" "):
            self.ui.lineEdit.setFocus()
            return
        print_v1("Button Clicked: EGAVInputPopup -> OK")
        self.inputText = self.ui.lineEdit.text()
        self.bAccepted = True
        self.close()

    def onCancel(self):
        print_v1("Button Clicked: EGAVInputPopup -> Cancel")
        self.inputText = ""
        self.bAccepted = False
        self.close()


class EGAVMessageYN(CustomQDialog):
    def __init__(self, messageText="Would you want to proceed forward?"):
        from pyUIClasses.msg_popupYN import Ui_Dialog
        super(EGAVMessageYN, self).__init__()
        self.messageText = messageText
        self.bAccepted = -1
        self.ui = Ui_Dialog()

        self.setUi()
        self.resetUi()
        self.setEvents()

    def setUi(self):
        self.ui.setupUi(self)

    def resetUi(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet(EGAVTheme.MessagePopup.style_dialog)
        self.ui.label.setStyleSheet(EGAVTheme.MessagePopup.style_label)
        self.ui.label_2.setStyleSheet(EGAVTheme.MessagePopup.style_label)
        self.ui.pushButton.setStyleSheet(EGAVTheme.MessagePopup.style_pushButton)
        self.ui.pushButton_2.setStyleSheet(EGAVTheme.MessagePopup.style_pushButton1)
        self.ui.pushButton_3.setStyleSheet(EGAVTheme.MessagePopup.style_pushButton1)
        self.ui.pushButton_4.setStyleSheet(EGAVTheme.MessagePopup.style_pushButton1)
        self.ui.groupBox.setStyleSheet(EGAVTheme.MessagePopup.style_groupBox)
        self.ui.groupBox_2.setStyleSheet(EGAVTheme.MessagePopup.style_groupBox1)
        self.ui.label_2.setText(self.messageText)

    def setEvents(self):
        self.ui.pushButton.clicked.connect(self.onCloseDialog)
        self.ui.pushButton_2.clicked.connect(self.onYes)
        self.ui.pushButton_3.clicked.connect(self.onCancel)
        self.ui.pushButton_4.clicked.connect(self.onNo)

    def onCloseDialog(self):
        print_v1("Button Clicked: EGAVMessageYN -> Close")
        self.close()

    def onYes(self):
        print_v1("Button Clicked: EGAVMessageYN -> Yes")
        self.bAccepted = 1
        self.close()

    def onNo(self):
        print_v1("Button Clicked: EGAVMessageYN -> No")
        self.bAccepted = 0
        self.close()

    def onCancel(self):
        print_v1("Button Clicked: EGAVMessageYN -> Cancel")
        self.close()


class EGAVMessage(CustomQDialog):
    def __init__(self, messageText="This is a simple text MessageBox"):
        from pyUIClasses.msg_popup import Ui_Dialog
        super(EGAVMessage, self).__init__()
        self.messageText = messageText
        self.ui = Ui_Dialog()
        self.setUi()
        self.resetUi()
        self.setEvents()

        # self.init()

    def setUi(self):
        self.ui.setupUi(self)

    def resetUi(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet(EGAVTheme.MessagePopup.style_dialog)
        self.ui.label.setStyleSheet(EGAVTheme.MessagePopup.style_label)
        self.ui.label_2.setStyleSheet(EGAVTheme.MessagePopup.style_label)
        self.ui.pushButton.setStyleSheet(EGAVTheme.MessagePopup.style_pushButton)
        self.ui.pushButton_2.setStyleSheet(EGAVTheme.MessagePopup.style_pushButton1)
        self.ui.groupBox.setStyleSheet(EGAVTheme.MessagePopup.style_groupBox)
        self.ui.groupBox_2.setStyleSheet(EGAVTheme.MessagePopup.style_groupBox1)
        self.ui.label_2.setText(self.messageText)

    def setEvents(self):
        self.ui.pushButton.clicked.connect(self.onCloseDialog)
        self.ui.pushButton_2.clicked.connect(self.onOk)

    def onCloseDialog(self):
        print_v1("Button Clicked: EGAVMessage -> Close ")
        self.close()

    def onOk(self):
        print_v1("Button Clicked: EGAVMessage -> OK")
        self.close()

    def simpleMessage(self, msg: str) -> None:
        self.messageText = msg
        self.ui.label_2.setText(self.messageText)
        self.setModal(True)
        self.exec()


def showEGAVInfoPopup():
    app = QtWidgets.QApplication(sys.argv)
    ex = EGAVInfoPopup(QtCore.QPoint(100, 120))
    ex.exec()
    # ex.show()
    # sys.exit(app.exec())


def showEGAVMessagePopup(yes_no=False):
    app = QtWidgets.QApplication(sys.argv)
    if yes_no:
        ex = EGAVMessageYN()
    else:
        ex = EGAVMessage()
    ex.exec()
    sys.exit()


if __name__ == '__main__':
    # test any code here
    pass
