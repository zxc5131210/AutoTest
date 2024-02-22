import glob
import subprocess
import os
from fabric import Connection
from pathlib import Path
import auto_test
import config


def clear_folder(folder_path):
    # get all data in the folder
    files = os.listdir(folder_path)

    # delete every data
    for file in files:
        file_path = os.path.join(folder_path, file)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                # if the data is folder，recursive delete all data
                clear_folder(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")


def download_remote_folder(connection, remote_path, local_path):
    # Get the list of files in the remote folder
    remote_files = connection.run(f"ls {remote_path}").stdout.strip().split("\n")

    # Recursively download each file
    for remote_file in remote_files:
        if remote_file.endswith(".apk"):
            remote_file_path = f"{remote_path}/{remote_file}"
            local_file_path = f"{local_path}/{remote_file}"
            connection.get(remote_file_path, local_file_path)


def upload_folder(connect, local_dir, remote_dir):
    try:
        # Make sure the remote directory exists
        connect.run(f'mkdir -p {remote_dir}')
        for root, dirs, files in os.walk(local_dir):
            for file in files:
                local_path = Path(root) / file
                # count path
                relative_path = local_path.relative_to(local_dir)
                remote_path = Path(remote_dir) / relative_path
                # upload report
                connect.put(str(local_path), str(remote_path))
    except Exception as e:
        print(f"Error uploading folder: {e}")


def install_apk_files(apk_files):
    # Connect to the target device via ADB

    subprocess.run(f"adb disconnect", shell=True)
    subprocess.run(f"adb connect {config.device_ip}", shell=True)

    # Install each APK file using ADB
    for apk_file in apk_files:
        adb_install_command = f"adb install -r -d '{apk_file}'"
        subprocess.run(adb_install_command, shell=True)


def uninstall_atx():
    subprocess.run(["adb", "uninstall", "com.github.uiautomator"], check=False)


def reboot_device():
    subprocess.run(["adb", "reboot"], check=True)
    subprocess.run(["adb", "wait-for-device"], check=True)


def main_script():
    # clear release folder
    clear_folder("release")
    # Establish SSH connection
    with Connection(host=config.hostname, user=config.username, connect_kwargs={"password": config.password}) as c:
        # Specify remote file path and local target path
        remote_folder_path = "/var/www/html/UI_3.0/Latest"
        local_target_path = "/Users/wuia/Desktop/AppiumAutotest/release/"
        download_remote_folder(c, remote_folder_path, local_target_path)

    # Get a list of APK files in the local target path
    apk_files = glob.glob(f"{local_target_path}/*.apk")
    # Install APK files on the target device using ADB
    install_apk_files(apk_files)
    # uninstall atx and rebuild to make sure uiautomator2 working
    uninstall_atx()
    # reboot to prepare testing
    reboot_device()
    # run all testcases
    auto_test.run_all_test()

    # upload html report to remote
    with Connection(host=config.hostname, user=config.username, connect_kwargs={"password": config.password}) as c:
        # Specify remote file path and local target path
        upload_path = "/var/www/html/UI_3.0/Latest/report"
        report_path = "/Users/wuia/Desktop/AppiumAutotest/html_report"
        upload_folder(c, report_path, upload_path)


if __name__ == "__main__":
    main_script()
