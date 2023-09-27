"""Timer test case"""


class Timer:

    def __init__(self, event_gen, logger, driver):
        self.event_gen = event_gen
        self.logger = logger
        self.driver = driver

    def STB_timer_all(self):
        self._STB_timer_start_ring()
        self._STB_timer_pause_resume_reset()
        self._STB_timer_expand()

    def _STB_timer_start_ring(self):
        self.logger.Test('STB timer-start to wait the bell ring')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/Tools/Timer/STB_timer_start_ring.json', driver=self.driver)

    def _STB_timer_pause_resume_reset(self):
        self.logger.Test('STB timer-pause & resume & reset button')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/Tools/Timer/STB_timer_pause_resume_reset.json', driver=self.driver)

    def _STB_timer_expand(self):
        self.logger.Test('STB timer-expand')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/Tools/Timer/STB_timer_expand.json', driver=self.driver)

    def run(self):
        while True:
            print("Spotlight Options:")
            print("0: Back to main menu")
            print("1: start and pause")
            print("2: pause & resume & reset")
            print("3: expand")
            print("ALL")

            choice = input("Enter your choice: ")

            if choice == '0':
                return
            elif choice == '1':
                self._STB_timer_start_ring()
            elif choice == '2':
                self._STB_timer_pause_resume_reset()
            elif choice == '3':
                self._STB_timer_expand()
            elif choice.lower() == 'all':
                self.STB_timer_all()
            else:
                print("Invalid option")
