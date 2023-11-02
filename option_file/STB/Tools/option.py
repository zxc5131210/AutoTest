"""STB tools test case"""
from option_file import item_strategy
from option_file.STB.Tools.Freezer.option import Freezer
from option_file.STB.Tools.Spotlight.option import Spotlight
from option_file.STB.Tools.Stopwatch.option import Stopwatch
from option_file.STB.Tools.Timer.option import Timer
from option_file.STB.Tools.Marker.option import Marker
from option_file.STB.Tools.Screenshot.option import Screenshot


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

    def __init__(self, event_gen, driver, html_report):
        super().__init__(event_gen, driver, html_report)

    def run_all(self):
        self.html_report.test_title("---STB Tools---")
        items = [Freezer, Spotlight, Stopwatch, Timer, Marker, Screenshot]
        for item in items:
            item(self.event_gen, self.driver, self.html_report).run_all()

    def run(self):
        while True:
            for option, test in self.menu_dict.items():
                print(f"{option}: {test}")
            choice = input("Enter your choice: ").lower()
            match choice:
                case "0":
                    return
                case "1":
                    Freezer(self.event_gen, self.driver, self.html_report).run()
                case "2":
                    Spotlight(self.event_gen, self.driver, self.html_report).run()
                case "3":
                    Stopwatch(self.event_gen, self.driver, self.html_report).run()
                case "4":
                    Timer(self.event_gen, self.driver, self.html_report).run()
                case "5":
                    Marker(self.event_gen, self.driver, self.html_report).run()
                case "6":
                    Screenshot(self.event_gen, self.driver, self.html_report).run()
                case "all":
                    self.run_all()
                case _:
                    print("Invalid option")
