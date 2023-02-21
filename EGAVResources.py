"""
EGAVResources.py :=> This file provides resources for EG ClamNet Antivirus
"""

import sys
from json import dumps as json_dumps, loads as json_loads
from os import makedirs, path, environ, getlogin

from PySide6 import QtCore
from PySide6.QtCore import QStandardPaths

from config import BASE64CHARS
from custom import get_current_working_dir, str_list_separation
from custom import shuffle_string_n_times, OS, dq, DEBUG_CODE, just_run_cmd, print_v1, paths_correction


# class EGAVSF:
#     """
#     class for static constant values of EG Antivirus Source Files
#     """
#     EGAV_TRAY = "EGAVTray"
#     CLAMAV_RESOURCES = "ClamAVResources"
#     CLAMAV_UPDATER = "ClamAVUpdater"
#     CLAMD_SCANNER = "ClamdScanner"
#     CUSTOM = "custom"
#     CUSTOM_QT = "customQt"
#     EGAV_MAIN = "EGAVMain"
#     EGAV_MSG_N_POPUP = "EGAVMsgNPopup"
#     EGAV_RESOURCES = "EGAVResources"
#     EGAV_SCANNER = "EGAVScanner"
#     EGAV_TITLE_BAR = "EGAVTitleBar"
#     INFO_WINDOW = "InfoWindow"
#     MAIN = "main"
#     PROCESSES = "processes"
#     RUN_AS_ROOT = "runasroot"
#     SETUP_CLAMAV = "SetupClamAV"
#     SETUP_EGAV = "SetupEGAV"
#     SINGLE_OBJ = "singleObj"

class EGAVCommonInfo:
    EGAV_TITLE_LONG = "EG ClamNet Antivirus 2.0"
    EGAV_TITLE_SHRT = "EGCNAV2"
    EGAV_SERVICE_NAME = "WinSerEGCNTray"
    EGAV_COPYRIGHT_STR = "© 2022 EG1"


class EGAVStatus:
    STR_TITLE = EGAVCommonInfo.EGAV_TITLE_LONG
    STATUS_UPDATED = "UPDATED"  # the antivirus is updated
    STATUS_NOT_UPDATED = "NOT_UPDATED"  # the antivirus is not updated
    STATUS_CRITICAL1 = "CRITICAL1"  # the real-time protection is off
    STATUS_CRITICAL2 = "CRITICAL2"  # the clamd service is not running

    STR_TOOLTIP_UPDATED = "Up To Date \nSYSTEM IS SECURED \n " + \
                          EGAVCommonInfo.EGAV_TITLE_LONG + "\n" + \
                          EGAVCommonInfo.EGAV_COPYRIGHT_STR

    STR_TOOLTIP_NOT_UPDATED = "Out Of Date  \nAV SIG. NOT UPDATED\n " + \
                              EGAVCommonInfo.EGAV_TITLE_LONG + " \n" + \
                              EGAVCommonInfo.EGAV_COPYRIGHT_STR

    STR_TOOLTIP_CRITICAL1 = "System At Risk \nREAL-TIME PROTECTION IS OFF\n " + \
                            EGAVCommonInfo.EGAV_TITLE_LONG + " \n"

    STR_TOOLTIP_CRITICAL2 = "System At Risk \nClamd Service is not running\n " + \
                            EGAVCommonInfo.EGAV_TITLE_LONG + " \n"

    STR_BALLOON_UPDATED = EGAVCommonInfo.EGAV_TITLE_LONG + \
                          " is UP-TO-DATE\n"

    STR_BALLOON_NOT_UPDATED = EGAVCommonInfo.EGAV_TITLE_LONG + \
                              " is OUT-OF-DATE\n"

    STR_BALLOON_CRITICAL1 = "Real-Time Protection is OFF\n"

    STR_BALLOON_CRITICAL2 = "Clamd Service is not running\n"


class EGAVResources:
    EGAV_WORKING_DIR = get_current_working_dir()
    EGAV_LOGS_DIR = path.join(EGAV_WORKING_DIR, "EGAVLogs")
    EGAV_IMAGE_CUSTOM_SCAN = path.join(EGAV_WORKING_DIR, "Resources", "btnimg", "cscan.png")
    EGAV_IMAGE_QUICK_SCAN = path.join(EGAV_WORKING_DIR, "Resources", "btnimg", "qscan.png")
    EGAV_IMAGE_FULL_SCAN = path.join(EGAV_WORKING_DIR, "Resources", "btnimg", "fscan.png")
    EGAV_ICON_STATUS = path.join(EGAV_WORKING_DIR, "Resources", "btnimg", "status.png")
    EGAV_ICON_SCAN = path.join(EGAV_WORKING_DIR, "Resources", "btnimg", "scan.png")
    EGAV_ICON_PREFERENCES = path.join(EGAV_WORKING_DIR, "Resources", "btnimg", "preferences.png")
    EGAV_ICON_SETTINGS = path.join(EGAV_WORKING_DIR, "Resources", "btnimg", "settings.png")
    EGAV_ICON_QUARANTINE = path.join(EGAV_WORKING_DIR, "Resources", "btnimg", "quarantine.png")
    EGAV_ICON_CLEANER = path.join(EGAV_WORKING_DIR, "Resources", "btnimg", "cleaner.png")
    EGAV_ICON_HELP = path.join(EGAV_WORKING_DIR, "Resources", "btnimg", "help.png")
    EGAV_ICON_ABOUT = path.join(EGAV_WORKING_DIR, "Resources", "btnimg", "about.png")
    EGAV_ICON_CLOSE_BUTTON = path.join(EGAV_WORKING_DIR, "Resources", "btnimg", "close.png")
    EGAV_WINDOW_ICON = path.join(EGAV_WORKING_DIR, "Resources", "egav.ico")
    EGAV_TRAY_ICON_UPDATED = path.join(EGAV_WORKING_DIR, "Resources", "egavu.ico")
    EGAV_TRAY_ICON_NOT_UPDATED = path.join(EGAV_WORKING_DIR, "Resources", "egavn.ico")
    EGAV_TRAY_ICON_CRITICAL = path.join(EGAV_WORKING_DIR, "Resources", "egavc.ico")
    EGAV_SCANNING_IMAGE_GIFF = path.join(EGAV_WORKING_DIR, "Resources", "egav.gif")
    EGAV_LOADING_IMAGE_GIFF = path.join(EGAV_WORKING_DIR, 'Resources', 'egavhg.gif')
    EGAV_Processing_IMAGE_GIFF = path.join(EGAV_WORKING_DIR, 'Resources', 'egaval.gif')
    EGAV_UI_FILES_FOLDER = path.join(EGAV_WORKING_DIR, "QtUIFiles")
    EGAV_UI_FILE_MAIN_WINDOW = path.join(EGAV_UI_FILES_FOLDER, "mainwindow.ui")
    EGAV_UI_FILE_MAIN_WINDOW2 = path.join(EGAV_UI_FILES_FOLDER, "mainwindow2.ui")
    EGAV_UI_FILE_INFO_POPUP = path.join(EGAV_UI_FILES_FOLDER, "info_popup.ui")
    EGAV_UI_FILE_SCANNER = path.join(EGAV_UI_FILES_FOLDER, "scanner_window.ui")
    EGAV_UI_FILE_INPUT_TEXT = path.join(EGAV_UI_FILES_FOLDER, "input_popup.ui")
    EGAV_UI_FILE_MESSAGE_BOX = path.join(EGAV_UI_FILES_FOLDER, "msg_popup.ui")
    EGAV_UI_FILE_MESSAGE_BOX_YN = path.join(EGAV_UI_FILES_FOLDER, "msg_popupYN.ui")
    EGAV_UI_FILE_SETUP_WINDOW = path.join(EGAV_UI_FILES_FOLDER, "setup_menu.ui")
    EGAV_UI_FILE_LOG_INFO = path.join(EGAV_UI_FILES_FOLDER, "log_info.ui")
    EGAV_UI_FILE_TITLE_BAR = path.join(EGAV_UI_FILES_FOLDER, "title_bar.ui")
    EGAV_UI_PY_CLASS_FILES_FOLDER = path.join(EGAV_WORKING_DIR, "pyUIClasses")


class QtPaths:
    """Returns the user's desktop directory. This is a generic value. On systems with no concept of
    a desktop, this is the same as QStandardPaths::HomeLocation."""
    DesktopLocation = QStandardPaths.standardLocations(QStandardPaths.DesktopLocation)

    """Returns the directory containing user document files. This is a generic value. The returned 
    path is never empty."""
    DocumentsLocation = QStandardPaths.standardLocations(QStandardPaths.DocumentsLocation)

    """Returns the directory containing user's fonts. This is a generic value. Note that installing 
    fonts may require additional, platform-specific operations."""
    FontsLocation = QStandardPaths.standardLocations(QStandardPaths.FontsLocation)

    """Returns the directory containing the user applications (either executables, application 
    bundles, or shortcuts to them). This is a generic value. Note that installing applications may 
    require additional, platform-specific operations. Files, folders or shortcuts in this directory 
    are platform-specific."""
    ApplicationsLocation = QStandardPaths.standardLocations(QStandardPaths.ApplicationsLocation)

    """Returns the directory containing the user's music or other audio files. This is a generic 
    value. If no directory specific for music files exists, a sensible fallback for storing user 
    documents is returned."""
    MusicLocation = QStandardPaths.standardLocations(QStandardPaths.MusicLocation)

    """Returns the directory containing the user's movies and videos. This is a generic value. 
    If no directory specific for movie files exists, a sensible fallback for storing user documents 
    is returned."""
    MoviesLocation = QStandardPaths.standardLocations(QStandardPaths.MoviesLocation)

    """Returns the directory containing the user's pictures or photos. This is a generic value. 
    If no directory specific for picture files exists, a sensible fallback for storing user documents 
    is returned."""
    PicturesLocation = QStandardPaths.standardLocations(QStandardPaths.PicturesLocation)

    """Returns a directory where temporary files can be stored. The returned value might be 
    application-specific, shared among other applications for this user, or even system-wide. 
    The returned path is never empty."""
    TempLocation = QStandardPaths.standardLocations(QStandardPaths.TempLocation)

    """Returns the user's home directory (the same as QDir::homePath()). On Unix systems, this is 
    equal to the HOME environment variable. This value might be generic or application-specific, 
    but the returned path is never empty."""
    HomeLocation = QStandardPaths.standardLocations(QStandardPaths.HomeLocation)

    """Returns a directory location where user-specific non-essential (cached) data should be written.
     This is an application-specific directory. The returned path is never empty."""
    CacheLocation = QStandardPaths.standardLocations(QStandardPaths.CacheLocation)

    """Returns a directory location where user-specific non-essential (cached) data, shared across 
    applications, should be written. This is a generic value. Note that the returned path may be empty
     if the system has no concept of shared cache."""
    GenericCacheLocation = QStandardPaths.standardLocations(QStandardPaths.GenericCacheLocation)

    """Returns a directory location where persistent data shared across applications can be stored.
     This is a generic value. The returned path is never empty."""
    GenericDataLocation = QStandardPaths.standardLocations(QStandardPaths.GenericDataLocation)

    """Returns a directory location where runtime communication files should be written, like Unix 
    local sockets. This is a generic value. The returned path may be empty on some systems."""
    RuntimeLocation = QStandardPaths.standardLocations(QStandardPaths.RuntimeLocation)

    """Returns a directory location where user-specific configuration files should be written. This
     may be either a generic value or application-specific, and the returned path is never empty."""
    ConfigLocation = QStandardPaths.standardLocations(QStandardPaths.ConfigLocation)

    """Returns a directory for user's downloaded files. This is a generic value. If no directory
     specific for downloads exists, a sensible fallback for storing user documents is returned."""
    DownloadLocation = QStandardPaths.standardLocations(QStandardPaths.DownloadLocation)

    """Returns a directory location where user-specific configuration files shared between 
    multiple applications should be written. This is a generic value and the returned path is never 
    empty."""
    GenericConfigLocation = QStandardPaths.standardLocations(QStandardPaths.GenericConfigLocation)

    """Returns a directory location where persistent application data can be stored. This is an 
    application-specific directory. To obtain a path to store data to be shared with other 
    applications, use QStandardPaths::GenericDataLocation. The returned path is never empty. 
    On the Windows operating system, this returns the roaming path. This enum value was added 
    in Qt 5.4."""
    AppDataLocation = QStandardPaths.standardLocations(QStandardPaths.AppDataLocation)

    """Returns the local settings path on the Windows operating system. On all other platforms,
     it returns the same value as AppDataLocation. This enum value was added in Qt 5.4."""
    AppLocalDataLocation = QStandardPaths.standardLocations(QStandardPaths.AppLocalDataLocation)

    """Returns a directory location where user-specific configuration files should be written. 
    This is an application-specific directory, and the returned path is never empty. This enum 
    value was added in Qt 5.5."""
    AppConfigLocation = QStandardPaths.standardLocations(QStandardPaths.AppConfigLocation)


class QuickScanPaths:
    if OS.Windows():
        HOME_USER_PATH = path.abspath(QtPaths.HomeLocation[0])
    else:
        HOME_USER_PATH = path.join("/", "home", getlogin())
    DOWNLOAD_FOLDER = path.join(HOME_USER_PATH, "Downloads")
    DESKTOP_FOLDER = path.join(HOME_USER_PATH, "Desktop")
    DOCUMENTS_FOLDER = path.join(HOME_USER_PATH, "Documents")
    PICTURE_LOCATION = path.join(HOME_USER_PATH, "Pictures")
    ALL_PATHS_LIST = [DESKTOP_FOLDER, DOWNLOAD_FOLDER, DOCUMENTS_FOLDER, PICTURE_LOCATION]
    ALL_PATHS_LIST = paths_correction(ALL_PATHS_LIST)
    print(ALL_PATHS_LIST)
    SPACE_SEPARATED_PATHS = str_list_separation(input_list_str=ALL_PATHS_LIST)


class EGAVPaths(QtCore.QStandardPaths):
    Resources = EGAVResources
    QPaths = QtPaths
    # CommonAppDataDir = QPaths.AppDataLocation[0].replace('/', "\\") if OS.Windows() else QPaths.AppDataLocation[0]
    if OS.Windows():
        # CommonAppDataDir = QPaths.AppDataLocation[0].replace('/', "\\")
        CommonAppDataDir = path.join(path.abspath(QPaths.HomeLocation[0]), "AppDATA", "Roaming")
    else:
        CommonAppDataDir = '/home/' + getlogin() + '/.local/share'

    # CommonAppDataDir = QPaths.AppDataLocation[0].replace('/', "\\") if OS.Windows() \
    #     else '/home/' + getlogin() + '/.local/share'

    AppDataDir = path.join(CommonAppDataDir, "EGCNAV2")
    QuarantineDir = path.join(AppDataDir, "Vault")
    SettingsDBDir = path.join(AppDataDir, "DB")

    # LogsDir = path.join(AppDataDir, "EGAVLogs")
    # InstallationPath = path.join(environ["PROGRAMFILES"], "egav") if OS.Windows() else "/opt/EGAV/bin"

    if DEBUG_CODE:
        LogsDir = path.join(EGAVResources.EGAV_WORKING_DIR, "Logs") if OS.Windows() \
            else path.join("/home/" + getlogin() + "/Downloads/pyEGAV/Logs")
        InstallationPath = EGAVResources.EGAV_WORKING_DIR if OS.Windows() \
            else path.join("/home/" + getlogin() + "/Downloads/pyEGAV")
    else:
        LogsDir = path.join(AppDataDir, "Logs")
        InstallationPath = path.join(environ["PROGRAMFILES"], "EG1", "EGClamNetAV2") if OS.Windows() \
            else "/home/" + getlogin() + "/.egcnav2/bin"

    SettingsDBFile = path.join(SettingsDBDir, "config.txt")
    SetupStateFile = path.join(SettingsDBDir, "status.txt")

    # AppInstallationPath = ""

    @staticmethod
    def python_str(venv=True):
        if venv:
            if OS.Windows():
                result = dq + path.join(EGAVResources.EGAV_WORKING_DIR, "venv", "Scripts", "python") + dq + " "
            elif OS.Linux():
                result = dq + path.join(EGAVResources.EGAV_WORKING_DIR, "venv", "bin", "python3") + dq + " "
            elif OS.OSX():
                result = dq + path.join(EGAVResources.EGAV_WORKING_DIR, "venv", "bin", "python") + dq + " "
            else:
                result = "python"
            return result
        else:
            if OS.Windows():
                result = "python"
            elif OS.Linux():
                result = "python3"
            elif OS.OSX():
                result = "python"
            else:
                result = "python"
            return result

    @staticmethod
    def python_str_abspath():
        result = dq + path.join(path.dirname(path.abspath(sys.executable)), EGAVPaths.python_str(venv=False)) + dq + " "
        return result

    @staticmethod
    def file_str(file, installation_path=True):
        if installation_path:
            return dq + path.join(EGAVPaths.InstallationPath, file) + dq
        else:
            return dq + path.join(EGAVResources.EGAV_WORKING_DIR, file) + dq

    @staticmethod
    def setInstalled(bInstalled=False):
        if bInstalled:
            info = {
                "status": True
            }
        else:
            info = {
                "status": False
            }
        info_json = json_dumps(info)
        e_info = EGAVEncodeAndDecode(in_str=info_json).encode64()
        with open(file=EGAVPaths.SetupStateFile, encoding="utf8", mode="w+") as file:
            file.write(e_info)

    @staticmethod
    def getInstalled():
        with open(file=EGAVPaths.SetupStateFile, encoding="utf8", mode="r") as file:
            eData = file.read()
            data = EGAVEncodeAndDecode.decode64(eData)
            res = json_loads(data)
        return res

    @staticmethod
    def execute_file(filename):
        if DEBUG_CODE:
            just_run_cmd(EGAVPaths.python_str_abspath() + path.join(EGAVResources.EGAV_WORKING_DIR, filename + ".py"))
        else:
            just_run_cmd(dq + path.join(EGAVResources.EGAV_WORKING_DIR, filename + ".exe") + dq)

    @staticmethod
    def execute_file_v1(filename):
        from pathlib import Path
        file_ext = Path(filename).suffix
        if file_ext in [".py", ".PY"]:
            just_run_cmd(dq + EGAVPaths.python_str_abspath() +
                         path.join(EGAVResources.EGAV_WORKING_DIR, filename) + dq)
        elif file_ext in [".exe", ".EXE"]:
            just_run_cmd(dq + path.join(EGAVResources.EGAV_WORKING_DIR, filename) + dq)
        else:
            just_run_cmd(dq + filename + dq)


class EGAVEncodeAndDecode:
    __base64_chars = BASE64CHARS

    def __init__(self, in_str="this is sample string", dynamic_base64_char=False):
        self.input_string = in_str
        if dynamic_base64_char:
            EGAVEncodeAndDecode.__base64_chars = shuffle_string_n_times(EGAVEncodeAndDecode.__base64_chars, 2)
            # print(EncodeAndDecode.__base64_chars)

    def encode64(self):
        strInput = self.input_string
        result = ""
        a = 0
        b = 0
        LengthOfS = len(strInput)
        for i in range(0, LengthOfS):
            x = ord(strInput[i])
            b = b * 256 + x
            a = a + 8
            while a >= 6:
                a = a - 6
                x = int(b / (1 << a))
                b = b % (1 << a)
                result += EGAVEncodeAndDecode.__base64_chars[x]
        if a > 0:
            x = b << (6 - a)
            result += EGAVEncodeAndDecode.__base64_chars[x]
        a = len(result) % 4
        if a == 2:
            result += "@"
        elif a == 3:
            result += "="
        return result

    @staticmethod
    def pos(in_str, chr):
        length = len(in_str)
        i = 0
        while i < length:
            if in_str[i] == chr:
                break
            i += 1
        if i >= 64:
            return -1
        return i

    @staticmethod
    def decode64(strIn):
        strIn = strIn[0:-1]
        result = ""
        a = 0
        b = 0
        lengthOfs = len(strIn)
        for i in range(0, lengthOfs):
            x = EGAVEncodeAndDecode.pos(EGAVEncodeAndDecode.__base64_chars, strIn[i])
            if x >= 0:
                b = b * 64 + x
                a = a + 6
                if a >= 8:
                    a = a - 8
                    x = b >> a
                    b = b % (1 << a)
                    x = x % 256
                    res = chr(x)
                    result += res
        return result


class EGAVDatabase:
    """
        Used as a singleton class
    """
    m_Instance = None

    def __init__(self, singleton=False, obj_dict=None):
        if not singleton:
            raise Exception("EGAVDatabase is a singleton class, use EGAVDatabase.object() instead of EGAVDatabase()")
        if obj_dict is None:
            obj_dict = EGAVDatabase.toDefaultDBDict()
        self.Preference_RealTimeProtectionOnOff = obj_dict["preferences"]["RealTimeProtectionOnOff"]
        self.Preferences_AutomaticUpdatesOnOff = obj_dict["preferences"]["AutomaticUpdatesOnOff"]
        self.Preferences_InfectedFilesRadioButton = obj_dict["preferences"]["InfectedFilesRadioButton"]
        self.Preferences_InfectedFilesNotifications = obj_dict["preferences"]["InfectedFilesNotifications"]
        self.Settings_DoNotScanFilesLargerThanMB = obj_dict["settings"]["DoNotScanFilesLargerThanMB"]
        self.Settings_DoNotReloadVirusSignatureDB = obj_dict["settings"]["DoNotReloadVirusSignatureDB"]
        self.Settings_ExtractFilesFromArchives = obj_dict["settings"]["ExtractFilesFromArchives"]
        self.Settings_DoNotExtractMoreThanMB = obj_dict["settings"]["DoNotExtractMoreThanMB"]
        self.Settings_DoNotExtractMoreThanFiles = obj_dict["settings"]["DoNotExtractMoreThanFiles"]
        self.Settings_DoNotExtractMoreThanSubArchives = obj_dict["settings"]["DoNotExtractMoreThanSubArchives"]
        self.Settings_ExcludeExtension = obj_dict["ExcludeExtension"]
        self.Settings_ScanOnlyExtension = obj_dict["ScanOnlyExtension"]

    @staticmethod
    def toDefaultDBDict():
        return {
            "preferences": {
                "RealTimeProtectionOnOff": 1,
                "AutomaticUpdatesOnOff": 1,
                "InfectedFilesRadioButton": 3,
                "InfectedFilesNotifications": 1
            },
            "settings": {
                "DoNotScanFilesLargerThanMB": 50,
                "DoNotReloadVirusSignatureDB": 0,
                "ExtractFilesFromArchives": 1,
                "DoNotExtractMoreThanMB": 10,
                "DoNotExtractMoreThanFiles": 100,
                "DoNotExtractMoreThanSubArchives": 10
            },
            "ExcludeExtension": ["jpg", "jpeg", "gif", "png", "tif", "tiff",
                                 "txt", "docx", "pptx", "xlsx", "pdf", "mp3",
                                 "mp4", "wav", "avi", "mpg", "mpeg", "wmv",
                                 "vob", "3gp", "webm", "flv", "mkv", "vob",
                                 "ogv", "ogg", "gifv", "mng", "qt", "yuv",
                                 "amv", "m4p", "m4v", "mp2", "mpe", "mpv",
                                 "m2v", "3g2", "f4v", "f4p", "f4a", "f4b",
                                 "dbx", "tbb", "pst", "dat", "log", "nsf",
                                 "ntf"],
            "ScanOnlyExtension": []
        }

    @staticmethod
    def toDefaultDBJSON():
        return json_dumps(EGAVDatabase.toDefaultDBDict())

    def toDict(self):
        return {
            "preferences": {
                "RealTimeProtectionOnOff": self.Preference_RealTimeProtectionOnOff,
                "AutomaticUpdatesOnOff": self.Preferences_AutomaticUpdatesOnOff,
                "InfectedFilesRadioButton": self.Preferences_InfectedFilesRadioButton,
                "InfectedFilesNotifications": self.Preferences_InfectedFilesNotifications
            },
            "settings": {
                "DoNotScanFilesLargerThanMB": self.Settings_DoNotScanFilesLargerThanMB,
                "DoNotReloadVirusSignatureDB": self.Settings_DoNotReloadVirusSignatureDB,
                "ExtractFilesFromArchives": self.Settings_ExtractFilesFromArchives,
                "DoNotExtractMoreThanMB": self.Settings_DoNotExtractMoreThanMB,
                "DoNotExtractMoreThanFiles": self.Settings_DoNotExtractMoreThanFiles,
                "DoNotExtractMoreThanSubArchives": self.Settings_DoNotExtractMoreThanSubArchives
            },
            "ExcludeExtension": self.Settings_ExcludeExtension,
            "ScanOnlyExtension": self.Settings_ScanOnlyExtension
        }

    def toJSON(self):
        return json_dumps(self.toDict())

    def saveToFile(self, filepath=EGAVPaths.SettingsDBFile):
        obj_json = self.toJSON()
        ed = EGAVEncodeAndDecode(in_str=obj_json)
        with open(filepath, encoding="utf8", mode="w") as f:
            f.write(ed.encode64())
        return

    def loadFromFile(self, filepath=EGAVPaths.SettingsDBFile):
        with open(filepath, encoding="utf8", mode="r") as f:
            s = f.read()
        obj_json = EGAVEncodeAndDecode.decode64(s)
        try:
            obj_dict = json_loads(obj_json)
            self.__init__(singleton=True, obj_dict=obj_dict)
            return True
        except Exception as e:
            print_v1("Error: loading database" + e.__str__())
            return False

    def loadDatabase(self):
        # log paths

        if not self.isSettingsDBFileOK():
            self.saveToFile()
        else:
            self.loadFromFile()

    def isSettingsDBFileOK(self):
        try:
            makedirs(EGAVPaths.SettingsDBDir)
            with open(EGAVPaths.SettingsDBFile, 'w'):
                bOk = False
        except:
            try:
                with open(EGAVPaths.SettingsDBFile, 'r'):
                    if path.getsize(EGAVPaths.SettingsDBFile):
                        bOk = self.loadFromFile()
                    else:
                        bOk = False
            except:
                with open(EGAVPaths.SettingsDBFile, 'w'):
                    bOk = False
        return bOk

    @staticmethod
    def object():
        if not EGAVDatabase.m_Instance:
            EGAVDatabase.m_Instance = EGAVDatabase(obj_dict=None, singleton=True)
            EGAVDatabase.m_Instance.loadDatabase()
            return EGAVDatabase.m_Instance
        else:
            EGAVDatabase.m_Instance.loadDatabase()
            return EGAVDatabase.m_Instance


class EGAVTheme:
    EGAV_TITLE_TRAY_WINDOW = "EGCNAV Tray"
    EGAV_TITLE_SCANNER_WINDOW = "EGCNAV Scanner"

    class SetupWindow:
        title = EGAVCommonInfo.EGAV_TITLE_LONG + " Setup"
        style_logInfo_window = lambda QMainWindow_OR_QDialog: QMainWindow_OR_QDialog + """
                        { 
                            background-color: rgb(30,31,34); 
                            color: rgb(240, 240, 240);
                            border: 0px solid rgb(0,96,48) /*rgb(240, 240, 240)*/;
                        }
                    """
        style_label = """
                    QLabel {
                        color: white;
                        background: transparent; font-size: 12pt; font-family: Courier; font-weight: normal;
                    } 
                    """
        style_text_edit = """
                        QTextEdit {
                        color: white;
                        background: transparent; font-size: 12pt; font-family: Courier; font-weight: normal;
                        background-color: rgb(30,31,34);
                        }                    
                        """

    class MainWindow:
        title_mainWindow = EGAVCommonInfo.EGAV_TITLE_LONG

        style_titleBar_box = """
                QGroupBox { 
                    background-color: rgb(64, 69, 74);
                    color: white; 
                    border: 1px solid white; 
                    /*border-radius: 10px;*/ 
                }
                    """
        style_titleBar_widget = """ 
                        QWidget {
                            background-color: rgb(64, 69, 74); 
                            border: 0px solid white;  
                        }
                        """
        style_red_close_button = """
                    QPushButton { 
                        background-color: rgb(243, 27, 43);
                        color: white;
                        border-radius: 3px;
                        border-color: white;
                        height: 30px;
                        width: 50px;
                        font-size: 12pt;
                        font-weight: bold;
                    } 
                    QPushButton:pressed {
                        background-color: rgb(160, 170, 220);
                        color: black; 
                    }
                    """
        style_close_button_with_image = """
                    QPushButton {
                        border-image : url(Resources/btnimg/close.png); 
                        height: 20px;
                        width: 20px;
                    }
                    QPushButton:hover{
                        background-color: rgb(243, 27, 43);
                    }
                    """

        style_blue_minimize_button = """
                    QPushButton { 
                        background-color: rgb(43, 27, 243);
                        color: white;
                        border-radius: 3px;
                        border-color: white;
                        height: 30px;
                        width: 50px;
                        font-size: 12pt;
                        font-weight: bold;
                    } 
                    QPushButton:pressed {
                        background-color: rgb(160, 170, 220);
                        color: black; 
                    }
                    """

        style_minimize_button_with_image = """
                            QPushButton {
                                border-image : url(Resources/btnimg/minimize.png); 
                                height: 20px;
                                width: 20px;
                            }
                            QPushButton:hover{
                                background-color: rgb(160, 170, 220);
                            }
                            """

        style_icon_titleBar_label = """
                QLabel { 
                    border-image : url(Resources/egav.ico); 
                }
                """
        style_icon_titleBar_label_size = QtCore.QSize(25, 25)

        style_mainWindow = """
                QMainWindow { 
                    background-color: rgb(30,31,34); 
                    border: 1px solid rgb(240, 240, 240);
                }
            """
        style_mainWidget = """
                .Widget { 
                    background-color: rgb(30,31,34); 
                    border: 1px solid rgb(240, 240, 240);
                }
            """
        style_label_link_facebook = """
                QLabel { 
                    border-image : url(Resources/facebook.png); 
                }
                """
        style_label_link_twitter = """
                QLabel { 
                    border-image : url(Resources/twitter.png); 
                }
                """
        style_label_link_instagram = """
                QLabel { 
                    border-image : url(Resources/instalogo.png); 
                }
                """
        style_Tab1 = """
                QTabBar::tab {
                    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                    stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                    stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
                    border: 2px solid #C4C4C3;
                    border-bottom-color: #C2C7CB; /* same as the pane color */
                    border-top-left-radius: 4px;
                    border-top-right-radius: 4px;
                    min-width: 8ex;
                    padding: 2px;
                }
    
                QTabBar::tab:selected, QTabBar::tab:hover {
                    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                    stop: 0 #fafafa, stop: 0.4 #f4f4f4,
                                    stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);
                }
    
                QTabBar::tab:selected {
                    border-color: #9B9B9B;
                    border-bottom-color: #C2C7CB; /* same as pane color */
                }
    
                QTabBar::tab:!selected {
                    margin-top: 2px; /* make non-selected tabs look smaller */
                }
                """
        style_Tab2 = """
            QTabBar::tab {
                background: rgb(44, 45, 48);
                color: white;
                border: 2px solid rgb(160, 170, 220);
                min-width: 64px;
                padding: 4px;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
            }
            QTabBar {
                background: transparent; 
                font-size: 10pt; 
                font-family: Courier; 
                font-weight: bold; 
            }
            QTabWidget::tab-bar {
                alignment: center;
            }
            QTabWidget::pane {
                border: 1px solid rgb(160, 170, 220);
            }
            QTabBar::tab:selected, QTabBar::tab:hover {
                background: rgb(227,235,255);
                color: black;
            }"""

        style_widget_with_tab = """
                    .QWidget { 
                        background-color: rgb(30,31,34); 
                        /*border: 1px solid rgb(240, 240, 240);*/
                    }     
                    QTabBar::tab {
                        background: rgb(44, 45, 48);
                        color: white;
                        border: 2px solid rgb(160, 170, 220);
                        min-width: 64px;
                        padding: 4px;
                        border-top-left-radius: 10px;
                        border-top-right-radius: 10px;
                    }
                    QTabBar {
                        background: transparent; 
                        font-size: 12pt; 
                        font-family: Courier; 
                        font-weight: bold; 
                    }
                    QTabWidget::tab-bar {
                        alignment: center;
                    }
                    QTabWidget::pane {
                        border: 1px solid rgb(160, 170, 220);
                    }
                    QTabBar::tab:selected, QTabBar::tab:hover {
                        background: rgb(227,235,255);
                        color: black;
                    }"""

        style_TabWidget = """
                QTabBar { 
                    font-size: 10pt; 
                    font-family: Courier; 
                    font-weight: bold; 
                }
                """
        size_social_media_link = QtCore.QSize(20, 20)
        size_TabWidget = QtCore.QSize(28, 28)
        style_groupBox = """
                QGroupBox { 
                    color: white; 
                    border: 1px solid rgb(0,96,48) /*white*/; 
                    border-radius: 10px;  
                }
                """
        style_groupBox_BorderNone = """
                        QGroupBox { 
                            border: None; 
                        }
                        """

        style_label_image_status_updated = """
                QLabel { 
                    border-image : url(Resources/egavu.ico); 
                }
                """
        style_label_image_status_not_updated = """
                QLabel { 
                    border-image : url(Resources/egavn.ico); 
                }
                """
        style_label_image_status_critical = """
                QLabel { 
                    border-image : url(Resources/egavc.ico); 
                }
                """

        style_label_status_updated = """
                    QLabel {
                        color: green;
                        background: transparent; font-size: 15pt; font-family: Calibri; font-weight: bold;
                    } 
                    """
        style_label_status_not_updated = """
                    QLabel {
                        color: yellow;
                        background: transparent; font-size: 15pt; font-family: Calibri; font-weight: bold;
                    } 
                    """
        style_label_status_critical = """
                    QLabel {
                        color: red;
                        background: transparent; font-size: 15pt; font-family: Calibri; font-weight: bold;
                    } 
                    """
        text_label_status_updated = """UP-TO-DATE"""
        text_label_status_not_updated = """ANTIVIRUS IS NOT UPDATED"""
        text_label_status_critical1 = """REAL-TIME PROTECTION IS OFF"""
        text_label_status_critical2 = """CLAMD SERVICE IS NOT RUNNING"""
        size_label_status_image = QtCore.QSize(90, 90)

        style_label_image_custom_scan = """
                QLabel { 
                    border-image : url(Resources/btnimg/cscan1.png); 
                }
                """
        style_label_image_quick_can = """
                QLabel { 
                    border-image : url(Resources/btnimg/qscan1.png); 
                }
                """
        style_label_image_full_scan = """
                QLabel { 
                    border-image : url(Resources/btnimg/fscan1.png); 
                }
                """
        size_label_image_scan = QtCore.QSize(80, 80)
        style_label_text_scan = """
                QLabel { 
                    font-family: Arial; 
                    font-style: normal;  
                    font-size: 16pt; 
                    font-weight: bold; 
                    color: white; 
                }
                """
        style_label_Title_EG = """
                QLabel { 
                    font-family: MV Boli; 
                    font-style: normal;  
                    font-size: 20pt; 
                    font-weight: bold; 
                    color: rgb(245, 182, 75); 
                }
                
                QToolTip {
                    border-width:2px;
                    border-style:solid;
                    border-radius:5px;
                    background-color: rgb(30,31,34);
                    border: 1px solid white;
                }
                
                """

        style_label_Title_ClamNet = """
                    QLabel { 
                        font-family: Courier; 
                        font-style: normal;  
                        font-size: 16pt; 
                        font-weight: normal; 
                        color: rgb(0, 162, 232); 
                    }
                    """

        style_label_Title_Antivirus = """
                    QLabel { 
                        font-family: Courier; 
                        font-style: normal;  
                        font-size: 16pt; 
                        font-weight: normal; 
                        color: rgb(64, 213, 128); 
                    }
                    """
        style_checkBox1 = """
                QCheckBox { 
                    color: white; 
                    background: transparent; font-size: 10pt; font-family: Courier; font-weight: normal;
                }
                """
        style_radioButton1 = """
                    QRadioButton { 
                        color: white; 
                        background: transparent; font-size: 10pt; font-family: Courier; font-weight: normal;
    
                    }
                    """
        style_label1 = """
                    QLabel {
                        color: white;
                        background: transparent; font-size: 10pt; font-family: Courier; font-weight: normal;
                    } 
                    """
        style_checkBox2 = """
                QCheckBox { 
                    color: white; 
                    background: transparent; font-size: 12pt; font-weight: normal;
                    /*border: 0px solid rgb(0,96,48);*/   
                }
                """
        style_radioButton2 = """
                    QRadioButton { 
                        color: white; 
                        background: transparent; font-size: 12pt; font-weight: normal;
    
                    }
                    """
        style_label2 = """
                    QLabel {
                        color: white;
                        background: transparent; font-size: 12pt; font-weight: normal;
                    } 
                    """
        style_label3 = """
                    QLabel {
                        color: white;
                        background: transparent; font-size: 11pt; font-weight: normal;
                    } 
                    """
        style_label4 = """
                            QLabel {
                                color: lightgray;
                                font-family: Courier; 
                                background: transparent; 
                                font-size: 10pt; 
                                font-weight: normal;
                            } 
                            """

        style_checkBox = style_checkBox2
        style_radioButton = style_radioButton2
        style_label = style_label2
        style_command_link_button = """
                QCommandLinkButton { 
                    background-color: rgb(44, 45, 48);
                    border-radius: 5px;
                    color: white; 
                }
                QCommandLinkButton:pressed {
                    background-color: rgb(160, 170, 220);
                    color: blue; 
                }
                """
        style_pushButton = """
                QPushButton { 
                    background-color: rgb(44, 45, 48);
                    color: white;
                    font-size: 11pt;
                    border-radius: 5px;
                    border-color: white;
                    height: 35px;
                    width: 120px;
                } 
                QPushButton:pressed {
                    background-color: rgb(160, 170, 220);
                    color: black; 
                }
                QPushButton:disabled {
                    background-color: rgb(64, 65, 68);
                    color: rgb(44, 45, 48);
                }                
                """
        style_pushButton1 = """
                    QPushButton { 
                        background-color: rgb(44, 45, 48);
                        color: white;
                        border-radius: 3px;
                        border-color: white;
                        height: 30px;
                        width: 70px;
                    } 
                    QPushButton:pressed {
                        background-color: rgb(160, 170, 220);
                        color: black; 
                    }
                    """

        style_lineEdit = """ 
                    QLineEdit { 
                        border: 1px solid white; 
                        border-radius: 3px;      
                    } 
                    """
        style_textEdit = """
                    QTextEdit {
                        border: 1px solid white; 
                        border-radius: 5px;   
                    }
                    """
        style_textEdit_os_info = """
                            QPlainTextEdit {
                                background-color: rgb(30,31,34);
                                color: white;
                                font-size: 11pt;
                            }
                            """
        style_spinBox = """ 
                    QSpinBox {
                        /*background-color: rgb(30,31,34);
                        color: white;*/ 
                        font-size: 11pt; 
                    }
                    """
        style_tableWidget = """
                    QTableWidget {
                        background-color: rgb(30,31,34);
                        border: 1px solid white; 
                        border-radius: 2px;
                        color: white;
                        font-size: 11pt;
                        gridline-color: gray;  
                    }
                    """
        eg_label_tooltip = """
            <h1 style="color: #5e9ca0;">
                <span style="color: #ff9900;">EG</span> 
                <span style="color: #339966;">
                    Antivirus 
                    <span style="color: #000080;">2022&nbsp;</span> 
                    <img src="Resources/egav.png" width="30" height="30"> 
                </span>
            </h1> 
            
            <p>
                <span style="color: #000080;">Copyright:</span> 
                <span style="color: #ff6600;">
                    &copy; 2022 EG1, 
                    All Rights Reserved
                </span>
            </p> 
                
            <p>
                <span style="color: #000080;">Website:</span> 
                <a 
                    href="http://www.eg1.in">http://www.eg1.in
                </a>		
            </p> 
                
            <p>
                <span style="color: #000080;">Email:</span> 
                <span style="color: #003366;">&lt;eg1dotin@gmail.com&gt;</span>
            </p> 
            <p>&nbsp;</p> 
            <p>
                Powered by: 
                <a 
                    href="https://www.clamav.net/"><strong>ClamAV</strong>
                </a>
            </p> 
            <p>
                Gui by: 
                <a 
                    href="https://wiki.qt.io/Qt_for_Python">Qt, 
                    <strong>PySide6</strong>
                </a>
                &nbsp;
            </p> 
        """

    class InfoPopup:
        style_dialog = """
                    QDialog { 
                        background-color: rgb(30,31,34); 
                        border: 1px solid rgb(0,96,48) /*rgb(240,240,240)*/; 
                        /*border-radius: 10px;*/  
                    }
                """
        style_label_eg = """
                    QLabel { 
                        font-family: MV Boli; 
                        font-style: normal;  
                        font-size: 20pt; 
                        font-weight: bold; 
                        color: rgb(245, 182, 75); 
                    }
                    """
        style_label_ClamNet = """
                    QLabel { 
                        font-style: normal;  
                        font-size: 20pt; 
                        font-weight: normal; 
                        color: rgb(0, 162, 232); 
                    }
                    """
        style_label_antivirus = """
                    QLabel { 
                        /*font-family: Courier;*/ 
                        font-style: normal;  
                        font-size: 20pt; 
                        font-weight: normal; 
                        color: rgb(64, 213, 128); 
                    }
                    """
        style_label_year = """
                    QLabel { 
                        /*font-family: Courier;*/ 
                        font-style: normal;  
                        font-size: 12pt; 
                        font-weight: normal; 
                        color: rgb(64, 128 , 213); 
                    }
                    """
        style_label_copyright_website_email = """
                    QLabel { 
                        /*font-family: Courier;*/ 
                        font-style: normal;  
                        font-size: 12pt; 
                        font-weight: normal; 
                        color: rgb(0, 128 , 64); 
                    }
                    """
        style_label_copyright_text = """
                        QLabel { 
                            /*font-family: Courier;*/ 
                            font-style: normal;  
                            font-size: 12pt; 
                            font-weight: normal; 
                            color: rgb(207, 166 , 1); 
                        }
                        """
        style_label_website_email_text = """
                        QLabel { 
                            /*font-family: Courier;*/ 
                            font-style: normal;  
                            font-size: 12pt; 
                            font-weight: normal; 
                            color: rgb(220, 220 , 220); 
                        }
                        """
        style_label_poweredBy_GuiBy = """
                        QLabel { 
                            /*font-family: Courier;*/ 
                            font-style: normal;  
                            font-size: 16pt; 
                            font-weight: normal; 
                            color: rgb(100, 100 , 100); 
                        }
                        """
        style_label_image_egav = """
                QLabel { 
                    border-image : url(Resources/egav.png); 
                }
                """
        size_label_image_egav = QtCore.QSize(80, 80)
        style_label_image_clamAV = """
                    QLabel { 
                        border-image : url(Resources/clamav.png); 
                    }
                    """
        size_label_image_clamAV = QtCore.QSize(100, 56)
        style_label_image_QtPyside6 = """
                    QLabel { 
                        border-image : url(Resources/pyside6.png); 
                    }
                    """
        size_label_image_QtPyside6 = QtCore.QSize(100, 56)

    class InputPopup:
        style_dialog = """
                    QDialog { 
                        background-color: rgb(30,31,34); 
                        border: 0px solid rgb(0,96,48);/*1px solid rgb(240,240,240);*/ 
                        /*border-radius: 10px;*/  
                    }
                """
        style_label = """
                    QLabel {
                        color: white;
                        background: transparent; font-size: 12pt; font-weight: normal;
                    } 
                    """
        style_lineEdit = """ 
                            QLineEdit { 
                                border: 1px solid white; 
                                border-radius: 3px;   
                                height: 25px;   
                            } 
                            """
        style_pushButton = """
                    QPushButton { 
                        background-color: rgb(243, 27, 43);
                        color: white;
                        border-radius: 3px;
                        border-color: white;
                        height: 30px;
                        width: 50px;
                        font-size: 12pt;
                        font-weight: bold;
                    } 
                    QPushButton:pressed {
                        background-color: rgb(160, 170, 220);
                        color: black; 
                    }
                    """
        style_pushButton1 = """
                    QPushButton { 
                        background-color: rgb(44, 45, 48);
                        color: white;
                        border-radius: 3px;
                        border-color: white;
                        height: 30px;
                        width: 70px;
                        font-size: 12pt;
                    } 
                    QPushButton:pressed {
                        background-color: rgb(160, 170, 220);
                        color: black; 
                    }
                    """
        style_groupBox = """
                QGroupBox { 
                    background-color: rgb(64, 69, 74);
                    color: white; 
                    border: 0px solid white; 
                    /*border-radius: 10px;*/ 
                }
                """
        style_groupBox1 = """
                        QGroupBox { 
                            background-color: rgb(30,31,34);
                            color: white; 
                            border: 1px solid rgb(0,96,48); 
                            border-radius: 10px; 
                        }
                        """

    class MessagePopup:
        style_dialog = """
                    QDialog { 
                        background-color: rgb(30,31,34); 
                        border: 0px solid white; 
                        border-radius: 10px;  
                    }
                """
        style_label = """
                    QLabel {
                        color: white;
                        background: transparent; font-size: 12pt; font-weight: normal;
                    } 
                    """
        style_lineEdit = """ 
                            QLineEdit { 
                                border: 1px solid white; 
                                border-radius: 3px;   
                                height: 25px;   
                            } 
                            """
        style_pushButton = """
                    QPushButton { 
                        background-color: rgb(243, 27, 43);
                        color: white;
                        border-radius: 3px;
                        border-color: white;
                        height: 30px;
                        width: 50px;
                        font-size: 12pt;
                        font-weight: bold;
                    } 
                    QPushButton:pressed {
                        background-color: rgb(160, 170, 220);
                        color: black; 
                    }
                    """
        style_pushButton1 = """
                    QPushButton { 
                        background-color: rgb(44, 45, 48);
                        color: white;
                        border-radius: 3px;
                        border-color: white;
                        height: 30px;
                        width: 70px;
                        font-size: 12pt;
                    } 
                    QPushButton:pressed {
                        background-color: rgb(160, 170, 220);
                        color: black; 
                    }
                    """
        style_groupBox = """
                QGroupBox { 
                    background-color: rgb(64, 69, 74);
                    color: white; 
                    border: 0px solid white; 
                    /*border-radius: 10px;*/ 
                }
                """
        style_groupBox1 = """
                        QGroupBox { 
                            background-color: rgb(30,31,34);
                            color: white; 
                            border: 1px solid rgb(0,96,48); 
                            border-radius: 10px; 
                        }
                        """

    class ScannerWindow:
        style_dialog = """
                    QWidget { 
                        background-color: rgb(35,35,35);    
                        /*border: 1px solid rgb(0,96,48);*/
                    }
                    """
        style_label_scanType = """
                    QLabel {
                        font-family: Courier;  
                        font-style: normal;  
                        font-size: 22pt; 
                        font-weight: bold; 
                        color: rgb(240, 240, 240); 
                    }
                    """
        style_label_scanning_text = """
                    QLabel { 
                        font-style: normal;  
                        font-size: 10pt; 
                        font-weight: normal; 
                        color: rgb(240, 240, 240); 
                    }
                    """
        style_label_infectedFiles_text = """
                    QLabel { 
                        font-style: normal;  
                        font-size: 16pt; 
                        font-weight: bold; 
                        color: rgb(240, 240, 240); 
                    }
                    """
        style_label_infectedFilesNumber_text = """
                    QLabel { 
                        font-style: normal;  
                        font-size: 16pt; 
                        font-weight: bold; 
                        color: rgb(240, 10, 10); 
                    }
                    """
        style_stop_button = """
                QPushButton { 
                    background-color: rgb(44, 45, 48);
                    color: white;
                    font-size: 11pt;
                    border-radius: 5px;
                    border-color: white;
                    height: 35px;
                    width: 120px;
                } 
                QPushButton:pressed {
                    background-color: rgb(160, 170, 220);
                    color: black; 
                }                
                """

    class SetupMenu:
        title = EGAVCommonInfo.EGAV_TITLE_SHRT + " Setup"
        style_widget = """
                            QWidget { 
                                background-color: rgb(30,31,34);    
                            }
                            """
        style_pushButton = """
                        QPushButton { 
                            background-color: rgb(44, 45, 48);
                            color: white;
                            font-size: 11pt;
                            border-radius: 5px;
                            border-color: white;
                            height: 35px;
                            width: 120px;
                        } 
                        QPushButton:pressed {
                            background-color: rgb(160, 170, 220);
                            color: black; 
                        }
                        QPushButton:disabled {
                            background-color: rgb(64, 65, 68);
                            color: rgb(44, 45, 48);
                        }                
                        """

    class Html_Text:
        PARAGRAPH_SIMPLE = lambda value_str: "<p>" + value_str + "</p>"
        PARAGRAPH_GENERAL = lambda value_str, color, font_size: """<p style="color:""" + color + \
                                                                """;font-size:""" + str(font_size) + \
                                                                """px;">""" + value_str + """</p>"""
        STYLE_GENERAL = lambda value_str, color, font_size: """<span style="color:""" + color + \
                                                            """;font-size:""" + str(font_size) + \
                                                            """px;">""" + value_str + """</span>"""
        LINE_BREAK = """<br>"""


if __name__ == "__main__":
    # test any code here
    pass
