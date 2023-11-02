"""recent app test case"""
from option_file import item_strategy


class RecentApp(item_strategy.Strategy):
    menu_dict = {
        "0": "Back to main menu",
        "1": "clear app",
        "2": "clear all button",
        "all": "all Test",
    }
    folder_path = "option_file/vLauncher/recent_app"

    def __init__(self, event_gen, driver, html_report):
        super().__init__(event_gen, driver, html_report)

    def _recent_app_clear_app(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/recentApp_clear_app.json",
            driver=self.driver,
        )
        self.html_report.report_data["category"] = "vlauncher"
        self.html_report.test_case("clear the last App in recent app")

    def _recent_app_clear_all_btn(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/recentApp_clear_all.json",
            driver=self.driver,
        )
        self.html_report.report_data["category"] = "vlauncher"
        self.html_report.test_case("'clear all' button in recent app")

    def run_all(self):
        self.html_report.test_title("---Recent App---")
        self._recent_app_clear_app()
        self._recent_app_clear_all_btn()

    def run(self):
        while True:
            for option, test in self.menu_dict.items():
                print(f"{option}: {test}")
            choice = input("Enter your choice: ").lower()
            match choice:
                case "0":
                    return
                case "1":
                    self._recent_app_clear_app()
                case "2":
                    self._recent_app_clear_all_btn()
                case "all":
                    self.run_all()
                case _:
                    print("Invalid option")
