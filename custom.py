"""
custom.py :=> This file provides custom functions and classes used in this source code
"""

from datetime import datetime
from inspect import currentframe, getouterframes
from json import loads as json_loads, dumps as json_dumps, dump as json_dump, load as json_load
from ntpath import split as ntpath_split
from os import remove as remove_file, makedirs
from os import system, getcwd, name as os_name_, walk as os_walk, path
from platform import system as platform_detail
from shutil import copyfile as copy_file, move as move_file
from subprocess import CalledProcessError
from subprocess import STDOUT as subprocess_STDOUT, DEVNULL as subprocess_DEVNULL
from subprocess import check_output as cmd_check_output, Popen as process_open, PIPE as subprocess_pipe
from sys import executable
from requests import get as requests_get
from send2trash import send2trash
from config import CURRENT_VERSION_INFO
from config import EGAVLinks, DEBUG_CODE, IS_CURRENT_WORKING_DIR_IN_PROG_FILES

# CONSTANTS
dq = "\""


# Classes
class OS:
    """ this class is used to check Operating System details."""
    WINDOWS = "Windows"
    LINUX = "Linux"
    MAC = "MAC"
    UNKNOWN = "Unknown"

    @staticmethod
    def get_os_details():
        """
        get operating system detail
        :return: str that represent Windows/Linux/MAC
        """
        os_name = os_name_
        system_str = platform_detail()
        result = OS.UNKNOWN
        if (os_name == 'posix') and (system_str == 'Linux'):
            result = OS.LINUX
        elif (os_name == 'nt') and (system_str == 'Windows'):
            result = OS.WINDOWS
        elif (os_name == 'posix') and (system_str == 'Darwin'):
            result = OS.MAC
        return result

    @staticmethod
    def Windows():
        """
        Check if OS is Windows
        :return: True if OS is Windows else False
        """
        return OS.get_os_details() == OS.WINDOWS

    @staticmethod
    def Linux():
        """
        Check if OS is Linux
        :return: True if OS is Linux else False
        """
        return OS.get_os_details() == OS.LINUX

    @staticmethod
    def OSX():
        """
        Check is OS is MAC
        :return: True if OS is MAC else False
        """
        return OS.get_os_details() == OS.MAC

    @staticmethod
    def Unknown():
        """
        Check if OS is unknown
        :return: return True if OS is Unknown, else return False
        """
        os_name = OS.get_os_details()
        if os_name != OS.WINDOWS and os_name != OS.LINUX and os_name != OS.MAC:
            return True
        else:
            return False


class DiskDrives:
    """
    this class is used to get details of disk drives of an operating system
    """

    @staticmethod
    def getDiskDrivesList():
        """
        get list of disk drives
        :return:
        """
        if OS.Windows():
            return DiskDrives.getWindowsDiskDrives()
        elif OS.Linux():
            return DiskDrives.getLinuxDiskDrives()
        elif OS.OSX():
            return DiskDrives.getMacDiskDrives()
        else:
            print_v1("Unknown Operating System")
            exit(-1)

    @staticmethod
    def getWindowsDiskDrives():
        """
        get list of Windows disk drives
        :return:
        """
        drive_list = process_open('wmic logicaldisk get name', shell=True, stdout=subprocess_pipe)
        drive_list_out, error = drive_list.communicate()
        drive_lines = drive_list_out.split(b'\r\r\n')
        res = []
        for dLine in drive_lines:
            ddLine = dLine.decode("utf8")
            ddLine = ddLine.replace(' ', '')
            if ddLine not in ['Name', '']:
                ddLine = ddLine.replace(':', ":\\")
                res += [ddLine]
        return res

    @staticmethod
    def getLinuxDiskDrives():
        list_drives = process_open('mount', shell=True, stdout=subprocess_pipe)
        list_drives_out, err = list_drives.communicate()
        for idx, drive in enumerate(filter(None, list_drives_out)):
            list_drives_out[idx] = drive.split()[2]
        return list_drives_out

    @staticmethod
    def getMacDiskDrives():
        return DiskDrives.getLinuxDiskDrives()


# FUNCTIONS
def do_nothing():
    """
    this function do nothing :)
    :return:
    """
    return


def str_quote(str_obj):
    """
    this function enquote a string
    :param str_obj: (string)
    :return: quoted (string)
    """
    return "\"" + str_obj + "\""


def pretty_dict(d: dict):
    """
    return a dict object in pretty format string
    :param d: (dict)
    :return: (string)
    """
    res = ""
    res += "\n"
    for k, v in d.items():
        res += str(k) + " : " + str(v) + "\n"
    res += "-" * 55
    return res


def print_v1(args, logs=True):
    """
    this function is used for logs
    :param args:
    :param logs: if True it prints logs in file otherwise only print on terminal
    :return: (None)
    """
    from EGAVResources import EGAVPaths
    res = dict()
    time_now = datetime.now()
    log_file_name = time_now.strftime("%Y%m%d") + ".txt"
    current_time = time_now.strftime("%Y-%m-%d %H:%M:%S")
    res["Time"] = current_time
    res["Message"] = args

    if DEBUG_CODE:
        print(args)
        if not OS.Windows():
            log_file_full_path = path.join(EGAVPaths.LogsDir, log_file_name)
        else:
            log_file_full_path = path.join(getcwd(), "EGAVLogs", log_file_name)
    else:
        log_file_full_path = path.join(EGAVPaths.LogsDir, log_file_name)

    if logs:
        curframe = currentframe()
        calframe = getouterframes(curframe, 2)
        # current_func_name = str(calframe[0][0]).split(',')[-1].split(' ')[-1][0:-1]
        res["Function"] = calframe[1][3]
        res["Line"] = calframe[1][2]
        res["File"] = calframe[1][1]

        with open(log_file_full_path, 'a', encoding='utf-8') as f:
            print(pretty_dict(res), file=f)
    return


def print_v2(args, logs=True, log_file_name="EGAVMain.txt"):
    """
    this function is used for logs (old version use print_v1)
    :param args:
    :param logs:
    :param log_file_name:
    :return:
    """
    if DEBUG_CODE:
        print(args)
    if logs:
        curframe = currentframe()
        calframe = getouterframes(curframe, 2)
        # current_func_name = str(calframe[0][0]).split(',')[-1].split(' ')[-1][0:-1]
        for k in calframe:
            print(k)

        with open(path.join(getcwd(), "EGAVLogs", log_file_name), 'a') as f:
            print("", file=f)
            print("------------------------------------------------------", file=f)
            print(get_time_str(datetime.now()), file=f)
            print("Function Called: " + calframe[1][3] + ", " + args, file=f)
            print("------------------------------------------------------", file=f)
            print("", file=f)
    return


def check_network():
    """
    this function is used for check if internet is working
    :return: return True if internet is there otherwise return false
    """
    import socket
    REMOTE_SERVER = "one.one.one.one"
    try:
        host = socket.gethostbyname(REMOTE_SERVER)
        s = socket.create_connection((host, 80), 2)
        s.close()
        return True
    except Exception as e:
        print_v1("Error in network connection, " + e.__str__())
        return False


def test_func(func, param=None):
    """
    this function is used for checking a function's calling time
    :param func: function identifier
    :param param: function parameters (list)
    :return: None
    """
    if param is None:
        param = []
    import time
    start = time.process_time()
    print(func(*param))
    print(time.process_time() - start)


def shuffle_string(in_str):
    """
    to shuffle a string
    :param in_str:
    :return: shuffled string (string)
    """
    import random
    list_str = list(in_str)
    random.shuffle(list_str)
    new_str = ''
    for i in list_str:
        new_str += i
    return new_str


def shuffle_string_n_times(in_str, n):
    """
    to shuffle a string n times
    :param in_str: input (string)
    :param n: (int) number of time you want to shuffle
    :return: n times shuffled (string)
    """
    for i in range(n):
        in_str = shuffle_string(in_str)
    return in_str


def just_run_cmd(cmd, logs=True):
    """
    to execute a command using system , no output of the command
    :param cmd: command (string)
    :param logs: (bool) if true, command string and working directory printed as json otherwise nothing printed
    :return: None
    """
    if logs:
        json_details = {
            "CommandExecuted": cmd,
            "WorkingDirectory": getcwd()
        }
        print_v1(json_dumps(json_details))
    system(cmd)


def run_command(cmd):
    """
    to execute a command using subprocess.check_output
    :param cmd: command (string)
    :return: command output (string)
    """
    print_v1("Command Executed: " + cmd)
    output = None
    if cmd:
        try:
            output = cmd_check_output(cmd).decode('utf8').replace('\n', '')
        except Exception as e:
            output = e.__str__()
    else:
        pass
    return output


def run_command_and_get_output(cmd):
    """
    to execute a command using subprocess.check_output and output is printed in the logs
    :param cmd: command string
    :return: (bool) if command successfully executed, return True else return False
    """
    print_v1("Command Executed: " + cmd)
    output = ""
    success = False
    if cmd:
        try:
            output = cmd_check_output(cmd).decode('utf8').replace('\n', '')
            success = True
        except Exception as e:
            print_v1("Error: " + e.__str__())
            success = False
    if success:
        print_v1("Executed Command: " + " ".join(cmd))
        print_v1("Command Output: " + output)
    else:
        print_v1("Error -> Command: " + " ".join(cmd))
    return success


def run_command_async(cmd, shell=True):
    """
    async execution of a command using process.open
    :param cmd: pass a command as string if shell=True, else pass command as list
    :param shell: True or False
    :return: Generator of output lines
    """
    print_v1("Command Executed: " + cmd)
    popen = process_open(cmd, stdout=subprocess_pipe,
                         stderr=subprocess_STDOUT,
                         stdin=subprocess_DEVNULL,
                         universal_newlines=True,
                         shell=shell)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise CalledProcessError(return_code, cmd)


def run_command_async_and_get_output(cmd, shell=True):
    """
    async execution of a command using process.open
    :param cmd: pass a command as string if shell=True, else pass command as list
    :param shell: True or False
    :return: output in (string)
    """
    print_v1("Command Executed: " + cmd)
    outputs = run_command_async(cmd, shell)
    res = ""
    for output in outputs:
        res += output
    return res


def run_command_async_and_print_output(cmd, shell=True):
    """
    async execution of a command using process.open and print output (Errors are printed in logs)
    :param cmd: pass a command as string if shell=True, else pass command as list
    :param shell: True or False
    :return: (bool) True if command successfully executed else False
    """
    print_v1("Command Executed: " + cmd)
    success = False
    try:
        for line in run_command_async(cmd, shell):
            print(line)
        success = True
    except Exception as e:
        print("Error: " + e.__str__())
        print_v1("Error: " + e.__str__())
    return success


def get_files_list_from_folder(walk_dir):
    """
    this function iterate through a folder and return the list of files
    :param walk_dir: (string) input folder path
    :return: (list) of files in the input folder
    """
    list_Files = []
    for root, subdirs, files in os_walk(walk_dir):
        for filename in files:
            file_path = path.join(root, filename)
            list_Files.append(file_path)
    return list_Files


def get_total_number_of_files(ext, walk_dir):
    """
    this function calculates total number of files in a dir
    :param ext: extension of file (string)
    :param walk_dir: dir path (string)
    :return: (int) number of files that matches the file extension
    """
    n = 0
    for root, subdirs, files in os_walk(walk_dir):
        for filename in files:
            file_name, file_ext = path.splitext(filename)
            if file_ext == ext:
                n += 1
    return n


def get_files_list_str_from_folder(walk_dir, separator=" "):
    """
    this function iterate through a folder and return the list of files in string format
    :param walk_dir: (string) input folder path
    :param separator:  separator symbol (example "," , " ", "-" etc)
    :return: (string) separated files path
    """
    list_Files_str = ""
    for root, subdirs, files in os_walk(walk_dir):
        for filename in files:
            file_path = path.join(root, filename)
            list_Files_str += dq + file_path + dq + separator
    return list_Files_str


def get_time_str(datetime0, format="%Y-%m-%d %H:%M:%S"):
    """
    get time in string format
    :param datetime0: datetime
    :param format:
    :return: (string)
    """
    return datetime0.strftime(format=format)


def get_time_diff(datetime1: datetime, datetime2: datetime) -> str:
    """
    This function returns time difference (in String) between two datetime values.
    :param datetime1:
    :param datetime2:
    :return: time difference between datetime1 and datetime2
    """
    dt = datetime2 - datetime1
    time_in_secs = dt.seconds
    time_in_mins = time_in_secs / 60
    time_in_hrs = time_in_mins / 60
    time_in_days = dt.days

    if time_in_secs and (time_in_secs < 60):
        return str(time_in_secs) + " seconds"
    elif time_in_mins and (time_in_mins < 60):
        return str(time_in_mins) + " minutes"
    elif time_in_hrs and (time_in_hrs < 24):
        return str(time_in_hrs) + " hours"
    elif time_in_secs == 0 and time_in_days == 0:
        return str(time_in_secs) + " seconds"
    else:
        return str(time_in_days) + " days"


def action_on_infected_file(file, result, action, quarantine_path):
    """
    this function is used to take an action on infected file
    :param file: file full path
    :param result: scanned result
    :param action: 1= Reported, 2= Deleted, 3= Quarantined
    :param quarantine_path: full path of Quarantine folder
    :return: (None)
    """
    if action == 1:
        destination_virus = path.join(quarantine_path, path.basename(file) + ".infected")
        copy_file(src=file, dst=destination_virus)
        destination_virus_detail = path.join(quarantine_path, path.basename(file) + ".json")
        virus_details = dict()
        virus_details["Date"] = get_time_str(datetime.now())
        virus_details["Detected Item"] = result[file][1]
        virus_details["Action Taken"] = "Action Not Taken"
        virus_details["Found At Location"] = file
        virus_details["Status"] = 'Reported'
        virus_details["Current Location"] = destination_virus
        with open(file=destination_virus_detail, mode="w") as f:
            json_dump(virus_details, f)
    elif action == 2:
        remove_file(file)
        destination_virus_detail = path.join(quarantine_path, path.basename(file) + ".json")
        virus_details = dict()
        virus_details["Date"] = get_time_str(datetime.now())
        virus_details["Detected Item"] = result[file][1]
        virus_details["Action Taken"] = "Deleted"
        virus_details["Found At Location"] = file
        virus_details["Status"] = 'Removed'
        virus_details["Current Location"] = None
        with open(file=destination_virus_detail, mode="w") as f:
            json_dump(virus_details, f)
    elif action == 3:
        destination_virus = path.join(quarantine_path, path.basename(file) + ".infected")
        move_file(src=file, dst=destination_virus)
        destination_virus_detail = path.join(quarantine_path, path.basename(file) + ".json")
        virus_details = dict()
        virus_details["Date"] = get_time_str(datetime.now())
        virus_details["Detected Item"] = result[file][1]
        virus_details["Action Taken"] = "Action Not Taken"
        virus_details["Found At Location"] = file
        virus_details["Status"] = 'Quarantined'
        virus_details["Current Location"] = destination_virus
        with open(file=destination_virus_detail, mode="w") as f:
            json_dump(virus_details, f)
    else:
        pass


def modification_date(file_full_path):
    """
    get modification date of a file
    :param file_full_path:
    :return: (string)
    """
    if path.isfile(file_full_path):
        t = path.getmtime(file_full_path)
        return datetime.fromtimestamp(t)
    else:
        return None


def empty_dir(dir_path, bRecycleBin=False):
    """
    to delete all files and folders in a folder
    :param dir_path: folder path (string)
    :param bRecycleBin: (bool) if True, then send files/folders in trash, otherwise do nothing just print only
    :return: (None)
    """
    if bRecycleBin:
        print("removing ... " + dir_path)
        print("deleted files are in trash or recycle bin")
        send2trash(dir_path)
    else:
        print("MOCK: removing ... " + dir_path)

    # use only send2trash function here for removing files/folders
    # never un-comment this below code, it is very dangerous function
    # of deleting files completely in recursively manner, there is no
    # recovering method, it was used only for testing purposes
    #
    # ******************** DANGER ZONE *************************
    # for files in list_dir(dir_path):
    #     file_path = path.join(dir_path, files)
    #     print("removing file" + file_path) if debug else do_nothing()
    #     try:
    #         remove_tree(file_path)
    #     except OSError:
    #         try:
    #             remove_file(file_path)
    #         except Exception as e:
    #             print_v1("Error: " + e.__str__())
    # **********************************************************


def str_list_separation(input_list_str, separator=" ", end_quote="\""):
    """
    separate a list of string with input separator and input quote symbol
    :param input_list_str: (list) of strings
    :param separator: separator symbol (string)
    :param end_quote: quote symbol (string)
    :return: (string)
    """
    # assert(type(input_list_str[0]) == str)
    res = ""
    for e in input_list_str:
        res += end_quote + e + end_quote + separator
    return res[0:-1]


def path_correction(path_str: str) -> str:
    """
    to make path correction, if Windows, the path includes "\\" otherwise "/"
    :param path_str: (string)
    :return: (string)
    """
    if not OS.Windows():
        res = path.join(path_str)
    else:
        res = path_str.replace("/", "\\")
    return res


def paths_correction(paths_list):
    """
    to make path correction, if Windows, the path includes "\\" otherwise "/"
    :param paths_list: (list) of string
    :return: (list) of string
    """
    res = []
    for ff in paths_list:
        if not OS.Windows():
            res.append(path.join(ff))
        else:
            res.append(ff.replace("/", "\\"))
    return res


def set_cmd_str_as_root(cmd):
    """
    rewrite a command for executing it from root permission
    :param cmd: (string) command
    :return: (string)
    """
    sudo_str = ''
    if OS.Windows():
        sudo_str = ''
    elif OS.Linux():
        sudo_str = 'pkexec '
    elif OS.OSX():
        sudo_str = 'sudo '
    cmd1 = sudo_str + cmd
    return cmd1


def get_windows_service(name="clamd"):
    """
    get details of a Windows Service
    :param name: name of Windows service (string)
    :return: (dict) if a service exist else (None)
    """
    from psutil import win_service_get
    service = None
    try:
        service = win_service_get(name)
        service = service.as_dict()
        service['exist'] = True
    except Exception as ex:
        print(str(ex))
    return service


def check_linux_daemon(daemon_name='clamd'):
    """
    this function checks linux daemon, return "1" if running else return "0"
    :param daemon_name: name of daemon to check
    :return: "1" if running else return "0" <str>
    """
    cmd = "ps -ef | grep -v grep | grep -cw " + daemon_name
    try:
        output = run_command_async_and_get_output(cmd)
    except Exception as e:
        print_v1(args="Error: " + str(e))
        output = "0"
    return output


def check_service(service_name='clamd', turn_on=True):
    """
    check clam av services status, if stopped, start them
    :param service_name: (string)
    :param turn_on: (bool)
    :return: (None)
    """
    if OS.Windows():
        clamd_service = get_windows_service(service_name)
        print_v1(pretty_dict(clamd_service))
        if clamd_service['exist']:
            if clamd_service['status'] != 'running':
                if turn_on:
                    print_v1(service_name + ' service is not running, starting service now...')
                    cmd = 'sc start ' + service_name
                    just_run_cmd(cmd)
                    just_run_cmd('sc start freshclam') if service_name == 'clamd' else do_nothing()
                else:
                    print_v1(service_name + ' service is not running')
            else:
                print_v1(service_name + ' service is running')
        else:
            print_v1(service_name + " service doesn't exist")
            # here you can install the service

    elif OS.Linux():
        if check_linux_daemon() != '1':
            if turn_on:
                print_v1(service_name + ' daemon is not running, fixing it now...')
                cmd = '/etc/init.d/clamav-daemon start'
                cmd = set_cmd_str_as_root(cmd)
                just_run_cmd(cmd)
            else:
                print_v1(service_name + ' daemon is not running')
        else:
            print_v1(service_name + ' daemon is already running')
    elif OS.OSX():
        pass


def email_valid(email_text):
    """
    Check Email validation
    :param email_text: (string)
    :return: (bool) True if email is valid else None
    """
    import re
    regex = '\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b'
    if re.fullmatch(regex, email_text):
        return True
    return None


def STR_T(time):
    """
    used for making double-digit for time in string
    :param time: (int)
    :return: (string)
    """
    if not (time >= 0 or time <= 9):
        return str(time)
    else:
        return '0' + str(time)


def get_version_file_of_app(url=EGAVLinks.EGAV_VERSION_LINK):
    """
    get version from remote JSON file
    :param url: JSON file Download URL
    :return: (dict)
    """
    response = requests_get(url)
    data = response.text
    data_dict = json_loads(data)
    return data_dict


def is_version_changed(latest_version=CURRENT_VERSION_INFO):
    """
    check if version got changed
    :param latest_version:
    :return: (bool)
    """
    version_detail = get_version_file_of_app()
    if version_detail["AppUpdateVersion"] == latest_version:
        return False
    else:
        return True


def add_my_program_to_WindowsRegistry(myExe_fullpath):
    """
    add an executable in Windows registry
    :param myExe_fullpath: Exe path (string)
    :return: (None)
    """
    if OS.Windows() is True:
        from winreg import OpenKey, SetValueEx, REG_SZ, KEY_SET_VALUE, HKEY_LOCAL_MACHINE
        key = OpenKey(HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run', 0, KEY_SET_VALUE)
        SetValueEx(key, 'myFile', 0, REG_SZ, myExe_fullpath)
        key.Close()
    else:
        pass


def write_in_file(file_fullpath, texts):
    """
    write in file, if file not exist, create it, otherwise write in already existed file
    :param file_fullpath: (string)
    :param texts: (string)
    :return: (None)
    """
    def write_file(file_path, texts_to_write):
        with open(file_path, 'w') as file:
            file.write(texts_to_write)
        return

    try:
        dir_path, file_name = ntpath_split(file_fullpath)
        makedirs(dir_path, exist_ok=True)
        write_file(file_fullpath, texts)
    except:
        write_file(file_fullpath, texts)
    return


def class_attribute_to_json(c):
    """
    get class attributes and return information in dict
    :param c: class identifier (string)
    :return: (dict)
    """
    res = {}
    for i, j in c.__dict__.items():
        if not i.__contains__("__") and (type(j) in [str, list]):
            res[i] = j
    return res


def class_attribute_to_jsonStr(c):
    """
    get class attributes and return information in json string
    :param c: class identifier (string)
    :return: (string)
    """
    return json_dumps(class_attribute_to_json(c))


def get_current_working_dir():
    """
    get current working directory path
    :return: (string)
    """
    if not DEBUG_CODE:
        if IS_CURRENT_WORKING_DIR_IN_PROG_FILES:
            application_path = path.dirname(executable)
        else:
            application_path = getcwd()
    else:
        application_path = getcwd()
    return application_path


def json_key(json_path, key):
    """
    get JSON key from json file
    :param json_path: (string)
    :param key: (string)
    :return: (string) return full json if key is None or empty
    """
    with open(json_path, "r") as f:
        d = json_load(f)
    return d[key] if key else d


if __name__ == "__main__":
    # test any code here
    pass

