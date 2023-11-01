"""Timer test case"""
import item_strategy


class Timer(item_strategy.Strategy):
    menu_dict = {
        "0": "Back to main menu",
        "1": "start and wait the bell",
        "2": "pause & resume & reset",
        "3": "expand",
        "all": "all Test",
    }
    folder_path = "option_file/STB/Tools/Timer"

    def __init__(self, event_gen, driver, html_report):
        super().__init__(event_gen, driver, html_report)

    def _STB_timer_start_ring(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_timer_start_ring.json",
            driver=self.driver,
        )
        self.html_report.report_data["category"] = "STB"
        self.html_report.test_case("STB timer-start to wait the bell ring")

    def _STB_timer_pause_resume_reset(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_timer_pause_resume_reset.json",
            driver=self.driver,
        )
        self.html_report.report_data["category"] = "STB"
        self.html_report.test_case("STB timer-pause & resume & reset button")

    def _STB_timer_expand(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_timer_expand.json",
            driver=self.driver,
        )
        self.html_report.report_data["category"] = "STB"
        self.html_report.test_case("STB timer-expand the timer window")

    def run_all(self):
        self.html_report.test_title("---STB Tool - Stopwatch---")
        self._STB_timer_start_ring()
        self._STB_timer_pause_resume_reset()
        self._STB_timer_expand()

    def run(self):
        while True:
            for option, test in self.menu_dict.items():
                print(f"{option}: {test}")
            choice = input("Enter your choice: ").lower()
            match choice:
                case "0":
                    return
                case "1":
                    self._STB_timer_start_ring()
                case "2":
                    self._STB_timer_pause_resume_reset()
                case "3":
                    self._STB_timer_expand()
                case "all":
                    self.run_all()
                case _:
                    print("Invalid option")
