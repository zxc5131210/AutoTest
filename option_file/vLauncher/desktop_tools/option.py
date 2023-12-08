"""desktop tools test case"""
from option_file import item_strategy


class TestCase:
    def __init__(self, description, json_path):
        self.description = description
        self.json_path = json_path


class vLauncherTools(item_strategy.Strategy):
    test_cases = [
        TestCase("Date & Time", "date_and_time.json"),
        TestCase("Device tip", "device_tip.json"),
        TestCase("Drag seekbar to set the backlight", "backlight_seekbar.json"),
        TestCase("set auto backlight", "backlight_auto.json"),
        TestCase("set volume", "volume.json"),
        TestCase("ethernet settings", "ethernet.json"),
        TestCase("wifi settings", "wifi.json"),
        TestCase("input source", "input_source.json"),
        TestCase("sign out button", "sign_out_button.json"),
    ]
    folder_path = "option_file/vLauncher/desktop_tools"

    def __init__(self, event_gen, driver, reporter):
        super().__init__(event_gen, driver, reporter)

    def run(self, test_case):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/{test_case.json_path}",
            driver=self.driver,
        )
        self.reporter.test_case(test_case.description)

    def run_all(self):
        self.reporter.test_title("---desktop tools---")
        for test_case in self.test_cases:
            self.run(test_case)

    def invalid(self, choice_int) -> bool:
        return choice_int < -1 or choice_int > len(self.test_cases)

    def run_with_interaction(self):
        while True:
            self.print_option()
            choice = input("Enter your choice: ").lower()
            try:
                choice_int = int(choice)
                if self.invalid(choice_int):
                    raise ValueError
                if choice_int == -1:
                    return
                if choice_int == len(self.test_cases):
                    self.run_all()
                    continue
                self.run(self.test_cases[choice_int])
            except ValueError:
                print(
                    "Invalid input. Please enter a valid choice, range is between -1 ~ length of test cases."
                )
