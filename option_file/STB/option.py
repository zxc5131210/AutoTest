"""STB test case"""
from option_file.STB.Tools.option import STBTools
from option_file import item_strategy


class TestCase:
    def __init__(self, description, json_path):
        self.description = description
        self.json_path = json_path


class STB(item_strategy.Strategy):
    test_cases = [
        TestCase("back button", "FirstClass/back_button.json"),
        TestCase("homepage button", "FirstClass/homepage_button.json"),
        TestCase("element in all apps", "app_show_in_all_apps.json"),
        TestCase(
            "add & delete apps in shortcut", "SecondClass/add_delete_app_shortcut.json"
        ),
        TestCase("app order in shortcut", "SecondClass/app_order_in_shortcut.json"),
        TestCase(
            "add & delete tools in shortcut", "ThirdClass/add_delete_app_shortcut.json"
        ),
        TestCase("tools order in shortcut", "ThirdClass/app_order_in_shortcut.json"),
        TestCase(
            "error message popup of exists app", "SecondClass/exists_apps_popup.json"
        ),
        TestCase(
            "maximum apps error message popup", "SecondClass/maximum_apps_popup.json"
        ),
    ]
    folder_path = "option_file/STB"

    def __init__(self, event_gen, driver, reporter):
        super().__init__(event_gen, driver, reporter)

    def run(self, test_case):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/{test_case.json_path}",
            driver=self.driver,
        )
        self.reporter.test_case(test_case.description)

    def run_all(self):
        # STB root_view
        self.reporter.test_title("---STB root view---")
        for test_case in self.test_cases:
            self.run(test_case)
        STBTools(self.event_gen, self.driver, self.reporter).run_all()

    def print_option(self):
        print(f"-1 : {self.option_menu}")
        for i in range(len(self.test_cases)):
            print(f"{i} : {self.test_cases[i].description}")
        print(f"{len(self.test_cases)} : STB tools")
        print(f"{len(self.test_cases)+1} : {self.option_all}")

    def invalid(self, choice_int) -> bool:
        if choice_int == len(self.test_cases):
            STBTools(self.event_gen, self.driver, self.reporter).run_with_interaction()
            return False
        if choice_int < -1 or choice_int > len(self.test_cases) + 1:
            return True

    def run_with_interaction(self):
        while True:
            self.print_option()
            choice = input("Enter your choice: ").lower()
            try:
                choice_int = int(choice)
                if not self.invalid(choice_int):
                    continue
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
