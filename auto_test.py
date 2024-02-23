import logging
import subprocess
import uiautomator2 as u2

import abstract_reporter
from html_runner import HTMLReporter
from event_generator import EventGen
from folder_processor import FolderProcessor
from locator import locator


def connect_driver():
    """
    Connect to the UI Automator2 driver.
    """
    driver = u2.connect()
    driver.service("uiautomator").start()
    return driver


def setup_logger():
    """
    Configure the logging settings.
    """
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)-2s %(message)s",
        datefmt="%Y%m%d %H:%M:%S",
    )


def get_fw_version():
    """
    Get the firmware version.
    """
    return subprocess.run(
        "adb shell getprop ro.build.fingerprint",
        shell=True,
        capture_output=True,
        text=True,
        check=False,
    ).stdout


def get_app_versions(driver, app_list):
    """
    Get versions of specified apps.
    """
    for app_name, package_name in app_list.items():
        version_info = driver.app_info(package_name)
        version_name = version_info["versionName"]
        abstract_reporter.APP_VERSION.extend([app_name, version_name])


def common_setup(driver):
    # Step 4: Get model name & fw version
    abstract_reporter.MODEL = driver.device_info["model"]
    abstract_reporter.FW_VERSION = get_fw_version()

    # Step 5: Get every app version
    app_list = {
        "vLauncher": locator["vlauncher_package"],
        "SideToolBar": locator["stb_package"],
        "ScreenLock": locator["screen_lock_package"],
        "QuickSettings": locator["quicksettings_package"],
        "WallpaperPicker": locator["wallpaper_package"],
        "Authenticator": locator["authenticator_package"],
    }
    get_app_versions(driver, app_list)
    return abstract_reporter.MODEL, abstract_reporter.FW_VERSION, app_list


def setup_and_run(driver, run_type=""):
    reporter = HTMLReporter()
    event_gen = EventGen(reporter)
    setup_logger()
    common_setup(driver)
    option_file = "option_file"

    if run_type == "all":
        FolderProcessor(event_gen, driver, reporter, option_file).run_all(option_file)
    else:
        FolderProcessor(event_gen, driver, reporter, option_file).run()


def run_all_test():
    driver = connect_driver()
    setup_and_run(driver, run_type="all")


def main():
    driver = connect_driver()
    setup_and_run(driver, run_type="")


if __name__ == "__main__":
    main()
