"""wall paper test case"""
import item_strategy


class WallPaper(item_strategy.Strategy):
    menu_dict = {
        "0": "Back to main menu",
        "1": "Change By_default",
        "2": "Change By_update",
        "all": "all Test",
    }
    folder_path = "Test_Jason/vLauncher/Wallpaper"

    def __init__(self, event_gen, logger, driver):
        super().__init__(event_gen, logger, driver)

    def _wallpaper_by_default(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/wallpaper_by_default.json",
            driver=self.driver,
        )
        self.report["category"] = "wallpaper"
        self.logger.Test("Change wallpaper to default style")

    def _wallpaper_by_update(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/wallpaper_by_update.json",
            driver=self.driver,
        )
        self.report["category"] = "wallpaper"
        self.logger.Test("Change wallpaper to update image")

    def run_all(self):
        self.logger.test_title("---Wallpaper Test---")
        self._wallpaper_by_default()
        self._wallpaper_by_update()

    def run(self):
        while True:
            for option, test in self.menu_dict.items():
                print(f"{option}: {test}")
            choice = input("Enter your choice: ").lower()
            match choice:
                case "0":
                    return
                case "1":
                    self._wallpaper_by_default()
                case "2":
                    self._wallpaper_by_update()
                case "all":
                    self.run_all()
                case _:
                    print("Invalid option")
