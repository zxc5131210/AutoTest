"""Gesture Class."""
import subprocess
import cv2
import numpy as np
from logger import Logger


class Gesture:
    """
    define gesture needed
    """
    location_storage = []

    def __init__(self, driver) -> None:
        self.logger = Logger()
        if not driver:
            raise ValueError('driver can not be null.')
        self.driver = driver

    def open_activity(self, element) -> None:
        """
        open activity by package name and activity name
        args:
            element=[{package},{activity}]
        """
        package = element[0]
        activity = element[1]
        self.driver.app_start(package, activity)

    @staticmethod
    def tap(element) -> None:
        element.click()

    def tap_image(self, element) -> None:
        self.driver.image.click(element)

    def zoom_in(self, element=None) -> None:
        if element is None:
            element = self.driver()
        element.pinch_out(percent=10, steps=10)

    def zoom_out(self, element=None) -> None:
        if element is None:
            element = self.driver()
        element.pinch_in(percent=10, steps=10)

    @staticmethod
    def send_keys(element, keyword) -> None:
        element.send_keys(keyword)

    @staticmethod
    def clear_keys(element) -> None:
        element.clear_text()

    def back(self) -> None:
        """
        back by physical button
        """
        self.driver.keyevent("back")

    def screenshot(self, save_location) -> None:
        # screenshot current screen
        self.driver.screenshot(save_location)

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

    def current_app(self) -> None:
        """
        get current app
        @rtype: dict
        """
        return self.driver.app_current()

    def get_device_info(self) -> None:
        """
        get device info
        @rtype: dict
        """
        return self.driver.device_info

    def swipe_left(self, element=None) -> None:
        # swipe left function
        if element is None:
            element = self.driver()
        element.swipe("left")

    def swipe_right(self, element=None) -> None:
        # swipe left function
        if element is None:
            element = self.driver()
        element.swipe("right")

    def swipe_up(self, element=None) -> None:
        # Swipe up function
        if element is None:
            element = self.driver()
        element.swipe("up")

    def swipe_down(self, element=None) -> None:
        # Swipe up function
        if element is None:
            element = self.driver()
        element.swipe("down")

    def get_element_location(self, element) -> None:
        element_bounds = element.info['bounds']
        center_x = (element_bounds['left'] + element_bounds['right']) // 2
        center_y = (element_bounds['top'] + element_bounds['bottom']) // 2
        self.location_storage.append(center_x)
        self.location_storage.append(center_y)

    def compare_location_different(self) -> None:
        x_before = self.location_storage[0]
        y_before = self.location_storage[1]
        x_after = self.location_storage[2]
        y_after = self.location_storage[3]
        if x_before != x_after or y_before != y_after:
            pass
        else:
            self.logger.error('the element does not move')
        self.location_storage.clear()

    def drag_element_to_screen_edge(self, element, direction) -> None:
        """
        Args:
            element (str): the drag element
            direction (str): one of ("left", "right", "up", "down")
        """
        element_bounds = element.info['bounds']
        # center x,y is element center , edge x , y is screen edge , height
        center_x = (element_bounds['left'] + element_bounds['right']) // 2
        center_y = (element_bounds['top'] + element_bounds['bottom']) // 2
        edge_x = self.driver.info['displayWidth'] - 1
        edge_y = self.driver.info['displayHeight'] - 1

        assert direction in ("left", "right", "up", "down")
        if direction == 'up':
            self.driver.drag(center_x, center_y, center_x, 0)
        elif direction == 'down':
            self.driver.drag(center_x, center_y, center_x, edge_y)
        elif direction == 'left':
            self.driver.drag(center_x, center_y, 0, center_y)
        elif direction == 'right':
            self.driver.drag(center_x, center_y, edge_x, center_y)

    @staticmethod
    def install_app(element) -> None:
        command = ['adb', 'install', "-r", element]
        subprocess.run(command, check=False)

    @staticmethod
    def uninstall_app(element) -> None:
        """
        uninstall the application
        args:
            element= package name
        """
        command = ['adb', 'uninstall', element]
        subprocess.run(command, check=False)

    def file_is_exists(self, filepath) -> None:
        """
        verify the file is existing
        args: filepath
        """
        command = f'adb shell ls {filepath}'
        try:
            result = subprocess.run(command, check=False, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, shell=True, text=True)
            # check the command success or not
            if result.returncode == 0:
                pass
            else:
                self.logger.error('file is not exist')
        except subprocess.CalledProcessError:
            self.logger.error('file is not exist')

    @staticmethod
    def get_overview_activities() -> list[str]:
        result = subprocess.check_output(
            ["adb", "shell", "dumpsys", "activity", "recents"], universal_newlines=True)
        lines = result.split("\n")
        activities = []
        activities = [line.split(
        )[2] for line in lines if "ActivityRecord" in line and len(line.split()) >= 4]
        return activities

    def check_background_activities(self, element) -> None:
        """
         check background activities match the app or not
        """
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
        """
        compare two pixel different , if different pixel over 3000
        determine the difference between two pictures
        """
        # read two pictures
        img1 = cv2.imread(compare_1)
        img2 = cv2.imread(compare_2)

        # compare all pixel different
        diff_image = cv2.absdiff(img1, img2)
        diff_pixels = np.sum(diff_image, axis=2)  # count different pixel
        different_pixel_count = np.count_nonzero(diff_pixels)
        if different_pixel_count > 3000:
            pass

        else:
            self.logger.error('compare different fail')

    @staticmethod
    def clean_activity(element):
        """
        clean activity user data
        arg: element= package name
        """
        command = ['adb', 'shell', 'pm', 'clear', element]
        subprocess.run(
            command, capture_output=True, text=True, check=True)

    @staticmethod
    def update_file(element):
        command = ['adb', 'push', element, '/sdcard/']
        subprocess.run(command, check=False)

    @staticmethod
    def delete_file(element):
        command = f'adb shell rm /sdcard/{element}'
        subprocess.run(command, shell=True, capture_output=True,
                       text=True, check=False)

    def get_file_count(self, element):
        command = f'adb shell ls -1 /sdcard/{element} | wc -l'
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        file_count = int(result.stdout.strip())
        if file_count >= 1:
            pass
        else:
            self.logger.error(f"no file in {element}")

    @staticmethod
    def reboot():
        command = ['adb', 'reboot']
        subprocess.run(command, check=True)

    @staticmethod
    def wait_for_device():
        command = ['adb', 'wait-for-device']
        subprocess.run(command, check=True)

    def close_app(self, element):
        self.driver.app_stop(element)
