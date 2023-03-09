"""
config.py :=> On creating setup file, need to change constants, functions, classes, URLs from this file
"""

# ----------------------------------------#
DEBUG_CODE = False  # make false when creating setup files using pyinstaller
IS_CURRENT_WORKING_DIR_IN_PROG_FILES = True  # make true when creating setup files using pyinstaller
STARTING_UPDATE_CLAMAV_DB_FILES = True  # make true when creating setup files using pyinstaller
EXE_SETUP_CLAMAV = not DEBUG_CODE

EGAV_SETUP_ZIP_NAME = "EGCNAVSETUP20X.zip"
EGAV_UPDATE_ZIP_NAME = "EGCNAVUPDATE20X.zip"

CURRENT_VERSION_INFO = "EGCNAV2.1.0.1"  # "EGCNAV2.0.1"
CURRENT_CLAMAV_VERSION_STR = "clamav-1.0.1"  # "clamav-0.105.1"
BASE64CHARS = "SLH#8T5oy4VOUEcjxQX10GmpvIlZDugiAP2dzfq$JBkrY6Wwtnhs%M7FNbe@RCK93a"


# ----------------------------------------#

class EGAVLinks:
    """
    This class contains all required links of EG ClamNet Antivirus
    """

    EGAV_SETUP_ZIP_WIN_LINK = 'https://drive.google.com/uc?export=download&id=1mKnz9lD6ncDPBlfn55bH4b_JOap3tcxW&confirm=t'
    EGAV_SETUP_ZIP_LIN_LINK = 'https://drive.google.com/uc?export=download&id=1GJfS-0msSsPhWPW1nF6fdR5A9XnJbwB0&confirm=t'
    EGAV_SETUP_ZIP_MAC_LINK = ""

    EGAV_UPDATE_ZIP_WIN_LINK = 'https://drive.google.com/uc?export=download&id=1ITXST_4zfx6iq38b0xF-5iwiXaO4LeXl&confirm=t'
    EGAV_UPDATE_ZIP_LIN_LINK = 'https://drive.google.com/uc?export=download&id=1tyQOeM0czYscCn8Xq5L3C47p6IZIdr9K&confirm=t'
    EGAV_UPDATE_ZIP_MAC_LINK = ""

    EGAV_VERSION_LINK = 'https://drive.google.com/uc?export=download&id=1VG64hCQunfJJpRXy-zI065ap53SaCxRi'
    EGAV_FACEBOOK_PAGE_LINK = 'https://www.facebook.com/EGAVF'
    EGAV_TWITTER_PAGE_LINK = 'https://twitter.com/EGAV7'
    EGAV_INSTAGRAM_PAGE_LINK = 'https://www.instagram.com/egclamav/'

    EGAV_WEBSITE_LINK = "http://av.eg1.in/"
    EGAV_RATE_LINK = "https://www.facebook.com/EGAVF/reviews"
    EGAV_SUPPORT_LINK = "http://eg1.in/supportEG1.aspx"
    EG1_WEBSITE_LINK = "http://eg1.in/"


class OtherLinks:
    """
    This class contains all required links except EG ClamNet Antivirus
    """
    CLAMAV_WEBSITE_LINK = "https://www.clamav.net/"
    PYSIDE6_WIKI_LINK = "https://wiki.qt.io/Qt_for_Python"


if __name__ == '__main__':
    # test any code here
    pass
