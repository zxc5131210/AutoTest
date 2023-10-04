"""
Start activity , to choose option u want to test for
"""
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


# Test
def TestJson(driver):
    event_gen.generate_event(
        json_path='./Test_Jason/Test/Test.json', driver=driver)


# Step 4 : choose test option
while True:
    print("Main Menu:")
    print("0: Quit")
    print("1: ScreenLock")
    print("2: Wallpaper")
    print("3: Edit Launcher")
    print("4: Recent App")
    print("5: STB")
    print("6: STB Tools")

    first_choice = input("Please select action: ")

    if first_choice == '0':
        exit()
    elif first_choice == '1':
        ScreenLock(event_gen, logger, driver).run()
    elif first_choice == '2':
        WallPaper(event_gen, logger, driver).run()
    elif first_choice == '3':
        EditLauncher(event_gen, logger, driver).run()
    elif first_choice == '4':
        RecentApp(event_gen, logger, driver).run()
    elif first_choice == '5':
        STB(event_gen, logger, driver).run()
    elif first_choice == '6':
        STBTools(event_gen, logger, driver).run()
    elif first_choice.lower() == 'test':
        TestJson(driver)
    else:
        print("Invalid option")
