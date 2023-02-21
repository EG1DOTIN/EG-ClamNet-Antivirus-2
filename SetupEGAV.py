"""
SetupEGAV.py :=> this file is used to install/uninstall EG ClamNet Antivirus
"""

import sys
import time
from os import path, getcwd

from PySide6 import QtCore, QtGui, QtWidgets

import pyUIClasses.log_info as log_info
import pyUIClasses.setup_menu as setup_menu
from EGAVMsgNPopup import EGAVMessageYN, EGAVMessage
from EGAVResources import EGAVTheme, EGAVResources, EGAVPaths
from EGAVTitleBar import EGAVTitleBar
from InfoWindow import LicenseWindow
from config import EXE_SETUP_CLAMAV, DEBUG_CODE
from custom import OS, do_nothing
from custom import check_network, is_version_changed


class SetupMenu(QtWidgets.QWidget):
    def __init__(self):
        super(SetupMenu, self).__init__()
        # self.title_bar.setMinimumSize(QtCore.QSize(self.size().width(), self.title_bar.height()))
        # self.title_bar.setMaximumSize(QtCore.QSize(self.size().width(), self.title_bar.height()))
        self.layout = QtWidgets.QVBoxLayout()
        self.title_bar = EGAVTitleBar(self)
        self.ui = setup_menu.Ui_Form()
        self.setupUi()
        self.resetUi()
        self.setEvents()
        self.initialize()

    def setupUi(self):
        self.ui.setupUi(self)

    def setUi_TitleBar(self):
        # adding title bar
        self.layout.addWidget(self.title_bar)
        self.layout.addStretch(-1)
        self.layout.addWidget(self.ui.verticalLayoutWidget)
        self.layout.addSpacing(20)
        self.layout.addStretch(-1)
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.title_bar.setFixedWidth(self.width())

    def resetUi(self):
        self.setUi_TitleBar()
        # self.setWindowIcon(QtGui.QIcon(EGAVResources.EGAV_WINDOW_ICON))
        # self.setWindowTitle(EGAVTheme.SetupMenu.title)
        self.setStyleSheet(EGAVTheme.SetupMenu.style_widget)
        self.ui.pushButton.setStyleSheet(EGAVTheme.SetupMenu.style_pushButton)
        self.ui.pushButton_2.setStyleSheet(EGAVTheme.SetupMenu.style_pushButton)
        self.ui.pushButton_3.setStyleSheet(EGAVTheme.SetupMenu.style_pushButton)
        self.ui.pushButton_4.setStyleSheet(EGAVTheme.SetupMenu.style_pushButton)
        icon = QtGui.QIcon(EGAVResources.EGAV_WINDOW_ICON)
        self.setWindowIcon(icon)

    def setEvents(self):
        self.ui.pushButton.clicked.connect(self.on_install)
        self.ui.pushButton_2.clicked.connect(self.on_uninstall)
        self.ui.pushButton_3.clicked.connect(self.on_update)
        self.ui.pushButton_4.clicked.connect(self.on_send_error_logs)

        # QtCore.QObject.connect(self.ui.pushButton,
        #                        QtCore.SIGNAL("clicked()"),
        #                        self.on_install)

    def initialize(self):
        try:
            info_setup = EGAVPaths.getInstalled()
        except:
            EGAVPaths.setInstalled()
            info_setup = EGAVPaths.getInstalled()

        if info_setup["status"]:
            # self.ui.pushButton.setText("Installed")
            self.ui.pushButton.setEnabled(False)
            self.ui.pushButton_2.setEnabled(True)
            self.ui.pushButton_3.setEnabled(True)
        else:
            self.ui.pushButton.setEnabled(True)
            self.ui.pushButton_2.setEnabled(False)
            self.ui.pushButton_3.setEnabled(False)
        # log all required paths
        from ClamAVResources import log_all_paths_info
        log_all_paths_info()

    def on_install(self):
        print("install button clicked")
        # self.hide()
        if not check_network():
            EGAVMessage().simpleMessage(msg="Please check your internet connection\n and try again.")
            return

        # show license window
        lw = LicenseWindow()
        lw.exec()
        if not lw.accepted:
            return

        os_detail = OS.get_os_details()
        if os_detail == "Windows":
            from runasroot import is_admin
            if is_admin():
                w = SetupDetail(parent=None, setup_detail="install")
                w.show()
            else:
                yn = EGAVMessageYN(messageText="For installation and starting the clamav services,\n"
                                               "it is required to run as admin. Would you like to \n"
                                               "restart as admin ?")
                yn.setModal(True)
                # print("showing yes no dialog")
                yn.exec()
                if yn.bAccepted == 1:
                    from elevate import elevate
                    self.close()
                    elevate(show_console=False)
                else:
                    return
        else:
            w = SetupDetail(parent=None, setup_detail="install")
            w.show()
        self.close()
        return

    def on_uninstall(self):
        print("uninstall button clicked")
        os_detail = OS.get_os_details()
        if os_detail == "Windows":
            from runasroot import is_admin
            if is_admin():
                w = SetupDetail(parent=None, setup_detail="uninstall")
                w.show()
            else:
                yn = EGAVMessageYN(messageText="To remove and stop the clamav services,\n"
                                               "it is required to run as admin. Would you like to \n"
                                               "restart as admin ?")
                yn.setModal(True)
                yn.exec()
                if yn.bAccepted == 1:
                    from elevate import elevate
                    self.close()
                    elevate(show_console=False)
                else:
                    return
        else:
            w = SetupDetail(parent=None, setup_detail="uninstall")
            w.show()
        self.close()
        return

    def on_update(self, e):
        print("Clicked on Update")
        # check version file
        if is_version_changed():
            if not check_network():
                EGAVMessage().simpleMessage(msg="Please check your internet connection and try again.")
                return

            os_detail = OS.get_os_details()
            if os_detail == "Windows":
                from runasroot import is_admin
                if is_admin():
                    w = SetupDetail(parent=None, setup_detail="updateEGAV")
                    w.setModal()
                    w.show()
                else:
                    yn = EGAVMessageYN(messageText="For installation and starting the clamav services,\n"
                                                   "it is required to run as admin. Would you like to \n"
                                                   "restart as admin ?")
                    yn.setModal(True)
                    # print("showing yes no dialog")
                    yn.exec()
                    if yn.bAccepted == 1:
                        from elevate import elevate
                        self.close()
                        elevate(show_console=False)
                    else:
                        return
            else:
                w = SetupDetail(parent=None, setup_detail="updateEGAV")
                w.setModal()
                w.show()
            return
        else:
            print("Already up to date")
            EGAVMessage().simpleMessage(msg="Version is already up to date.")
        # if diff them download files and extract in prg files
        pass

    def on_send_error_logs(self, e):
        print("Clicked on Send Error Logs")
        EGAVMessage().simpleMessage("This feature is in under construction.\nIt will be added in next version.")
        pass


class SetupDetail(QtWidgets.QWidget):
    def __init__(self, parent=None, setup_detail="install"):
        """
        This class is used to command output for installation, uninstallation and update EGCNAV.
        :param parent: parent Window
        :param setup_detail: can be "install" or "uninstall", or "updateEGAV" or "updateClamAV"
        """
        super(SetupDetail, self).__init__(parent)

        self.parent = parent
        self.setup_detail = setup_detail
        self.os = OS.get_os_details()

        self.layout = QtWidgets.QVBoxLayout()
        self.title_bar = EGAVTitleBar(self)
        self.ui = log_info.Ui_Form()
        self.p = QtCore.QProcess(self)
        self.icon = QtGui.QIcon(EGAVResources.EGAV_WINDOW_ICON)

        self.setupUi()
        self.resetUi()
        self.initialize()

    def initialize(self):
        # Download required setup files
        # self.ui.textEdit.setPlainText("Please wait while downloading required setup files...")
        # downloadEGAVFilesNExtract()
        self.p.setProgram("dirb")
        self.p.setProcessChannelMode(QtCore.QProcess.MergedChannels)
        self.setWindowIcon(self.icon)
        self.start_process(self.get_process_cmd())
        pass

    def setupUi(self):
        self.ui.setupUi(self)

    def setUi_TitleBar(self):
        # adding title bar
        self.layout.addWidget(self.title_bar)
        self.layout.addStretch(-1)
        self.layout.addWidget(self.ui.verticalLayoutWidget)
        self.layout.addStretch(-1)
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addStretch(-1)
        self.title_bar.setFixedWidth(self.width())

    def resetUi(self):
        self.setUi_TitleBar()
        # self.setWindowIcon(EGAVTheme.)
        # self.setWindowTitle(EGAVTheme.SetupWindow.title)
        if self.setup_detail == "install":
            self.ui.label.setText("Please wait, while installing required components...")
        elif self.setup_detail == "uninstall":
            self.ui.label.setText("Please wait, while uninstalling services and packages...")
        elif self.setup_detail == "updateEGAV":
            self.ui.label.setText("Please wait, while downloading & updating required components...")
        elif self.setup_detail == "updateClamAV":
            self.ui.label.setText("Please wait, while downloading & updating ClamAV executables...")
        else:
            self.ui.label.setText("#UNEXPECTED ERROR!!")
        self.setStyleSheet(EGAVTheme.SetupWindow.style_logInfo_window("QWidget"))
        # self.ui.verticalLayoutWidget.setStyleSheet(EGAVTheme.SetupWindow.style_logInfo_window("QWidget"))
        self.ui.label.setStyleSheet(EGAVTheme.SetupWindow.style_label)
        self.ui.label.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.pushButton.hide()
        self.ui.pushButton_2.hide()
        pass

    def message(self, s):
        # time.sleep(0.01)
        self.ui.textEdit.append(s)

    def get_process_cmd(self, bDistEXE=EXE_SETUP_CLAMAV):
        cmd = None
        if self.setup_detail == "install":
            if not bDistEXE:
                cmd = EGAVPaths.python_str_abspath() + EGAVPaths.file_str("SetupClamAV.py") + " --install"
            else:
                cmd = EGAVPaths.file_str(file="SetupClamAV", installation_path=False) + " --install"
        elif self.setup_detail == "uninstall":
            if not bDistEXE:
                cmd = EGAVPaths.python_str_abspath() + EGAVPaths.file_str("SetupClamAV.py") + " --uninstall"
            else:
                cmd = EGAVPaths.file_str("SetupClamAV") + " --uninstall"
        elif self.setup_detail == "updateEGAV":
            if not bDistEXE:
                cmd = EGAVPaths.python_str_abspath() + EGAVPaths.file_str("EGAVDownloader.py") + " --update"
            else:
                cmd = EGAVPaths.file_str("EGAVDownloader") + " --update"
        elif self.setup_detail == "updateClamAV":
            if not bDistEXE:
                cmd = EGAVPaths.python_str_abspath() + EGAVPaths.file_str("SetupClamAV.py") + " --update"
            else:
                cmd = EGAVPaths.file_str(file="SetupClamAV", installation_path=False) + " --update"
        else:
            cmd = None

        sudo_str = ""
        if self.os == "Windows":
            sudo_str = ""
        elif self.os == "Linux":
            sudo_str = "pkexec "
        elif self.os == "MAC":
            sudo_str = "sudo "
        cmd = sudo_str + cmd
        print(cmd)
        return cmd

    def start_process(self, cmd):
        self.title_bar.setClose(bEnable=False)
        # Keep a reference to the QProcess (e.g. on self) while it's running.
        self.p.readyReadStandardOutput.connect(self.handle_stdout)
        self.p.readyReadStandardError.connect(self.handle_stderr)
        self.p.stateChanged.connect(self.handle_state)
        self.p.finished.connect(self.process_finished)  # Clean up once complete.
        # self.p.start("python3", ['dummy_script.py'])
        self.p.startCommand(cmd)

    def handle_stderr(self):
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        self.message(stderr)

    def handle_stdout(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.message(stdout)

    def handle_state(self, state):
        states = {
            QtCore.QProcess.NotRunning: 'Process Completed',
            QtCore.QProcess.Starting: 'Setup Starting',
            QtCore.QProcess.Running: 'Setup Running',
        }
        state_name = states[state]
        self.message(f" {state_name}")

    def process_finished(self):
        self.message("Finished.")
        self.p = None
        self.title_bar.setClose(bEnable=True)
        setup_logs_filename = "setup_logs.txt"
        setup_logs = self.ui.textEdit.toPlainText()

        if DEBUG_CODE:
            if not OS.Windows():
                setup_logs_filename = path.join(EGAVPaths.LogsDir, setup_logs_filename)
            else:
                setup_logs_filename = path.join(getcwd(), "EGAVLogs", setup_logs_filename)
        else:
            setup_logs_filename = path.join(EGAVPaths.LogsDir, setup_logs_filename)

        with open(setup_logs_filename, 'a', encoding='utf-8') as f:
            print(setup_logs, file=f)

        self.ui.label.setText("Process finished.")
        if self.setup_detail == "updateEGAV":
            time.sleep(1)
            self.close()
            w = SetupDetail(parent=None, setup_detail="updateClamAV")
            w.setModal()
            w.show()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        # if self.parent().windowTitle() == EGAVTheme.SetupMenu.title:
        #     self.parent().close()
        # self.parent().show()
        w = SetupMenu()
        w.show()
        self.close()

    def setModal(self, modal=True):
        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal) if modal else do_nothing()


def main():
    app = QtWidgets.QApplication(sys.argv)
    w = SetupMenu()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
