"""
SetupClamAV.py :=> this file is used to install ClamAV and ClamAV Services
"""

from os import path, makedirs, getlogin
from platform import platform
from time import sleep
from zipfile import ZipFile

from ClamAVResources import ClamAVResources
from EGAVDownloader import downloadEGAVFilesNExtract, download_clamav_files
from EGAVResources import EGAVPaths
from apis import info_installation2, info_uninstallation2
from config import DEBUG_CODE, STARTING_UPDATE_CLAMAV_DB_FILES
from custom import check_network, run_command_async_and_print_output, just_run_cmd
from custom import dq, empty_dir, get_windows_service
from singleObj import clamav_commands


class ConsoleColor:
    HEADER = '\033[95m'
    OK_BLUE = '\033[94m'
    OK_CYAN = '\033[96m'
    OK_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END_C = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def setup_clamAV_Windows(clamav_path_and_conf, bInstall=True, updateDB=STARTING_UPDATE_CLAMAV_DB_FILES):
    if bInstall:
        directory_to_extract_to = path.join(ClamAVResources.CLAMAV_DIR)
        print("Checking system architecture...")
        arch = clamav_path_and_conf.arch
        path_to_zip_file = path.join(ClamAVResources.CLAMAV_DIR)
        url = 'https://www.clamav.net/downloads/production/'
        if arch == "64bit":
            print("System Architecture -> 64Bit")
            """define latest ClamAV executable zip file name here for 64Bit Windows"""
            clam_av_exe_zip = ClamAVResources.WINDOWS_CLAMAV_PACKAGE_64BIT
            url += clam_av_exe_zip
            path_to_zip_file = path.join(path_to_zip_file, clam_av_exe_zip)
        elif arch == "32bit":
            print("System Architecture -> 32Bit")
            """define latest ClamAV executable zip file name here for 32Bit Windows"""
            clam_av_exe_zip = ClamAVResources.WINDOWS_CLAMAV_PACKAGE_32BIT
            url += clam_av_exe_zip
            path_to_zip_file = path.join(path_to_zip_file, clam_av_exe_zip)
        else:
            print("Error -> Unable to find System Architecture... ")
            return
        print("Downloading ClamAV ...")
        print("from url - " + url)
        # urllib.request.urlretrieve(url, path_to_zip_file)
        try:
            download_clamav_files(download_url=url, download_folder=ClamAVResources.CLAMAV_DIR)
        except Exception as e:
            print("Error: " + str(e))
            return
        print("Downloading done -> ClamAV downloaded")
        sleep(0.5)
        print("Extracting ClamAV zip file...")
        with ZipFile(path_to_zip_file) as zip_ref:
            zip_ref.extractall(directory_to_extract_to)
        print("Extracting -> Done")
        sleep(0.5)
        # --------------------------------------------------------------------------------------#
        print("Configuring ClamAV services...")
        cmd = clamav_path_and_conf.clamd_exe + ' ' + '--install'
        if not run_command_async_and_print_output(cmd):
            return
        # --------------------------------------------------------------------------------------#
        # first install fresh clam service and then start fresh clam service and update VSD database,
        # then start clamav services
        print("Configuring FreshClam services...")
        cmd = clamav_path_and_conf.freshclam_exe + ' ' + '--install'
        if not run_command_async_and_print_output(cmd):
            return

        if updateDB:
            if not clamav_path_and_conf.clamav_db_updated():
                print("Manually Updating ClamAV signature database for first time, it will be automatically updated in "
                      "future...")
                cmd = clamav_path_and_conf.freshclam_exe + " --show-progress --check=2 --datadir=" + dq + \
                      clamav_path_and_conf.clamav_db_dir + dq + " --log=" + dq + clamav_path_and_conf.freshclam_logs + \
                      dq
                if not run_command_async_and_print_output(cmd):
                    return
        # --------------------------------------------------------------------------------------#
        print("Starting ClamAV services...")
        cmd = "sc.exe start clamd"
        if not run_command_async_and_print_output(cmd):
            return
        sleep(1)
        cmd = "sc.exe start freshclam"
        if not run_command_async_and_print_output(cmd):
            return
        sleep(1)
        # --------------------------------------------------------------------------------------#
        if not DEBUG_CODE:
            just_run_cmd(dq + path.join(EGAVPaths.InstallationPath, "EGCNAVWinSer.exe") + dq + " -i")
            cmd = "sc.exe start WinSerEGCNTray"
            run_command_async_and_print_output(cmd)
        sleep(1)
        # set db to confirm we installed all successfully
        EGAVPaths.setInstalled(bInstalled=True)
    else:
        clamdStatus = get_windows_service(name="clamd")
        freshClamStatus = get_windows_service(name="freshclam")

        print("Stopping & Deleting ClamAV services...")

        if clamdStatus is not None:
            print("stopping clamd service ...")
            if clamdStatus["status"] == "running":
                cmd = "sc.exe stop clamd"
                if not run_command_async_and_print_output(cmd):
                    return
            else:
                print("clamd service is already stopped.")
            sleep(1)
            print("Deleting clamd service ...")
            cmd = "sc.exe delete clamd"
            if not run_command_async_and_print_output(cmd):
                return
        else:
            print("clamd service is not installed.")

        if freshClamStatus is not None:
            print("stopping freshclam service ...")
            if freshClamStatus["status"] == "running":
                cmd = "sc.exe stop freshclam"
                if not run_command_async_and_print_output(cmd):
                    return
            else:
                print("freshclam service is already stopped.")
            sleep(1)
            print("Deleting freshclam service ...")
            cmd = "sc.exe delete freshclam"
            if not run_command_async_and_print_output(cmd):
                return
        else:
            print("freshclam service is not installed.")
        sleep(1)
        if not DEBUG_CODE:
            cmd = "sc.exe stop WinSerEGCNTray"
            run_command_async_and_print_output(cmd)
            cmd = "sc.exe delete WinSerEGCNTray"
            run_command_async_and_print_output(cmd)
        sleep(1)
        empty_dir(EGAVPaths.AppDataDir)
        EGAVPaths.setInstalled(bInstalled=False)


def setup_clamAV_Linux(bInstall=True):
    if bInstall:
        # if platform().__contains__("debian"):
        # --------------------------------------------------------------------------------------#
        print("Updating system packages...")
        cmd = "apt-get update -y"
        run_command_async_and_print_output(cmd)
        # do not return here because it is not must
        # --------------------------------------------------------------------------------------#
        print("Installing clamAV, clamAV -Daemon...")
        cmd = "apt-get install clamav clamav-daemon -y"
        if not run_command_async_and_print_output(cmd):
            return
        # --------------------------------------------------------------------------------------#
        print("Manually Updating ClamAV signature database for first time, it will be automatically updated in "
              "future...")
        cmd = "systemctl stop clamav-freshclam"
        run_command_async_and_print_output(cmd)
        cmd = "freshclam"
        run_command_async_and_print_output(cmd)

        print("Restarting the service to update the database in the background...")
        cmd = "systemctl start clamav-freshclam"
        run_command_async_and_print_output(cmd)

        # --------------------------------------------------------------------------------------#
        # set status for setup install
        EGAVPaths.setInstalled(bInstalled=True)

        # set permission of execution to folders
        cmd = "chmod -R 777 " + path.join("/", "home", getlogin(), ".egcnav2")
        run_command_async_and_print_output(cmd)
        cmd = "chmod -R 777 " + EGAVPaths.AppDataDir
        run_command_async_and_print_output(cmd)
    else:
        # pass commands to uninstall
        # --------------------------------------------------------------------------------------#
        print("Removing clamAV, clamAV -Daemon...")
        cmd = "apt-get remove clamav clamav-daemon -y"
        if not run_command_async_and_print_output(cmd):
            return
        # --------------------------------------------------------------------------------------#
        # set status for setup uninstall
        EGAVPaths.setInstalled(bInstalled=False)


def setup_clamAV_MAC(bInstall=True):
    if bInstall:
        # --------------------------------------------------------------------------------------#
        print("Installing homebrew package...")
        cmd = """/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""""
        if not run_command_async_and_print_output(cmd):
            return
        print("Installing ClamAV packages...")
        cmd = "sh " + path.join("scripts", "OSX", "install-on-macos.sh")
        if not run_command_async_and_print_output(cmd):
            return
        # do other task here
        #

        # set status for setup install
        EGAVPaths.setInstalled(bInstalled=True)
        pass
    else:
        print("Uninstalling ClamAV packages...")
        cmd = "sh " + path.join("scripts", "OSX", "uninstall-on-macos.sh")
        if not run_command_async_and_print_output(cmd):
            return
        # set status for setup uninstall
        EGAVPaths.setInstalled(bInstalled=False)


def setup_clamAV(mode="install"):
    clamav_path_and_conf = clamav_commands.clamav_paths_and_configs
    os_name = clamav_path_and_conf.os
    if mode == "install" or mode == "update":

        # check if already updated or not if updated just return with print(already updated)

        print("Checking network connection ...")
        if check_network():
            print("Network Connection -> OK")
            makedirs(EGAVPaths.InstallationPath, exist_ok=True)

            ####
            if mode == "install":
                downloadEGAVFilesNExtract(egav_update=False)

            if os_name == "Windows":
                print("Configuring ClamAV Resources directories...")
                clamav_path_and_conf.save_conf_clamd()
                clamav_path_and_conf.save_conf_fresh()
                print("Configuring ClamAV Resources directories -> OK")
                print("Checking Operating system...")
                print("OS -> " + platform())
                setup_clamAV_Windows(clamav_path_and_conf, bInstall=True)
            elif os_name == "Linux":
                print("Configuring ClamAV Resources directories...")
                print("OS -> " + platform())
                setup_clamAV_Linux(bInstall=True)
            elif os_name == "MAC":
                print("Downloading EGAV files...")
                # download zip egav
                print("Extracting EGAV Zip files...")
                # extract zip files
                print("Configuring ClamAV Resources directories...")
                print("Configuring ClamAV Resources directories...")
                print("OS -> " + platform())
                setup_clamAV_MAC(bInstall=True)
            # send installation details of user to server
            info_installation2()
        else:
            print("Please check your network and try again.")
            return
    elif mode == "uninstall":
        if os_name == "Windows":
            setup_clamAV_Windows(clamav_path_and_conf, bInstall=False)
        elif os_name == "Linux":
            setup_clamAV_Linux(bInstall=False)
        elif os_name == "MAC":
            setup_clamAV_MAC(bInstall=False)
        else:
            print("Unknown OS")
            return
        # delete egav files from installation folder
        info_uninstallation2()
        empty_dir(EGAVPaths.InstallationPath)
    else:
        print("Unknown Error!!")


def main():
    import sys
    n = len(sys.argv)
    if n == 2:
        if sys.argv[1] in ["-i", "--install"]:
            setup_clamAV(mode="install")
        elif sys.argv[1] in ["-p", "--update"]:
            setup_clamAV(mode="update")
        elif sys.argv[1] in ["-u", "--uninstall"]:
            setup_clamAV(mode="uninstall")
        elif sys.argv[1] in ["-h", "--help"]:
            print("SetupClamAV commandline help")
            print("SetupClamAV  [-i, --install]\t\tinstall ClamAV")
            print("SetupClamAV  [-p, --update]\t\tupdate ClamAV")
            print("SetupClamAV  [-u, -uninstall]\t\tuninstall ClamAV")
            print("SetupClamAV  [-h, --help]\t\tshows help")
    else:
        print("Invalid arguments are passed. Type SetupClamAV --help to see all options.")


if __name__ == "__main__":
    main()
    pass
