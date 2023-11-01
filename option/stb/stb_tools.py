"""STB tools test case"""
import item_strategy
from .freezer import Freezer
from .spotlight import Spotlight
from .stopwatch import Stopwatch
from .timer import Timer
from .marker import Marker
from .screenshot import Screenshot


class STBTools(item_strategy.Strategy):
    menu_dict = {
        "0": "Back to main menu",
        "1": "Freezer",
        "2": "Spotlight",
        "3": "Stopwatch",
        "4": "Timer",
        "5": "Marker",
        "6": "Screenshot",
        "all": "all test",
    }

    def __init__(self, event_gen, logger, driver):
        super().__init__(event_gen, logger, driver)

    def run_all(self):
        self.logger.test_title("---STB Tools---")
        items = [Freezer, Spotlight, Stopwatch, Timer, Marker, Screenshot]
        for item in items:
            item(self.event_gen, self.logger, self.driver).run_all()

    def run(self):
        while True:
            for option, test in self.menu_dict.items():
                print(f"{option}: {test}")
            choice = input("Enter your choice: ").lower()
            match choice:
                case "0":
                    return
                case "1":
                    Freezer(self.event_gen, self.logger, self.driver).run()
                case "2":
                    Spotlight(self.event_gen, self.logger, self.driver).run()
                case "3":
                    Stopwatch(self.event_gen, self.logger, self.driver).run()
                case "4":
                    Timer(self.event_gen, self.logger, self.driver).run()
                case "5":
                    Marker(self.event_gen, self.logger, self.driver).run()
                case "6":
                    Screenshot(self.event_gen, self.logger, self.driver).run()
                case "all":
                    self.run_all()
                case _:
                    print("Invalid option")
