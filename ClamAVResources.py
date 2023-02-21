"""
ClamAVResources.py :=> This file contains information about ClamAV's Resources, paths, commands, services etc.
"""

from datetime import datetime
from os import makedirs, path
from platform import architecture

from EGAVResources import EGAVDatabase, EGAVPaths, EGAVResources, QtPaths
from config import CURRENT_CLAMAV_VERSION_STR
from custom import action_on_infected_file, run_command_async_and_get_output, write_in_file
from custom import class_attribute_to_json, pretty_dict
from custom import dq, OS, print_v1, get_files_list_from_folder


class ClamAVResources:
    WINDOWS_CLAMD_EXE = "clamd.exe"
    WINDOWS_CLAMSCAN_EXE = "clamscan.exe"
    WINDOWS_CLAMDSCAN_EXE = "clamdscan.exe"
    WINDOWS_FRESHCLAM_EXE = "freshclam.exe"

    LINUX_CLAMD_EXE = "clamd"
    LINUX_CLAMSCAN_EXE = "clamscan"
    LINUX_CLAMDSCAN_EXE = "clamdscan"
    LINUX_FRESHCLAM_EXE = "freshclam"

    MAC_CLAMD_EXE = "clamd"
    MAC_CLAMSCAN_EXE = "clamscan"
    MAC_CLAMDSCAN_EXE = "clamdscan"
    MAC_FRESHCLAM_EXE = "freshclam"

    WINDOWS_CLAMD_LOG_FILE = "ClamdLog.txt"
    WINDOWS_CLAMD_PID_FILE = "clamd.pid"
    WINDOWS_CLAMD_LOCAL_SOCKET = "clamd.socket"
    CLAMD_CONFIG_FILE = "clamd.conf"

    LINUX_CLAMD_LOG_FILE = "clamav.log"
    LINUX_CLAMD_PID_FILE = "clamd.pid"
    LINUX_CLAMD_LOCAL_SOCKET = "clamd.ctl"
    LINUX_FRESHCLAM_LOG_FILE = "freshclam.log"

    WINDOWS_FRESHCLAM_UPDATE_LOG_FILE = "FreshClamLog.txt"
    FRESHCLAM_DNS_DATABASE_INFO = "current.cvd.clamav.net"
    FRESHCLAM_DATABASE_MIRROR = ["db.uk.clamav.net", "database.clamav.net"]
    FRESHCLAM_CONFIG_FILE = "freshclam.conf"

    CLAMAV_DIR = path.join(EGAVPaths.AppDataDir, "ClamAV")

    WINDOWS_CLAMAV_PACKAGE_64BIT = CURRENT_CLAMAV_VERSION_STR + ".win.x64.zip"
    WINDOWS_CLAMAV_PACKAGE_32BIT = CURRENT_CLAMAV_VERSION_STR + ".win.win32.zip"
    WINDOWS_CLAMAV_MAIN_DIR_64BIT = path.join(CLAMAV_DIR, WINDOWS_CLAMAV_PACKAGE_64BIT[0:-4])
    WINDOWS_CLAMAV_MAIN_DIR_32BIT = path.join(CLAMAV_DIR, WINDOWS_CLAMAV_PACKAGE_32BIT[0:-4])
    WINDOWS_CLAMAV_DATABASE_DIR_64BIT = path.join(CLAMAV_DIR, "db")
    WINDOWS_CLAMAV_DATABASE_DIR_32BIT = path.join(CLAMAV_DIR, "db")
    WINDOWS_CLAMD_FULLPATH_64BIT = path.join(WINDOWS_CLAMAV_MAIN_DIR_64BIT, WINDOWS_CLAMD_EXE)
    WINDOWS_CLAMD_FULLPATH_32BIT = path.join(WINDOWS_CLAMAV_MAIN_DIR_32BIT, WINDOWS_CLAMD_EXE)
    WINDOWS_CLAMSCAN_FULLPATH_64BIT = path.join(WINDOWS_CLAMAV_MAIN_DIR_64BIT, WINDOWS_CLAMSCAN_EXE)
    WINDOWS_CLAMSCAN_FULLPATH_32BIT = path.join(WINDOWS_CLAMAV_MAIN_DIR_32BIT, WINDOWS_CLAMSCAN_EXE)
    WINDOWS_CLAMDSCAN_FULLPATH_64BIT = path.join(WINDOWS_CLAMAV_MAIN_DIR_64BIT, WINDOWS_CLAMDSCAN_EXE)
    WINDOWS_CLAMDSCAN_FULLPATH_32BIT = path.join(WINDOWS_CLAMAV_MAIN_DIR_32BIT, WINDOWS_CLAMDSCAN_EXE)
    WINDOWS_FRESHCLAM_FULLPATH_64BIT = path.join(WINDOWS_CLAMAV_MAIN_DIR_64BIT, WINDOWS_FRESHCLAM_EXE)
    WINDOWS_FRESHCLAM_FULLPATH_32BIT = path.join(WINDOWS_CLAMAV_MAIN_DIR_32BIT, WINDOWS_FRESHCLAM_EXE)

    WINDOWS_CLAMAV_LOGS_DIR = path.join(CLAMAV_DIR, "ClamAVLogs")
    WINDOWS_CLAMD_LOGFILE_FULLPATH = path.join(WINDOWS_CLAMAV_LOGS_DIR, WINDOWS_CLAMD_LOG_FILE)
    WINDOWS_FRESHCLAM_UPDATE_LOGFILE_FULLPATH = path.join(WINDOWS_CLAMAV_LOGS_DIR, WINDOWS_FRESHCLAM_UPDATE_LOG_FILE)

    # actual path for config files
    WINDOWS_CLAMD_CONFIG_FILE_FULLPATH_64BIT = path.join(WINDOWS_CLAMAV_MAIN_DIR_64BIT, CLAMD_CONFIG_FILE)
    WINDOWS_CLAMD_CONFIG_FILE_FULLPATH_32BIT = path.join(WINDOWS_CLAMAV_MAIN_DIR_32BIT, CLAMD_CONFIG_FILE)
    WINDOWS_FRESHCLAM_CONFIG_FILE_FULLPATH_64BIT = path.join(WINDOWS_CLAMAV_MAIN_DIR_64BIT, FRESHCLAM_CONFIG_FILE)
    WINDOWS_FRESHCLAM_CONFIG_FILE_FULLPATH_32BIT = path.join(WINDOWS_CLAMAV_MAIN_DIR_32BIT, FRESHCLAM_CONFIG_FILE)

    WINDOWS_CLAMD_PIDFILE_FULLPATH_64BIT = path.join(CLAMAV_DIR, WINDOWS_CLAMD_PID_FILE)
    WINDOWS_CLAMD_PIDFILE_FULLPATH_32BIT = path.join(CLAMAV_DIR, WINDOWS_CLAMD_PID_FILE)
    WINDOWS_CLAMD_LOCAL_SOCKET_FULLPATH_64BIT = path.join(CLAMAV_DIR, WINDOWS_CLAMD_LOCAL_SOCKET)
    WINDOWS_CLAMD_LOCAL_SOCKET_FULLPATH_32BIT = path.join(CLAMAV_DIR, WINDOWS_CLAMD_LOCAL_SOCKET)

    LINUX_CLAMAV_DATABASE_DIR = path.join('/', 'var', 'lib', 'clamav')
    MAC_CLAMAV_DATABASE_DIR = path.join('/', 'var', 'lib', 'clamav')

    LINUX_CLAMAV_LOGS_DIR = path.join('/', 'var', 'log', 'clamav')
    LINUX_CLAMD_LOGFILE_FULLPATH = path.join(LINUX_CLAMAV_LOGS_DIR, LINUX_CLAMD_LOG_FILE)
    LINUX_FRESHCLAM_UPDATE_LOGFILE_FULLPATH = path.join(LINUX_CLAMAV_LOGS_DIR, LINUX_FRESHCLAM_LOG_FILE)
    LINUX_CLAMD_SOCKET_FULLPATH = path.join('/', 'var', 'run', 'clamav', LINUX_CLAMD_LOCAL_SOCKET)
    LINUX_CLAMD_CONFIG_FILE_FULLPATH = path.join('/', 'etc', 'clamav', CLAMD_CONFIG_FILE)

    MAC_CLAMD_CONFIG_FILE_FULLPATH = path.join('/', 'usr', 'local', 'etc', 'clamav', CLAMD_CONFIG_FILE)

    LINUX_FRESHCLAM_CONFIG_FILE_FULLPATH = path.join('/', 'etc', 'clamav', FRESHCLAM_CONFIG_FILE)
    MAC_FRESHCLAM_CONFIG_FILE_FULLPATH = path.join('/', 'usr', 'local', 'etc', 'clamav', FRESHCLAM_CONFIG_FILE)

    # ---------------------
    @staticmethod
    def get_clam_av_resources_details():
        str_details = ""
        str_details += "WINDOWS_CLAMD_EXE: " + ClamAVResources.WINDOWS_CLAMD_EXE + "\n"
        str_details += "WINDOWS_CLAMSCAN_EXE: " + ClamAVResources.WINDOWS_CLAMSCAN_EXE + "\n"
        str_details += "WINDOWS_CLAMDSCAN_EXE: " + ClamAVResources.WINDOWS_CLAMDSCAN_EXE + "\n"
        str_details += "WINDOWS_FRESHCLAM_EXE: " + ClamAVResources.WINDOWS_FRESHCLAM_EXE + "\n"

        str_details += "LINUX_CLAMD_EXE: " + ClamAVResources.LINUX_CLAMD_EXE + "\n"
        str_details += "LINUX_CLAMSCAN_EXE: " + ClamAVResources.LINUX_CLAMSCAN_EXE + "\n"
        str_details += "LINUX_CLAMDSCAN_EXE: " + ClamAVResources.LINUX_CLAMDSCAN_EXE + "\n"
        str_details += "LINUX_FRESHCLAM_EXE: " + ClamAVResources.LINUX_FRESHCLAM_EXE + "\n"

        str_details += "MAC_CLAMD_EXE: " + ClamAVResources.MAC_CLAMD_EXE + "\n"
        str_details += "MAC_CLAMSCAN_EXE: " + ClamAVResources.MAC_CLAMSCAN_EXE + "\n"
        str_details += "MAC_CLAMDSCAN_EXE: " + ClamAVResources.MAC_CLAMDSCAN_EXE + "\n"
        str_details += "MAC_FRESHCLAM_EXE: " + ClamAVResources.MAC_FRESHCLAM_EXE + "\n"

        str_details += "WINDOWS_CLAMD_LOG_FILE: " + ClamAVResources.WINDOWS_CLAMD_LOG_FILE + "\n"
        str_details += "WINDOWS_CLAMD_PID_FILE: " + ClamAVResources.WINDOWS_CLAMD_PID_FILE + "\n"
        str_details += "WINDOWS_CLAMD_LOCAL_SOCKET: " + ClamAVResources.WINDOWS_CLAMD_LOCAL_SOCKET + "\n"
        str_details += "CLAMD_CONFIG_FILE: " + ClamAVResources.CLAMD_CONFIG_FILE + "\n"

        str_details += "WINDOWS_FRESHCLAM_UPDATE_LOG_FILE: " + ClamAVResources.WINDOWS_FRESHCLAM_UPDATE_LOG_FILE + "\n"
        str_details += "FRESHCLAM_DNS_DATABASE_INFO: " + ClamAVResources.FRESHCLAM_DNS_DATABASE_INFO + "\n"
        str_details += "FRESHCLAM_DATABASE_MIRROR: " + str(ClamAVResources.FRESHCLAM_DATABASE_MIRROR) + "\n"
        str_details += "FRESHCLAM_CONFIG_FILE: " + ClamAVResources.FRESHCLAM_CONFIG_FILE + "\n"

        str_details += "CLAMAV_DIR: " + ClamAVResources.CLAMAV_DIR + "\n"

        str_details += "WINDOWS_CLAMAV_DATABASE_DIR_64BIT: " + ClamAVResources.WINDOWS_CLAMAV_DATABASE_DIR_64BIT + "\n"
        str_details += "WINDOWS_CLAMAV_DATABASE_DIR_32BIT: " + ClamAVResources.WINDOWS_CLAMAV_DATABASE_DIR_32BIT + "\n"
        str_details += "WINDOWS_CLAMAV_PACKAGE_64BIT: " + ClamAVResources.WINDOWS_CLAMAV_PACKAGE_64BIT + "\n"
        str_details += "WINDOWS_CLAMAV_PACKAGE_32BIT: " + ClamAVResources.WINDOWS_CLAMAV_PACKAGE_32BIT + "\n"
        str_details += "WINDOWS_CLAMAV_MAIN_DIR_64BIT: " + ClamAVResources.WINDOWS_CLAMAV_MAIN_DIR_64BIT + "\n"
        str_details += "WINDOWS_CLAMAV_MAIN_DIR_32BIT: " + ClamAVResources.WINDOWS_CLAMAV_MAIN_DIR_32BIT + "\n"
        str_details += "WINDOWS_CLAMD_FULLPATH_64BIT: " + ClamAVResources.WINDOWS_CLAMD_FULLPATH_64BIT + "\n"
        str_details += "WINDOWS_CLAMD_FULLPATH_32BIT: " + ClamAVResources.WINDOWS_CLAMD_FULLPATH_32BIT + "\n"
        str_details += "WINDOWS_CLAMSCAN_FULLPATH_64BIT: " + ClamAVResources.WINDOWS_CLAMSCAN_FULLPATH_64BIT + "\n"
        str_details += "WINDOWS_CLAMSCAN_FULLPATH_32BIT: " + ClamAVResources.WINDOWS_CLAMSCAN_FULLPATH_32BIT + "\n"

        str_details += "WINDOWS_CLAMDSCAN_FULLPATH_64BIT: " + ClamAVResources.WINDOWS_CLAMDSCAN_FULLPATH_64BIT + "\n"
        str_details += "WINDOWS_CLAMDSCAN_FULLPATH_32BIT: " + ClamAVResources.WINDOWS_CLAMDSCAN_FULLPATH_32BIT + "\n"

        str_details += "WINDOWS_FRESHCLAM_FULLPATH_64BIT: " + ClamAVResources.WINDOWS_FRESHCLAM_FULLPATH_64BIT + "\n"
        str_details += "WINDOWS_FRESHCLAM_FULLPATH_32BIT: " + ClamAVResources.WINDOWS_FRESHCLAM_FULLPATH_32BIT + "\n"

        str_details += "WINDOWS_CLAMAV_LOGS_DIR: " + ClamAVResources.WINDOWS_CLAMAV_LOGS_DIR + "\n"
        str_details += "WINDOWS_CLAMD_LOGFILE_FULLPATH: " + ClamAVResources.WINDOWS_CLAMD_LOGFILE_FULLPATH + "\n"
        str_details += "WINDOWS_CLAMD_PIDFILE_FULLPATH_64BIT: " + ClamAVResources.WINDOWS_CLAMD_PIDFILE_FULLPATH_64BIT + "\n"
        str_details += "WINDOWS_CLAMD_PIDFILE_FULLPATH_32BIT: " + ClamAVResources.WINDOWS_CLAMD_PIDFILE_FULLPATH_32BIT + "\n"
        str_details += "WINDOWS_CLAMD_LOCAL_SOCKET_FULLPATH_64BIT: " + ClamAVResources.WINDOWS_CLAMD_LOCAL_SOCKET_FULLPATH_64BIT + "\n"
        str_details += "WINDOWS_CLAMD_LOCAL_SOCKET_FULLPATH_32BIT: " + ClamAVResources.WINDOWS_CLAMD_LOCAL_SOCKET_FULLPATH_32BIT + "\n"
        str_details += "WINDOWS_FRESHCLAM_UPDATE_LOGFILE_FULLPATH: " + ClamAVResources.WINDOWS_FRESHCLAM_UPDATE_LOGFILE_FULLPATH + "\n"

        # actual path for config files
        str_details += "WINDOWS_CLAMD_CONFIG_FILE_FULLPATH_64BIT: " + ClamAVResources.WINDOWS_CLAMD_CONFIG_FILE_FULLPATH_64BIT + "\n"
        str_details += "WINDOWS_CLAMD_CONFIG_FILE_FULLPATH_32BIT: " + ClamAVResources.WINDOWS_CLAMD_CONFIG_FILE_FULLPATH_32BIT + "\n"
        str_details += "WINDOWS_FRESHCLAM_CONFIG_FILE_FULLPATH_64BIT: " + ClamAVResources.WINDOWS_FRESHCLAM_CONFIG_FILE_FULLPATH_64BIT + "\n"
        str_details += "WINDOWS_FRESHCLAM_CONFIG_FILE_FULLPATH_32BIT: " + ClamAVResources.WINDOWS_FRESHCLAM_CONFIG_FILE_FULLPATH_32BIT + "\n"
        # ---------------------
        return str_details


class ClamAVPathsAndConfigs:
    """
    this class is used for ClamAV paths, configurations and other settings, It should be used as a singleton class
    """
    m_Instance = None

    def __init__(self, singleton=False):
        if not singleton:
            raise Exception("ClamAVPathsAndConfigs is a singleton class, use ClamAVPathsAndConfigs.object() instead "
                            "of ClamAVPathsAndConfigs()")

        self.isOK = True
        self.os = OS.get_os_details()
        self.arch = architecture()[0]

        # make default dirs
        try:
            makedirs(EGAVPaths.AppDataDir, exist_ok=True)
            makedirs(EGAVPaths.QuarantineDir, exist_ok=True)
            makedirs(EGAVPaths.SettingsDBDir, exist_ok=True)
            makedirs(ClamAVResources.CLAMAV_DIR, exist_ok=True)
            makedirs(EGAVPaths.LogsDir, exist_ok=True)
            # makedirs(EGAVPaths.InstallationPath, exist_ok=True)
        except Exception as e:
            print_v1("Error: error in creating dir" + e.__str__())
            self.isOK = False
            return

        if self.os == "Windows":
            if self.arch == "64bit":
                self.clamd_exe = ClamAVResources.WINDOWS_CLAMD_FULLPATH_64BIT
                self.clamscan_exe = ClamAVResources.WINDOWS_CLAMSCAN_FULLPATH_64BIT
                self.clamdscan_exe = ClamAVResources.WINDOWS_CLAMDSCAN_FULLPATH_64BIT
                self.freshclam_exe = ClamAVResources.WINDOWS_FRESHCLAM_FULLPATH_64BIT
                self.clamd_conf = ClamAVResources.WINDOWS_CLAMD_CONFIG_FILE_FULLPATH_64BIT
                self.freshclam_conf = ClamAVResources.WINDOWS_FRESHCLAM_CONFIG_FILE_FULLPATH_64BIT
                self.clamav_dir = ClamAVResources.WINDOWS_CLAMAV_MAIN_DIR_64BIT
                self.clamav_db_dir = ClamAVResources.WINDOWS_CLAMAV_DATABASE_DIR_64BIT
                self.clamav_logs_dir = ClamAVResources.WINDOWS_CLAMAV_LOGS_DIR
                self.clamd_pid = ClamAVResources.WINDOWS_CLAMD_PIDFILE_FULLPATH_64BIT
                self.clamd_socket = ClamAVResources.WINDOWS_CLAMD_LOCAL_SOCKET_FULLPATH_64BIT
                self.clamd_logs = ClamAVResources.WINDOWS_CLAMD_LOGFILE_FULLPATH
                self.freshclam_logs = ClamAVResources.WINDOWS_FRESHCLAM_UPDATE_LOGFILE_FULLPATH
                try:
                    makedirs(self.clamav_dir, exist_ok=True)
                    makedirs(self.clamav_db_dir, exist_ok=True)
                    makedirs(self.clamav_logs_dir, exist_ok=True)
                except Exception as e:
                    print_v1("Error: error in creating dir" + e.__str__())
                    self.isOK = False
            elif self.arch == '32bit':
                self.clamd_exe = ClamAVResources.WINDOWS_CLAMD_FULLPATH_32BIT
                self.clamscan_exe = ClamAVResources.WINDOWS_CLAMSCAN_FULLPATH_32BIT
                self.clamdscan_exe = ClamAVResources.WINDOWS_CLAMDSCAN_FULLPATH_32BIT
                self.freshclam_exe = ClamAVResources.WINDOWS_FRESHCLAM_FULLPATH_32BIT
                self.clamd_conf = ClamAVResources.WINDOWS_CLAMD_CONFIG_FILE_FULLPATH_32BIT
                self.freshclam_conf = ClamAVResources.WINDOWS_FRESHCLAM_CONFIG_FILE_FULLPATH_32BIT
                self.clamav_dir = ClamAVResources.WINDOWS_CLAMAV_MAIN_DIR_32BIT
                self.clamav_db_dir = ClamAVResources.WINDOWS_CLAMAV_DATABASE_DIR_32BIT
                self.clamav_logs_dir = ClamAVResources.WINDOWS_CLAMAV_LOGS_DIR
                self.clamd_pid = ClamAVResources.WINDOWS_CLAMD_PIDFILE_FULLPATH_32BIT
                self.clamd_socket = ClamAVResources.WINDOWS_CLAMD_LOCAL_SOCKET_FULLPATH_32BIT
                self.clamd_logs = ClamAVResources.WINDOWS_CLAMD_LOGFILE_FULLPATH
                self.freshclam_logs = ClamAVResources.WINDOWS_FRESHCLAM_UPDATE_LOGFILE_FULLPATH
                try:
                    makedirs(self.clamav_dir, exist_ok=True)
                    makedirs(self.clamav_db_dir, exist_ok=True)
                    makedirs(self.clamav_logs_dir, exist_ok=True)
                except Exception as e:
                    print_v1("Error: error in creating dir" + e.__str__())
                    self.isOK = False
            else:
                print_v1("Error: unknown Windows architecture")
                self.isOK = False
                return
            self.json_conf_clamd = {
                "LogFile": dq +  self.clamd_logs + dq,
                "LogFileMaxSize": "2M",
                "LogClean": "yes",
                "LogTime": "no",
                "LogSyslog": "yes",
                "LogVerbose": "yes",
                "LogRotate": "yes",
                "ExtendedDetectionInfo": "yes",
                "PidFile": dq + self.clamd_pid + dq,
                "DatabaseDirectory": dq + self.clamav_db_dir + dq,
                "LocalSocket": dq + self.clamd_socket + dq,
                "FixStaleSocket": "yes",
                "MaxDirectoryRecursion": "20",
                "TCPSocket": "3310",
                "TCPAddr": "127.0.0.1",
                "StreamMaxLength": "100M"
            }
            self.json_conf_fresh = {
                "DatabaseDirectory": dq + self.clamav_db_dir + dq,
                "UpdateLogFile": dq + self.freshclam_logs + dq,
                "LogFileMaxSize": "1M",
                "LogTime": "yes",
                "LogVerbose": "yes",
                "LogSyslog": "yes",
                "LogFacility": "LOG_MAIL",
                "LogRotate": "yes",
                "DNSDatabaseInfo": ClamAVResources.FRESHCLAM_DNS_DATABASE_INFO,
                "DatabaseMirror": ClamAVResources.FRESHCLAM_DATABASE_MIRROR,
                "MaxAttempts": "5",
                "ScriptedUpdates": "yes",
                "CompressLocalDatabase": "no",
                "Checks": "12",
                "Foreground": "yes",
                "ConnectTimeout": "60",
                "ReceiveTimeout": "60",
                "TestDatabases": "yes",
                "SafeBrowsing": "yes",
            }
        elif self.os == "Linux":
            self.clamd_exe = ClamAVResources.LINUX_CLAMD_EXE
            self.clamscan_exe = ClamAVResources.LINUX_CLAMSCAN_EXE
            self.clamdscan_exe = ClamAVResources.LINUX_CLAMDSCAN_EXE
            self.freshclam_exe = ClamAVResources.LINUX_FRESHCLAM_EXE
            self.clamd_conf = ClamAVResources.LINUX_CLAMD_CONFIG_FILE_FULLPATH
            self.freshclam_conf = ClamAVResources.LINUX_FRESHCLAM_CONFIG_FILE_FULLPATH
            # self.clamav_dir = ""
            self.clamav_db_dir = ClamAVResources.LINUX_CLAMAV_DATABASE_DIR
            self.clamav_logs_dir = ClamAVResources.LINUX_CLAMAV_LOGS_DIR
            # self.clamd_pid = ""
            self.clamd_socket = ClamAVResources.LINUX_CLAMD_SOCKET_FULLPATH
            self.clamd_logs = ClamAVResources.LINUX_CLAMD_LOGFILE_FULLPATH
            self.freshclam_logs = ClamAVResources.LINUX_FRESHCLAM_UPDATE_LOGFILE_FULLPATH

            self.json_conf_clamd = {
                'LocalSocket': self.clamd_socket,
                'FixStaleSocket': 'true',
                'LocalSocketGroup': 'clamav',
                'LocalSocketMode': '666',
                'User': 'clamav',
                'ScanMail': 'true',
                'ScanArchive': 'true',
                'ArchiveBlockEncrypted': 'false',
                'MaxDirectoryRecursion': '15',
                'FollowDirectorySymlinks': 'false',
                'FollowFileSymlinks': 'false',
                'ReadTimeout': '180',
                'MaxThreads': '12',
                'MaxConnectionQueueLength': '15',
                'LogSyslog': 'false',
                'LogRotate': 'true',
                'LogFacility': 'LOG_LOCAL6',
                'LogClean': 'false',
                'LogVerbose': 'false',
                'PreludeEnable': 'no',
                'PreludeAnalyzerName': 'ClamAV',
                'DatabaseDirectory': self.clamav_db_dir,
                'OfficialDatabaseOnly': 'false',
                'SelfCheck': '3600',
                'Foreground': 'false',
                'Debug': 'false',
                'ScanPE': 'true',
                'MaxEmbeddedPE': '10M',
                'ScanOLE2': 'true',
                'ScanPDF': 'true',
                'ScanHTML': 'true',
                'MaxHTMLNormalize': '10M',
                'MaxHTMLNoTags': '2M',
                'MaxScriptNormalize': '5M',
                'MaxZipTypeRcg': '1M',
                'ScanSWF': 'true',
                'ExitOnOOM': 'false',
                'LeaveTemporaryFiles': 'false',
                'AlgorithmicDetection': 'true',
                'ScanELF': 'true',
                'IdleTimeout': '30',
                'CrossFilesystems': 'true',
                'PhishingSignatures': 'true',
                'PhishingScanURLs': 'true',
                'PhishingAlwaysBlockSSLMismatch': 'false',
                'PhishingAlwaysBlockCloak': 'false',
                'PartitionIntersection': 'false',
                'DetectPUA': 'false',
                'ScanPartialMessages': 'false',
                'HeuristicScanPrecedence': 'false',
                'StructuredDataDetection': 'false',
                'CommandReadTimeout': '30',
                'SendBufTimeout': '200',
                'MaxQueue': '100',
                'ExtendedDetectionInfo': 'true',
                'OLE2BlockMacros': 'false',
                'AllowAllMatchScan': 'true',
                'ForceToDisk': 'false',
                'DisableCertCheck': 'false',
                'DisableCache': 'false',
                'MaxScanTime': '120000',
                'MaxScanSize': '100M',
                'MaxFileSize': '25M',
                'MaxRecursion': '16',
                'MaxFiles': '10000',
                'MaxPartitions': '50',
                'MaxIconsPE': '100',
                'PCREMatchLimit': '10000',
                'PCRERecMatchLimit': '5000',
                'PCREMaxFileSize': '25M',
                'ScanXMLDOCS': 'true',
                'ScanHWP3': 'true',
                'MaxRecHWP3': '16',
                'StreamMaxLength': '25M',
                'LogFile': self.clamd_logs,
                'LogTime': 'true',
                'LogFileUnlock': 'false',
                'LogFileMaxSize': '0',
                'Bytecode': 'true',
                'BytecodeSecurity': 'TrustSigned',
                'BytecodeTimeout': '60000',
                'OnAccessMaxFileSize': '5M',
            }
            self.json_conf_fresh = {
                'DatabaseOwner': 'clamav',
                'UpdateLogFile': self.freshclam_logs,
                'LogVerbose': 'false',
                'LogSyslog': 'false',
                'LogFacility': 'LOG_LOCAL6',
                'LogFileMaxSize': '0',
                'LogRotate': 'true',
                'LogTime': 'true',
                'Foreground': 'false',
                'Debug': 'false',
                'MaxAttempts': '5',
                'DatabaseDirectory': self.clamav_db_dir,
                'DNSDatabaseInfo': 'current.cvd.clamav.net',
                'ConnectTimeout': '30',
                'ReceiveTimeout': '0',
                'TestDatabases': 'yes',
                'ScriptedUpdates': 'yes',
                'CompressLocalDatabase': 'no',
                'Bytecode': 'true',
                'NotifyClamd': self.clamd_conf,
                'Checks': '24',
                'DatabaseMirror': ['db.local.clamav.net', 'database.clamav.net'],
            }

        elif self.os == "MAC":
            self.clamd_exe = ClamAVResources.MAC_CLAMD_EXE
            self.clamscan_exe = ClamAVResources.MAC_CLAMSCAN_EXE
            self.clamdscan_exe = ClamAVResources.MAC_CLAMDSCAN_EXE
            self.freshclam_exe = ClamAVResources.MAC_FRESHCLAM_EXE
            self.clamd_conf = ClamAVResources.MAC_CLAMD_CONFIG_FILE_FULLPATH
            self.freshclam_conf = ClamAVResources.MAC_FRESHCLAM_CONFIG_FILE_FULLPATH
            # self.clamav_dir = ""
            self.clamav_db_dir = ""
            # self.clamav_logs_dir = ""
            # self.clamd_pid = ""
            # self.clamd_socket = ""
            # self.json_conf_clamd = {}
            # self.json_conf_fresh = {}
        else:
            print_v1(args="Error: unknown OS")
            self.isOK = False
            exit(-1)

    @staticmethod
    def object():
        if not ClamAVPathsAndConfigs.m_Instance:
            ClamAVPathsAndConfigs.m_Instance = ClamAVPathsAndConfigs(singleton=True)
            return ClamAVPathsAndConfigs.m_Instance
        else:
            return ClamAVPathsAndConfigs.m_Instance

    def clamav_db_updated(self, days=5):
        """
        :param days: if database older than days then not updated else updated
        :return: True or False
        """
        # clamav_db_files_list = ["bytecode.cld", "bytecode.cvd", "daily.cld",
        #                         "daily.cvd", "freshclam.dat", "mirrors.dat",
        #                         "mirrors.dat", "main.cvd", "main.cld"]
        try:
            # clamav_db_files_fullpath_list = [path.join(self.clamav_db_dir, file) for file in clamav_db_files_list]
            # clamav_db_files_time_list = [modification_date(f) for f in clamav_db_files_fullpath_list]
            # clamav_db_files_time_list = [t for t in clamav_db_files_time_list if t]
            # min_file_time = min(clamav_db_files_time_list)
            clamdVersionStr = run_command_async_and_get_output(cmd=self.clamd_exe + " -V")
            clamdVersionStr = clamdVersionStr.replace("\n", "")
            last_updated_time = clamdVersionStr.split("/")[-1]
            time_split = last_updated_time.split(" ")
            last_updated_time = " ".join(time_split)
            # print(last_updated_time)
            min_file_time = datetime.strptime(last_updated_time, "%a %b %d %H:%M:%S %Y")
            # print(min_file_time)
            # print((datetime.now() - min_file_time).days)
            if (datetime.now() - min_file_time).days > days:
                return False
            else:
                return True
        except Exception as e:
            print_v1(e.__str__())
            print("error")
            return False

    def save_conf_clamd(self):
        str_to_write = ""
        for key, value in self.json_conf_clamd.items():
            str_to_write += key + " " + value + "\n\n"
        str_to_write = str_to_write[0:-2]
        # print(str_to_write)
        with open(self.clamd_conf, "w+") as f:
            f.write(str_to_write)
        return

    def save_conf_fresh(self):
        str_to_write = ""
        for key, value in self.json_conf_fresh.items():
            if type(value) != list:
                str_to_write += key + " " + value + "\n\n"
            else:
                for e in value:
                    str_to_write += key + " " + e + "\n\n"
        str_to_write = str_to_write[0:-2]
        # print(str_to_write)
        with open(self.freshclam_conf, "w+") as f:
            f.write(str_to_write)
        return


class ClamAVCommands:
    """
    this class is used for ClamAV commands, it should be used as a singleton class
    """
    m_Instance = None

    def __init__(self, singleton=False):
        if not singleton:
            raise Exception("ClamAVCommands is a singleton class, use ClamAVCommands.object() instead of "
                            "ClamAVCommands()")
        self.egav_db = EGAVDatabase.object()
        self.clamav_paths_and_configs = ClamAVPathsAndConfigs.object()
        self.clamscan_exe = self.clamav_paths_and_configs.clamscan_exe
        self.clamdscan_exe = self.clamav_paths_and_configs.clamdscan_exe
        self.freshclam_exe = self.clamav_paths_and_configs.freshclam_exe
        self.clamav_db_dir = self.clamav_paths_and_configs.clamav_db_dir
        self.freshclam_logs = self.clamav_paths_and_configs.freshclam_logs

    @staticmethod
    def object():
        if not ClamAVCommands.m_Instance:
            ClamAVCommands.m_Instance = ClamAVCommands(singleton=True)
            ClamAVCommands.m_Instance.reload_egav_db()
            return ClamAVCommands.m_Instance
        else:
            ClamAVCommands.m_Instance.reload_egav_db()
            return ClamAVCommands.m_Instance

    def reload_egav_db(self):
        self.egav_db.loadDatabase()

    def get_remove_or_quarantine_str(self):
        QuarantineFolder = EGAVPaths.QuarantineDir
        res = self.egav_db.Preferences_InfectedFilesRadioButton
        if res == 1:
            res = ""
        if res == 2:
            res = "--remove=yes"
        if res == 3:
            res = "--move=\"" + QuarantineFolder + "\""
        return res

    def get_in_exclude_str_from_db(self):
        in_exclude_cmd = ""
        list_scan_only_ext = self.egav_db.Settings_ScanOnlyExtension
        if list_scan_only_ext:
            for ext in list_scan_only_ext:
                in_exclude_cmd = in_exclude_cmd + "--include=(^.*\\" + ext + ")$ "
        else:
            list_exclude_ext = self.egav_db.Settings_ExcludeExtension
            if list_exclude_ext:
                for ext in list_exclude_ext:
                    in_exclude_cmd = in_exclude_cmd + "--exclude=(^.*\\" + ext + ")$ "

                ExcludeCommonOption = "infected"
                in_exclude_cmd = in_exclude_cmd + "--exclude=(^.*\\" + ExcludeCommonOption + ")$ "

        return in_exclude_cmd

    @staticmethod
    def get_quick_scan_include_option():
        include_files_ext = [
            ".EXE", ".DLL", ".SRC",
            ".SYS", ".MSI", ".REG",
            ".CAB", ".JAR", ".VBS",
            ".COM", ".BAT", ".SHS",
            ".PIF", ".SCR", ".DOC"
        ]
        res = ""
        for ext in include_files_ext:
            res += "--include=(^.*\\" + ext + ")$ "
        return res

    def get_max_info_str_from_db(self):
        s1 = str(self.egav_db.Settings_DoNotScanFilesLargerThanMB)
        s2 = str(self.egav_db.Settings_DoNotExtractMoreThanMB)
        s3 = str(self.egav_db.Settings_DoNotExtractMoreThanFiles)
        s4 = str(self.egav_db.Settings_DoNotExtractMoreThanSubArchives)

        if self.egav_db.Settings_ExtractFilesFromArchives:
            res = "--max-filesize=" + s1 + "M "
        else:
            res = "--max-filesize=" + s1 + "M --max-scansize=" + s2 + "M --max-files=" + s3 + " --max-recursion=" + s4 + " "
        return res

    @staticmethod
    def get_quick_scan_max_info_option():
        res = "--max-filesize=5M "
        return res

    def get_scan_cmd(self):
        if self.clamscan_exe == "":
            return None
        remove_or_quarantine_str = self.get_remove_or_quarantine_str()
        in_exclude_str_from_db = self.get_in_exclude_str_from_db()
        max_info_str_from_db = self.get_max_info_str_from_db()
        res = self.clamscan_exe + " --stdout --bell --recursive=yes " + remove_or_quarantine_str + " " + \
              in_exclude_str_from_db + max_info_str_from_db
        return res

    def get_fast_scan_cmd(self):
        if self.clamdscan_exe == "":
            return None
        remove_or_quarantine_str = self.get_remove_or_quarantine_str()
        res = self.clamdscan_exe + " --stdout " + remove_or_quarantine_str + " "
        return res

    def get_full_scan_cmd(self):
        if self.clamscan_exe == "":
            return None
        remove_or_quarantine_str = self.get_remove_or_quarantine_str()
        in_exclude_str_from_db = self.get_in_exclude_str_from_db()
        max_info_str_from_db = self.get_max_info_str_from_db()
        res = self.clamscan_exe + " --stdout --bell --recursive=yes " + \
              remove_or_quarantine_str + " " + in_exclude_str_from_db + max_info_str_from_db
        return res

    def get_quick_scan_cmd(self):
        if self.clamscan_exe == "":
            return None
        remove_or_quarantine_str = self.get_remove_or_quarantine_str()
        quick_scan_include_option = self.get_quick_scan_include_option()
        res = self.clamscan_exe + " --stdout --bell --recursive=yes " + \
              remove_or_quarantine_str + " " + quick_scan_include_option + "--max-filesize=4M "
        return res

    def get_memory_scan_cmd(self, unload_infected_program_from_memory):
        if self.clamscan_exe == "":
            return None
        remove_or_quarantine_str = self.get_remove_or_quarantine_str()
        if unload_infected_program_from_memory:
            res = self.clamscan_exe + " --stdout --bell " + remove_or_quarantine_str + \
                  " --memory -k -u --max-filesize=4M "
        else:
            res = self.clamscan_exe + " --stdout --bell " + remove_or_quarantine_str + \
                  " --memory -k --max-filesize=4M "
        return res

    def get_freshclam_cmd(self):
        res = self.freshclam_exe + " --show-progress --check=2 --datadir=" + dq + self.clamav_db_dir + dq + \
              " --log=" + dq + self.freshclam_logs + dq
        return res

    def print_all_commands(self):
        print("scan_cmd: " + self.get_scan_cmd())
        print("fast_scan_cmd: " + self.get_fast_scan_cmd())
        print("full_scan_cmd: " + self.get_full_scan_cmd())
        print("quick_scan_cmd: " + self.get_quick_scan_cmd())
        print("memory_scan_cmd: " + self.get_memory_scan_cmd(unload_infected_program_from_memory=True))
        print("freshclam_cmd: " + self.get_freshclam_cmd())


class ClamdService:
    """
    this class is used for ClamAV services/daemon/Socket, it should be used as a singleton class
    """

    m_Instance = None

    def __init__(self, singleton=False):
        if not singleton:
            raise Exception("ClamdService is a singleton class, use ClamdService.object() instead of ClamdService()")
        self.os = OS.get_os_details()
        self.ping = None
        self.clamd_socket = None
        self.version = None
        if self.os == "Windows":
            from clamd import ClamdNetworkSocket
            try:
                self.clamd_socket = ClamdNetworkSocket()
                self.ping = self.clamd_socket.ping()
                if self.ping == "PONG":
                    self.version = self.clamd_socket.version()
            except Exception as e:
                # print("Error: " + e.__str__())
                print_v1("Error: " + e.__str__())
            pass
        elif self.os == "Linux":
            from clamd import ClamdUnixSocket
            try:
                self.clamd_socket = ClamdUnixSocket()
                self.ping = self.clamd_socket.ping()
                if self.ping == "PONG":
                    self.version = self.clamd_socket.version()
                else:
                    print_v1("Error: service is not running")
            except Exception as e:
                print("Error: " + e.__str__())
        elif self.os == "MAC":
            from clamd import ClamdUnixSocket
            try:
                self.clamd_socket = ClamdUnixSocket()
                self.ping = self.clamd_socket.ping()
                if self.ping == "PONG":
                    self.version = self.clamd_socket.version()
                else:
                    print_v1("Error: service is not running")
            except Exception as e:
                print_v1("Error: " + e.__str__())
        else:
            print("Error: unknown OS")
            exit(-1)

    def isOK(self):
        try:
            return self.clamd_socket.ping() == "PONG"
        except Exception as e:
            print_v1("Error: " + e.__str__())
            return False

    @staticmethod
    def object():
        if not ClamdService.m_Instance:
            ClamdService.m_Instance = ClamdService(singleton=True)
            return ClamdService.m_Instance
        else:
            return ClamdService.m_Instance

    def scan_file(self, file, cmd=None, action=3):
        """
        scan file using clamd service/daemon
        :param file: file full path
        :param cmd: can be one in { 'SCAN', 'CONTSCAN', 'MULTISCAN' }
        :param action: 1= Report only, 2= Remove, 3= Quarantine
        :return: response in a dict
        """
        if cmd is None:
            cmd = 'SCAN'
        result = self.clamd_socket._file_system_scan(cmd, file)
        if result[file][0] == 'FOUND':
            action_on_infected_file(file=file, result=result, action=action, quarantine_path=EGAVPaths.QuarantineDir)
        print(result)
        return result

    def scan_files(self, files_list, cmd='SCAN', action=3):
        for file in files_list:
            self.scan_file(file, cmd, action)

    def scan_folder(self, folder, cmd='SCAN', action=3):
        files_list = get_files_list_from_folder(folder)
        self.scan_files(files_list, cmd, action)

    def scan(self, any_file_folder, cmd='SCAN', action=3):
        if path.isfile(any_file_folder):
            self.scan_file(file=any_file_folder, cmd=cmd, action=action)
        elif path.isdir(any_file_folder):
            self.scan_folder(folder=any_file_folder, cmd=cmd, action=action)
        else:
            print("Error: invalid parameter")

    def scan_and_get_result(self, any_file_folder, cmd='SCAN', action=3):
        if path.isfile(any_file_folder):
            return self.scan_file(file=any_file_folder, cmd=cmd, action=action)
        elif path.isdir(any_file_folder):
            return self.scan_folder(folder=any_file_folder, cmd=cmd, action=action)
        else:
            print("Error: invalid parameter")
            return None

    def scan_multiple_files_folders(self, separated_files_folders_paths_str, separator=",", cmd='SCAN', action=3):
        files_folders_list = separated_files_folders_paths_str.split(separator)
        for item in files_folders_list:
            self.scan(item, cmd, action)

    def scan_memory(self, action=3):
        if self.os == "Windows":
            if self.isOK():
                from processes import WindowsProcesses
                wp = WindowsProcesses()
                wp.scan_memory(function_clamdscan=self.clamd_socket.scan,
                               action=action,
                               quarantine_path=EGAVPaths.QuarantineDir)
            else:
                print("Error: clamd is not running.")
        else:
            print("memory scan option is available only for Windows OS")
        pass


def log_all_paths_info(log_file_name="paths.txt"):
    paths_info = pretty_dict(class_attribute_to_json(EGAVResources)) + "\n\n"
    paths_info += pretty_dict(class_attribute_to_json(QtPaths)) + "\n\n"
    paths_info += pretty_dict(class_attribute_to_json(EGAVPaths)) + "\n\n"
    paths_info += pretty_dict(class_attribute_to_json(ClamAVResources)) + "\n\n"
    write_in_file(file_fullpath=path.join(EGAVPaths.LogsDir, log_file_name),
                  texts=paths_info)


if __name__ == '__main__':
    # test any code here
    pass
