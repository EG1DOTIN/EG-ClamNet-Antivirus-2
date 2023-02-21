"""
ClamdScanner.py :=> This file provides command line for scanning files/folders with ClamAV (clamd)
"""

import sys


def show_help(error=0):
    help_text = """clamdscanner commandline help""" + "\n" + \
                """clamdscanner [-v, --version] shows version of ClamAV """ + "\n" + \
                """clamdscanner [-h, --help] shows help""" + "\n" + \
                """clamdscanner [-a,--action] [-m, --memory] (works in Windows OS and if clamd service running) """ + \
                """clamdscanner [-a,--action] [-p, --path]* comma separated files/folders paths to scan\n""" + \
                """clamdscanner [-a,--action] [-P, --Paths] space separated files/folders paths to scan \n""" + \
                """ *work only if clamd service is running (clamd.exe is running)\n""" + \
                """action can be 1,2 or 3. 1 denotes Report only, 2 -> Remove, 3 -> Quarantined.\n""" + \
                """Example:  clamdscanner -a 3 -p \"D://sample_folder\" \n""" + \
                """          clamdscanner -a 2 -m \n""" + \
                """          clamdscanner --action 3 --path  \"D://sample_folder\" \n"""

    error_text = "invalid arguments passed."
    if not error:
        print(help_text)
    else:
        print(error_text)


def main():
    from subprocess import run as subprocess_run
    from singleObj import clamav_service, clamav_commands
    # total arguments
    n = len(sys.argv)
    if n < 2:
        show_help()
    else:
        try:
            if clamav_service.isOK():
                if n == 2:
                    if sys.argv[1] in ['-v', '--version']:
                        print(clamav_service.version)
                    elif sys.argv[1] in ['-h', '--help']:
                        show_help()
                    else:
                        show_help()
                elif n > 3:
                    if sys.argv[3] in ['-p', '--path']:
                        if sys.argv[1] in ['-a', '--action']:
                            separated_files_folders_paths_str = ",".join(sys.argv[4:len(sys.argv)])
                            action = int(sys.argv[2])
                            clamav_service.scan_multiple_files_folders(
                                separated_files_folders_paths_str=separated_files_folders_paths_str,
                                separator=",", cmd='SCAN', action=action)
                        else:
                            show_help()
                    elif sys.argv[3] in ['-m', '--memory']:
                        if sys.argv[1] in ['-a', '--action']:
                            from custom import OS
                            if OS.get_os_details() == OS.WINDOWS:
                                clamav_service.scan_memory(action=int(sys.argv[2]))
                            else:
                                print("memory scan is available only for Windows")
                        else:
                            show_help()
                    elif sys.argv[3] in ['-P', '--Paths']:
                        if sys.argv[1] in ['-a', '--action']:
                            cmd_scan = clamav_commands.get_scan_cmd()
                            if cmd_scan is not None:
                                cmd_scan += " ".join(sys.argv[4:len(sys.argv)])
                                subprocess_run(cmd_scan, shell=True)
                        else:
                            show_help()
                    else:
                        show_help()
                else:
                    show_help()
            else:
                # print("Running scan from clamav executables...")
                # print(cmd_scan)
                if sys.argv[1] in ['-v', '--version']:
                    cmd_scan = clamav_commands.clamscan_exe + " -V"
                    subprocess_run(cmd_scan.split(" "))
                elif sys.argv[1] in ['-h', '--help']:
                    show_help()
                elif sys.argv[3] in ['-P', '--Paths']:
                    if sys.argv[1] in ['-a', '--action']:
                        cmd_scan = clamav_commands.get_scan_cmd()
                        if cmd_scan is not None:
                            cmd_scan += " ".join(sys.argv[4:len(sys.argv)])
                            subprocess_run(cmd_scan, shell=True)
                        else:
                            print("unknown error")
                    else:
                        show_help()
                else:
                    show_help()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
    pass
