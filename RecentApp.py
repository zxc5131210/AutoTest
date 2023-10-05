"""recent app test case"""
import ItemStrategy


class RecentApp(ItemStrategy.Strategy):
    menu_dict = {
        "0": "Back to main menu",
        "1": "clear app",
        "2": "clear all button",
        "all": "all Test",
    }

    def __init__(self, event_gen, logger, driver):
        super().__init__(event_gen, logger, driver)

    def _recent_app_clear_app(self):
        self.logger.Test("recent-clear app")
        self.event_gen.generate_event(
            json_path="./Test_Jason/vLauncher/recentApp/recentApp_clear_app.json",
            driver=self.driver,
        )

    def _recent_app_clear_all_btn(self):
        self.logger.Test("recent-clear all button")
        self.event_gen.generate_event(
            json_path="./Test_Jason/vLauncher/recentApp/recentApp_clear_all.json",
            driver=self.driver,
        )

    def run_all(self):
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
