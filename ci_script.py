import logging
import subprocess
import os
import glob  # 添加這一行
from fabric import Connection
from pathlib import Path
import auto_test
import config
import datetime

# 設定日誌紀錄
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-2s %(message)s",
    datefmt="%Y%m%d %H:%M:%S",
)

# 常數
REMOTE_LATEST_FOLDER = "/var/www/html/UI_3.0/Latest"
LOCAL_RELEASE_PATH = "/Users/wuia/Desktop/AppiumAutotest/release/"
REMOTE_UPLOAD_PATH = f"/var/www/html/UI_3.0/{datetime.date.today().strftime('%Y%m%d')}"
LOCAL_REPORT_PATH = "/Users/wuia/Desktop/AppiumAutotest/html_report"


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


def download_remote_folder(connection, remote_path, local_path):
    """Get the list of files in the remote folder"""
    remote_files = connection.run(f"ls {remote_path}").stdout.strip().split("\n")
    for remote_file in remote_files:
        if remote_file.endswith(".apk"):
            remote_file_path = f"{remote_path}/{remote_file}"
            local_file_path = f"{local_path}/{remote_file}"
            connection.get(remote_file_path, local_file_path)


def upload_folder(connect, local_dir, remote_dir):
    """upload folder to remote"""
    try:
        connect.run(f"mkdir -p {remote_dir}")
        for root, dirs, files in os.walk(local_dir):
            for file in files:
                local_path = Path(root) / file
                relative_path = local_path.relative_to(local_dir)
                remote_path = Path(remote_dir) / relative_path
                connect.put(str(local_path), str(remote_path))
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


def check_and_create_folder(connection, folder_path):
    """檢查遠端資料夾是否存在，不存在則創建"""
    try:
        check_folder_exists = connection.run(
            f"test -d {folder_path} && echo 'Folder exists' || echo 'Folder does not exist'",
            hide=True,
        )
        if "Folder does not exist" in check_folder_exists.stdout:
            connection.run(f"mkdir -p {folder_path}")
    except Exception as e:
        logging.error(f"檢查並創建資料夾時發生錯誤: {e}")


def main_script():
    try:
        # clear release folder
        clear_folder(LOCAL_RELEASE_PATH)
        # setup SSH connection
        with Connection(
            host=config.hostname,
            user=config.username,
            connect_kwargs={"password": config.password},
        ) as c:
            download_remote_folder(c, REMOTE_LATEST_FOLDER, LOCAL_RELEASE_PATH)
        # Get the list of APK files in the local path
        apk_files = glob.glob(f"{LOCAL_RELEASE_PATH}/*.apk")
        # install apk files
        install_apk_files(apk_files)
        # Uninstall the ATX application and rebuild it to ensure that uiautomator2 works properly
        uninstall_atx()
        # Reboot the device to prepare for testing
        reboot_device()
        # Execute all testcases
        auto_test.run_all_test()

        # After running testcases, upload report to remote
        check_and_create_folder(c, REMOTE_UPLOAD_PATH)
        check_and_create_folder(c, f"{REMOTE_UPLOAD_PATH}/report")
        # Check if the latest folder exists and create a soft link if it does not exist
        check_and_create_folder(c, REMOTE_LATEST_FOLDER)
        c.run(f"ln -s {REMOTE_UPLOAD_PATH}/report '{REMOTE_LATEST_FOLDER}'")
        # upload to remote
        upload_folder(c, LOCAL_REPORT_PATH, f"{REMOTE_UPLOAD_PATH}/report")

    except Exception as e:
        logging.error(f"main script error: {e}")
        raise


if __name__ == "__main__":
    main_script()
