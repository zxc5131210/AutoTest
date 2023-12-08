"""vLauncher test case"""
from option_file.vLauncher.title.option import vLauncherTitle
from option_file.vLauncher.edit_launcher.option import EditLauncher
from option_file.vLauncher.desktop_tools.option import vLauncherTools
from option_file.vLauncher.recent_app.option import RecentApp
from option_file.vLauncher.user_select.option import UserSelect
from option_file import item_strategy


class Category:
    def __init__(self, description, category):
        self.description = description
        self.category = category


class vLauncher(item_strategy.Strategy):
    categories = [
        Category("vLauncher title", vLauncherTitle),
        Category("Edit Launcher", EditLauncher),
        Category("Recent App", RecentApp),
        Category("Desktop tools", vLauncherTools),
        Category("User Select", UserSelect),
    ]

    def __init__(self, event_gen, driver, reporter):
        super().__init__(event_gen, driver, reporter)

    def run_all(self):
        for category in self.categories:
            category.category(self.event_gen, self.driver, self.reporter).run_all()

    def run(self, category):
        category.category(
            self.event_gen, self.driver, self.reporter
        ).run_with_interaction()

    def print_option(self):
        print(f"-1 : {self.option_menu}")
        for i in range(len(self.categories)):
            print(f"{i} : {self.categories[i].description}")
        print(f"{len(self.categories)} : {self.option_all}")

    def invalid(self, choice_int) -> bool:
        return choice_int < -1 or choice_int > len(self.categories)

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
                if choice_int == len(self.categories):
                    self.run_all()
                    continue
                self.run(self.categories[choice_int])
            except ValueError:
                print(
                    "Invalid input. Please enter a valid choice, range is between -1 ~ length of test cases."
                )
