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
            self.gesture_cases(event, json_gesture, driver, json_sequence,
                               json_element, json_gesture, location_x, location_y)
            self.logger.info(
                f'Sequence {json_sequence} {json_gesture} complete.')
        self.logger.info("Flow complete")

    def gesture_cases(self, event, gesture, driver, json_sequence, json_element, json_gesture, location_x, location_y):
        gesture = Gesture(driver)
        match json_gesture:
            case 'open_activity':
                gesture.open_activity(json_element)

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
                now_time = time.strftime("%Y%m%d.%H.%M.%S")
                filename = event['args'][-1]
                gesture.screenshot(f'./{filename}.png')
                time.sleep(3)

            case 'swipe_up':
                gesture.swipe_up()

            case 'longpress_location':
                gesture.longpress_location(location_x, location_y)

            case 'overview':
                gesture.overview_page()

            case 'homepage':
                gesture.home_page()

            case 'findelement_ByAccessibility_ID':
                try:
                    element = driver.find_element(
                        AppiumBy.ACCESSIBILITY_ID,
                        json_element
                    )
                except NoSuchElementException:
                    logger.error(f'{json_sequence} Verify Fail')

            case 'findelement_ByClassName':
                elements = driver.find_elements(
                    AppiumBy.CLASS_NAME,
                    json_element
                )
                hotseat_list = []
                for element in elements:
                    element_text = element.text
                    hotseat_list.append(element_text)

            case 'isElement_onHotseat':
                element = driver.find_element(
                    AppiumBy.ACCESSIBILITY_ID,
                    json_element
                )
                if element.text in hotseat_list:
                    logger.info('App is on the hot seat')
                else:
                    logger.error('App is not on the hot seat')

            case 'isCurrentApp_excepted':
                current_app_package = driver.current_package
                if current_app_package == json_element:
                    logger.info('Current App is excepted')
                else:
                    logger.error('Current app is not excepted')

            case 'isScreenShotEnable':
                current_directory = os.getcwd()
                file_list = os.listdir(current_directory)
                for filename in file_list:
                    if json_gesture in filename:
                        logger.info("ScreenShot is worked ")
                        break
                logger.error('ScreenShot Fail')

            case 'isActivityBackgroung':
                gesture.get_overview_activities()
                gesture.check_background_activities(json_element)

            case 'compare_images_pixel':
                compare_1 = event['element'][0]
                compare_2 = event['element'][1]
                gesture.compare_images_pixel(compare_1, compare_2)

            case 'clean_package':
                gesture.clear_package(element)

            case 'end_activity':
                gesture.close_app()
                gesture.home_page()
                gesture.clean_activity(json_element)

            case _:
                self.logger.warring(
                    f'gesture type: {json_gesture} not defined.')


if __name__ == '__main__':
    eventgen = EventGen()
