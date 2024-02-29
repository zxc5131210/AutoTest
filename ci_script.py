import logging
import shutil
import subprocess
import os
import glob
from fabric import Connection
from pathlib import Path
import auto_test
import config
import datetime

# setting log
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-2s %(message)s",
    datefmt="%Y%m%d %H:%M:%S",
)

LATEST_FOLDER = "/var/www/html/UI_3.0/Latest"
RELEASE_FOLDER = "/Users/wuia/Desktop/AppiumAutotest/release/"
UPLOAD_PATH = f"/var/www/html/UI_3.0/{datetime.date.today().strftime('%Y%m%d')}"
REPORT_PATH = "/Users/wuia/Desktop/AppiumAutotest/html_report"


def clear_folder(folder_path):
    """clear all data in the folder"""
    files = os.listdir(folder_path)
    for file in files:
        file_path = os.path.join(folder_path, file)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                clear_folder(file_path)
        except Exception as e:
            logging.error(f"delete {file_path} has error: {e}")


def download_remote_folder(remote_path, local_path):
    """Get the list of files in the remote folder"""
    remote_files = subprocess.run(f"ls {remote_path}").stdout.strip().split("\n")
    for remote_file in remote_files:
        if remote_file.endswith(".apk"):
            remote_file_path = f"{remote_path}/{remote_file}"
            local_file_path = f"{local_path}/{remote_file}"
            shutil.copy(remote_file_path, local_file_path)


def upload_folder(local_dir, remote_dir):
    """upload folder to remote"""
    try:
        subprocess.run(f"mkdir -p {remote_dir}")
        for root, dirs, files in os.walk(local_dir):
            for file in files:
                local_path = Path(root) / file
                relative_path = local_path.relative_to(local_dir)
                remote_path = Path(remote_dir) / relative_path
                shutil.copy(str(local_path), str(remote_path))
    except Exception as e:
        logging.error(f"Error uploading folder: {e}")


def install_apk_files(apk_files):
    """install apk files via ADB"""
    subprocess.run(["adb", "disconnect"], check=True)
    subprocess.run(["adb", "connect", config.device_ip], check=True)
    for apk_file in apk_files:
        adb_install_command = f"adb install -r -d '{apk_file}'"
        subprocess.run(adb_install_command, shell=True, check=True)


def uninstall_atx():
    """uninstall atx to make sure uiautomator working"""
    subprocess.run(["adb", "uninstall", "com.github.uiautomator"], check=False)


def reboot_device():
    subprocess.run(["adb", "reboot"], check=True)
    subprocess.run(["adb", "wait-for-device"], check=True)


def check_and_create_folder(folder_path):
    """Check whether the remote folder exists, create it if it does not exist"""
    try:
        subprocess.run(
            ["test", "-d", folder_path],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        print("Folder exists")
    except subprocess.CalledProcessError:
        print("Folder does not exist")
        subprocess.run(["mkdir", "-p", folder_path])


def main_script():
    try:
        # clear release folder
        clear_folder(RELEASE_FOLDER)
        # setup SSH connection
        download_remote_folder(LATEST_FOLDER, RELEASE_FOLDER)
        # Get the list of APK files in the local path
        apk_files = glob.glob(f"{RELEASE_FOLDER}/*.apk")
        # install apk files
        install_apk_files(apk_files)
        # Uninstall the ATX application and rebuild it to ensure that uiautomator2 works properly
        uninstall_atx()
        # Reboot the device to prepare for testing
        reboot_device()
        # Execute all testcases
        auto_test.run_all_test()

        # After running testcases, upload report to remote
        check_and_create_folder(UPLOAD_PATH)
        check_and_create_folder(f"{UPLOAD_PATH}/report")
        # Check if the latest folder exists and create a soft link if it does not exist
        check_and_create_folder(LATEST_FOLDER)
        subprocess.run(f"ln -s {UPLOAD_PATH}/report '{LATEST_FOLDER}'")
        # upload to remote
        upload_folder(REPORT_PATH, f"{UPLOAD_PATH}/report")

    except Exception as e:
        logging.error(f"main script error: {e}")
        raise


if __name__ == "__main__":
    main_script()
