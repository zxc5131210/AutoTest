"""Stopwatch test case"""
from option_file import item_strategy


class TestCase:
    def __init__(self, description, json_path):
        self.description = description
        self.json_path = json_path


class Stopwatch(item_strategy.Strategy):
    test_cases = [
        TestCase("start the stopwatch and pause it", "start_pause.json"),
        TestCase("lap the stopwatch to record the seconds", "lap.json"),
        TestCase("expand the stopwatch window", "expand.json"),
        TestCase(
            "resume the stopwatch and reset the stopwatch to '00:00:00'",
            "resume_reset.json",
        ),
        TestCase("moving stopwatch", "move.json"),
    ]
    folder_path = "option_file/STB/Tools/Stopwatch"

    def __init__(self, event_gen, driver, reporter):
        super().__init__(event_gen, driver, reporter)

    def run(self, test_case):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/{test_case.json_path}",
            driver=self.driver,
        )
        self.reporter.test_case(test_case.description)

    def run_all(self):
        self.reporter.test_title("---STB Tool - Stopwatch---")
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
