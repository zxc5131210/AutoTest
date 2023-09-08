"""Gesture Class."""
import subprocess
import cv2
import numpy as np
from logger import Logger


class Gesture:
    # define gesture
    def __init__(self, driver) -> None:
        self.logger = Logger()
        if not driver:
            raise ValueError('driver can not be null.')
        self.driver = driver

    def open_activity(self, element) -> None:
        package = element[0]
        self.driver.app_start(package, stop=True)

    def tap(self, element) -> None:
        # Tap function
        element.click()

    def send_keys(self, element, keyword) -> None:
        element.send_keys(keyword)

    def clear_keys(self, element) -> None:
        element.clear_text()

    def double_tap(self, element) -> None:
        # double tap function
        element.double_click()

    def back(self) -> None:
        # back button
        self.driver.keyevent("back")

    def screenshot(self, save_location) -> None:
        # screenshot current screen
        self.driver.screenshot(save_location)

    def double_finger(self) -> None:
        # double_finger use
        pass

    def long_press_element(self, element) -> None:
        # long_press fuction
        element.long_click(duration=2)

    def long_press_location(self, location_x, location_y):
        self.driver.long_click(x=location_x, y=location_y, duration=2)

    def home_page(self) -> None:
        # home page button
        self.driver.keyevent("home")

    def overview_page(self) -> None:
        # overview button
        self.driver.keyevent("overview")

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
        # swipe left function
        self.driver.swipe(start_x, start_y, end_x, end_y, duration=500)

    def swipe_up(
        self,
        start_x: float = 523,
        start_y: float = 1560,
        end_x: float = 481,
        end_y: float = 229
    ) -> None:
        # Swipe up function
        self.driver.swipe(start_x, start_y, end_x, end_y, duration=500)

    def install_app(self, element) -> None:
        command = ['adb', 'install', "-r", element]
        subprocess.run(command, check=False)

    def uninstall_app(self, element) -> None:
        command = ['adb', 'uninstall', element]
        subprocess.run(command, check=False)

    def get_overview_activities(self) -> None:
        result = subprocess.check_output(
            ["adb", "shell", "dumpsys", "activity", "recents"], universal_newlines=True)
        lines = result.split("\n")
        activities = []
        activities = [line.split(
        )[2] for line in lines if "ActivityRecord" in line and len(line.split()) >= 4]
        return activities

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
        # read two pictures
        img1 = cv2.imread(compare_1)
        img2 = cv2.imread(compare_2)

        # choose left-up area
        x, y, x_offset, y_offset = 50, 50, 100, 100
        img1 = img1[y:y+y_offset, x:x+x_offset]
        img2 = img2[y:y+y_offset, x:x+x_offset]

        # compare all pixel different
        diff_image = cv2.absdiff(img1, img2)
        diff_pixels = np.sum(diff_image, axis=2)  # count different pixel
        different_pixel_count = np.count_nonzero(diff_pixels)
        if different_pixel_count > 5000:
            pass

        else:
            self.logger.error('Wallpaper changed fail')

    def clean_activity(self, element):
        command = ['adb', 'shell', 'pm', 'clear', element]
        subprocess.run(
            command, capture_output=True, text=True, check=True)

    def update_file(self, element):
        command = ['adb', 'push', element, '/sdcard/']
        subprocess.run(command, check=False)

    def delete_file(self, element):
        command = ['adb', 'shell', 'rm', '/sdcard/', element]
        subprocess.run(command, shell=True, capture_output=True,
                       text=True, check=False)

    def close_app(self, element):
        self.driver.app_stop(element)
