"""Quicksetting test case"""
import ItemStrategy


class Quicksetting(ItemStrategy.Strategy):
    menu_dict = {
        "0": "Back to main menu",
        "1": "backlight",
        "2": "volume",
        "3": "auto brightness",
        "4": "eye care",
        "5": "color temperature",
        "all": "all Test",
    }

    def __init__(self, event_gen, logger, driver):
        super().__init__(event_gen, logger, driver)

    def _STB_quicksetting_backlight(self):
        self.logger.Test("STB quicksetting - backlight")
        self.event_gen.generate_event(
            json_path="./Test_Jason/STB/Quicksetting/STB_quicksetting_backlight.json",
            driver=self.driver,
        )

    def _STB_quicksetting_volume(self):
        self.logger.Test("STB quicksetting - volume")
        self.event_gen.generate_event(
            json_path="./Test_Jason/STB/Quicksetting/STB_quicksetting_volume.json",
            driver=self.driver,
        )

    def _STB_quicksetting_auto_brightness(self):
        self.logger.Test("STB quicksetting - autobrightness")
        self.event_gen.generate_event(
            json_path="Test_Jason/STB/Quicksetting/STB_quicksetting_auto_brightness.json",
            driver=self.driver,
        )

    def _STB_quicksetting_eye_care(self):
        self.logger.Test("STB quicksetting - eye care")
        self.event_gen.generate_event(
            json_path="./Test_Jason/STB/Quicksetting/STB_quicksetting_eye_care.json",
            driver=self.driver,
        )

    def _STB_quicksetting_color_temperature(self):
        self.logger.Test("STB quicksetting - color temperature")
        self.event_gen.generate_event(
            json_path="./Test_Jason/STB/Quicksetting/STB_quicksetting_color_temperature.json",
            driver=self.driver,
        )

    def run_all(self):
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
