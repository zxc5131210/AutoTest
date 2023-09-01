"""
Event generator will read a .json file and generate event.

"""
import os
import time
import json
from appium.webdriver.common.appiumby import AppiumBy
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

    def generate_event(self, json_path: str, driver):
        gesture = Gesture(driver)
        gesture.home_page()
        evnet_flow = self. read_json(json_path)
        flow = evnet_flow['steps']
        for event in flow:
            json_sequence = event['sequence']
            json_element = event['element']
            json_gesture = event['gesture']
            location_x = event['x']
            location_y = event['y']
            try:
                self.gesture_cases(event, json_gesture, driver,
                                   json_element, json_gesture, location_x, location_y)
                self.logger.info(
                    f'Sequence {json_sequence} {json_gesture}'
                )
            except NoSuchElementException:
                self.logger.error(
                    f'Sequence {json_sequence} {json_gesture}'
                )
        self.logger.info("Flow finished")

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
                element = driver.find_element(
                    AppiumBy.XPATH,
                    json_element
                )
                gesture.tap(element)

            case 'sendKey_byID':
                element = driver.find_element(
                    AppiumBy.ID,
                    json_element
                )
                keyword = event['args'][-1]
                gesture.send_keys(element, keyword)

            case 'clearKey_byID':
                element = driver.find_element(
                    AppiumBy.ID,
                    json_element
                )
                gesture.clear_keys(element)

            case 'tap_byID':
                element = driver.find_element(
                    AppiumBy.ID,
                    json_element
                )
                gesture.tap(element)

            case 'drag_drop':
                element = driver.find_element(
                    AppiumBy.ACCESSIBILITY_ID,
                    json_element
                )
                gesture.drag_drop_bylocation(element, location_x, location_y)

            case 'screenshot':
                time.sleep(3)
                filename = event['args'][-1]
                gesture.screenshot(f'./{filename}.png')

            case 'swipe_up':
                gesture.swipe_up()

            case 'longpress_location':
                gesture.longpress_location(location_x, location_y)

            case 'overview':
                gesture.overview_page()

            case 'homepage':
                gesture.home_page()

            case 'findelement_ByAccessibility_ID':
                element = driver.find_element(
                    AppiumBy.ACCESSIBILITY_ID,
                    json_element
                )

            case 'findelements_ByID':
                elements = driver.find_elements(
                    AppiumBy.ID,
                    json_element
                )

            case 'findelement_ByXpath':
                element = driver.find_element(
                    AppiumBy.XPATH,
                    json_element
                )

            case 'change_wallpaper_first':
                elements = driver.find_elements(
                    AppiumBy.ID,
                    json_element
                )
                first_element = elements[1]
                gesture.tap(first_element)

            case 'change_wallpaper_second':
                elements = driver.find_elements(
                    AppiumBy.ID,
                    json_element
                )
                first_element = elements[2]
                gesture.tap(first_element)

            case 'isCurrentApp_excepted':
                current_app_package = driver.current_package

            case 'isScreenShotEnable':
                current_directory = os.getcwd()
                file_list = os.listdir(current_directory)
                for filename in file_list:
                    if event['args'][-1] in filename:
                        pass
                    else:
                        logger.error('ScreenShot Fail')

            case 'isActivityBackgroung':
                gesture.get_overview_activities()
                gesture.check_background_activities(json_element)

            case 'compare_images_pixel':
                compare_1 = event['element'][0]
                compare_2 = event['element'][1]
                gesture.compare_images_pixel(compare_1, compare_2)

            case 'close_app':
                gesture.close_app()

            case 'update_image':
                gesture.update_image(json_element)

            case 'end_activity':
                gesture.close_app()
                gesture.home_page()
                gesture.clean_activity(json_element)

            case _:
                self.logger.warning(
                    f'gesture type: {json_gesture} not defined.')


if __name__ == '__main__':
    eventgen = EventGen()
