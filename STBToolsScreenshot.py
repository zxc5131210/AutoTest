"""Screenshot test case"""
import ItemStrategy


class Screenshot(ItemStrategy.Strategy):
    menu_dict = {
        "0": "Back to main menu",
        "1": "crop",
        "2": "full screen",
        "3": "save",
        "4": "close",
        "all": "all Test",
    }

    def __init__(self, event_gen, logger, driver):
        super().__init__(event_gen, logger, driver)

    def _STB_screenshot_crop(self):
        self.logger.Test("STB Screenshot-crop")
        self.event_gen.generate_event(
            json_path="./Test_Jason/STB/Tools/Screenshot/STB_screenshot_crop.json",
            driver=self.driver,
        )

    def _STB_screenshot_full_screen(self):
        self.logger.Test("STB Screenshot-full screen")
        self.event_gen.generate_event(
            json_path="./Test_Jason/STB/Tools/Screenshot/STB_screenshot_full_screen.json",
            driver=self.driver,
        )

    def _STB_screenshot_save(self):
        self.logger.Test("STB Screenshot-save")
        self.event_gen.generate_event(
            json_path="./Test_Jason/STB/Tools/Screenshot/STB_screenshot_save.json",
            driver=self.driver,
        )

    def _STB_screenshot_close(self):
        self.logger.Test("STB Screenshot-close")
        self.event_gen.generate_event(
            json_path="./Test_Jason/STB/Tools/Screenshot/STB_screenshot_close.json",
            driver=self.driver,
        )

    def run_all(self):
        self._STB_screenshot_crop()
        self._STB_screenshot_full_screen()
        self._STB_screenshot_save()
        self._STB_screenshot_close()

    def run(self):
        while True:
            for option, test in self.menu_dict.items():
                print(f"{option}: {test}")
            choice = input("Enter your choice: ").lower()
            match choice:
                case "0":
                    return
                case "1":
                    self._STB_screenshot_crop()
                case "2":
                    self._STB_screenshot_full_screen()
                case "3":
                    self._STB_screenshot_save()
                case "4":
                    self._STB_screenshot_close()
                case "all":
                    self.run_all()
                case _:
                    print("Invalid option")
