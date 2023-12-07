"""vLauncher test case"""
from option_file.vLauncher.title.option import vLauncherTitle
from option_file.vLauncher.edit_launcher.option import EditLauncher
from option_file.vLauncher.desktop_tools.option import vLauncherTools
from option_file.vLauncher.recent_app.option import RecentApp
from option_file.vLauncher.user_select.option import UserSelect
from option_file import item_strategy


class TestClass:
    def __init__(self, description, test_class):
        self.description = description
        self.test_class = test_class


class vLauncher(item_strategy.Strategy):
    test_class = [
        TestClass("vLauncher title", vLauncherTitle),
        TestClass("Edit Launcher", EditLauncher),
        TestClass("Recent App", RecentApp),
        TestClass("Desktop tools", vLauncherTools),
        TestClass("User Select", UserSelect),
    ]

    def __init__(self, event_gen, driver, reporter):
        super().__init__(event_gen, driver, reporter)

    def run_all(self):
        for test_case in self.test_class:
            test_case.test_class(self.event_gen, self.driver, self.reporter).run_all()

    def run(self, test_case):
        test_case.test_class(
            self.event_gen, self.driver, self.reporter
        ).run_with_interaction()

    def print_option(self):
        print(f"-1 : {self.option_menu}")
        for _ in range(len(self.test_class)):
            print(f"{_} : {self.test_class[_].description}")
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
                self.run(self.test_class[choice])
            else:
                print("Invalid input. Please enter a valid choice.")
