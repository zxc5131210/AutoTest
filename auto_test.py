"""
Start activity , to choose option u want to test for
"""
import logging
import sys
import subprocess
import uiautomator2 as u2
import abstract_reporter
from html_runner import HTMLReporter
from option_file.ScreenLock.option import ScreenLock
from option_file.vLauncher.Wallpaper.option import WallPaper
from option_file.vLauncher.Edit_Launcher.option import EditLauncher
from option_file.vLauncher.recent_app.option import RecentApp
from option_file.STB.option import STB
from option_file.vLauncher.option import vLauncher
from option_file.STB.Tools.option import STBTools
from event_generator import EventGen

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
    "vlauncher": "com.viewsonic.vlauncher",
    "STB": "com.viewsonic.sidetoolbar",
    "screenlock": "com.viewsonic.screenlock",
    "quicksettings": "com.viewsonic.quicksettings",
    "wallpaper": "com.viewsonic.wallpaperpicker",
    "authenticator": "com.viewsonic.authenticator",
}
for app_name, package_name in app_list.items():
    version_info = driver.app_info(package_name)
    version_name = version_info["versionName"]
    abstract_reporter.APP_VERSION.append(app_name)
    abstract_reporter.APP_VERSION.append(version_name)


menu_dict = {
    "0": "Quit",
    "1": "ScreenLock",
    "2": "Wallpaper",
    "3": "vLauncher",
    "4": "STB",
    "5": "STB Tools",
    "all": "all test",
}


# Test
def TestJson(driver):
    event_gen.generate_event(json_path="option_file/Test/Test.json", driver=driver)


def run_all(event_gen, driver, reporter):
    items = [ScreenLock, WallPaper, vLauncher, STB]
    for item in items:
        item(event_gen, driver, reporter).run_all()


# Step 6 : choose test option
while True:
    for option, test in menu_dict.items():
        print(f"{option}: {test}")
    first_choice = input("Please select action: ").lower()
    match first_choice:
        case "0":
            sys.exit()
        case "1":
            ScreenLock(event_gen, driver, reporter).run()
        case "2":
            WallPaper(event_gen, driver, reporter).run()
        case "3":
            vLauncher(event_gen, driver, reporter).run()
        case "4":
            STB(event_gen, driver, reporter).run()
        case "5":
            STBTools(event_gen, driver, reporter).run()
        case "6":
            pass
        case "7":
            pass
        case "all":
            run_all(event_gen, driver, reporter)
        case "test":
            TestJson(driver)
        case _:
            print("Invalid option")
