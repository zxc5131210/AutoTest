"""Gesture Class."""
import logging
import subprocess
import time
import cv2
import numpy as np
import remote_controller_map


class Gesture:
    """
    define gesture needed
    """

    compare_different_list = []

    def __init__(self, driver, reporter) -> None:
        if not driver:
            raise ValueError("driver can not be null.")
        self.driver = driver
        self.reporter = reporter

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
        element = element or self.driver()
        element.pinch_out(percent=10, steps=10)

    def zoom_out(self, element=None) -> None:
        element = element or self.driver()
        element.pinch_in(percent=10, steps=10)

    @staticmethod
    def send_keys(element, keyword) -> None:
        element.send_keys(keyword)

    @staticmethod
    def clear_keys(element) -> None:
        element.clear_text()

    @staticmethod
    def get_element_text(element):
        return element.get_text()

    def back(self) -> None:
        """
        back by physical button
        """
        self.driver.keyevent("back")

    def screenshot(self, save_location) -> None:
        # screenshot current screen
        self.driver.screenshot(save_location)

    def long_press_location(self, location_x, location_y):
        self.driver.click(x=location_x, y=location_y)
        self.driver.long_click(x=location_x, y=location_y)

    def home_page(self) -> None:
        # home page button
        self.driver.keyevent("home")

    def overview_page(self) -> None:
        # overview button
        self.driver.keyevent("overview")

    def quit_driver(self) -> None:
        # quit driver
        self.driver.quit()

    def current_app(self):
        """
        get current app
        @rtype: dict
        """
        return self.driver.app_current()

    def get_device_info(self):
        """
        get device info
        @rtype: dict
        """
        return self.driver.device_info

    def get_toast(self):
        return self.driver.toast.get_message()

    def swipe_left(self, element=None) -> None:
        # swipe left function
        element = element or self.driver()
        element.swipe("left")

    def swipe_right(self, element=None) -> None:
        # swipe left function
        element = element or self.driver()
        element.swipe("right")

    def swipe_up(self, element=None) -> None:
        # Swipe up function
        element = element or self.driver()
        element.swipe("up")

    def swipe_down(self, element=None) -> None:
        # Swipe up function
        element = element or self.driver()
        element.swipe("down")

    @staticmethod
    def wait_element_exist(element):
        element.wait()

    def scroll_down(self, element=None) -> None:
        # scroll down function
        element = element or self.driver()
        element.scroll.toEnd()

    def get_element_location(self, element) -> None:
        element_bounds = element.info["bounds"]
        center_x = (element_bounds["left"] + element_bounds["right"]) // 2
        center_y = (element_bounds["top"] + element_bounds["bottom"]) // 2
        self.compare_different_list.extend([center_x, center_y])

    def drag_element_to_screen_edge(self, element, direction) -> None:
        """
        Args:
            element (str): the drag element
            direction (str): one of ("left", "right", "up", "down")
        """
        element_bounds = element.info["bounds"]
        # center x,y is element center , edge x , y is screen edge , height
        center_x = (element_bounds["left"] + element_bounds["right"]) // 2
        center_y = (element_bounds["top"] + element_bounds["bottom"]) // 2
        edge_x = self.driver.info["displayWidth"] - 1
        edge_y = self.driver.info["displayHeight"] - 1

        assert direction in ("left", "right", "up", "down")
        if direction == "up":
            self.driver.drag(center_x, center_y, center_x, 0)
        elif direction == "down":
            self.driver.drag(center_x, center_y, center_x, edge_y)
        elif direction == "left":
            self.driver.drag(center_x, center_y, 0, center_y)
        elif direction == "right":
            self.driver.drag(center_x, center_y, edge_x, center_y)

    @staticmethod
    def install_app(element) -> None:
        command = ["adb", "install", "-r", element]
        subprocess.run(command, check=False)

    @staticmethod
    def uninstall_app(element) -> None:
        """
        uninstall the application
        args:
            element= package name
        """
        subprocess.run(["adb", "uninstall", element], check=False)

    def file_is_exists(self, filepath) -> None:
        """
        verify the file is existing
        args: filepath
        """
        command = f"adb shell ls {filepath}"
        try:
            result = subprocess.run(
                command,
                check=False,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True,
                text=True,
            )
            # check the command success or not
            if result.returncode != 0:
                logging.error(msg="file is not exist")
                self.reporter.fail_step("error", "file is not exist")
        except subprocess.CalledProcessError:
            logging.error(msg="file is not exist")
            self.reporter.fail_step("error", "file is not exist")

    @staticmethod
    def get_overview_activities() -> list[str]:
        result = subprocess.check_output(
            ["adb", "shell", "dumpsys", "activity", "recents"], universal_newlines=True
        )
        lines = result.split("\n")
        activities = [
            line.split()[2]
            for line in lines
            if "ActivityRecord" in line and len(line.split()) >= 4
        ]
        return activities

    def check_background_activities(self, element) -> None:
        """
        check background activities match the app or not
        """
        overview_activities = self.get_overview_activities()
        if not overview_activities:
            logging.error(msg="not find the event.")
            self.reporter.fail_step("error", f"{element} not in the background")
            return
        if any(element in background for background in overview_activities):
            logging.info(msg=f"{element} in the background")
        else:
            logging.error(msg=f"{element} not in background")
            self.reporter.fail_step("error", f"{element} not in background")

    def compare_images_pixel(self, compare_1, compare_2) -> None:
        """
        compare two pixel different , if different pixel over 5000
        determine the difference between two pictures
        """
        # read two pictures
        img1 = cv2.imread(compare_1)
        img2 = cv2.imread(compare_2)

        # compare all pixel different
        diff_image = cv2.absdiff(img1, img2)
        diff_pixels = np.sum(diff_image, axis=2)  # count different pixel
        different_pixel_count = np.count_nonzero(diff_pixels)
        if different_pixel_count > 5000:
            pass
        else:
            logging.error(msg="compare different fail")
            self.reporter.fail_step("error", "compare different fail")

    @staticmethod
    def clean_activity(element):
        """
        clean activity user data
        arg: element= package name
        """
        subprocess.run(
            ["adb", "shell", "pm", "clear", element],
            capture_output=True,
            text=True,
            check=True,
        )
        time.sleep(5)

    @staticmethod
    def update_file(element):
        subprocess.run(["adb", "push", element, "/sdcard/"], check=False)

    @staticmethod
    def delete_file(element):
        subprocess.run(
            f"adb shell rm /sdcard/{element}",
            shell=True,
            capture_output=True,
            text=True,
            check=False,
        )

    @staticmethod
    def get_volume():
        command = "adb shell settings get system volume_music_speaker"
        volume = subprocess.run(
            command, shell=True, capture_output=True, text=True, check=False
        ).stdout
        return volume

    def get_file_count(self, element):
        command = f"adb shell ls -1 /sdcard/{element} | wc -l"
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, check=False
        )
        file_count = int(result.stdout.strip())
        if file_count < 1:
            logging.error(msg=f"no file in {element}")
            self.reporter.fail_step("error", f"no file in {element}")

    @staticmethod
    def reboot():
        subprocess.run(["adb", "reboot"], check=True)

    @staticmethod
    def wait_for_device():
        subprocess.run(["adb", "wait-for-device"], check=True)

    def close_app(self, element):
        self.driver.app_stop(element)

    def send_event(self, event):
        device_model = self.driver.device_info["model"]
        # get model to map
        if device_model == "IFP8633" or device_model == "IFP7550-5":
            controller_map = remote_controller_map.ifp33_keycode
        else:
            controller_map = None
            logging.error(msg=f"can't map the device")
            self.reporter.fail_step("error", "can't map the device")

        send_event = controller_map[event]
        input_event = "/dev/input/event{}".format(controller_map["input_event"])
        subprocess.call(
            ["adb", "shell", "sendevent", input_event, "1", f"{send_event}", "1"]
        )
        subprocess.call(["adb", "shell", "sendevent", input_event, "0", "0", "0"])
        subprocess.call(
            ["adb", "shell", "sendevent", input_event, "1", f"{send_event}", "0"]
        )
        subprocess.call(["adb", "shell", "sendevent", input_event, "0", "0", "0"])
