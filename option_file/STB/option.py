"""STB test case"""
from option_file.vLauncher.recent_app.option import RecentApp
from option_file.STB.Quicksetting.option import Quicksettings
from option_file.STB.Tools.option import STBTools
import item_strategy


class STB(item_strategy.Strategy):
    menu_dict = {
        "0": "Back to main menu",
        "1": "back button",
        "2": "homepage button",
        "3": "recent app",
        "4": "element in all apps",
        "5": "add & delete apps in shortcut",
        "6": "app order in shortcut",
        "7": "add & delete tools in shortcut",
        "8": "tools order in shortcut",
        "9": "STB tools",
        "10": "QuickSetting",
        "all": "all test",
    }
    folder_path = "option_file/STB"

    def __init__(self, event_gen, logger, driver):
        super().__init__(event_gen, logger, driver)

    # STB first class
    def _STB_back_btn(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/FirstClass/STB_back_button.json",
            driver=self.driver,
        )
        self.report["category"] = "STB"
        self.logger.Test("STB-back button")

    def _STB_homepage_btn(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/FirstClass/STB_homepage_button.json",
            driver=self.driver,
        )
        self.report["category"] = "STB"
        self.logger.Test("STB-homepage button")

    # STB_Second class

    def _STB_element_in_all_apps(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/SecondClass/STB_app_show_in_all_apps.json",
            driver=self.driver,
        )
        self.report["category"] = "STB"
        self.logger.Test("STB_apps-element in all apps")

    def _STB_apps_add_delete_app_in_shortcut(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/SecondClass/STB_add_delete_app_shortcut.json",
            driver=self.driver,
        )
        self.report["category"] = "STB"
        self.logger.Test("STB_apps-add & delete apps in shortcut")

    def _STB_apps_order_in_shortcut(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/SecondClass/STB_app_order_in_shortcut.json",
            driver=self.driver,
        )
        self.report["category"] = "STB"
        self.logger.Test("STB_apps-app order in shortcut")

    # STB_Third class

    def _STB_tools_add_delete_app_in_shortcut(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/ThirdClass/STB_add_delete_app_shortcut.json",
            driver=self.driver,
        )
        self.report["category"] = "STB"
        self.logger.Test("STB_tools-add & delete apps in shortcut")

    def _STB_tools_order_in_shortcut(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/ThirdClass/STB_app_order_in_shortcut.json",
            driver=self.driver,
        )
        self.report["category"] = "STB"
        self.logger.Test("STB_tools-app order in shortcut")

    def run_all(self):
        # STB root_view
        self._STB_back_btn()
        self._STB_homepage_btn()
        RecentApp(
            event_gen=self.event_gen, logger=self.logger, driver=self.driver
        ).run_all()
        self.logger.test_title("---STB root view---")
        self._STB_apps_add_delete_app_in_shortcut()
        self._STB_apps_order_in_shortcut()
        self._STB_element_in_all_apps()
        self._STB_tools_add_delete_app_in_shortcut()
        self._STB_tools_order_in_shortcut()
        # STB Tools
        STBTools(
            event_gen=self.event_gen, logger=self.logger, driver=self.driver
        ).run_all()
        Quicksettings(
            event_gen=self.event_gen, logger=self.logger, driver=self.driver
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
                    RecentApp(self.event_gen, self.logger, self.driver).run()
                case "4":
                    self._STB_element_in_all_apps()
                case "5":
                    self._STB_apps_add_delete_app_in_shortcut()
                case "6":
                    self._STB_apps_order_in_shortcut()
                case "7":
                    self._STB_tools_add_delete_app_in_shortcut()
                case "8":
                    self._STB_tools_order_in_shortcut()
                case "9":
                    STBTools(
                        event_gen=self.event_gen, logger=self.logger, driver=self.driver
                    ).run()
                case "10":
                    Quicksettings(
                        event_gen=self.event_gen, logger=self.logger, driver=self.driver
                    ).run()
                case "all":
                    self.run_all()
                case _:
                    print("Invalid option")
