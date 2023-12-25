"""
Start activity , to choose option u want to test for
"""
import logging
import subprocess
import uiautomator2 as u2
import abstract_reporter
from folder_processor import FolderProcessor
from locator import locator
from html_runner import HTMLReporter
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
    check=False,
).stdout
# Step 5 : Get every app version
app_list = {
    "vLauncher": locator["vlauncher_package"],
    "SideToolBar": locator["stb_package"],
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

option_file = "option_file"
FolderProcessor(event_gen, driver, reporter, option_file).run()
