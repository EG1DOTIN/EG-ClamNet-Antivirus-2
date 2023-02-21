"""
EGAVDownloader.py :=> this file is used for downloading EG ClamNet Antivirus content from remote server
"""
from os import path
from time import sleep
from zipfile import ZipFile
from gdown import download as gdown_download
from requests import get as requests_get
from EGAVResources import QuickScanPaths, EGAVPaths
from config import EGAVLinks, EGAV_SETUP_ZIP_NAME, EGAV_UPDATE_ZIP_NAME
from custom import OS, path_correction


def download_clamav_files(download_url, download_folder):
    chunk_size = 8192
    current_progress = 0
    total_approx_size = 10 * 1024 * 1024
    local_filename = download_url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests_get(download_url, stream=True, headers={'User-Agent': 'Mozilla/5.0'}) as r:
        r.raise_for_status()
        download_file_fullpath = download_folder + "/" + local_filename
        with open(download_file_fullpath, 'wb') as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                current_progress += chunk_size
                print("Downloading completed " + str(int(current_progress * 100 / total_approx_size)) + "% ...")
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                # if chunk:
                f.write(chunk)
    return local_filename


def download_egav_files(download_url, download_folder):
    chunk_size = 8192
    current_progress = 0
    total_approx_size = 8 * 1024 * 1024 * 171
    # NOTE the stream=True parameter below
    with requests_get(download_url, stream=True, headers={'User-Agent': 'Mozilla/5.0'}) as r:
        r.raise_for_status()
        download_file_fullpath = path.join(download_folder, EGAV_SETUP_ZIP_NAME)
        download_file_fullpath = path_correction(download_file_fullpath)
        with open(download_file_fullpath, 'wb') as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                current_progress += chunk_size
                print("Downloading completed " + str(int(current_progress * 100 / total_approx_size)) + "% ...")
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                # if chunk:
                f.write(chunk)
    return


def downloadEGAVFilesNExtract(egav_update=False):
    print("Downloading EGAV files...")
    if not egav_update:
        download_link = EGAVLinks.EGAV_SETUP_ZIP_WIN_LINK
        if OS.Windows():
            download_link = EGAVLinks.EGAV_SETUP_ZIP_WIN_LINK
        elif OS.Linux():
            download_link = EGAVLinks.EGAV_SETUP_ZIP_LIN_LINK
        elif OS.OSX():
            download_link = EGAVLinks.EGAV_SETUP_ZIP_MAC_LINK
        download_folder = QuickScanPaths.DOWNLOAD_FOLDER
        path_zip_file = path.join(download_folder, EGAV_SETUP_ZIP_NAME)
    else:
        download_link = EGAVLinks.EGAV_UPDATE_ZIP_WIN_LINK
        if OS.Windows():
            download_link = EGAVLinks.EGAV_UPDATE_ZIP_WIN_LINK
        elif OS.Linux():
            download_link = EGAVLinks.EGAV_UPDATE_ZIP_LIN_LINK
        elif OS.OSX():
            download_link = EGAVLinks.EGAV_UPDATE_ZIP_MAC_LINK
        download_folder = QuickScanPaths.DOWNLOAD_FOLDER
        path_zip_file = path.join(download_folder, EGAV_UPDATE_ZIP_NAME)

    gdown_download(download_link, path_zip_file, quiet=False)
    print("Extracting EGAV Zip files...")
    with ZipFile(path_zip_file) as zip_ref:
        zip_ref.extractall(EGAVPaths.InstallationPath)
    print("Extracting -> Done")
    sleep(0.5)


if __name__ == '__main__':
    import sys

    if sys.argv[1] == "--setup":
        downloadEGAVFilesNExtract(egav_update=False)
    elif sys.argv[1] == "--update":
        downloadEGAVFilesNExtract(egav_update=True)
    else:
        print("Error: invalid args.")
