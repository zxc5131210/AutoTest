"""
Start activity , to choose option u want to test for
"""
import logging
import subprocess
import uiautomator2 as u2
import abstract_reporter
from locator import locator
from html_runner import HTMLReporter
from option_file.ScreenLock.option import ScreenLock
from option_file.Wallpaper.option import WallPaper
from option_file.STB.option import STB
from option_file.vLauncher.option import vLauncher
from option_file.Quicksettings.option import Quicksettings
from option_file.Authenticator.option import Authenticator
from event_generator import EventGen


class Application:
    def __init__(self, description, application):
        self.description = description
        self.application = application


class AutoTest:
    option_menu = "Exit auto test"
    option_all = "All Test"
    apps = [
        Application("ScreenLock", ScreenLock),
        Application("Wallpaper", WallPaper),
        Application("vLauncher", vLauncher),
        Application("STB", STB),
        Application("Quicksettings", Quicksettings),
        Application("Authenticator", Authenticator),
    ]

    def run_all(self):
        for test_case in self.apps:
            test_case.application(event_gen, driver, reporter).run_all()

    @staticmethod
    def run(application):
        application.application(event_gen, driver, reporter).run_with_interaction()

    def print_option(self):
        print(f"-1 : {self.option_menu}")
        for i in range(len(self.apps)):
            print(f"{i} : {self.apps[i].description}")
        print(f"{len(self.apps)} : {self.option_all}")

    def invalid(self, choice_int) -> bool:
        """
        check range in -1~len
           1. < -1
           2. > len
        """
        return choice_int < -1 or choice_int > len(self.apps)

    def run_with_interaction(self):
        while True:
            self.print_option()
            choice = input("Enter your choice: ").lower()
            try:
                choice_int = int(choice)
                if self.invalid(choice_int):
                    raise ValueError
                if choice_int == -1:
                    exit()
                if choice_int == len(self.apps):
                    self.run_all()
                    continue
                self.run(self.apps[choice_int])
            except ValueError:
                print(
                    "Invalid input. Please enter a valid choice, range is between -1 ~ length of apps."
                )


if __name__ == "__main__":
    # step 1 : connect driver
    # driver = u2.connect(config.host)
    driver = u2.connect()
    driver.service("uiautomator").start()
    # Step 2 : choose report type
    reporter = HTMLReporter()
    event_gen = EventGen(reporter)
    # Step 3 : log config
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)-2s %(message)s",
        datefmt="%Y%m%d %H:%M:%S",
    )
    # Step 4 : Get model name & fw version
    abstract_reporter.MODEL = driver.device_info["model"]
    abstract_reporter.FW_VERSION = subprocess.run(
        "adb shell getprop ro.build.fingerprint",
        shell=True,
        capture_output=True,
        text=True,
    ).stdout
    # Step 5 : Get every app version
    app_list = {
        "vLauncher": locator["vlauncher_package"],
        "SideToolBar": locator["STB_package"],
        "ScreenLock": locator["screen_lock_package"],
        "QuickSettings": locator["quicksettings_package"],
        "WallpaperPicker": locator["wallpaper_package"],
        "Authenticator": locator["authenticator_package"],
    }
    for app_name, package_name in app_list.items():
        version_info = driver.app_info(package_name)
        version_name = version_info["versionName"]
        abstract_reporter.APP_VERSION.append(app_name)
        abstract_reporter.APP_VERSION.append(version_name)

    AutoTest().run_with_interaction()
