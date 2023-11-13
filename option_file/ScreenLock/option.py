"""screen lock test case"""
from option_file import item_strategy


class ScreenLock(item_strategy.Strategy):
    menu_dict = {
        "0": "Back to main menu",
        "1": "Set Password",
        "2": "Change Password",
        "3": "Remove Password",
        "4": "Reveal Password",
        "all": "all Test",
    }
    folder_path = "option_file/ScreenLock"

    def __init__(self, event_gen, driver, reporter):
        super().__init__(event_gen, driver, reporter)

    def _screen_lock_set_password(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/set_password.json",
            driver=self.driver,
        )
        self.reporter.add_category("screenlock")
        self.reporter.test_case("Set screenLock Password")

    def _screen_lock_change_password(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/change_password.json",
            driver=self.driver,
        )
        self.reporter.add_category("screenlock")
        self.reporter.test_case("Change screenLock Password")

    def _screen_lock_remove_password(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/remove_password.json",
            driver=self.driver,
        )
        self.reporter.add_category("screenlock")
        self.reporter.test_case("Change screenLock Password")

    def _screen_lock_reveal_password(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/reveal_password.json",
            driver=self.driver,
        )
        self.reporter.add_category("screenlock")
        self.reporter.test_case("Reveal Password in screenLock")

    def run_all(self):
        self.reporter.test_title("---ScreenLock---")
        self._screen_lock_set_password()
        self._screen_lock_change_password()
        self._screen_lock_remove_password()
        self._screen_lock_reveal_password()

    def run(self):
        while True:
            for option, test in self.menu_dict.items():
                print(f"{option}: {test}")
            choice = input("Enter your choice: ").lower()
            match choice:
                case "0":
                    return
                case "1":
                    self._screen_lock_set_password()
                case "2":
                    self._screen_lock_change_password()
                case "3":
                    self._screen_lock_remove_password()
                case "4":
                    self._screen_lock_reveal_password()
                case "all":
                    self.run_all()
                case _:
                    print("Invalid option")
