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

# def marker


def STB_marker_all(driver):
    STB_marker_selector(driver)
    STB_marker_pen(driver)
    STB_marker_highlighter(driver)
    STB_marker_eraser(driver)
    STB_marker_undo_redo(driver)
    STB_marker_delete(driver)
    STB_marker_save(driver)
    STB_marker_close(driver)
    STB_marker_moving(driver)


def STB_marker_selector(driver):
    logger.Test('STB marker-selector')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/Tools/Marker/STB_marker_selector.json', driver=driver)


def STB_marker_pen(driver):
    logger.Test('STB marker-pen')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/Tools/Marker/STB_marker_pen.json', driver=driver)


def STB_marker_highlighter(driver):
    logger.Test('STB marker-highlighter')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/Tools/Marker/STB_marker_highlighter.json', driver=driver)


def STB_marker_eraser(driver):
    logger.Test('STB marker-eraser')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/Tools/Marker/STB_marker_eraser.json', driver=driver)


def STB_marker_undo_redo(driver):
    logger.Test('STB marker-undo & redo')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/Tools/Marker/STB_marker_undo_redo.json', driver=driver)


def STB_marker_delete(driver):
    logger.Test('STB marker-delete')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/Tools/Marker/STB_marker_delete.json', driver=driver)


def STB_marker_save(driver):
    logger.Test('STB marker-save')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/Tools/Marker/STB_marker_save.json', driver=driver)


def STB_marker_close(driver):
    logger.Test('STB marker-close')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/Tools/Marker/STB_marker_close.json', driver=driver)


def STB_marker_moving(driver):
    logger.Test('STB marker-moving')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/Tools/Marker/STB_marker_moving.json', driver=driver)


# def menu

def marker_menu(driver):
    while True:
        print("Spotlight Options:")
        print("0: Back to main menu")
        print("1: selector")
        print("2: pen")
        print("3: highlighter")
        print("4: eraser")
        print("5: undo & redo")
        print("6: delete")
        print("7: save")
        print("8: close")
        print("9: moving")
        print("ALL")

        choice = input("Enter your choice: ")

        if choice == '0':
            return
        elif choice == '1':
            STB_marker_selector(driver)
        elif choice == '2':
            STB_marker_pen(driver)
        elif choice == '3':
            STB_marker_highlighter(driver)
        elif choice == '4':
            STB_marker_eraser(driver)
        elif choice == '5':
            STB_marker_undo_redo(driver)
        elif choice == '6':
            STB_marker_delete(driver)
        elif choice == '7':
            STB_marker_save(driver)
        elif choice == '8':
            STB_marker_close(driver)
        elif choice == '9':
            STB_marker_moving(driver)
        elif choice.lower() == 'all':
            STB_marker_all(driver)
        else:
            print("Invalid option")


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
