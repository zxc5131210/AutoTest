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
                self.gesture_cases(event, json_gesture, driver,
                                   json_element, json_gesture, location_x, location_y)
                self.logger.info(
                    f'Sequence {json_sequence} {json_gesture}'
                )
                time.sleep(1)

            except Exception:
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

            case 'long_press_location':
                gesture.long_press_location(location_x, location_y)

            case 'overview':
                gesture.overview_page()

            case 'back_btn':
                gesture.back()

            case 'homepage':
                gesture.home_page()

            case 'findelements_ByID':
                element = driver(resourceId=json_element)

            case 'findelement_ByXpath':
                element = driver.xpath(json_element)

            case 'change_wallpaper_first':
                element = driver(resourceId=json_element)
                first_element = element[1]
                gesture.tap(first_element)

            case 'change_wallpaper_second':
                element = driver(resourceId=json_element)
                first_element = element[2]
                gesture.tap(first_element)

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
                element = driver.xpath(json_element)
                if element.exists:
                    # if element exists ,get element location x,y
                    element_bounds = element.info['bounds']

                    # count begin and end
                    start_x = element_bounds['left'] + 50  # start
                    # center of element
                    start_y = (element_bounds['top'] +
                               element_bounds['bottom']) / 2
                    end_x = element_bounds['left'] - 1000  # end
                    end_y = start_y

                    # swipe to left
                    driver.swipe(start_x, start_y, end_x, end_y)
                    time.sleep(2)

                    if element.exists:
                        self.logger.error(f'{element} still in recent app')
                    else:
                        pass

                else:
                    self.logger.error('recent app not found')

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
