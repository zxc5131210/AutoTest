"""Authenticator test case"""
from option_file import item_strategy


class Authenticator(item_strategy.Strategy):
    menu_dict = {
        "0": "Back to main menu",
        "1": "myviewboard account",
        "2": "",
        "3": "",
        "4": "",
        "5": "",
        "all": "all Test",
    }
    folder_path = "option_file/Authenticator"

    def __init__(self, event_gen, driver, reporter):
        super().__init__(event_gen, driver, reporter)

    def _login_by_myviewboard(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/login_by_myviewboard.json",
            driver=self.driver,
        )
        self.reporter.add_category("authenticator")
        self.reporter.test_case("login by myviewboard account")

    def run_all(self):
        self.reporter.test_title("---Authenticator---")

    def run(self):
        while True:
            for option, test in self.menu_dict.items():
                print(f"{option}: {test}")
            choice = input("Enter your choice: ").lower()
            match choice:
                case "0":
                    return
                case "1":
                    self._login_by_myviewboard()
                case "2":
                    pass
                case "3":
                    pass
                case "4":
                    pass
                case "5":
                    pass
                case "all":
                    self.run_all()
                case _:
                    print("Invalid option")
