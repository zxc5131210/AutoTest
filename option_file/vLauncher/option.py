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
        vlauncher_list = [
            vLauncherTitle,
            EditLauncher,
            RecentApp,
            vLauncherTools,
            UserSelect,
        ]
        for test_case_all in vlauncher_list:
            test_case_all(self.event_gen, self.driver, self.reporter).run_all()

    def run(self, category):
        category.category(
            self.event_gen, self.driver, self.reporter
        ).run_with_interaction()

    def print_option(self):
        print(f"-1 : {self.option_menu}")
        for i in range(len(self.categories)):
            print(f"{i} : {self.categories[i].description}")
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
                self.run(self.categories[choice])
            else:
                print("Invalid input. Please enter a valid choice.")
