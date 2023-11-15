"""
Event generator will read a .json file and generate event.

"""
import logging
import os
import time
import json
from selenium.common.exceptions import NoSuchElementException
from gesture import Gesture
from id_locator import locator


def read_json(json_path: str) -> dict:
    with open(json_path, encoding="utf-8") as flow:
        flow = json.load(flow)
        return flow


def delete_temporarily_screenshots():
    current_directory = os.getcwd()
    files_to_delete = ["compareshot_1.png", "compareshot_2.png"]
    for filename in files_to_delete:
        filepath = os.path.join(current_directory, filename)
        if os.path.exists(filepath) and os.path.isfile(filepath):
            os.remove(filepath)
        else:
            pass


def crash_exclusion(driver):
    gesture = Gesture(driver)
    guest_btn = driver(resourceId=locator["vlauncher_btn_guest"])
    if guest_btn.exists:
        gesture.tap(guest_btn)
    else:
        pass


class EventGen:
    def __init__(self, reporter):
        self.reporter = reporter

    # Gen Event for use
    def generate_event(self, json_path: str, driver):
        gesture = Gesture(driver)
        # initial setting
        crash_exclusion(driver)
        gesture.home_page()
        event_flow = read_json(json_path)
        flow = event_flow["steps"]
        for event in flow:
            json_sequence = event["sequence"]
            json_describe = event["describe"]
            json_element = event["element"]
            json_gesture = event["gesture"]
            location_x = event["x"]
            location_y = event["y"]
            try:
                self.gesture_cases(
                    event,
                    driver,
                    json_element,
                    json_gesture,
                    location_x,
                    location_y,
                )
                logging.info(json_describe)
                self.reporter.succeed_step(json_sequence, json_describe)
                time.sleep(0.5)

            except Exception:
                logging.error(json_describe)
                self.reporter.fail_step(json_sequence, json_describe)
                time.sleep(0.5)

        self.reporter.succeed_step("Test End", "Flow finished")
        delete_temporarily_screenshots()

    def gesture_cases(
        self,
        event,
        driver,
        json_element,
        json_gesture,
        location_x,
        location_y,
    ):
        gesture = Gesture(driver)
        match json_gesture:
            case "open_activity":
                try:
                    app = [locator[key] for key in json_element]
                    gesture.open_activity(app)
                    time.sleep(3)
                except NoSuchElementException:
                    pass

            case "tap_byXpath":
                element = driver.xpath(json_element)
                gesture.tap(element)

            case "open_hot_seat_all_app":
                elements = driver(resourceId=locator[json_element])
                for element in elements:
                    gesture.tap(element)
                    time.sleep(3)
                    gesture.home_page()

            case "tap_byID":
                json_element = locator[json_element]
                element = driver(resourceId=json_element)
                gesture.tap(element)

            case "tap_byLocation":
                driver.click(location_x, location_y)

            case "tap_byDescription":
                element = driver(description=json_element)
                gesture.tap(element)

            case "tap_byImage":
                gesture.tap_image(json_element)

            case "tap_byText":
                element = driver(text=json_element)
                gesture.tap(element)

            case "get_element_text":
                element = driver(resourceId=locator[json_element])
                text = gesture.get_element_text(element)
                gesture.compare_different_list.append(text)

            case "sendKey_byID":
                """
                if there are multiple numbers with the same ID.
                args=[count(int), message(str)]
                if ID is unique can only send message
                args=[message(str)]
                """
                if isinstance(event["args"][0], int):
                    element = driver(
                        resourceId=locator[json_element], instance=event["args"][0]
                    )
                else:
                    element = driver(resourceId=locator[json_element])
                keyword = event["args"][-1]
                gesture.send_keys(element, keyword)

            case "sendKey_byClassName":
                element = driver(className=json_element)
                keyword = event["args"][-1]
                gesture.send_keys(element, keyword)

            case "clearKey_byID":
                element = driver(resourceId=locator[json_element])
                gesture.clear_keys(element)

            case "screenshot":
                time.sleep(3)
                filename = event["args"][-1]
                gesture.screenshot(f"./{filename}.png")

            case "crop_byID":
                element = driver(resourceId=locator[json_element])
                if element.wait(timeout=10.0):
                    time.sleep(3)
                    screenshot = driver.screenshot(format="pillow")
                    bounds = element.info["bounds"]
                    left = bounds["left"]
                    top = bounds["top"]
                    right = bounds["right"]
                    bottom = bounds["bottom"]
                    element_image = screenshot.crop((left, top, right, bottom))
                    filename = event["args"][-1]
                    element_image.save(f"{filename}.png")
                else:
                    logging.error(f"{element} is not found")

            case "stay_sign_in_microsoft":
                time.sleep(3)
                if driver(resourceId="KmsiCheckboxField").exists:
                    gesture.tap(
                        driver(
                            resourceId=locator["authenticator_microsoft_skip_checkbox"]
                        )
                    )
                    gesture.tap(
                        driver(
                            resourceId=locator[
                                "authenticator_btn_microsoft_skip_button"
                            ]
                        )
                    )
                else:
                    pass

            case "swipe_up":
                gesture.swipe_up()

            case "swipe_left":
                gesture.swipe_left()

            case "swipe_right":
                gesture.swipe_right()

            case "swipe_down":
                gesture.swipe_down()

            case "swipe_left_element":
                element = driver(resourceId=locator[json_element])
                gesture.swipe_left(element)

            case "swipe_right_element":
                element = driver(resourceId=locator[json_element])
                gesture.swipe_right(element)

            case "swipe_up_element":
                element = driver(resourceId=locator[json_element])
                gesture.swipe_up(element)

            case "swipe_down_element":
                element = driver(resourceId=locator[json_element])
                gesture.swipe_down(element)

            case "drag_element_to_screen_edge":
                element = driver(resourceId=locator[json_element])
                direction = event["args"]
                gesture.drag_element_to_screen_edge(element, direction=direction)
                time.sleep(2)

            case "get_element_location":
                element = driver(resourceId=locator[json_element])
                gesture.get_element_location(element)

            case "compare_location_different":
                x_before = gesture.compare_different_list[0]
                y_before = gesture.compare_different_list[1]
                x_after = gesture.compare_different_list[2]
                y_after = gesture.compare_different_list[3]
                if x_before != x_after or y_before != y_after:
                    pass
                else:
                    logging.error("the element does not move")
                    self.reporter.fail_step(msg="the element does not move")
                gesture.compare_different_list.clear()

            case "screen_zoom_in":
                element = driver()
                gesture.zoom_in(element)

            case "screen_zoom_out":
                element = driver()
                gesture.zoom_out(element)

            case "long_press_location":
                gesture.long_press_location(location_x, location_y)

            case "overview":
                gesture.overview_page()

            case "back_btn":
                gesture.back()

            case "homepage":
                gesture.home_page()

            case "reboot_to_homepage":
                gesture.reboot()
                gesture.wait_for_device()
                time.sleep(5)
                driver.service("uiautomator").start()
                time.sleep(5)

            case "findelements_ByID":
                """
                if verify not find the element = True, args ==False
                """
                element = driver(resourceId=locator[json_element])
                if element.exists:
                    pass
                else:
                    if event["args"] == "False":
                        pass
                    else:
                        logging.error(msg=f"Find {element} FAIL")
                        self.reporter.fail_step(msg=f"Find {element} FAIL")

            case "findelement_ByXpath":
                """
                if verify not find the element = True, args ==False
                """
                element = driver.xpath(json_element)
                if element.exists:
                    pass
                else:
                    if event["args"] == "False":
                        pass
                    else:
                        logging.error(msg=f"Find {element} FAIL")
                        self.reporter.fail_step(msg=f"Find {element} FAIL")

            case "findelement_ByText":
                element = driver(text=json_element)
                if element.exists:
                    pass
                else:
                    logging.error(msg=f"Find {element} FAIL")
                    self.reporter.fail_step(msg=f"Find {element} FAIL")

            case "change_wallpaper_first":
                if driver(text="com.viewsonic.wallpaperpicker").exists:
                    gesture.tap(driver(text="com.viewsonic.wallpaperpicker"))
                    gesture.tap(driver(resourceId="android:id/button_always"))

                element = driver(resourceId=locator[json_element])
                first_element = element[1]
                gesture.tap(first_element)

            case "change_wallpaper_second":
                element = driver(resourceId=locator[json_element])
                first_element = element[2]
                gesture.tap(first_element)

            case "stopwatch_lap":
                element = driver(resourceId=locator[json_element])
                for lap in range(10):
                    gesture.tap(element)

            case "is_screenShot_enable":
                current_directory = os.getcwd()
                file_list = os.listdir(current_directory)
                for filename in file_list:
                    if event["args"][-1] in filename:
                        pass
                    else:
                        logging.error(msg="ScreenShot Fail")
                        self.reporter.fail_step(msg="ScreenShot Fail")

            case "install_app":
                gesture.install_app(json_element)

            case "uninstall_app":
                gesture.uninstall_app(locator[json_element])

            case "is_activity_background":
                gesture.get_overview_activities()
                gesture.check_background_activities(json_element)

            case "recent_app_clear":
                element = driver(resourceId=locator[json_element])
                if element.exists:
                    element.click()
                else:
                    logging.error(msg="app not found in recent app")
                    self.reporter.fail_step(msg="app not found in recent app")

            case "marker_fill_up":
                element_bounds = driver.info
                center_x = (element_bounds["displayWidth"]) // 2
                for i in range(50):
                    y_start = i
                    driver.swipe(
                        fx=0, fy=y_start, tx=center_x, ty=y_start, duration=0.05
                    )

            case "marker_verify_file_is_exists":
                # get toast msg and verify the file is existing
                toast = driver.toast.get_message(wait_timeout=5)
                filename = toast.split("/")[-1]
                filepath = f"/sdcard/pictures/{filename}"
                gesture.file_is_exists(filepath)

            case "swipe_to_find_in_all_apps":
                x_a, y_a = driver(
                    resourceId="com.viewsonic.vlauncher:id/all_app_cell_5"
                ).center()
                x_b, y_b = driver(
                    resourceId="com.viewsonic.vlauncher:id/all_app_cell_1"
                ).center()
                determine_swipe = driver(
                    resourceId="com.viewsonic.vlauncher:id/all_app_cell_10"
                )
                element = driver(text=json_element)
                while True:
                    if element.exists:
                        break
                    elif determine_swipe.exists:
                        driver.swipe(x_a, y_a, x_b, y_b)
                    else:
                        logging.error(msg="Not Found App")
                        self.reporter.fail_step(msg="Not Found App")

            case "STB_scroll_horiz_to_element":
                x_a, y_a = driver(
                    resourceId="com.viewsonic.sidetoolbar:id/RlAllAppsTagFiveTeen"
                ).center()
                x_b, y_b = driver(
                    resourceId="com.viewsonic.sidetoolbar:id/RlAllAppsTagEleven"
                ).center()
                determine_swipe = driver(
                    resourceId="com.viewsonic.sidetoolbar:id/RlAllAppsTagFiveTeen"
                )
                element = driver(text=json_element)
                while True:
                    if element.exists:
                        break
                    elif determine_swipe.exists:
                        driver.swipe(x_a, y_a, x_b, y_b)
                    else:
                        logging.error(msg="Not Found App")
                        self.reporter.fail_step(msg="Not Found App")

            case "STB_secondClass_initialization":
                gesture.tap(driver(resourceId=locator["STB"]))
                if (
                    driver(
                        resourceId="com.viewsonic.sidetoolbar:id/RlThirdPartyApp1"
                    ).exists
                    or driver(
                        resourceId="com.viewsonic.sidetoolbar:id/RlThirdPartyApp2"
                    ).exists
                    or driver(
                        resourceId="com.viewsonic.sidetoolbar:id/imgViewAddApp3"
                    ).exists
                ):
                    gesture.tap(driver(resourceId=locator["STB_btn_all_apps"]))
                    gesture.tap(driver(resourceId=locator["STB_btn_edit_apps"]))
                    gesture.tap(
                        driver(
                            resourceId="com.viewsonic.sidetoolbar:id/clApp1Container"
                        )
                    )
                    gesture.tap(
                        driver(resourceId=locator["STB_btn_apps_container_two"])
                    )
                    gesture.tap(
                        driver(
                            resourceId="com.viewsonic.sidetoolbar:id/clApp3Container"
                        )
                    )
                    gesture.tap(driver(resourceId=locator["STB_btn_home"]))
                else:
                    gesture.tap(driver(resourceId=locator["STB_btn_home"]))

            case "STB_ThirdClass_initialization":
                gesture.tap(driver(resourceId=locator["STB"]))
                if (
                    driver(resourceId=locator["STB_btn_tools_shortcut_one"]).exists
                    or driver(
                        resourceId="com.viewsonic.sidetoolbar:id/imgViewAddTool2"
                    ).exists
                ):
                    gesture.tap(driver(resourceId=locator["STB_btn_all_tools"]))
                    gesture.tap(driver(resourceId=locator["STB_btn_edit_tools"]))
                    gesture.tap(
                        driver(resourceId=locator["STB_btn_tools_shortcut_one"])
                    )
                    gesture.tap(
                        driver(
                            resourceId="com.viewsonic.sidetoolbar:id/imgViewAddTool2"
                        )
                    )
                    gesture.tap(driver(resourceId=locator["STB_btn_home"]))
                else:
                    gesture.tap(driver(resourceId=locator["STB_btn_home"]))

            case "STB_spotlight_initialization":
                driver().pinch_in(percent=10, steps=10)
                gesture.tap(
                    driver(resourceId="com.viewsonic.sidetoolbar:id/settings_btn")
                )
                gesture.swipe_left(
                    driver(resourceId="com.viewsonic.sidetoolbar:id/seekbar_alpha")
                )

            case "STB_current_app_compare":
                dictionary = gesture.current_app()
                if (
                    dictionary["package"] == locator[json_element[0]]
                    and dictionary["activity"] == locator[json_element[1]]
                ):
                    pass
                else:
                    logging.error(msg=f"{json_element} is not current")
                    self.reporter.fail_step(msg=f"{json_element} is not current")

            case "Timer_scroll_to_findText":
                target_text = event["args"]
                # timer hour/min/sec setting
                if json_element == "hour":
                    target_scrollbar = "com.viewsonic.sidetoolbar:id/hour_wheelview"
                    element = (
                        '//*[@resource-id="com.viewsonic.sidetoolbar:id/hour_wheelview"]/android.widget'
                        ".FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]"
                    )
                elif json_element == "min":
                    target_scrollbar = "com.viewsonic.sidetoolbar:id/minute_wheelview"
                    element = (
                        '//*[@resource-id="com.viewsonic.sidetoolbar:id/minute_wheelview"]/android.widget'
                        ".FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]"
                    )
                elif json_element == "sec":
                    target_scrollbar = "com.viewsonic.sidetoolbar:id/second_wheelview"
                    element = (
                        '//*[@resource-id="com.viewsonic.sidetoolbar:id/second_wheelview"]/android.widget'
                        ".FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]"
                    )
                else:
                    element = json_element
                    target_scrollbar = None
                    logging.error(msg=f"{element} is not found")
                    self.reporter.fail_step(msg=f"{element} is not found")

                # scroll to find
                for _ in range(60):
                    if driver.xpath(element).text != target_text:
                        driver(resourceId=target_scrollbar).swipe("up")
                    else:
                        break

            case "STB_screenshot_verify_saving":
                gesture.get_file_count(json_element)

            case "get_volume":
                gesture.compare_different_list.append(gesture.get_volume())

            case "compare_different":
                if (
                    gesture.compare_different_list[0]
                    != gesture.compare_different_list[1]
                ):
                    pass
                else:
                    if event["args"] == "False":
                        pass
                    else:
                        logging.error(msg="The data is the same , not changed")
                        self.reporter.fail_step(
                            msg="The data is the same , not changed"
                        )
                gesture.compare_different_list.clear()

            case "tap_by_device_model":
                device = gesture.get_device_info()
                device_model = device["model"]
                element = driver(resourceId=locator[json_element]).child(
                    text=device_model
                )
                gesture.tap(element)

            case "time_wait":
                wait_time = event["args"]
                time.sleep(int(wait_time))

            case "compare_images_pixel":
                compare_1 = event["element"][0]
                compare_2 = event["element"][1]
                gesture.compare_images_pixel(compare_1, compare_2)

            case "verify_text":
                title_name = driver(resourceId=locator[json_element]).info["text"]
                if title_name == event["args"]:
                    pass
                else:
                    logging.error(msg="title changes fail")
                    self.reporter.fail_step(msg="title changes fail")

            case "close_app":
                gesture.close_app(json_element)

            case "update_image":
                gesture.update_file(json_element)

            case "delete_file":
                gesture.delete_file(json_element)

            case "end_activity":
                gesture.close_app(locator[json_element])
                gesture.home_page()
                gesture.clean_activity(locator[json_element])

            case _:
                logging.warning(msg=f"gesture type: {json_gesture} not defined.")
