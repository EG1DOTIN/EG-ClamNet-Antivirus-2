"""
ClamAVUpdater.py :=> This file provide UI to update ClamAV manually
"""

import sys
from PySide6 import QtCore, QtGui, QtWidgets
import pyUIClasses.log_info as log_info
from EGAVResources import EGAVTheme
from EGAVTitleBar import EGAVTitleBar
from custom import OS, print_v1, check_network
from singleObj import clamav_commands


class UpdateClamAV(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(UpdateClamAV, self).__init__(parent)

        self.parent = parent
        self.os = OS.get_os_details()
        self.layout = QtWidgets.QVBoxLayout()
        self.title_bar = EGAVTitleBar(self)
        self.ui = log_info.Ui_Form()
        self.p = QtCore.QProcess(self)

        self.setupUi()
        self.resetUi()

        self.p.setProgram("dirb")
        self.p.setProcessChannelMode(QtCore.QProcess.MergedChannels)

        if check_network() is True:
            self.start_process(self.get_process_cmd())
        else:
            self.ui.label.setText("No Internet Connection")
            self.ui.textEdit.append("Check your internet connection and try again.")

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
        self.ui.label.setText("Please wait, while updating ClamAV Virus Signature Database...")
        self.setStyleSheet(EGAVTheme.SetupWindow.style_logInfo_window("QWidget"))
        # self.ui.verticalLayoutWidget.setStyleSheet(EGAVTheme.SetupWindow.style_logInfo_window("QWidget"))
        self.ui.label.setStyleSheet(EGAVTheme.SetupWindow.style_label)
        self.ui.label.setAlignment(QtCore.Qt.AlignCenter)
        pass

    def message(self, s):
        # time.sleep(0.01)
        self.ui.textEdit.append(s)

    def get_process_cmd(self, bDistEXE=False):
        cmd = None
        # clamav_path_and_conf = clamav_commands.clamav_paths_and_configs
        if self.os == "Windows":
            # cmd = clamav_path_and_conf.freshclam_exe + " --show-progress --check=2 --datadir=" + dq + \
            #       clamav_path_and_conf.clamav_db_dir + dq + " --log=" + dq + clamav_path_and_conf.freshclam_logs + dq
            cmd = clamav_commands.get_freshclam_cmd()
        elif self.os == "Linux":
            cmd = clamav_commands.get_freshclam_cmd()
        elif self.os == "MAC":
            cmd = clamav_commands.get_freshclam_cmd()
        print_v1("ClamAV Updater Command: " + cmd)
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
            QtCore.QProcess.Starting: 'ClamAV Virus Signature Database Update Starting',
            QtCore.QProcess.Running: 'Update Running',
        }
        state_name = states[state]
        self.message(f" {state_name}")

    def process_finished(self):
        self.message("Finished.")
        self.p = None
        self.title_bar.setClose(bEnable=True)
        self.ui.label.setText("Update Finished. Check logs below for Success.")

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        # if self.parent().windowTitle() == EGAVTheme.SetupMenu.title:
        #     self.parent().close()
        # self.parent().show()
        self.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    w = UpdateClamAV()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

