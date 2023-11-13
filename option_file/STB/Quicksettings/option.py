"""Quicksettings test case"""
from option_file import item_strategy


class Quicksettings(item_strategy.Strategy):
    menu_dict = {
        "0": "Back to main menu",
        "1": "backlight",
        "2": "volume",
        "3": "auto brightness",
        "4": "eye care",
        "5": "color temperature",
        "all": "all Test",
    }
    folder_path = "option_file/STB/Quicksettings"

    def __init__(self, event_gen, driver, reporter):
        super().__init__(event_gen, driver, reporter)

    def _STB_quicksetting_backlight(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/backlight.json",
            driver=self.driver,
        )
        self.reporter.add_category("quicksettings")
        self.reporter.test_case("backlight")

    def _STB_quicksetting_volume(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/volume.json",
            driver=self.driver,
        )
        self.reporter.add_category("quicksettings")
        self.reporter.test_case("volume")

    def _STB_quicksetting_auto_brightness(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/auto_brightness.json",
            driver=self.driver,
        )
        self.reporter.add_category("quicksettings")
        self.reporter.test_case("autobrightness")

    def _STB_quicksetting_eye_care(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/eye_care.json",
            driver=self.driver,
        )
        self.reporter.add_category("quicksettings")
        self.reporter.test_case("eye care")

    def _STB_quicksetting_color_temperature(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/color_temperature.json",
            driver=self.driver,
        )
        self.reporter.add_category("quicksettings")
        self.reporter.test_case("color temperature")

    def run_all(self):
        self.reporter.test_title("---STB - QuickSetting---")
        self._STB_quicksetting_backlight()
        self._STB_quicksetting_volume()
        self._STB_quicksetting_auto_brightness()
        self._STB_quicksetting_eye_care()
        self._STB_quicksetting_color_temperature()

    def run(self):
        while True:
            for option, test in self.menu_dict.items():
                print(f"{option}: {test}")
            choice = input("Enter your choice: ").lower()
            match choice:
                case "0":
                    return
                case "1":
                    self._STB_quicksetting_backlight()
                case "2":
                    self._STB_quicksetting_volume()
                case "3":
                    self._STB_quicksetting_auto_brightness()
                case "4":
                    self._STB_quicksetting_eye_care()
                case "5":
                    self._STB_quicksetting_color_temperature()
                case "all":
                    self.run_all()
                case _:
                    print("Invalid option")
