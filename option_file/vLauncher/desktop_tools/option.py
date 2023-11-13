"""desktop tools test case"""
from option_file import item_strategy


class vLauncherTools(item_strategy.Strategy):
    menu_dict = {
        "0": "back to previous page",
        "1": "Date & Time",
        "2": "Device tip",
        "3": "Drag seekbar to set the backlight",
        "4": "set auto backlight",
        "all": "all Test",
    }
    folder_path = "option_file/vLauncher/desktop_tools"

    def __init__(self, event_gen, driver, reporter):
        super().__init__(event_gen, driver, reporter)

    def _date_and_time(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/date_and_time.json",
            driver=self.driver,
        )
        self.reporter.add_category("vlauncher")
        self.reporter.test_case("date & time")

    def _device_tip(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/device_tip.json",
            driver=self.driver,
        )
        self.reporter.add_category("vlauncher")
        self.reporter.test_case("device tip")

    def _backlight_seekbar(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/backlight_seekbar.json",
            driver=self.driver,
        )
        self.reporter.add_category("vlauncher")
        self.reporter.test_case("backlight by seekbar")

    def _backlight_auto(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/backlight_auto.json",
            driver=self.driver,
        )
        self.reporter.add_category("vlauncher")
        self.reporter.test_case("backlight by autobrightness")

    def _volume(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/volume.json",
            driver=self.driver,
        )
        self.reporter.add_category("vlauncher")
        self.reporter.test_case("set volume")

    def run_all(self):
        self.reporter.test_title("---desktop tools---")
        self._date_and_time()
        self._device_tip()
        self._backlight_seekbar()
        self._backlight_auto()
        self._volume()

    def run(self):
        while True:
            for option, test in self.menu_dict.items():
                print(f"{option}: {test}")
            choice = input("Enter your choice: ").lower()
            match choice:
                case "0":
                    return
                case "1":
                    self._date_and_time()
                case "2":
                    self._device_tip()
                case "3":
                    self._backlight_seekbar()
                case "4":
                    self._backlight_auto()
                case "5":
                    self._volume()
                case "all":
                    self.run_all()
                case _:
                    print("Invalid option")
