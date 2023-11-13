"""Screenshot test case"""
from option_file import item_strategy


class Screenshot(item_strategy.Strategy):
    menu_dict = {
        "0": "Back to main menu",
        "1": "crop",
        "2": "full screen",
        "3": "save",
        "4": "close",
        "all": "all Test",
    }
    folder_path = "option_file/STB/Tools/Screenshot"

    def __init__(self, event_gen, driver, reporter):
        super().__init__(event_gen, driver, reporter)

    def _STB_screenshot_crop(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/crop.json",
            driver=self.driver,
        )
        self.reporter.add_category("STB")
        self.reporter.test_case("Screenshot-crop")

    def _STB_screenshot_full_screen(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/full_screen.json",
            driver=self.driver,
        )
        self.reporter.add_category("STB")
        self.reporter.test_case("Screenshot-full screen")

    def _STB_screenshot_save(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/save.json",
            driver=self.driver,
        )
        self.reporter.add_category("STB")
        self.reporter.test_case("Screenshot-save")

    def _STB_screenshot_close(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/close.json",
            driver=self.driver,
        )
        self.reporter.add_category("STB")
        self.reporter.test_case("Screenshot-close")

    def run_all(self):
        self.reporter.test_title("---STB Tool - Screenshot---")
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
