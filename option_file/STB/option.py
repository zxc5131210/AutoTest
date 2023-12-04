"""STB test case"""
from option_file.STB.Tools.option import STBTools
from option_file import item_strategy


class STB(item_strategy.Strategy):
    menu_dict = {
        "0": "Back to main menu",
        "1": "back button",
        "2": "homepage button",
        "3": "element in all apps",
        "4": "add & delete apps in shortcut",
        "5": "app order in shortcut",
        "6": "add & delete tools in shortcut",
        "7": "tools order in shortcut",
        "8": "exists apps error message",
        "9": "maximum apps error message",
        "10": "STB tools",
        "all": "all test",
    }
    folder_path = "option_file/STB"

    def __init__(self, event_gen, driver, reporter):
        super().__init__(event_gen, driver, reporter)

    # STB first class
    def _STB_back_btn(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/FirstClass/back_button.json",
            driver=self.driver,
        )
        self.reporter.add_category("STB")
        self.reporter.test_case("STB-back button")

    def _STB_homepage_btn(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/FirstClass/homepage_button.json",
            driver=self.driver,
        )
        self.reporter.add_category("STB")
        self.reporter.test_case("STB-homepage button")

    # STB_Second class

    def _STB_element_in_all_apps(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/SecondClass/app_show_in_all_apps.json",
            driver=self.driver,
        )
        self.reporter.add_category("STB")
        self.reporter.test_case("STB_apps-element in all apps")

    def _STB_apps_add_delete_app_in_shortcut(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/SecondClass/add_delete_app_shortcut.json",
            driver=self.driver,
        )
        self.reporter.add_category("STB")
        self.reporter.test_case("STB_apps-add & delete apps in shortcut")

    def _STB_apps_order_in_shortcut(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/SecondClass/app_order_in_shortcut.json",
            driver=self.driver,
        )
        self.reporter.add_category("STB")
        self.reporter.test_case("STB_apps-app order in shortcut")

    # STB_Third class

    def _STB_tools_add_delete_app_in_shortcut(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/ThirdClass/add_delete_app_shortcut.json",
            driver=self.driver,
        )
        self.reporter.add_category("STB")
        self.reporter.test_case("STB_tools-add & delete apps in shortcut")

    def _STB_tools_order_in_shortcut(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/ThirdClass/app_order_in_shortcut.json",
            driver=self.driver,
        )
        self.reporter.add_category("STB")
        self.reporter.test_case("STB_tools-app order in shortcut")

    def _STB_exists_apps_error_message(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/SecondClass/exists_apps_popup.json",
            driver=self.driver,
        )
        self.reporter.add_category("STB")
        self.reporter.test_case("STB_apps-error message popup of exists app")

    def _STB_maximum_apps_error_message(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/SecondClass/maximum_apps_popup.json",
            driver=self.driver,
        )
        self.reporter.add_category("STB")
        self.reporter.test_case("STB_apps-maximum apps error message popup")

    def run_all(self):
        # STB root_view
        self.reporter.test_title("---STB root view---")
        self._STB_back_btn()
        self._STB_homepage_btn()
        self._STB_apps_add_delete_app_in_shortcut()
        self._STB_apps_order_in_shortcut()
        self._STB_element_in_all_apps()
        self._STB_tools_add_delete_app_in_shortcut()
        self._STB_tools_order_in_shortcut()
        self._STB_exists_apps_error_message()
        self._STB_maximum_apps_error_message()
        # STB Tools
        STBTools(
            event_gen=self.event_gen, driver=self.driver, reporter=self.reporter
        ).run_all()

    def run(self):
        while True:
            for option, test in self.menu_dict.items():
                print(f"{option}: {test}")
            choice = input("Enter your choice: ").lower()
            match choice:
                case "0":
                    return
                case "1":
                    self._STB_back_btn()
                case "2":
                    self._STB_homepage_btn()
                case "3":
                    self._STB_element_in_all_apps()
                case "4":
                    self._STB_apps_add_delete_app_in_shortcut()
                case "5":
                    self._STB_apps_order_in_shortcut()
                case "6":
                    self._STB_tools_add_delete_app_in_shortcut()
                case "7":
                    self._STB_tools_order_in_shortcut()
                case "8":
                    self._STB_exists_apps_error_message()
                case "9":
                    self._STB_maximum_apps_error_message()
                case "10":
                    STBTools(
                        event_gen=self.event_gen,
                        driver=self.driver,
                        reporter=self.reporter,
                    ).run()
                case "all":
                    self.run_all()
                case _:
                    print("Invalid option")
