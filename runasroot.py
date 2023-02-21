"""
runasroot.py :=> this file is used for checking if an exe is running from admin in Windows
"""

import ctypes


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# if is_admin():
#     # Code of your program here
#     os.system("notepad.exe")
# else:
#     # Re-run the program with admin rights
#     ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
