"""user select test case"""
from option_file import item_strategy


class UserSelect(item_strategy.Strategy):
    menu_dict = {
        "0": "Back to main menu",
        "1": "guest",
        "2": "sign in",
        "3": "",
        "4": "",
        "5": "",
        "6": "",
        "all": "all Test",
    }
    folder_path = "option_file/vLauncher/user_select"

    def __init__(self, event_gen, driver, reporter):
        super().__init__(event_gen, driver, reporter)

    def _guest(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/guest_button.json",
            driver=self.driver,
        )
        self.reporter.add_category("vlauncher")
        self.reporter.test_case("guest")

    def _sign_in(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/sign_in_button.json",
            driver=self.driver,
        )
        self.reporter.add_category("vlauncher")
        self.reporter.test_case("sign in button")

    def run_all(self):
        self.reporter.test_title("---User Select---")
        self._guest()
        self._sign_in()

    def run(self):
        while True:
            for option, test in self.menu_dict.items():
                print(f"{option}: {test}")
            choice = input("Enter your choice: ").lower()
            match choice:
                case "0":
                    return
                case "1":
                    self._guest()
                case "2":
                    self._sign_in()
                case "3":
                    pass
                case "4":
                    pass
                case "5":
                    pass
                case "6":
                    pass
                case "all":
                    self.run_all()
                case _:
                    print("Invalid option")
