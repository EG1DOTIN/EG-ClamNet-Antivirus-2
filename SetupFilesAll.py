"""
SetupFilesAll.py :=> This file is used for making all executables that are used to make setup for EG ClamNet Antivirus
"""

from os import getcwd, path, walk as os_walk
from zipfile import ZipFile, ZIP_STORED

from config import EGAV_SETUP_ZIP_NAME, EGAV_UPDATE_ZIP_NAME
from custom import OS


class SetupAll:
    FILE_ClamdScanner = "ClamdScanner"
    FILE_EGAVMain = "EGAVMain"
    FILE_EGAVTray = "EGAVTray"
    FILE_SetupClamAV = "SetupClamAV"
    FILE_SetupEGAV = "SetupEGAV"
    FILE_EGAVDownloader = "EGAVDownloader"
    FILE_egcnextras = "egcnextras"

    def __init__(self):
        self.m_files = [self.FILE_ClamdScanner, self.FILE_EGAVMain, self.FILE_EGAVTray,
                        self.FILE_SetupClamAV, self.FILE_SetupEGAV, self.FILE_egcnextras,
                        self.FILE_EGAVDownloader]
        self.m_icon_path = path.join(getcwd(), "Resources", "egav.ico")
        self.EXE_EXT = ".exe" if OS.Windows() else ""
        self.pyinstaller = "pyinstaller"
        self.EXE_FILES_PATH = path.join(getcwd(), "dist")
        pass

    def get_setup_cmd(self, file_name, onedir=False):
        from custom import dq
        if onedir:
            cmd = self.pyinstaller + self.EXE_EXT + " --onefile --onedir --name " + file_name + self.EXE_EXT + \
                  " --icon=" + dq + self.m_icon_path + dq + " " + file_name + ".py"
        else:
            cmd = self.pyinstaller + self.EXE_EXT + " --onefile --name " + file_name + self.EXE_EXT + \
                  " --icon=" + dq + self.m_icon_path + dq + " " + file_name + ".py"
        return cmd

    def run(self, zipFiles=False):
        from time import sleep
        from custom import just_run_cmd
        # make setup files
        for file in self.m_files:
            print("making setup file of " + file + ".py ...")
            cmd = self.get_setup_cmd(file)
            print("executing cmd: \n" + cmd)
            print("\n\n")
            just_run_cmd(cmd, False)
            sleep(0.1)
        # make zip file
        if zipFiles:
            self.zip_exe_files()
        return

    def zip_exe_files(self):
        # make zip of required setup files
        with ZipFile(path.join(self.EXE_FILES_PATH, EGAV_SETUP_ZIP_NAME), 'w', ZIP_STORED) as zipf:
            # add exe files carefully
            zipf.write(arcname=self.FILE_ClamdScanner + self.EXE_EXT,
                       filename=path.join(self.EXE_FILES_PATH, self.FILE_ClamdScanner + self.EXE_EXT))
            zipf.write(arcname=self.FILE_EGAVDownloader + self.EXE_EXT,
                       filename=path.join(self.EXE_FILES_PATH, self.FILE_EGAVDownloader + self.EXE_EXT))
            zipf.write(arcname=self.FILE_EGAVMain + self.EXE_EXT,
                       filename=path.join(self.EXE_FILES_PATH, self.FILE_EGAVMain + self.EXE_EXT))
            zipf.write(arcname=self.FILE_EGAVTray + self.EXE_EXT,
                       filename=path.join(self.EXE_FILES_PATH, self.FILE_EGAVTray + self.EXE_EXT))
            zipf.write(arcname=self.FILE_SetupClamAV + self.EXE_EXT,
                       filename=path.join(self.EXE_FILES_PATH, self.FILE_SetupClamAV + self.EXE_EXT))
            zipf.write(arcname=self.FILE_SetupEGAV + self.EXE_EXT,
                       filename=path.join(self.EXE_FILES_PATH, self.FILE_SetupEGAV + self.EXE_EXT))

            if OS.Windows():
                zipf.write(arcname="EGCNAVWinSer" + self.EXE_EXT,
                           filename=path.join(self.EXE_FILES_PATH, "EGCNAVWinSer" + self.EXE_EXT))

            # add documents
            zipf.write(arcname="Docs/EULA_EGCNAV2_X.htm",
                       filename=path.join(self.EXE_FILES_PATH, "Docs", "EULA_EGCNAV2_X.htm"))
            # add resources
            for root, subdirs, files in os_walk(path.join(self.EXE_FILES_PATH, "Resources")):
                for filename in files:
                    file_path = path.join(root, filename)
                    head, tail = path.split(file_path)
                    file = tail
                    head1, tail1 = path.split(head)
                    folder = tail1
                    if folder == "Resources":
                        zipf.write(arcname=path.join(folder, file),
                                   filename=file_path)
                    else:
                        zipf.write(arcname=path.join("Resources", folder, file),
                                   filename=file_path)

    def zip_update_files(self):
        # make zip of required setup files
        with ZipFile(path.join(self.EXE_FILES_PATH, EGAV_UPDATE_ZIP_NAME), 'w', ZIP_STORED) as zipf:
            # add exe files carefully
            zipf.write(arcname=self.FILE_ClamdScanner + self.EXE_EXT,
                       filename=path.join(self.EXE_FILES_PATH, self.FILE_ClamdScanner + self.EXE_EXT))
            zipf.write(arcname=self.FILE_EGAVMain + self.EXE_EXT,
                       filename=path.join(self.EXE_FILES_PATH, self.FILE_EGAVMain + self.EXE_EXT))
            zipf.write(arcname=self.FILE_EGAVTray + self.EXE_EXT,
                       filename=path.join(self.EXE_FILES_PATH, self.FILE_EGAVTray + self.EXE_EXT))
            zipf.write(arcname=self.FILE_SetupClamAV + self.EXE_EXT,
                       filename=path.join(self.EXE_FILES_PATH, self.FILE_SetupClamAV + self.EXE_EXT))
            # add documents
            zipf.write(arcname="Docs/EULA_EGCNAV2_X.htm",
                       filename=path.join(self.EXE_FILES_PATH, "Docs", "EULA_EGCNAV2_X.htm"))
            # add resources
            for root, subdirs, files in os_walk(path.join(self.EXE_FILES_PATH, "Resources")):
                for filename in files:
                    file_path = path.join(root, filename)
                    head, tail = path.split(file_path)
                    file = tail
                    head1, tail1 = path.split(head)
                    folder = tail1
                    if folder == "Resources":
                        zipf.write(arcname=path.join(folder, file),
                                   filename=file_path)
                    else:
                        zipf.write(arcname=path.join("Resources", folder, file),
                                   filename=file_path)


if __name__ == '__main__':
    setup = SetupAll()
    setup.run()
    setup.zip_exe_files()
    setup.zip_update_files()
    pass
