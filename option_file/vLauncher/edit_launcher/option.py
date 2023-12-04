"""edit launcher test case"""
from option_file import item_strategy


class EditLauncher(item_strategy.Strategy):
    menu_dict = {
        "0": "Back to main menu",
        "1": "Add_delete_re-range app on hot seat",
        "2": "install Testapp and find in all apps",
        "3": "exists app error popup",
        "4": "maximum app error popup",
        "5": "confirm button",
        "all": "all Test",
    }
    folder_path = "option_file/vLauncher/edit_launcher"

    def __init__(self, event_gen, driver, reporter):
        super().__init__(event_gen, driver, reporter)

    def _edit_launcher_add_app(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/add_delete_re-rangeApps.json",
            driver=self.driver,
        )
        self.reporter.add_category("vlauncher")
        self.reporter.test_case("Test App re-range on hot seat")

    def _edit_launcher_find_all(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/find_apps_in_All.json",
            driver=self.driver,
        )
        self.reporter.add_category("vlauncher")
        self.reporter.test_case(
            "install TestApp and find TestApp in Edit Launcher - all apps"
        )

    def _exists_app_popup(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/exists_app_error_message.json",
            driver=self.driver,
        )
        self.reporter.add_category("vlauncher")
        self.reporter.test_case("exists app error message popup")

    def _maximum_app_popup(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/maximum_app_error_message.json",
            driver=self.driver,
        )
        self.reporter.add_category("vlauncher")
        self.reporter.test_case("maximum app error message popup")

    def _confirm_button(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/confirm_button.json",
            driver=self.driver,
        )
        self.reporter.add_category("vlauncher")
        self.reporter.test_case("confirm button")

    def run_all(self):
        self.reporter.test_title("---Edit Launcher---")
        self._edit_launcher_add_app()
        self._edit_launcher_find_all()
        self._exists_app_popup()
        self._maximum_app_popup()
        self._confirm_button()

    def run(self):
        while True:
            for option, test in self.menu_dict.items():
                print(f"{option}: {test}")
            choice = input("Enter your choice: ").lower()
            match choice:
                case "0":
                    return
                case "1":
                    self._edit_launcher_add_app()
                case "2":
                    self._edit_launcher_find_all()
                case "3":
                    self._exists_app_popup()
                case "4":
                    self._maximum_app_popup()
                case "5":
                    self._confirm_button()
                case "all":
                    self.run_all()
                case _:
                    print("Invalid option")
