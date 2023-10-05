"""
Start activity , to choose option u want to test for
"""
import sys

import uiautomator2 as u2
from logger import Logger
from ScreenLock import ScreenLock
from WallPaper import WallPaper
from EditLauncher import EditLauncher
from RecentApp import RecentApp
from STB import STB
from STBTools import STBTools
from event_generator import EventGen

# step 1 : connect driver
# driver = u2.connect(config.host)
driver = u2.connect()
driver.service("uiautomator").start()
# Step 3 : Create gesture automation flow
event_gen = EventGen()
logger = Logger()


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
    event_gen.generate_event(json_path="./Test_Jason/Test/Test.json", driver=driver)


def run_all(event_gen, logger, driver):
    items = [ScreenLock, WallPaper, EditLauncher, RecentApp, STB]
    for item in items:
        item(event_gen, logger, driver).run_all()


# Step 4 : choose test option
while True:
    for option, test in menu_dict.items():
        print(f"{option}: {test}")
    first_choice = input("Please select action: ").lower()
    match first_choice:
        case "0":
            sys.exit()
        case "1":
            ScreenLock(event_gen, logger, driver).run()
        case "2":
            WallPaper(event_gen, logger, driver).run()
        case "3":
            EditLauncher(event_gen, logger, driver).run()
        case "4":
            RecentApp(event_gen, logger, driver).run()
        case "5":
            STB(event_gen, logger, driver).run()
        case "6":
            STBTools(event_gen, logger, driver).run()
        case "all":
            run_all(event_gen, logger, driver)
        case "test":
            TestJson(driver)
        case _:
            print("Invalid option")
