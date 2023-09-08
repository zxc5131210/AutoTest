'''
Start activity , to choose option u want to test for
'''
import uiautomator2 as u2
import config
from event_generator import EventGen

# step 1 : connect driver
driver = u2.connect(config.host)
driver.implicitly_wait(3)
# Step 3 : Create gesture automation flow
event_gen = EventGen()

# Test


def TestJson(driver):
    event_gen.generate_event(
        json_path='./Test_Jason/Test/Test.json', driver=driver)

# ScreenLock


def screen_lock_ALL(driver):
    event_gen.generate_event(
        json_path='./Test_Jason/ScreenLock/screenLock_all.json', driver=driver)


def screen_lock_setPassword(driver):
    event_gen.generate_event(
        json_path='./Test_Jason/ScreenLock/screenLock_setPassword.json', driver=driver)


def screen_lock_changePassword(driver):
    event_gen.generate_event(
        json_path='./Test_Jason/ScreenLock/screenLock_changePassword.json', driver=driver)


def screen_lock_removePassword(driver):
    event_gen.generate_event(
        json_path='./Test_Jason/ScreenLock/screenLock_removePassword.json', driver=driver)

# wallpaper


def wallpaper_ALL(driver):
    event_gen.generate_event(
        json_path='./Test_Jason/Wallpaper/wallpaper_all.json', driver=driver)


def wallpaper_By_default(driver):
    event_gen.generate_event(
        json_path='./Test_Jason/Wallpaper/wallpaper_By_default.json', driver=driver)


def wallpaper_By_update(driver):
    event_gen.generate_event(
        json_path='./Test_Jason/Wallpaper/wallpaper_By_update.json', driver=driver)

# Edit Launcher


def edit_launcher_all(driver):
    event_gen.generate_event(
        json_path='./Test_Jason/Edit_Launcher/editLauncher_all.json', driver=driver)


def edit_launcher_add_app(driver):
    event_gen.generate_event(
        json_path='./Test_Jason/Edit_Launcher/editLauncher_add_delete_re-rangeApps.json', driver=driver)


def edit_launcher_find_all(driver):
    event_gen.generate_event(
        json_path='./Test_Jason/Edit_Launcher/editLauncher_find_apps_in_All.json', driver=driver)

# recent App


def recent_app_all(driver):
    event_gen.generate_event(
        json_path='./Test_Jason/recentApp/recentApp_all.json', driver=driver)


def recent_app_clear_app(driver):
    event_gen.generate_event(
        json_path='./Test_Jason/recentApp/recentApp_clear_app.json', driver=driver)


def recent_app_clear_all_btn(driver):
    event_gen.generate_event(
        json_path='./Test_Jason/recentApp/recentApp_clear_all.json', driver=driver)

# def menu


def screen_lock_menu(driver):
    while True:
        print("ScreenLock Options:")
        print("1: Set Password")
        print("2: Change Password")
        print("3: Remove Password")
        print("4: ALL")
        print("0: Back to main menu")

        choice = input("Enter your choice: ")

        if choice == '0':
            return
        elif choice == '1':
            screen_lock_setPassword(driver)
        elif choice == '2':
            screen_lock_changePassword(driver)
        elif choice == '3':
            screen_lock_removePassword(driver)
        elif choice == '4':
            screen_lock_ALL(driver)
        else:
            print("Invalid option")


def wallpaper_menu(driver):
    while True:
        print("Wallpaper Options:")
        print("1: Change By_default")
        print("2: Change By_update")
        print("3: ALL")
        print("0: Back to main menu")

        choice = input("Enter your choice: ")

        if choice == '0':
            return
        elif choice == '1':
            wallpaper_By_default(driver)
        elif choice == '2':
            wallpaper_By_update(driver)
        elif choice == '3':
            wallpaper_ALL(driver)
        else:
            print("Invalid option")


def edit_launcher_menu(driver):
    while True:
        print("Edit Launcher Options:")
        print("1: Add_delete_re-range app on hot seat")
        print("2:install Testapp and find in all apps")
        print("3: ALL")
        print("0: Back to main menu")

        choice = input("Enter your choice: ")

        if choice == '0':
            return
        elif choice == '1':
            edit_launcher_add_app(driver)
        elif choice == '2':
            edit_launcher_find_all(driver)
        elif choice == '3':
            edit_launcher_all(driver)
        else:
            print("Invalid option")


def recent_app_menu(driver):
    while True:
        print("Recent App Options:")
        print("1:clear app")
        print("2:clear all button")
        print("3: ALL")
        print("0: Back to main menu")

        choice = input("Enter your choice: ")

        if choice == '0':
            return
        elif choice == '1':
            recent_app_clear_app(driver)
        elif choice == '2':
            recent_app_clear_all_btn(driver)
        elif choice == '3':
            recent_app_all(driver)
        else:
            print("Invalid option")
# Add more functions for Edit Launcher and Recent App menus similarly


while True:
    print("Main Menu:")
    print("1: ScreenLock")
    print("2: Wallpaper")
    print("3: Edit Launcher")
    print("4: Recent App")
    print("0: Quit")

    first_choice = input("Please select action: ")

    if first_choice == '0':
        # Step 4 : quit driver
        driver.service('uiautomator').stop()
        exit()
    elif first_choice == '1':
        screen_lock_menu(driver)
    elif first_choice == '2':
        wallpaper_menu(driver)
    elif first_choice == '3':
        edit_launcher_menu(driver)
    elif first_choice == '4':
        recent_app_menu(driver)
    elif first_choice.lower() == 'test':
        TestJson(driver)
    else:
        print("Invalid option")
