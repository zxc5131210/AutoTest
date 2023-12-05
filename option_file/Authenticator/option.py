"""Authenticator test case"""
from option_file import item_strategy


class Authenticator(item_strategy.Strategy):
    menu_dict = {
        "0": "Back to main menu",
        "1": "myviewboard account",
        "2": "google SSO",
        "3": "microsoft SSO",
        "4": "education SSO",
        "5": "auto login viewboard by myviewboard account",
        "6": "auto login viewboard by google SSO",
        "7": "auto login viewboard by microsoft SSO",
        "8": "auto login viewboard by education SSO",
        "9": "back button",
        "10": "duplicate login by myviewboard",
        "11": "duplicate login by google SSO",
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

    def _login_by_google(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/login_by_google.json",
            driver=self.driver,
        )
        self.reporter.add_category("authenticator")
        self.reporter.test_case("login by google account")

    def _login_by_microsoft(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/login_by_microsoft.json",
            driver=self.driver,
        )
        self.reporter.add_category("authenticator")
        self.reporter.test_case("login by microsoft account")

    def _login_by_education(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/login_by_education.json",
            driver=self.driver,
        )
        self.reporter.add_category("authenticator")
        self.reporter.test_case("login by education account")

    def _auto_login_myviewboard_by_myviewboard(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/auto_login_myviewboard.json",
            driver=self.driver,
        )
        self.reporter.add_category("authenticator")
        self.reporter.test_case("auto login viewboard by myviewboard account")

    def _auto_login_myviewboard_by_google(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/auto_login_google.json",
            driver=self.driver,
        )
        self.reporter.add_category("authenticator")
        self.reporter.test_case("auto login viewboard by google account")

    def _auto_login_myviewboard_by_microsoft(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/auto_login_microsoft.json",
            driver=self.driver,
        )
        self.reporter.add_category("authenticator")
        self.reporter.test_case("auto login viewboard by microsoft account")

    def _auto_login_myviewboard_by_education(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/auto_login_education.json",
            driver=self.driver,
        )
        self.reporter.add_category("authenticator")
        self.reporter.test_case("auto login viewboard by education account")

    def _back_button(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/back_button.json",
            driver=self.driver,
        )
        self.reporter.add_category("authenticator")
        self.reporter.test_case("back button")

    def _duplicate_login_myviewboard(self):
        for _ in range(10):
            self.event_gen.generate_event(
                json_path=f"{self.folder_path}/login_by_myviewboard.json",
                driver=self.driver,
            )
        self.reporter.add_category("authenticator")
        self.reporter.test_case("duplicate login by myviewboard")

    def _duplicate_login_google(self):
        for _ in range(10):
            self.event_gen.generate_event(
                json_path=f"{self.folder_path}/login_by_google.json",
                driver=self.driver,
            )
        self.reporter.add_category("authenticator")
        self.reporter.test_case("duplicate login by google SSO")

    def run_all(self):
        self.reporter.test_title("---Authenticator---")
        self._login_by_myviewboard()
        self._login_by_google()
        self._login_by_microsoft()
        self._login_by_education()
        self._auto_login_myviewboard_by_myviewboard()
        self._auto_login_myviewboard_by_google()
        self._auto_login_myviewboard_by_microsoft()
        self._auto_login_myviewboard_by_education()
        self._back_button()
        self._duplicate_login_myviewboard()
        self._duplicate_login_google()

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
                    self._login_by_google()
                case "3":
                    self._login_by_microsoft()
                case "4":
                    self._login_by_education()
                case "5":
                    self._auto_login_myviewboard_by_myviewboard()
                case "6":
                    self._auto_login_myviewboard_by_google()
                case "7":
                    self._auto_login_myviewboard_by_microsoft()
                case "8":
                    self._auto_login_myviewboard_by_education()
                case "9":
                    self._back_button()
                case "10":
                    self._duplicate_login_myviewboard()
                case "11":
                    self._duplicate_login_google()
                case "all":
                    self.run_all()
                case _:
                    print("Invalid option")
