"""STB tools test case"""
from option_file import item_strategy
from option_file.STB.Tools.Freezer.option import Freezer
from option_file.STB.Tools.Spotlight.option import Spotlight
from option_file.STB.Tools.Stopwatch.option import Stopwatch
from option_file.STB.Tools.Timer.option import Timer
from option_file.STB.Tools.Marker.option import Marker
from option_file.STB.Tools.Screenshot.option import Screenshot


class Category:
    def __init__(self, description, category):
        self.description = description
        self.category = category


class STBTools(item_strategy.Strategy):
    categories = [
        Category("Freezer", Freezer),
        Category("Spotlight", Spotlight),
        Category("Stopwatch", Stopwatch),
        Category("Timer", Timer),
        Category("Marker", Marker),
        Category("Screenshot", Screenshot),
    ]

    def __init__(self, event_gen, driver, reporter):
        super().__init__(event_gen, driver, reporter)

    def run_all(self):
        self.reporter.test_title("---STB Tools---")
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
