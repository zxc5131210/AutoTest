"""Stopwatch test case"""


class Stopwatch:

    def __init__(self, event_gen, logger, driver):
        self.event_gen = event_gen
        self.logger = logger
        self.driver = driver

    def STB_stopwatch_all(self):
        self._STB_stopwatch_start_pause()
        self._STB_stopwatch_lap()
        self._STB_stopwatch_expand()
        self._STB_stopwatch_resume_reset()
        self._STB_stopwatch_move()

    def _STB_stopwatch_start_pause(self):
        self.logger.Test('STB stopwatch-start and pause')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/Tools/Stopwatch/STB_stopwatch_start_pause.json', driver=self.driver)

    def _STB_stopwatch_lap(self):
        self.logger.Test('STB stopwatch-lap')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/Tools/Stopwatch/STB_stopwatch_lap.json', driver=self.driver)

    def _STB_stopwatch_expand(self):
        self.logger.Test('STB stopwatch-expand')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/Tools/Stopwatch/STB_stopwatch_expand.json', driver=self.driver)

    def _STB_stopwatch_resume_reset(self):
        self.logger.Test('STB stopwatch-resume & reset')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/Tools/Stopwatch/STB_stopwatch_resume_reset.json', driver=self.driver)

    def _STB_stopwatch_move(self):
        self.logger.Test('STB stopwatch-move')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/Tools/Stopwatch/STB_stopwatch_move.json', driver=self.driver)

    def run(self):
        while True:
            print("Spotlight Options:")
            print("0: Back to main menu")
            print("1: start and pause")
            print("2: lap")
            print("3: expand")
            print("4: resume_reset")
            print("5: moving")
            print("ALL")

            choice = input("Enter your choice: ")

            if choice == '0':
                return
            elif choice == '1':
                self._STB_stopwatch_start_pause()
            elif choice == '2':
                self._STB_stopwatch_lap()
            elif choice == '3':
                self._STB_stopwatch_expand()
            elif choice == '4':
                self._STB_stopwatch_resume_reset()
            elif choice == '5':
                self._STB_stopwatch_move()
            elif choice.lower() == 'all':
                self.STB_stopwatch_all()
            else:
                print("Invalid option")
