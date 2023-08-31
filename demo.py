'''This is a demo test for gesture automation.'''
from appium import webdriver
import config
from event_generator import EventGen

# Step 1 : Create Desired Capabilities
desired_caps = {}
desired_caps['platformName'] = config.platformName
desired_caps['platformVersion'] = config.platformVersion
desired_caps['deviceName'] = config.deviceName

# Step 2 : Create Driver object
driver = webdriver.Remote(
    f'http://{config.host}:{config.port}/wd/hub', desired_caps)

# Step 3 : Create gesture automation flow
event_gen = EventGen()
# ScreenLock


def screen_lock_ALL(driver):
    event_gen.generate_event(
        json_path='./Test_Jason/ScreenLock/screenLock_all.json', driver=driver
    )


def screen_lock_setPassword(driver):
    event_gen.generate_event(
        json_path='./Test_Jason/ScreenLock/screenLock_setPassword.json', driver=driver
    )


def screen_lock_changePassword(driver):
    event_gen.generate_event(
        json_path='./Test_Jason/ScreenLock/screenLock_changePassword.json', driver=driver
    )


def screen_lock_removePassword(driver):
    event_gen.generate_event(
        json_path='./Test_Jason/ScreenLock/screenLock_removePassword.json', driver=driver
    )

# wallpaper


def wallpaper_ALL(driver):
    event_gen.generate_event(
        json_path='./Test_Jason/Wallpaper/wallpaper_all.json', driver=driver
    )


def wallpaper_Bydefault(driver):
    event_gen.generate_event(
        json_path='./Test_Jason/Wallpaper/wallpaper_Bydefault.json', driver=driver
    )


def wallpaper_Byupdate(driver):
    event_gen.generate_event(
        json_path='./Test_Jason/Wallpaper/wallpaper_Byupdate.json', driver=driver
    )


# first choice
first_choice = input("請選擇操作(1: ScreenLock 2: Wallpaper):")
if first_choice == '1':
    # second choice
    second_choice = input(
        "請選擇操作(1 : Set Password 2 : Change Password 3 : Remove Password,ALL):").split(',')
    for choices in second_choice:
        if choices.lower() == 'all':
            screen_lock_ALL(driver)

        elif choices == '1':
            screen_lock_setPassword(driver)

        elif choices == '2':
            screen_lock_changePassword(driver)

        elif choices == '3':
            screen_lock_removePassword(driver)

        else:
            print(f"無效的選項：{choices}")

elif first_choice == '2':
    second_choice = input(
        "請選擇操作(1 : Change Bydefault 2 : Change Byupdate ,ALL):").split(',')
    for choices in second_choice:
        if choices.lower() == 'all':
            wallpaper_ALL(driver)

        elif choices == '1':
            wallpaper_Bydefault(driver)

        elif choices == '2':
            wallpaper_Byupdate(driver)

        else:
            print(f"無效的選項：{choices}")

else:
    print("無效的選項")


# Step 4 : quit driver
driver.quit()
