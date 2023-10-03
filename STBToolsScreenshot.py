"""Screenshot test case"""


class Screenshot:

    def __init__(self, event_gen, logger, driver):
        self.event_gen = event_gen
        self.logger = logger
        self.driver = driver

    def STB_screenshot_all(self):
        self._STB_screenshot_crop()
        self._STB_screenshot_full_screen()
        self._STB_screenshot_save()
        self._STB_screenshot_close()

    def _STB_screenshot_crop(self):
        self.logger.Test('STB Screenshot-crop')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/Tools/Screenshot/STB_screenshot_crop.json', driver=self.driver)

    def _STB_screenshot_full_screen(self):
        self.logger.Test('STB Screenshot-full screen')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/Tools/Screenshot/STB_screenshot_full_screen.json', driver=self.driver)

    def _STB_screenshot_save(self):
        self.logger.Test('STB Screenshot-save')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/Tools/Screenshot/STB_screenshot_save.json', driver=self.driver)

    def _STB_screenshot_close(self):
        self.logger.Test('STB Screenshot-close')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/Tools/Screenshot/STB_screenshot_close.json', driver=self.driver)

    def run(self):
        while True:
            print("Freezer Options:")
            print("0: Back to main menu")
            print("1: crop")
            print("2: full screen")
            print("3: save")
            print("4: close")
            print("5: ")
            print("ALL")

            choice = input("Enter your choice: ")

            if choice == '0':
                return
            elif choice == '1':
                self._STB_screenshot_crop()
            elif choice == '2':
                self._STB_screenshot_full_screen()
            elif choice == '3':
                self._STB_screenshot_save()
            elif choice == '4':
                self._STB_screenshot_close()
            elif choice == '5':
                pass
            elif choice.lower() == 'all':
                self.STB_screenshot_all()
            else:
                print("Invalid option")
