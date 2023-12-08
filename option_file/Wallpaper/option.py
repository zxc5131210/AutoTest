"""wall paper test case"""
from option_file import item_strategy


class TestCase:
    def __init__(self, description, json_path):
        self.description = description
        self.json_path = json_path


class WallPaper(item_strategy.Strategy):
    test_cases = [
        TestCase("Change wallpaper to default style", "change_by_default.json"),
        TestCase("Change wallpaper to update image", "change_by_update.json"),
        TestCase("Change to 480p wallpaper", "change_by_480p.json"),
        TestCase("Change to 720p wallpaper", "change_by_720p.json"),
        TestCase("Change to 720p wallpaper", "change_by_720p.json"),
        TestCase("Change to 1080p wallpaper", "change_by_1080p.json"),
        TestCase("Change to 2k wallpaper", "change_by_2k.json"),
        TestCase("Change to 4k wallpaper", "change_by_4k.json"),
        TestCase("Change to 8k wallpaper", "change_by_8k.json"),
        TestCase("delete the upload wallpaper", "delete_upload_wallpaper.json"),
        TestCase("tap close button to close wallpaperpicker", "close_button.json"),
    ]
    folder_path = "option_file/Wallpaper"

    def __init__(self, event_gen, driver, reporter):
        super().__init__(event_gen, driver, reporter)

    def run(self, test_case):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/{test_case.json_path}",
            driver=self.driver,
        )
        self.reporter.test_case(test_case.description)

    def run_all(self):
        self.reporter.test_title("---Wallpaper---")
        for test_case in self.test_cases:
            self.run(test_case)

    def print_option(self):
        print(f"-1 : {self.option_menu}")
        for i in range(len(self.test_cases)):
            print(f"{i} : {self.test_cases[i].description}")
        print(f"{len(self.test_cases)} : {self.option_all}")

    def invalid(self, choice_int) -> bool:
        return choice_int < -1 or choice_int > len(self.test_cases)

    def run_with_interaction(self):
        while True:
            self.print_option()
            choice = input("Enter your choice: ").lower()
            try:
                choice_int = int(choice)
                if self.invalid(choice_int):
                    raise ValueError
                if choice_int == -1:
                    return
                if choice_int == len(self.test_cases):
                    self.run_all()
                    continue
                self.run(self.test_cases[choice_int])
            except ValueError:
                print(
                    "Invalid input. Please enter a valid choice, range is between -1 ~ length of test cases."
                )
