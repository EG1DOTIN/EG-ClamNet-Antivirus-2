from os import path
from EGAVTitleBar import EGAVTitleBar
from EGAVResources import EGAVTheme, EGAVResources, EGAVCommonInfo
from PySide6 import QtGui, QtCore, QtWidgets
import pyUIClasses.log_info as info_ui


class InfoWin(QtWidgets.QDialog):
    def __init__(self,
                 parent=None,
                 window_title="Logs Information",
                 info_title="Antivirus",
                 info_text="Antivirus protects a computer from viruses.",
                 button1_caption="OK",
                 button2_caption="Cancel",
                 buttons_hide=True,
                 custom_title_bar=True):
        super(InfoWin, self).__init__(parent)

        self.window_title = window_title
        self.ui = info_ui.Ui_Form()
        self.button1_caption = button1_caption
        self.button2_caption = button2_caption
        self.buttons_hide = buttons_hide
        self.custom_title_bar = custom_title_bar
        self.button1_clicked = False
        self.button2_clicked = False
        if self.custom_title_bar:
            self.layout = QtWidgets.QVBoxLayout()
            self.title_bar = EGAVTitleBar(self)

        self.setupUi()
        self.resetUi(info_title, info_text)
        self.setEvents()

    def setUi_TitleBar(self):
        self.layout.addWidget(self.title_bar)
        self.layout.addWidget(self.ui.verticalLayoutWidget)
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.title_bar.setFixedWidth(self.width())

    def setupUi(self):
        self.ui.setupUi(self)

    def resetUi(self, info_title, info_text):
        if self.custom_title_bar:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setUi_TitleBar()
        else:
            self.setWindowIcon(QtGui.QIcon(EGAVResources.EGAV_WINDOW_ICON))
            self.setWindowTitle(self.window_title)

        self.ui.label.setText(info_title)
        self.setStyleSheet(EGAVTheme.SetupWindow.style_logInfo_window("QDialog"))
        self.ui.label.setStyleSheet(EGAVTheme.SetupWindow.style_label)
        self.ui.label.setAlignment(QtGui.Qt.AlignCenter)
        self.ui.textEdit.setStyleSheet(EGAVTheme.SetupWindow.style_text_edit)
        self.ui.textEdit.insertHtml(info_text)
        self.ui.pushButton.setText(self.button1_caption)
        self.ui.pushButton_2.setText(self.button2_caption)
        self.hideButtons() if self.buttons_hide else None

    def setEvents(self):
        self.ui.pushButton.clicked.connect(self.onButton1)
        self.ui.pushButton_2.clicked.connect(self.onButton2)
        pass

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        try:
            if self.parent().windowTitle() == EGAVTheme.EGAV_TITLE_SCANNER_WINDOW:
                self.parent().close()
        except:
            pass

    def hideButtons(self):
        self.ui.pushButton.hide()
        self.ui.pushButton_2.hide()

    def onButton1(self, e):
        print(self.ui.pushButton.text() + " clicked.")
        self.button1_clicked = True
        pass

    def onButton2(self, e):
        print(self.ui.pushButton_2.text() + " clicked.")
        self.button2_clicked = True
        pass

    def insert_doc_file(self, file=path.join("Docs", "EULA_EGCNAV2_X.htm")):
        print(file)
        f = QtCore.QFile(file)
        f.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
        istream = QtCore.QTextStream(f)
        self.ui.textEdit.setHtml(istream.readAll())
        f.close()


class LicenseWindow(InfoWin):
    def __init__(self):
        super().__init__(
            parent=None,
            window_title=EGAVCommonInfo.EGAV_TITLE_LONG,
            info_title="Please read carefully and accept the license \n "
                       "to use this software on you computer...",
            info_text="",
            button1_caption="Accept",
            button2_caption="Cancel",
            buttons_hide=False,
            custom_title_bar=True
        )

        self.insert_doc_file()
        self.accepted = False
        self.ui.pushButton.setStyleSheet(EGAVTheme.MainWindow.style_pushButton)
        self.ui.pushButton_2.setStyleSheet(EGAVTheme.MainWindow.style_pushButton)

    def onButton1(self, e):
        print("License Accepted")
        self.accepted = True
        self.close()

    def onButton2(self, e):
        print("License Not Accepted")
        self.accepted = False
        self.close()


def showLicense():
    from sys import argv
    app = QtWidgets.QApplication(argv)
    ex = InfoWin(
        parent=None,
        window_title="EG ClamNet Antivirus",
        info_title="Read carefully and accept the license to use this software...",
        info_text="",
        button1_caption="Accept",
        button2_caption="Cancel",
        buttons_hide=False,
        custom_title_bar=True
    )
    ex.insert_doc_file()
    ex.exec()
    if ex.button1_clicked:
        print("License Accepted")
    elif ex.button2_clicked:
        print("License not Accepted")


def showLicenseFromLicenseWindowClass():
    from sys import argv
    app = QtWidgets.QApplication(argv)
    lw = LicenseWindow()
    lw.exec()
    print(lw.accepted)


if __name__ == '__main__':
    showLicenseFromLicenseWindowClass()
    pass
