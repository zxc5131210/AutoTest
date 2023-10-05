"""Stopwatch test case"""
import ItemStrategy


class Stopwatch(ItemStrategy.Strategy):
    menu_dict = {
        "0": "Back to main menu",
        "1": "start and pause",
        "2": "lap",
        "3": "expand",
        "4": "resume_reset",
        "5": "moving",
        "all": "all Test",
    }

    def __init__(self, event_gen, logger, driver):
        super().__init__(event_gen, logger, driver)

    def _STB_stopwatch_start_pause(self):
        self.logger.Test("STB stopwatch-start and pause")
        self.event_gen.generate_event(
            json_path="./Test_Jason/STB/Tools/Stopwatch/STB_stopwatch_start_pause.json",
            driver=self.driver,
        )

    def _STB_stopwatch_lap(self):
        self.logger.Test("STB stopwatch-lap")
        self.event_gen.generate_event(
            json_path="./Test_Jason/STB/Tools/Stopwatch/STB_stopwatch_lap.json",
            driver=self.driver,
        )

    def _STB_stopwatch_expand(self):
        self.logger.Test("STB stopwatch-expand")
        self.event_gen.generate_event(
            json_path="./Test_Jason/STB/Tools/Stopwatch/STB_stopwatch_expand.json",
            driver=self.driver,
        )

    def _STB_stopwatch_resume_reset(self):
        self.logger.Test("STB stopwatch-resume & reset")
        self.event_gen.generate_event(
            json_path="./Test_Jason/STB/Tools/Stopwatch/STB_stopwatch_resume_reset.json",
            driver=self.driver,
        )

    def _STB_stopwatch_move(self):
        self.logger.Test("STB stopwatch-move")
        self.event_gen.generate_event(
            json_path="./Test_Jason/STB/Tools/Stopwatch/STB_stopwatch_move.json",
            driver=self.driver,
        )

    def run_all(self):
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
