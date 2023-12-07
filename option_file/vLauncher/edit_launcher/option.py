"""edit launcher test case"""
from option_file import item_strategy


class TestCase:
    def __init__(self, description, json_path):
        self.description = description
        self.json_path = json_path


class EditLauncher(item_strategy.Strategy):
    test_case = [
        TestCase("Rearrange app on hot seat", "rearrange_apps.json"),
        TestCase("Install Testapp and find in all apps", "find_apps_in_All.json"),
        TestCase("Exists app error message popup", "exists_app_error_message.json"),
        TestCase("Maximum app error message popup", "maximum_app_error_message.json"),
        TestCase("Confirm button", "confirm_button.json"),
    ]

    folder_path = "option_file/vLauncher/edit_launcher"

    def __init__(self, event_gen, driver, reporter):
        super().__init__(event_gen, driver, reporter)

    def run(self, test_case):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/{test_case.json_path}",
            driver=self.driver,
        )
        self.reporter.test_case(test_case.description)

    def run_all(self):
        self.reporter.test_title("---Edit Launcher---")
        for test_case in self.test_case:
            self.run(test_case)

    def print_option(self):
        print(f"-1 : {self.option_menu}")
        for _ in range(len(self.test_case)):
            print(f"{_} : {self.test_case[_].description}")
        print(f"all : {self.option_all}")

    def run_with_interaction(self):
        while True:
            self.print_option()
            choice = input("Enter your choice: ").lower()
            if choice.isnumeric():
                choice = int(choice)
            if choice == "-1":
                return
            elif choice == "all":
                self.run_all()
            elif isinstance(choice, int):
                self.run(self.test_case[choice])
            else:
                print("Invalid input. Please enter a valid choice.")
