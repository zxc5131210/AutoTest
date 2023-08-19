"""Gesture Class."""
import subprocess
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from logger import Logger


class Gesture:
    # define gesture
    def __init__(self, driver) -> None:
        self.logger = Logger()
        if not driver:
            raise ValueError('driver can not be null.')
        self.driver = driver
        self.touch_action = TouchAction(self.driver)

        # implicitly_wait setting
        self.wait = WebDriverWait(self.driver, 2)
        self.implicitly_wait_timeout = 5
        self.driver.implicitly_wait(self.implicitly_wait_timeout)

    def tap(
            self,
            element
    ) -> None:
        # Tap fuction
        self.touch_action.tap(element).perform()
        self.logger.debug('tap complete.')

    def drag_drop_bylocation(
        self,
        drag_element,
        location_x,
        location_y
    ) -> None:
        # darg drop fuction
        self.touch_action.long_press(el=drag_element, duration=5000).move_to(
            x=location_x, y=location_y).release().perform()

    def double_tap(self, element) -> None:
        # double tap fuction
        self.tap(element).tap(element).perform()
        self.logger.debug('tap complete.')

    def back(self) -> None:
        # back button
        self.driver.press_keycode(4)

    def screenshot(self, save_location) -> None:
        # screenshot current screen
        self.driver.save_screenshot(save_location)

    def double_finger(self) -> None:
        # doublefinger use
        pass

    def longpress(self) -> None:
        # longpress fuction
        pass

    def home_page(self) -> None:
        # home page button
        self.driver.press_keycode(3)

    def overview_page(self) -> None:
        # overview button
        self.driver.press_keycode(187)

    def quit_driver(self) -> None:
        # quit driver
        self.driver.quit()

    def swipe_left(
        self,
        start_x: float = 992,
        start_y: float = 954,
        end_x: float = 50,
        end_y: float = 954
    ) -> None:
        # swipe left fuction
        self.driver.swipe(start_x, start_y, end_x, end_y, duration=500)

    def swipe_up(
        self,
        start_x: float = 523,
        start_y: float = 1560,
        end_x: float = 481,
        end_y: float = 229
    ) -> None:
        # Swipe up fuction
        self.driver.swipe(start_x, start_y, end_x, end_y, duration=500)

    def get_overview_activities(self) -> None:
        try:
            result = subprocess.check_output(
                ["adb", "shell", "dumpsys", "activity", "recents"], universal_newlines=True)
            lines = result.split("\n")
            activities = []
            activities = [line.split(
            )[2] for line in lines if "ActivityRecord" in line and len(line.split()) >= 4]
            return activities
        except subprocess.CalledProcessError:
            self.logger.error("Error executing ADB command.")

    def check_background_activities(self, element) -> None:
        # check background activities match the app or not
        overview_activities = self.get_overview_activities()
        activity_list = []
        if overview_activities:
            activity_list.extend(overview_activities)
            if any(element in background for background in activity_list):
                self.logger.info(f"{element} is in the background")
            else:
                self.logger.error(f"{element} is not in the background")
        else:
            self.logger.error("No overview activities found.")
