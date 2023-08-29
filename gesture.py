"""Gesture Class."""
import cv2
import numpy as np
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

    def open_activity(self, element) -> None:
        package = element[0]
        activity = element[1]
        self.driver.start_activity(package, activity)

    def tap(
            self,
            element
    ) -> None:
        # Tap fuction
        self.touch_action.tap(element).perform()
        self.logger.info('tap complete.')

    def send_keys(self, element, keyword) -> None:
        try:
            element.send_keys(keyword)
            self.logger.info('send key success')
        except:
            self.logger.error('send key fail')

    def clear_keys(self, element) -> None:
        try:
            element.clear()
            self.logger.info('clear key success')
        except:
            self.logger.error('clear key fail')

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

    def longpress_element(self, element) -> None:
        # longpress fuction
        self.touch_action.long_press(element, duration=5000)
        pass

    def longpress_location(self, location_x, location_y):
        self.touch_action.long_press(
            el=None, x=location_x, y=location_y, duration=5000).perform()

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

    def compare_images_pixel(self, compare_1, compare_2) -> None:
        image_path1 = compare_1  # 第一张图片的路径
        image_path2 = compare_2  # 第二张图片的路径
        # 读取两张图片
        img1 = cv2.imread(image_path1)
        img2 = cv2.imread(image_path2)
        x, y, x_offset, y_offset = 50, 50, 100, 100

        # 提取左上角区域
        img1 = img1[y:y+y_offset, x:x+x_offset]
        img2 = img2[y:y+y_offset, x:x+x_offset]
        # 计算每个像素通道的颜色值差异
        diff_image = cv2.absdiff(img1, img2)
        diff_pixels = np.sum(diff_image, axis=2)  # 计算通道差异总和
        different_pixel_count = np.count_nonzero(diff_pixels)
        if different_pixel_count > 5000:
            self.logger.info('Wallpaper changed success')
        else:
            self.logger.error('Wallpaper changed fail')

    def clean_activity(self, element):
        command = ['adb', 'shell', 'pm', 'clear', element]
        try:
            result = subprocess.run(
                command, capture_output=True, text=True, check=True)
            self.logger.info(f'clear activity data:{result.stdout}')
        except subprocess.CalledProcessError as e:
            self.logger.error(e.stderr)

    def close_app(self):
        self.driver.close_app()
