"""Stopwatch test case"""
import item_strategy


class Stopwatch(item_strategy.Strategy):
    menu_dict = {
        "0": "Back to main menu",
        "1": "start and pause",
        "2": "lap",
        "3": "expand",
        "4": "resume_reset",
        "5": "moving",
        "all": "all Test",
    }
    folder_path = "Test_Jason/STB/Tools/Stopwatch"

    def __init__(self, event_gen, logger, driver):
        super().__init__(event_gen, logger, driver)

    def _STB_stopwatch_start_pause(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_stopwatch_start_pause.json",
            driver=self.driver,
        )
        self.report["category"] = "STB"
        self.logger.Test("STB stopwatch-start the stopwatch and pause it")

    def _STB_stopwatch_lap(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_stopwatch_lap.json",
            driver=self.driver,
        )
        self.report["category"] = "STB"
        self.logger.Test("STB stopwatch-lap the stopwatch to record the seconds")

    def _STB_stopwatch_expand(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_stopwatch_expand.json",
            driver=self.driver,
        )
        self.report["category"] = "STB"
        self.logger.Test("STB stopwatch-expand the stopwatch window")

    def _STB_stopwatch_resume_reset(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_stopwatch_resume_reset.json",
            driver=self.driver,
        )
        self.report["category"] = "STB"
        self.logger.Test(
            "STB stopwatch-resume the stopwatch and reset the stopwatch to '00:00:00' "
        )

    def _STB_stopwatch_move(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_stopwatch_move.json",
            driver=self.driver,
        )
        self.report["category"] = "STB"
        self.logger.Test("STB stopwatch-move")

    def run_all(self):
        self.logger.test_title("---STB Tool - Stopwatch---")
        self._STB_stopwatch_start_pause()
        self._STB_stopwatch_lap()
        self._STB_stopwatch_expand()
        self._STB_stopwatch_resume_reset()
        self._STB_stopwatch_move()

    def run(self):
        while True:
            for option, test in self.menu_dict.items():
                print(f"{option}: {test}")
            choice = input("Enter your choice: ").lower()
            match choice:
                case "0":
                    return
                case "1":
                    self._STB_stopwatch_start_pause()
                case "2":
                    self._STB_stopwatch_lap()
                case "3":
                    self._STB_stopwatch_expand()
                case "4":
                    self._STB_stopwatch_resume_reset()
                case "5":
                    self._STB_stopwatch_move()
                case "all":
                    self.run_all()
                case _:
                    print("Invalid option")
