"""vLauncher title test case"""
from option_file import item_strategy


class vLauncherTitle(item_strategy.Strategy):
    menu_dict = {
        "0": "Back to main menu",
        "1": "change title",
        "2": "Set Password",
        "3": "reset Password",
        "4": "clear Password",
        "5": "Reveal Password",
        "all": "all Test",
    }
    folder_path = "option_file/vLauncher/title"

    def __init__(self, event_gen, driver, reporter):
        super().__init__(event_gen, driver, reporter)

    def _change_title(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/change_title.json",
            driver=self.driver,
        )
        self.reporter.add_category("vlauncher")
        self.reporter.test_case("change title")

    def _set_password(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/set_password.json",
            driver=self.driver,
        )
        self.reporter.add_category("vlauncher")
        self.reporter.test_case("set title password")

    def _reset_password(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/reset_password.json",
            driver=self.driver,
        )
        self.reporter.add_category("vlauncher")
        self.reporter.test_case("reset title password")

    def _clear_password(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/clear_password.json",
            driver=self.driver,
        )
        self.reporter.add_category("vlauncher")
        self.reporter.test_case("clear title password")

    def run_all(self):
        self.reporter.test_title("---Title---")
        self._change_title()
        self._set_password()
        self._reset_password()
        self._clear_password()

    def run(self):
        while True:
            for option, test in self.menu_dict.items():
                print(f"{option}: {test}")
            choice = input("Enter your choice: ").lower()
            match choice:
                case "0":
                    return
                case "1":
                    self._change_title()
                case "2":
                    self._set_password()
                case "3":
                    self._reset_password()
                case "4":
                    self._clear_password()
                case "all":
                    self.run_all()
                case _:
                    print("Invalid option")
