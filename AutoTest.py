'''
Start activity , to choose option u want to test for
'''
from logger import Logger
import uiautomator2 as u2
import config
from event_generator import EventGen

# step 1 : connect driver
# driver = u2.connect(config.host)
driver = u2.connect()
driver.uiautomator.start()
driver.implicitly_wait(3)
# Step 3 : Create gesture automation flow
event_gen = EventGen()
logger = Logger()
# Test


def TestJson(driver):
    event_gen.generate_event(
        json_path='./Test_Jason/Test/Test.json', driver=driver)


# vLauncher_wallpaper


def wallpaper_ALL(driver):
    event_gen.generate_event(
        json_path='./Test_Jason/vLauncher/Wallpaper/wallpaper_all.json', driver=driver)


def wallpaper_By_default(driver):
    logger.Test('Change By_default')
    event_gen.generate_event(
        json_path='./Test_Jason/vLauncher/Wallpaper/wallpaper_By_default.json', driver=driver)


def wallpaper_By_update(driver):
    logger.Test('Change By_update')
    event_gen.generate_event(
        json_path='./Test_Jason/vLauncher/Wallpaper/wallpaper_By_update.json', driver=driver)

# vLauncher_Edit Launcher


def edit_launcher_all(driver):
    event_gen.generate_event(
        json_path='./Test_Jason/vLauncher/Edit_Launcher/editLauncher_all.json', driver=driver)


def edit_launcher_add_app(driver):
    logger.Test('Add_delete_re-range app on hot seat')
    event_gen.generate_event(
        json_path='./Test_Jason/vLauncher/Edit_Launcher/editLauncher_add_delete_re-rangeApps.json', driver=driver)


def edit_launcher_find_all(driver):
    logger.Test('install Testapp and find in all apps')
    event_gen.generate_event(
        json_path='./Test_Jason/vLauncher/Edit_Launcher/editLauncher_find_apps_in_All.json', driver=driver)

# vLauncher_recent App


def recent_app_all(driver):
    logger.Test('recent-All')
    event_gen.generate_event(
        json_path='./Test_Jason/vLauncher/recentApp/recentApp_all.json', driver=driver)


def recent_app_clear_app(driver):
    logger.Test('recent-clear app')
    event_gen.generate_event(
        json_path='./Test_Jason/vLauncher/recentApp/recentApp_clear_app.json', driver=driver)


def recent_app_clear_all_btn(driver):
    logger.Test('recent-clear all button')
    event_gen.generate_event(
        json_path='./Test_Jason/vLauncher/recentApp/recentApp_clear_all.json', driver=driver)

# STB_ALL


def STB_all(driver):
    # STB root_view
    STB_back_btn(driver)
    STB_homepage_btn(driver)
    recent_app_all(driver)
    STB_element_in_all_apps(driver)
    STB_apps_add_delete_app_in_shortcut(driver)
    STB_apps_order_in_shortcut(driver)
    STB_tools_add_delete_app_in_shortcut(driver)
    STB_tools_order_in_shortcut(driver)
    # STB Tools
    STB_freezer_all(driver)
    STB_spotlight_all(driver)
    STB_stopwatch_all(driver)
    STB_timer_all(driver)

# STB_first class


def STB_back_btn(driver):
    logger.Test('STB-back button')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/FirstClass/STB_back_button.json', driver=driver)


def STB_homepage_btn(driver):
    logger.Test('STB-homepage button')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/FirstClass/STB_homepage_button.json', driver=driver)

# STB_Second class


def STB_element_in_all_apps(driver):
    logger.Test('STB_apps-element in all apps')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/SecondClass/STB_app_show_in_all_apps.json', driver=driver)


def STB_apps_add_delete_app_in_shortcut(driver):
    logger.Test('STB_apps-add & delete apps in shortcut')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/SecondClass/STB_add_delete_app_shortcut.json', driver=driver)


def STB_apps_order_in_shortcut(driver):
    logger.Test('STB_apps-app order in shortcut')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/SecondClass/STB_app_order_in_shortcut.json', driver=driver)

# STB_Third class


def STB_tools_add_delete_app_in_shortcut(driver):
    logger.Test('STB_tools-add & delete apps in shortcut')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/ThirdClass/STB_add_delete_app_shortcut.json', driver=driver)


def STB_tools_order_in_shortcut(driver):
    logger.Test('STB_tools-app order in shortcut')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/ThirdClass/STB_app_order_in_shortcut.json', driver=driver)

# STB_ScreenLock


def screen_lock_ALL(driver):
    event_gen.generate_event(
        json_path='./Test_Jason/ScreenLock/screenLock_all.json', driver=driver)


def screen_lock_setPassword(driver):
    logger.Test('Set Password')
    event_gen.generate_event(
        json_path='./Test_Jason/ScreenLock/screenLock_setPassword.json', driver=driver)


def screen_lock_changePassword(driver):
    logger.Test('Change Password')
    event_gen.generate_event(
        json_path='./Test_Jason/ScreenLock/screenLock_changePassword.json', driver=driver)


def screen_lock_removePassword(driver):
    logger.Test('Remove Password')
    event_gen.generate_event(
        json_path='./Test_Jason/ScreenLock/screenLock_removePassword.json', driver=driver)

# def STB tools
# def Freezer


def STB_freezer_all(driver):
    STB_freezer_reboot_to_use(driver)
    STB_freezer_zoom_in_out_button(driver)
    STB_freezer_zoom_in_out_fingers(driver)
    STB_freezer_zoom_mix(driver)
    STB_freezer_default_button(driver)


def STB_freezer_zoom_in_out_button(driver):
    logger.Test('STB Freezer-zoom in & out by button')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/Tools/Freezer/STB_freezer_zoom_in_out_button.json', driver=driver)


def STB_freezer_zoom_in_out_fingers(driver):
    logger.Test('STB Freezer-zoom in & out by fingers')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/Tools/Freezer/STB_freezer_zoom_in_out_fingers.json', driver=driver)


def STB_freezer_zoom_mix(driver):
    logger.Test('STB Freezer-zoom in button first than fingers')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/Tools/Freezer/STB_freezer_zoom_mix.json', driver=driver)


def STB_freezer_default_button(driver):
    logger.Test('STB Freezer-default screen button')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/Tools/Freezer/STB_freezer_default_button.json', driver=driver)


def STB_freezer_reboot_to_use(driver):
    logger.Test('STB Freezer-reboot to use')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/Tools/Freezer/STB_freezer_reboot_to_use.json', driver=driver)

# def Spotlight


def STB_spotlight_all(driver):
    STB_spotlight_zoom_in_out_button(driver)
    STB_spotlight_zoom_in_out_fingers(driver)
    STB_spotlight_transparency(driver)
    STB_spotlight_move(driver)


def STB_spotlight_zoom_in_out_button(driver):
    logger.Test('STB Spotlight-zoom in & out by button')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/Tools/Spotlight/STB_spotlight_zoom_in_out_button.json', driver=driver)


def STB_spotlight_zoom_in_out_fingers(driver):
    logger.Test('STB Spotlight-zoom in & out by fingers')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/Tools/Spotlight/STB_spotlight_zoom_in_out_fingers.json', driver=driver)


def STB_spotlight_transparency(driver):
    logger.Test('STB Spotlight-Transparency dark and light')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/Tools/Spotlight/STB_spotlight_transparency.json', driver=driver)


def STB_spotlight_move(driver):
    logger.Test('STB Spotlight-move')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/Tools/Spotlight/STB_spotlight_move.json', driver=driver)

# def stopwatch


def STB_stopwatch_all(driver):
    STB_stopwatch_start_pause(driver)
    STB_stopwatch_lap(driver)
    STB_stopwatch_expand(driver)
    STB_stopwatch_resume_reset(driver)
    STB_stopwatch_move(driver)


def STB_stopwatch_start_pause(driver):
    logger.Test('STB stopwatch-start and pause')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/Tools/Stopwatch/STB_stopwatch_start_pause.json', driver=driver)


def STB_stopwatch_lap(driver):
    logger.Test('STB stopwatch-lap')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/Tools/Stopwatch/STB_stopwatch_lap.json', driver=driver)


def STB_stopwatch_expand(driver):
    logger.Test('STB stopwatch-expand')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/Tools/Stopwatch/STB_stopwatch_expand.json', driver=driver)


def STB_stopwatch_resume_reset(driver):
    logger.Test('STB stopwatch-resume & reset')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/Tools/Stopwatch/STB_stopwatch_resume_reset.json', driver=driver)


def STB_stopwatch_move(driver):
    logger.Test('STB stopwatch-move')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/Tools/Stopwatch/STB_stopwatch_move.json', driver=driver)

# def timer


def STB_timer_all(driver):
    STB_timer_start_ring(driver)
    STB_timer_pause_resume_reset(driver)
    STB_timer_expand(driver)


def STB_timer_start_ring(driver):
    logger.Test('STB timer-start to wait the bell ring')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/Tools/Timer/STB_timer_start_ring.json', driver=driver)


def STB_timer_pause_resume_reset(driver):
    logger.Test('STB timer-pause & resume & reset button')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/Tools/Timer/STB_timer_pause_resume_reset.json', driver=driver)


def STB_timer_expand(driver):
    logger.Test('STB timer-expand')
    event_gen.generate_event(
        json_path='./Test_Jason/STB/Tools/Timer/STB_timer_expand.json', driver=driver)
# def marker


def STB_marker_all(driver):
    STB_marker_selector(driver)
    STB_marker_pen(driver)
    STB_marker_highlighter(driver)


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
# def menu


def screen_lock_menu(driver):
    while True:
        print("ScreenLock Options:")
        print("0: Back to main menu")
        print("1: Set Password")
        print("2: Change Password")
        print("3: Remove Password")
        print("ALL")

        choice = input("Enter your choice: ")

        if choice == '0':
            return
        elif choice == '1':
            screen_lock_setPassword(driver)
        elif choice == '2':
            screen_lock_changePassword(driver)
        elif choice == '3':
            screen_lock_removePassword(driver)
        elif choice.lower() == 'all':
            screen_lock_ALL(driver)
        else:
            print("Invalid option")


def wallpaper_menu(driver):
    while True:
        print("Wallpaper Options:")
        print("0: Back to main menu")
        print("1: Change By_default")
        print("2: Change By_update")
        print("ALL")

        choice = input("Enter your choice: ")

        if choice == '0':
            return
        elif choice == '1':
            wallpaper_By_default(driver)
        elif choice == '2':
            wallpaper_By_update(driver)
        elif choice.lower() == 'all':
            wallpaper_ALL(driver)
        else:
            print("Invalid option")


def edit_launcher_menu(driver):
    while True:
        print("Edit Launcher Options:")
        print("0: Back to main menu")
        print("1: Add_delete_re-range app on hot seat")
        print("2:install Testapp and find in all apps")
        print("ALL")

        choice = input("Enter your choice: ")

        if choice == '0':
            return
        elif choice == '1':
            edit_launcher_add_app(driver)
        elif choice == '2':
            edit_launcher_find_all(driver)
        elif choice.lower() == 'all':
            edit_launcher_all(driver)
        else:
            print("Invalid option")


def recent_app_menu(driver):
    while True:
        print("Recent App Options:")
        print("0: Back to main menu")
        print("1:clear app")
        print("2:clear all button")
        print("ALL")

        choice = input("Enter your choice: ")

        if choice == '0':
            return
        elif choice == '1':
            recent_app_clear_app(driver)
        elif choice == '2':
            recent_app_clear_all_btn(driver)
        elif choice.lower() == 'all':
            recent_app_all(driver)
        else:
            print("Invalid option")


def STB_tools_menu(driver):
    while True:
        print("STB tools Options:")
        print("0: Back to main menu")
        print("1: Freezer")
        print("2: Spotlight")
        print("3: Stopwatch")
        print("4: Timer")
        print("5: Marker")
        print("ALL")

        choice = input("Enter your choice: ")

        if choice == '0':
            return
        elif choice == '1':
            freezer_menu(driver)
        elif choice == '2':
            spotlight_menu(driver)
        elif choice == '3':
            stopwatch_menu(driver)
        elif choice == '4':
            timer_menu(driver)
        elif choice == '5':
            marker_menu(driver)
        elif choice.lower() == 'all':
            pass
        else:
            print("Invalid option")


def freezer_menu(driver):
    while True:
        print("Freezer Options:")
        print("0: Back to main menu")
        print("1: Zoom in & out, by button")
        print("2: Zoom in & out, by fingers")
        print("3: Zoom in, button first than fingers")
        print("4: default screen button")
        print("5: reboot to freezer")
        print("ALL")

        choice = input("Enter your choice: ")

        if choice == '0':
            return
        elif choice == '1':
            STB_freezer_zoom_in_out_button(driver)
        elif choice == '2':
            STB_freezer_zoom_in_out_fingers(driver)
        elif choice == '3':
            STB_freezer_zoom_mix(driver)
        elif choice == '4':
            STB_freezer_default_button(driver)
        elif choice == '5':
            STB_freezer_reboot_to_use(driver)
        elif choice.lower() == 'all':
            STB_freezer_all(driver)
        else:
            print("Invalid option")


def spotlight_menu(driver):
    while True:
        print("Spotlight Options:")
        print("0: Back to main menu")
        print("1: Zoom in & out, by button")
        print("2: Zoom in & out, by fingers")
        print("3: Transparency dark and light")
        print("4: Spotlight moving")
        print("ALL")

        choice = input("Enter your choice: ")

        if choice == '0':
            return
        elif choice == '1':
            STB_spotlight_zoom_in_out_button(driver)
        elif choice == '2':
            STB_spotlight_zoom_in_out_fingers(driver)
        elif choice == '3':
            STB_spotlight_transparency(driver)
        elif choice == '4':
            STB_spotlight_move(driver)
        elif choice.lower() == 'all':
            STB_spotlight_all(driver)
        else:
            print("Invalid option")


def stopwatch_menu(driver):
    while True:
        print("Spotlight Options:")
        print("0: Back to main menu")
        print("1: start and pause")
        print("2: lap")
        print("3: expand")
        print("4: resume_reset")
        print("5: moving")
        print("ALL")

        choice = input("Enter your choice: ")

        if choice == '0':
            return
        elif choice == '1':
            STB_stopwatch_start_pause(driver)
        elif choice == '2':
            STB_stopwatch_lap(driver)
        elif choice == '3':
            STB_stopwatch_expand(driver)
        elif choice == '4':
            STB_stopwatch_resume_reset(driver)
        elif choice == '5':
            STB_stopwatch_move(driver)
        elif choice.lower() == 'all':
            STB_stopwatch_all(driver)
        else:
            print("Invalid option")


def timer_menu(driver):
    while True:
        print("Spotlight Options:")
        print("0: Back to main menu")
        print("1: start and pause")
        print("2: pause & resume & reset")
        print("3: expand")
        print("4: ")
        print("5: ")
        print("ALL")

        choice = input("Enter your choice: ")

        if choice == '0':
            return
        elif choice == '1':
            STB_timer_start_ring(driver)
        elif choice == '2':
            STB_timer_pause_resume_reset(driver)
        elif choice == '3':
            STB_timer_expand(driver)
        elif choice == '4':
            pass
        elif choice == '5':
            pass
        elif choice.lower() == 'all':
            STB_timer_all(driver)
        else:
            print("Invalid option")


def marker_menu(driver):
    while True:
        print("Spotlight Options:")
        print("0: Back to main menu")
        print("1: selector")
        print("2: pen")
        print("3: highlighter")
        print("4: ")
        print("5: ")
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
            pass
        elif choice == '5':
            pass
        elif choice.lower() == 'all':
            STB_marker_all(driver)
        else:
            print("Invalid option")


def STB_menu(driver):
    while True:
        print("STB Options:")
        print("0: Back to main menu")
        print("1: back button")
        print("2: homepage button")
        print("3: recent app")
        print("4: element in all apps")
        print("5: add & delete apps in shortcut")
        print("6: app order in shortcut")
        print("7: add & delete tools in shortcut")
        print("8: tools order in shortcut")
        print("9: STB tools")
        print("ALL")

        choice = input("Enter your choice: ")

        if choice == '0':
            return
        elif choice == '1':
            STB_back_btn(driver)
        elif choice == '2':
            STB_homepage_btn(driver)
        elif choice == '3':
            recent_app_menu(driver)
        elif choice == '4':
            STB_element_in_all_apps(driver)
        elif choice == '5':
            STB_apps_add_delete_app_in_shortcut(driver)
        elif choice == '6':
            STB_apps_order_in_shortcut(driver)
        elif choice == '7':
            STB_tools_add_delete_app_in_shortcut(driver)
        elif choice == '8':
            STB_tools_order_in_shortcut(driver)
        elif choice == '9':
            STB_tools_menu(driver)
        elif choice.lower() == 'all':
            STB_all(driver)
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
        screen_lock_menu(driver)
    elif first_choice == '2':
        wallpaper_menu(driver)
    elif first_choice == '3':
        edit_launcher_menu(driver)
    elif first_choice == '4':
        recent_app_menu(driver)
    elif first_choice == '5':
        STB_menu(driver)
    elif first_choice == '6':
        STB_tools_menu(driver)
    elif first_choice.lower() == 'test':
        TestJson(driver)
    else:
        print("Invalid option")
