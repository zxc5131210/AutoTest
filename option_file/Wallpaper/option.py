"""wall paper test case"""
from option_file import item_strategy


class WallPaper(item_strategy.Strategy):
    menu_dict = {
        "0": "Back to main menu",
        "1": "Change By_default",
        "2": "Change By_update",
        "3": "480p wallpaper",
        "4": "720p wallpaper",
        "5": "1080p wallpaper",
        "6": "2k wallpaper",
        "7": "4k wallpaper",
        "8": "8k wallpaper",
        "9": "delete upload wallpaper",
        "10": "close button",
        "all": "all Test",
    }
    folder_path = "option_file/Wallpaper"

    def __init__(self, event_gen, driver, reporter):
        super().__init__(event_gen, driver, reporter)

    def _wallpaper_by_default(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/change_by_default.json",
            driver=self.driver,
        )
        self.reporter.add_category("wallpaper")
        self.reporter.test_case("Change wallpaper to default style")

    def _wallpaper_by_update(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/change_by_update.json",
            driver=self.driver,
        )
        self.reporter.add_category("wallpaper")
        self.reporter.test_case("Change wallpaper to update image")

    def _wallpaper_480p(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/change_by_480p.json",
            driver=self.driver,
        )
        self.reporter.add_category("wallpaper")
        self.reporter.test_case("Change to 480p wallpaper")

    def _wallpaper_720p(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/change_by_720p.json",
            driver=self.driver,
        )
        self.reporter.add_category("wallpaper")
        self.reporter.test_case("Change to 720p wallpaper")

    def _wallpaper_1080p(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/change_by_1080p.json",
            driver=self.driver,
        )
        self.reporter.add_category("wallpaper")
        self.reporter.test_case("Change to 1080p wallpaper")

    def _wallpaper_2k(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/change_by_2k.json",
            driver=self.driver,
        )
        self.reporter.add_category("wallpaper")
        self.reporter.test_case("Change to 2k wallpaper")

    def _wallpaper_4k(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/change_by_4k.json",
            driver=self.driver,
        )
        self.reporter.add_category("wallpaper")
        self.reporter.test_case("Change to 4k wallpaper")

    def _wallpaper_8k(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/change_by_8k.json",
            driver=self.driver,
        )
        self.reporter.add_category("wallpaper")
        self.reporter.test_case("Change to 8k wallpaper")

    def _delete_wallpaper(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/delete_upload_wallpaper.json",
            driver=self.driver,
        )
        self.reporter.add_category("wallpaper")
        self.reporter.test_case("delete the upload wallpaper")

    def _close_button(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/close_button.json",
            driver=self.driver,
        )
        self.reporter.add_category("wallpaper")
        self.reporter.test_case("tap close button to close wallpaperpicker")

    def run_all(self):
        self.reporter.test_title("---Wallpaper---")
        self._wallpaper_by_default()
        self._wallpaper_by_update()
        self._wallpaper_480p()
        self._wallpaper_720p()
        self._wallpaper_1080p()
        self._wallpaper_2k()
        self._wallpaper_4k()
        self._wallpaper_8k()
        self._delete_wallpaper()
        self._close_button()

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
                case "3":
                    self._wallpaper_480p()
                case "4":
                    self._wallpaper_720p()
                case "5":
                    self._wallpaper_1080p()
                case "6":
                    self._wallpaper_2k()
                case "7":
                    self._wallpaper_4k()
                case "8":
                    self._wallpaper_8k()
                case "9":
                    self._delete_wallpaper()
                case "10":
                    self._close_button()
                case "all":
                    self.run_all()
                case _:
                    print("Invalid option")
