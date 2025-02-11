"""
Event generator will read a .json file and generate event.

"""
import logging
import os
import time

import ddddocr
from selenium.common.exceptions import NoSuchElementException

import util
from gesture import Gesture
from locator import locator


def delete_temporarily_screenshots():
    current_directory = os.getcwd()
    files_to_delete = ["compareshot_1.png", "compareshot_2.png", "2fa.png"]
    for filename in files_to_delete:
        filepath = os.path.join(current_directory, filename)
        if os.path.exists(filepath) and os.path.isfile(filepath):
            os.remove(filepath)
        else:
            pass


class EventGen:
    def __init__(self, reporter):
        self.reporter = reporter

    # Gen Event for use
    def generate_event(self, json_path: str, driver):
        self.initial_setting(driver)
        flow = util.parse_step(json_path)
        for event in flow:
            self.process_event(event, driver)
        self.reporter.succeed_step("Test End", "Flow finished")
        delete_temporarily_screenshots()

    def process_event(self, event, driver):
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
            time.sleep(1)

        except Exception:
            logging.error(json_describe)
            self.reporter.fail_step(json_sequence, json_describe)
            time.sleep(1)

    def initial_setting(self, driver):
        gesture = Gesture(driver, self.reporter)
        guest_btn = driver(resourceId=locator["vlauncher_btn_guest"])
        back_btn = driver(resourceId=locator["authenticator_btn_back"])
        while True:
            if back_btn.exists:
                gesture.tap(back_btn)
                time.sleep(1)
            if guest_btn.exists:
                gesture.tap(guest_btn)
                time.sleep(1)
            else:
                break
        gesture.home_page()

    def gesture_cases(
        self,
        event,
        driver,
        json_element,
        json_gesture,
        location_x,
        location_y,
    ):
        gesture = Gesture(driver, self.reporter)
        element = util.assort_element(json_element, json_gesture, driver)
        match json_gesture:
            case "open_activity":
                try:
                    app = [locator[key] for key in json_element]
                    gesture.open_activity(app)
                    time.sleep(3)
                except NoSuchElementException:
                    pass

            case "tap_by_xpath":
                gesture.tap(element)

            case "open_hot_seat_all_app":
                for i in element:
                    gesture.tap(i)
                    time.sleep(3)
                    gesture.home_page()

            case "tap_hot_seat_all_app":
                for i in element:
                    gesture.tap(i)

            case "tap_by_id":
                gesture.tap(element)

            case "tap_by_location":
                driver.click(location_x, location_y)

            case "tap_by_description":
                gesture.tap(element)

            case "tap_by_text":
                gesture.tap(element)

            case "get_element_text":
                text = gesture.get_element_text(element)
                gesture.compare_different_list.append(text)

            case "wait_element_exist":
                gesture.wait_element_exist(element)
                time.sleep(5)

            case "send_key_by_id":
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
                keyword = event["args"][-1]
                gesture.send_keys(element, keyword)

            case "send_key_by_classname":
                keyword = event["args"][-1]
                gesture.send_keys(element, keyword)

            case "screenshot":
                time.sleep(3)
                filename = event["args"][-1]
                gesture.screenshot(f"./{filename}.png")

            case "crop_by_id":
                if element.wait(timeout=20):
                    time.sleep(3)
                    screenshot = driver.screenshot(format="pillow")
                    bounds = element.info["bounds"]
                    element_image = screenshot.crop(
                        (
                            bounds["left"],
                            bounds["top"],
                            bounds["right"],
                            bounds["bottom"],
                        )
                    )
                    filename = event["args"][-1]
                    element_image.save(f"{filename}.png")
                else:
                    logging.error(f"{element} is not found")

            case "identify_edu_verification_code":
                while driver(resourceId="id1").exists:
                    # Capture the image of the verification code.
                    time.sleep(1)
                    password = driver(resourceId=locator[json_element], instance=0)
                    gesture.send_keys(password, event["args"])
                    element = driver.xpath("//*[@resource-id='id2b']")
                    screenshot = driver.screenshot(format="pillow")
                    bounds = element.info["bounds"]
                    element_image = screenshot.crop(
                        (
                            bounds["left"],
                            bounds["top"],
                            bounds["right"],
                            bounds["bottom"],
                        )
                    )
                    element_image.save("2fa.png")
                    # Adjust the brightness and contrast of the image to make it easier to recognize
                    image = PIL.Image.open("2fa.png")
                    image = PIL.ImageEnhance.Contrast(image).enhance(1.5)
                    image = PIL.ImageEnhance.Brightness(image).enhance(2)
                    image.save("2fa.png")
                    # Perform recognition by comparing against the train data.
                    ocr = ddddocr.DdddOcr()
                    with open("2fa.png", "rb") as f:
                        image = f.read()
                    verification_code = ocr.classification(image)
                    # If the recognized verification code is not three integers, switch to the next photo for
                    # recognition.
                    if not verification_code.isnumeric() or len(verification_code) != 3:
                        gesture.tap(driver.xpath("//*[@text='換下一個']"))
                    else:
                        ele = (
                            driver(resourceId="id14")
                            .child(className="android.view.View", instance=4)
                            .child(className="android.widget.EditText")
                        )
                        gesture.send_keys(ele, verification_code)
                        gesture.tap(
                            driver(resourceId=locator["authenticator_edu_login"])
                        )
                        time.sleep(5)

            case "stay_sign_in_microsoft":
                gesture.tap(
                    driver(resourceId=locator["authenticator_microsoft_skip_checkbox"])
                )
                gesture.tap(
                    driver.xpath(
                        "//*[@resource-id='pageContent']/android.view.View[1]/android.view.View[1]/android.view.View["
                        "2]/android.view.View[2]"
                    )
                )

            case "swipe_up":
                gesture.swipe_up()

            case "swipe_left":
                gesture.swipe_left()

            case "swipe_right":
                gesture.swipe_right()

            case "swipe_down":
                gesture.swipe_down()

            case "swipe_left_element":
                gesture.swipe_left(element)

            case "swipe_right_element":
                gesture.swipe_right(element)

            case "swipe_up_element":
                gesture.swipe_up(element)

            case "swipe_down_element":
                gesture.swipe_down(element)

            case "scroll_down_element":
                gesture.scroll_down(element)

            case "drag_element_to_screen_edge":
                direction = event["args"]
                gesture.drag_element_to_screen_edge(element, direction=direction)
                time.sleep(2)

            case "get_element_location":
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
                    self.reporter.fail_step("error", "the element does not move")
                gesture.compare_different_list.clear()

            case "screen_zoom_in":
                gesture.zoom_in(element)

            case "screen_zoom_out":
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
                gesture.uninstall_utx()
                gesture.reboot()
                gesture.wait_for_device()
                time.sleep(5)
                driver.service("uiautomator").start()
                time.sleep(5)
                gesture.tap(driver(resourceId=locator["vlauncher_btn_guest"]))

            case "findelement_by_id":
                """
                If you want to verify that the element is not found, args ==False
                """
                if not element.exists and event["args"].lower() != "false":
                    logging.error(msg=f"Find [{json_element}] FAIL")
                    self.reporter.fail_step("error", f"Find [{json_element}] FAIL")

            case "findelement_by_xpath":
                """
                if verify not find the element = True, args ==False
                """
                if not element.exists and event["args"].lower() != "false":
                    logging.error(msg=f"Find [{element}] FAIL")
                    self.reporter.fail_step("error", f"Find [{element}] FAIL")

            case "findelement_by_text":
                if not element.exists and event["args"] != "False":
                    logging.error(f"Find {element} FAIL")
                    self.reporter.fail_step("error", f"Find {element} FAIL")

            case "change_wallpaper_first":
                if driver(text="com.viewsonic.wallpaperpicker").exists:
                    gesture.tap(driver(text="com.viewsonic.wallpaperpicker"))
                    gesture.tap(driver(resourceId="android:id/button_always"))
                first_element = element[1]
                gesture.tap(first_element)

            case "change_wallpaper_second":
                first_element = element[2]
                gesture.tap(first_element)

            case "stopwatch_lap":
                for lap in range(10):
                    gesture.tap(element)

            case "install_app":
                gesture.install_app(json_element)

            case "uninstall_app":
                gesture.uninstall_app(locator[json_element])

            case "recent_app_clear":
                if element.exists:
                    element.click()
                else:
                    logging.error(msg="app not found in recent app")
                    self.reporter.fail_step("error", "app not found in recent app")

            case "recent_app_list":
                running_apps_list = [app.get_text() for app in element]
                for expect_app in event["args"]:
                    if expect_app not in running_apps_list:
                        logging.error("can't find the running app in recent app")

            case "marker_fill_up":
                center_x = driver.info["displayWidth"] // 2
                for y_start in range(50):
                    driver.swipe(
                        fx=0, fy=y_start, tx=center_x, ty=y_start, duration=0.05
                    )

            case "marker_verify_file_is_exists":
                # get toast msg and verify the file is existing
                toast = gesture.get_toast()
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
                while not element.exists:
                    if determine_swipe.exists:
                        driver.swipe(x_a, y_a, x_b, y_b)
                    else:
                        logging.error(msg="Not Found App")
                        self.reporter.fail_step("error", "Not Found App")
                        break

            case "stb_scroll_horiz_to_element":
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
                while not element.exists:
                    if determine_swipe.exists:
                        driver.swipe(x_a, y_a, x_b, y_b)
                    else:
                        logging.error(msg="Not Found App")
                        self.reporter.fail_step("error", "Not Found App")
                        break

            case "stb_second_class_initialization":
                while not driver(resourceId=locator["stb_btn_all_apps"]).exists:
                    gesture.tap(driver(resourceId=locator["stb"]))
                    time.sleep(1)
                gesture.tap(driver(resourceId=locator["stb_btn_all_apps"]))
                gesture.tap(driver(resourceId=locator["stb_btn_edit_apps"]))

                gesture.tap(driver(resourceId=locator["stb_btn_root_app1"]))
                gesture.tap(driver(resourceId=locator["stb_btn_root_app2"]))
                gesture.tap(driver(resourceId=locator["stb_btn_root_app3"]))
                gesture.tap(driver(resourceId=locator["stb_btn_home"]))

            case "stb_third_class_initialization":
                while not driver(resourceId=locator["stb_btn_all_tools"]).exists:
                    gesture.tap(driver(resourceId=locator["stb"]))
                    time.sleep(1)
                gesture.tap(driver(resourceId=locator["stb_btn_all_tools"]))
                gesture.tap(driver(resourceId=locator["stb_btn_edit_tools"]))

                gesture.tap(driver(resourceId=locator["stb_btn_tools_shortcut_one"]))
                gesture.tap(driver(resourceId=locator["stb_btn_tools_shortcut_two"]))
                gesture.tap(driver(resourceId=locator["stb_btn_home"]))

            case "stb_spotlight_initialization":
                gesture.zoom_out()
                gesture.tap(driver(resourceId=locator["spotlight_btn_settings"]))
                gesture.swipe_left(
                    driver(resourceId=locator["spotlight_seekbar_transparency"])
                )

            case "current_app_compare":
                dictionary = gesture.current_app()
                if (
                    dictionary["package"] == locator[json_element[0]]
                    or dictionary["package"] == locator["lango_" + json_element[0]]
                ) and (
                    locator[json_element[1]] in dictionary["activity"]
                    or locator["lango_" + json_element[1]] in dictionary["activity"]
                ):
                    pass
                else:
                    logging.error(msg=f"{json_element} is not current")
                    self.reporter.fail_step("error", f"{json_element} is not current")

            case "timer_scroll_to_findtext":
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
                    target_scrollbar = None
                    logging.error(msg=f"{json_element} is not found")
                    self.reporter.fail_step("error", f"{json_element} is not found")

                # scroll to find
                for i in range(60):
                    if driver.xpath(element).text != target_text:
                        gesture.swipe_up(driver(resourceId=target_scrollbar))
                    else:
                        break

            case "stb_screenshot_verify_saving":
                gesture.get_file_count(json_element)

            case "get_volume":
                gesture.compare_different_list.append(gesture.get_volume())

            case "get_toast_expect":
                msg = gesture.get_toast()
                if msg == event["args"]:
                    pass
                else:
                    logging.error(msg="toast is not expect")
                    self.reporter.fail_step("error", "toast is not expect")

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
                            "error", "The data is the same , not changed"
                        )
                gesture.compare_different_list.clear()

            case "tap_by_device_model":
                device = gesture.get_device_info()
                device_model = device["model"]
                element = element.child(text=device_model)
                gesture.tap(element)

            case "wait_time":
                wait_time = event["args"]
                time.sleep(int(wait_time))

            case "compare_images_pixel":
                compare_1 = event["element"][0]
                compare_2 = event["element"][1]
                gesture.compare_images_pixel(compare_1, compare_2)

            case "verify_text":
                title_name = element.info["text"]
                if title_name == event["args"]:
                    pass
                else:
                    logging.error(msg="title changes fail")
                    self.reporter.fail_step("error", "title changes fail")

            case "close_app":
                gesture.close_app(json_element)

            case "upload_image":
                gesture.upload_file(json_element)

            case "delete_file":
                gesture.delete_file(json_element)

            case "end_activity":
                gesture.close_app(locator[json_element])
                gesture.clean_activity(locator[json_element])
                time.sleep(5)
                gesture.home_page()

            case "send_remote_controller_event":
                gesture.send_event(json_element)

            case _:
                logging.warning(msg=f"gesture type: {json_gesture} not defined.")
