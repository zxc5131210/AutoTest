"""STB first class test case"""
from option_file import item_strategy


class TestCase:
    def __init__(self, description, json_path):
        self.description = description
        self.json_path = json_path


class SecondClass(item_strategy.Strategy):
    test_cases = [
        TestCase("element in all apps", "app_show_in_all_apps.json"),
        TestCase("add & delete apps in shortcut", "add_delete_app_shortcut.json"),
        TestCase("app order in shortcut", "app_order_in_shortcut.json"),
        TestCase("error message popup of exists app", "exists_apps_popup.json"),
        TestCase("maximum apps error message popup", "maximum_apps_popup.json"),
    ]
    folder_path = "option_file/STB/SecondClass/"

    def __init__(self, event_gen, driver, reporter):
        super().__init__(event_gen, driver, reporter)

    def run(self, test_case):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/{test_case.json_path}",
            driver=self.driver,
        )
        self.reporter.test_case(test_case.description)

    def run_all(self):
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
