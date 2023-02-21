"""
processes.py :=> This file is used for processes
"""

from signal import SIGINT
from custom import str_quote, OS, action_on_infected_file, print_v1
from psutil import process_iter, NoSuchProcess, AccessDenied, ZombieProcess

os_name = OS.get_os_details()


def kill_proc_safely(process_pid):
    from subprocess import Popen as subprocess_open
    if OS.Windows():
        subprocess_open("taskkill /F /T /PID %i" % process_pid, shell=True)
    else:
        from os import killpg
        from signal import SIGINT
        killpg(process_pid, SIGINT)


class Processes:
    def __init__(self):
        # Iterate over all running process
        self.processes_list = []
        self.processes_iter = sorted(process_iter(), key=lambda i: i.name())
        for proc in self.processes_iter:
            try:
                # Get process name & pid from process object.
                # processName = proc.name()
                # processID = proc.pid
                processPath = proc.cwd()
                # print(processName)
                if processPath:
                    # pp = processPath + "/" + processName
                    # pp = pp.replace("\\", "/")
                    # print(proc.exe())
                    self.processes_list.append(str_quote(proc.exe()))
            except (NoSuchProcess, AccessDenied, ZombieProcess) as e:
                # print(e)
                pass

    @staticmethod
    def kill_process_by_name(proc_name, close_signal=SIGINT):
        from os import kill as kill_proc
        processes_iter = sorted(process_iter(), key=lambda i: i.name())
        for proc in processes_iter:
            try:
                # Get process name & pid from process object.
                if proc.name() == proc_name:
                    processID = proc.pid
                    print_v1("Process with ID=" + str(processID) + " & Name=" + proc_name + " interrupted")
                    kill_proc(processID, close_signal)
                    break
            except (NoSuchProcess, AccessDenied, ZombieProcess) as e:
                # print(e)
                pass
        return

    def getListAsSpaceSeparatedStr(self, separator=" "):
        ret = ""
        for process in self.processes_list:
            ret += process + separator
        return ret

    def checkIfProcessRunning(self, process_name):
        return process_name in (pr.name() for pr in self.processes_iter)


if os_name == "Windows":
    from os import remove as remove_file
    from os.path import basename
    from win32api import OpenProcess, TerminateProcess
    from collections import namedtuple
    from win32con import PROCESS_VM_READ
    from win32process import GetCurrentProcess, GetModuleFileNameEx
    from win32process import EnumProcessModulesEx, LIST_MODULES_ALL, EnumProcesses
    from win32security import TOKEN_ALL_ACCESS, SE_DEBUG_NAME, AdjustTokenPrivileges
    from win32security import SE_PRIVILEGE_ENABLED, LookupPrivilegeValue, OpenProcessToken


    class WindowsProcesses:
        STANDARD_RIGHTS_REQUIRED = 0x000F0000
        SYNCHRONIZE = 0x00100000
        PROCESS_ALL_ACCESS = (STANDARD_RIGHTS_REQUIRED | SYNCHRONIZE | 0xFFFF)
        PROCESS_QUERY_LIMITED_INFORMATION = 0x1000

        def __init__(self):
            self.Process = namedtuple('Process', 'name path pid modules')
            pass

        def adjust_privilege(self, name, attr=SE_PRIVILEGE_ENABLED):
            if isinstance(name, str):
                state = (LookupPrivilegeValue(None, name), attr)
            else:
                state = name
            hToken = OpenProcessToken(GetCurrentProcess(),
                                      TOKEN_ALL_ACCESS)
            return AdjustTokenPrivileges(hToken, False, [state])

        def get_process_modules(self, hProcess):
            imagepath = GetModuleFileNameEx(hProcess, None)
            imagepath_upper = imagepath.upper()
            modules = []
            for hModule in EnumProcessModulesEx(hProcess,
                                                LIST_MODULES_ALL):
                modulepath = GetModuleFileNameEx(hProcess, hModule)
                if modulepath.upper() != imagepath_upper:
                    modules.append(modulepath)
            return imagepath, sorted(modules)

        def list_processes(self):
            prev_state = self.adjust_privilege(SE_DEBUG_NAME)
            try:
                for pid in EnumProcesses():
                    hProcess = None
                    path = ''
                    modules = []
                    if pid == 0:
                        name = 'System Idle Process'
                    elif pid == 4:
                        name = 'System'
                    else:
                        try:
                            hProcess = OpenProcess(
                                self.PROCESS_QUERY_LIMITED_INFORMATION |
                                PROCESS_VM_READ,
                                False, pid)
                        except Exception as e:
                            try:
                                hProcess = OpenProcess(
                                    self.PROCESS_QUERY_LIMITED_INFORMATION,
                                    False, pid)
                            except Exception as e:
                                print("Exception: " + e.__str__())
                                pass
                        if hProcess:
                            try:
                                path, modules = self.get_process_modules(hProcess)
                            except Exception as e:
                                print("Exception: " + e.__str__())
                                pass
                        name = basename(path)
                    yield self.Process(name, path, pid, modules)
            finally:
                if prev_state:
                    self.adjust_privilege(prev_state[0])

        def list_all(self):
            prev_state = self.adjust_privilege(SE_DEBUG_NAME)
            info = dict()
            try:
                for pid in EnumProcesses():
                    hProcess = None
                    path = ''
                    modules = []
                    if pid == 0:
                        name = 'System Idle Process'
                    elif pid == 4:
                        name = 'System'
                    else:
                        try:
                            hProcess = OpenProcess(
                                self.PROCESS_ALL_ACCESS |
                                PROCESS_VM_READ,
                                False, pid)
                        except Exception as e:
                            try:
                                hProcess = OpenProcess(
                                    self.PROCESS_ALL_ACCESS,
                                    False, pid)
                            except Exception as e:
                                print("Exception: " + e.__str__())
                                pass
                        if hProcess:
                            try:
                                path, modules = self.get_process_modules(hProcess)
                                info[path] = modules
                            except Exception as e:
                                print("Exception: " + e.__str__())
                                pass
                        name = basename(path)
                    # yield Process(name, path, pid, modules)
                return info
            finally:
                if prev_state:
                    self.adjust_privilege(prev_state[0])

        def scan_memory(self, function_clamdscan, quarantine_path, action=3):
            prev_state = self.adjust_privilege(SE_DEBUG_NAME)
            try:
                for pid in EnumProcesses():
                    hProcess = None
                    path = ''
                    modules = []
                    if pid == 0:
                        name = 'System Idle Process'
                    elif pid == 4:
                        name = 'System'
                    else:
                        try:
                            hProcess = OpenProcess(
                                self.PROCESS_ALL_ACCESS |
                                PROCESS_VM_READ,
                                False, pid)
                        except Exception as e:
                            try:
                                hProcess = OpenProcess(
                                    self.PROCESS_ALL_ACCESS,
                                    False, pid)
                            except Exception as e:
                                print("Exception: " + e.__str__())
                                pass
                        if hProcess:
                            try:
                                path, modules = self.get_process_modules(hProcess)
                                res = function_clamdscan(path)
                                print(res)
                                if res[path][0] == "FOUND":
                                    TerminateProcess(hProcess, 0)
                                    action_on_infected_file(file=path, result=res, action=action,
                                                            quarantine_path=quarantine_path)
                                for module in modules:
                                    res = function_clamdscan(module)
                                    print(res)
                                    if res[module][0] == "FOUND":
                                        TerminateProcess(hProcess, 0)
                                        action_on_infected_file(file=module, result=res,
                                                                action=action, quarantine_path=quarantine_path)
                                        break
                            except Exception as e:
                                print("Exception: " + e.__str__())
                                pass
                    # yield Process(name, path, pid, modules)
            finally:
                if prev_state:
                    self.adjust_privilege(prev_state[0])

# def process():
#     plist = psutil.process_iter()
#     plist = sorted(plist, key=lambda i: i.name())
#     for i in plist:
#         try:
#             print(i.name(), i.cwd())
#         except psutil.AccessDenied:
#             print ("'%s' Process is not allowing us to view the CPU Usage!" % i.name)


def main():
    wp = WindowsProcesses()
    print(wp.list_all())


if __name__ == "__main__":
    # test any code here
    pass
