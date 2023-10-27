"""edit launcher test case"""
import ItemStrategy


class EditLauncher(ItemStrategy.Strategy):
    menu_dict = {
        "0": "Back to main menu",
        "1": "Add_delete_re-range app on hot seat",
        "2": "install Testapp and find in all apps",
        "all": "all Test",
    }
    folder_path = "Test_Jason/vLauncher/Edit_Launcher"

    def __init__(self, event_gen, logger, driver):
        super().__init__(event_gen, logger, driver)

    def _edit_launcher_add_app(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/editLauncher_add_delete_re-rangeApps.json",
            driver=self.driver,
        )
        self.report["category"] = "vlauncher"
        self.logger.Test("Test App re-range on hot seat")

    def _edit_launcher_find_all(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/editLauncher_find_apps_in_All.json",
            driver=self.driver,
        )
        self.report["category"] = "vlauncher"
        self.logger.Test("install TestApp and find TestApp in Edit Launcher - all apps")

    def run_all(self):
        self.logger.test_title("---Edit Launcher---")
        self._edit_launcher_add_app()
        self._edit_launcher_find_all()

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
                case "all":
                    self.run_all()
                case _:
                    print("Invalid option")
