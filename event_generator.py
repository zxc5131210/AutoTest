"""
Event generator will read a .json file and generate event.

"""
import os
import time
import json
from selenium.common.exceptions import NoSuchElementException
from logger import Logger
from gesture import Gesture

# entity log
logger = Logger()


class EventGen():
    # Gen Event for use
    def __init__(self) -> None:
        self.logger = Logger()

    def read_json(self, json_path: str) -> dict:
        with open(json_path, encoding='utf-8') as flow:
            flow = json.load(flow)
            return flow

    def delete_temporarily_screenshots(self):
        current_directory = os.getcwd()
        files_to_delete = ['compareshot_1.png', 'compareshot_2.png']
        for filename in files_to_delete:
            filepath = os.path.join(current_directory, filename)
            if os.path.exists(filepath) and os.path.isfile(filepath):
                os.remove(filepath)
            else:
                pass

    def crash_exclusion(self, driver):
        gesture = Gesture(driver)
        guest_btn = driver(resourceId='com.viewsonic.vlauncher:id/btn_guest')
        if guest_btn.exists:
            gesture.tap(guest_btn)
        else:
            pass

    def generate_event(self, json_path: str, driver):
        gesture = Gesture(driver)
        # 設定初始
        gesture.home_page()
        event_flow = self.read_json(json_path)
        flow = event_flow['steps']
        for event in flow:
            json_sequence = event['sequence']
            json_element = event['element']
            json_gesture = event['gesture']
            location_x = event['x']
            location_y = event['y']
            try:
                self.crash_exclusion(driver)
                self.gesture_cases(event, json_gesture, driver,
                                   json_element, json_gesture, location_x, location_y)
                self.logger.info(
                    f'Sequence {json_sequence} {json_gesture}'
                )
                time.sleep(0.5)

            except Exception:
                self.logger.error(
                    f'Sequence {json_sequence} {json_gesture}'
                )
                time.sleep(0.5)

        self.logger.info("Flow finished")
        self.delete_temporarily_screenshots()

    def gesture_cases(
            self, event, gesture, driver, json_element, json_gesture, location_x, location_y
    ):
        gesture = Gesture(driver)
        match json_gesture:
            case 'open_activity':
                try:
                    gesture.open_activity(json_element)
                except NoSuchElementException:
                    pass

            case 'tap_byXpath':
                element = driver.xpath(json_element)
                gesture.tap(element)

            case 'open_hot_seat_all_app':
                elements = driver(resourceId=json_element)
                for element in elements:
                    gesture.tap(element)
                    time.sleep(3)
                    gesture.home_page()

            case 'tap_byID':
                element = driver(resourceId=json_element)
                gesture.tap(element)

            case 'tap_byImage':
                gesture.tap_image(json_element)

            case 'tap_byText':
                element = driver(text=json_element)
                gesture.tap(element)

            case 'sendKey_byID':
                element = driver(resourceId=json_element)
                keyword = event['args'][-1]
                gesture.send_keys(element, keyword)

            case 'clearKey_byID':
                element = driver(resourceId=json_element)
                gesture.clear_keys(element)

            case 'screenshot':
                time.sleep(3)
                filename = event['args'][-1]
                gesture.screenshot(f'./{filename}.png')

            case 'swipe_up':
                gesture.swipe_up()

            case 'swipe_left':
                gesture.swipe_left()

            case 'swipe_right':
                gesture.swipe_right()

            case 'swipe_down':
                gesture.swipe_down()

            case 'swipe_left_element':
                element = driver(resourceId=json_element)
                gesture.swipe_left(element)

            case 'swipe_right_element':
                element = driver(resourceId=json_element)
                gesture.swipe_right(element)

            case 'swipe_up_element':
                element = driver(resourceId=json_element)
                gesture.swipe_up(element)

            case 'swipe_down_element':
                element = driver(resourceId=json_element)
                gesture.swipe_down(element)

            case 'drag_element_to_screen_edge':
                element = driver(resourceId=json_element)
                direction = event['args']
                gesture.drag_element_to_screen_edge(
                    element, direction=direction)
                time.sleep(2)

            case 'screen_zoom_in':
                element = driver()
                gesture.zoom_in(element)

            case 'screen_zoom_out':
                element = driver()
                gesture.zoom_out(element)

            case 'long_press_location':
                gesture.long_press_location(location_x, location_y)

            case 'overview':
                gesture.overview_page()

            case 'back_btn':
                gesture.back()

            case 'homepage':
                gesture.home_page()

            case 'reboot_to_homepage':
                gesture.reboot()
                gesture.wait_for_device()
                driver.uiautomator.start()
                time.sleep(5)
                gesture.tap(
                    driver(resourceId='com.viewsonic.vlauncher:id/btn_guest'))

            case 'findelements_ByID':
                element = driver(resourceId=json_element)

            case 'findelement_ByXpath':
                element = driver.xpath(json_element)

            case 'findelement_ByText':
                element = driver(text=json_element)
                if element.exists:
                    pass
                else:
                    self.logger.error('Find Text FAIL')

            case 'change_wallpaper_first':
                element = driver(resourceId=json_element)
                first_element = element[1]
                gesture.tap(first_element)

            case 'change_wallpaper_second':
                element = driver(resourceId=json_element)
                first_element = element[2]
                gesture.tap(first_element)

            case 'stopwatch_lap':
                element = driver(resourceId=json_element)
                for lap in range(10):
                    gesture.tap(element)

            case 'is_screenShot_enable':
                current_directory = os.getcwd()
                file_list = os.listdir(current_directory)
                for filename in file_list:
                    if event['args'][-1] in filename:
                        pass
                    else:
                        self.logger.error('ScreenShot Fail')

            case 'install_app':
                gesture.install_app(json_element)

            case 'uninstall_app':
                gesture.uninstall_app(json_element)

            case 'is_activity_background':
                gesture.get_overview_activities()
                gesture.check_background_activities(json_element)

            case 'recent_app_clear':
                element = driver(resourceId=json_element)
                if element.exists:
                    element.click()
                else:
                    self.logger.error('app not found in recent app')

            case 'marker_fill_up':
                element_bounds = driver.info
                center_x = (element_bounds['displayWidth']) // 2
                for i in range(50):
                    y_start = i
                    driver.swipe(fx=0, fy=y_start, tx=center_x,
                                 ty=y_start, duration=0.05)

            case 'swipe_to_find_in_all_apps':
                x_a, y_a = driver(
                    resourceId="com.viewsonic.vlauncher:id/all_app_cell_5").center()
                x_b, y_b = driver(
                    resourceId="com.viewsonic.vlauncher:id/all_app_cell_1").center()
                determine_swipe = driver(
                    resourceId='com.viewsonic.vlauncher:id/all_app_cell_10')
                element = driver(text=json_element)
                while True:
                    if element.exists:
                        break
                    elif determine_swipe.exists:
                        driver.swipe(x_a, y_a, x_b, y_b)
                    else:
                        self.logger.error("Not Found App")

            case 'STB_scroll_horiz_to_element':
                x_a, y_a = driver(
                    resourceId="com.viewsonic.sidetoolbar:id/RlAllAppsTagFiveTeen").center()
                x_b, y_b = driver(
                    resourceId="com.viewsonic.sidetoolbar:id/RlAllAppsTagEleven").center()
                determine_swipe = driver(
                    resourceId='com.viewsonic.sidetoolbar:id/RlAllAppsTagFiveTeen')
                element = driver(text=json_element)
                while True:
                    if element.exists:
                        break
                    elif determine_swipe.exists:
                        driver.swipe(x_a, y_a, x_b, y_b)
                    else:
                        self.logger.error("Not Found App")
                        break

            case 'STB_secondClass_initialization':
                gesture.tap(
                    driver(resourceId='com.viewsonic.sidetoolbar:id/arrow'))
                if driver(resourceId='com.viewsonic.sidetoolbar:id/RlAllAppTagFirst').exists or \
                        driver(resourceId='com.viewsonic.sidetoolbar:id/RlAllAppTagSecond').exists or \
                        driver(resourceId='com.viewsonic.sidetoolbar:id/RlAllAppTagThird').exists:

                    gesture.tap(driver(
                        resourceId='com.viewsonic.sidetoolbar:id/btnAllApp'))
                    gesture.tap(driver(
                        resourceId="com.viewsonic.sidetoolbar:id/iv_all_app_edit_status"))
                    gesture.tap(driver(
                        resourceId="com.viewsonic.sidetoolbar:id/RlAllAppTagFirst"))
                    gesture.tap(driver(
                        resourceId="com.viewsonic.sidetoolbar:id/RlAllAppTagSecond"))
                    gesture.tap(driver(
                        resourceId="com.viewsonic.sidetoolbar:id/RlAllAppTagThird"))
                    gesture.tap(
                        driver(resourceId="com.viewsonic.sidetoolbar:id/btnHome"))
                else:
                    gesture.tap(
                        driver(resourceId="com.viewsonic.sidetoolbar:id/btnHome"))

            case 'STB_ThirdClass_initialization':
                gesture.tap(
                    driver(resourceId='com.viewsonic.sidetoolbar:id/arrow'))
                if driver(resourceId='com.viewsonic.sidetoolbar:id/RlAllToolsTagFirst').exists or \
                        driver(resourceId='com.viewsonic.sidetoolbar:id/RlAllToolsTagSecond').exists:

                    gesture.tap(driver(
                        resourceId='com.viewsonic.sidetoolbar:id/btnAllTools'))
                    gesture.tap(driver(
                        resourceId='com.viewsonic.sidetoolbar:id/iv_all_tools_edit_status'))
                    gesture.tap(driver(
                        resourceId='com.viewsonic.sidetoolbar:id/RlAllToolsTagFirst'))
                    gesture.tap(driver(
                        resourceId='com.viewsonic.sidetoolbar:id/RlAllToolsTagSecond'))
                    gesture.tap(
                        driver(resourceId="com.viewsonic.sidetoolbar:id/btnHome"))
                else:
                    gesture.tap(
                        driver(resourceId="com.viewsonic.sidetoolbar:id/btnHome"))

            case 'STB_spotlight_initialization':
                driver().pinch_in(percent=10, steps=10)
                gesture.tap(
                    driver(resourceId='com.viewsonic.sidetoolbar:id/settings_btn'))
                gesture.swipe_left(driver(
                    resourceId='com.viewsonic.sidetoolbar:id/seekbar_alpha'))

            case 'STB_current_app_compare':
                current_app = gesture.current_app()
                if current_app['package'] == json_element[0] and \
                        current_app['activity'] == json_element[1]:
                    pass
                else:
                    self.logger.error(f'{json_element} is not current')

            case 'Timer_scroll_to_findText':
                target_text = event['args']
                # timer hour/min/sec setting
                if json_element == 'hour':
                    target_scrollbar = 'com.viewsonic.sidetoolbar:id/hour_wheelview'
                    element = '//*[@resource-id="com.viewsonic.sidetoolbar:id/hour_wheelview"]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]'
                elif json_element == 'min':
                    target_scrollbar = 'com.viewsonic.sidetoolbar:id/minute_wheelview'
                    element = '//*[@resource-id="com.viewsonic.sidetoolbar:id/minute_wheelview"]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]'
                elif json_element == 'sec':
                    target_scrollbar = 'com.viewsonic.sidetoolbar:id/second_wheelview'
                    element = '//*[@resource-id="com.viewsonic.sidetoolbar:id/second_wheelview"]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]'

                # scroll to find
                for _ in range(60):
                    if driver.xpath(element).text == target_text:
                        break
                    else:
                        driver(resourceId=target_scrollbar).swipe('up')

            case 'time_wait':
                wait_time = event['args']
                time.sleep(int(wait_time))

            case 'compare_images_pixel':
                compare_1 = event['element'][0]
                compare_2 = event['element'][1]
                gesture.compare_images_pixel(compare_1, compare_2)

            case 'close_app':
                gesture.close_app(json_element)

            case 'update_image':
                gesture.update_file(json_element)

            case 'delete_file':
                gesture.delete_file(json_element)

            case 'end_activity':
                gesture.close_app(json_element)
                gesture.home_page()
                gesture.clean_activity(json_element)

            case _:
                self.logger.warning(
                    f'gesture type: {json_gesture} not defined.')


if __name__ == '__main__':
    eventgen = EventGen()
