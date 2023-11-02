"""
Start activity , to choose option u want to test for
"""
import logging
import sys
import subprocess
import uiautomator2 as u2
from html_runner import HTMLReporter
from option_file.ScreenLock.option import ScreenLock
from option_file.vLauncher.Wallpaper.option import WallPaper
from option_file.vLauncher.Edit_Launcher.option import EditLauncher
from option_file.vLauncher.recent_app.option import RecentApp
from option_file.STB.option import STB
from option_file.STB.Tools.option import STBTools
from event_generator import EventGen

# step 1 : connect driver
# driver = u2.connect(config.host)
driver = u2.connect()
driver.service("uiautomator").start()
# Step 3 : Create gesture automation flow and log
event_gen = EventGen()
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-2s %(message)s",
    datefmt="%Y%m%d %H:%M:%S",
)


menu_dict = {
    "0": "Quit",
    "1": "ScreenLock",
    "2": "Wallpaper",
    "3": "Edit Launcher",
    "4": "Recent App",
    "5": "STB",
    "6": "STB Tools",
    "all": "all test",
}


# Test
def TestJson(driver):
    event_gen.generate_event(json_path="option_file/Test/Test.json", driver=driver)


def run_all(event_gen, logger, driver):
    items = [ScreenLock, WallPaper, EditLauncher, STB]
    for item in items:
        item(event_gen, logger, driver).run_all()


# Step 6 : choose test option
while True:
    for option, test in menu_dict.items():
        print(f"{option}: {test}")
    first_choice = input("Please select action: ").lower()
    match first_choice:
        case "0":
            sys.exit()
        case "1":
            ScreenLock(event_gen, driver, HTMLReporter()).run()
        case "2":
            WallPaper(event_gen, driver, HTMLReporter()).run()
        case "3":
            EditLauncher(event_gen, driver, HTMLReporter()).run()
        case "4":
            RecentApp(event_gen, driver, HTMLReporter()).run()
        case "5":
            STB(event_gen, driver, HTMLReporter()).run()
        case "6":
            STBTools(event_gen, driver, HTMLReporter()).run()
        case "all":
            run_all(event_gen, driver, HTMLReporter())
        case "test":
            TestJson(driver)
        case _:
            print("Invalid option")
