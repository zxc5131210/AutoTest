"""Spotlight test case"""


class Spotlight:

    def __init__(self, event_gen, logger, driver):
        self.event_gen = event_gen
        self.logger = logger
        self.driver = driver

    def STB_spotlight_all(self):
        self._STB_spotlight_zoom_in_out_button()
        self._STB_spotlight_zoom_in_out_fingers()
        self._STB_spotlight_transparency()
        self._STB_spotlight_move()

    def _STB_spotlight_zoom_in_out_button(self):
        self.logger.Test('STB Spotlight-zoom in & out by button')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/Tools/Spotlight/STB_spotlight_zoom_in_out_button.json', driver=self.driver)

    def _STB_spotlight_zoom_in_out_fingers(self):
        self.logger.Test('STB Spotlight-zoom in & out by fingers')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/Tools/Spotlight/STB_spotlight_zoom_in_out_fingers.json', driver=self.driver)

    def _STB_spotlight_transparency(self):
        self.logger.Test('STB Spotlight-Transparency dark and light')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/Tools/Spotlight/STB_spotlight_transparency.json', driver=self.driver)

    def _STB_spotlight_move(self):
        self.logger.Test('STB Spotlight-move')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/Tools/Spotlight/STB_spotlight_move.json', driver=self.driver)

    def run(self):
        while True:
            print("Spotlight Options:")
            print("0: Back to main menu")
            print("1: Zoom in & out, by button")
            print("2: Zoom in & out, by fingers")
            print("3: Transparency dark and light")
            print("4: Spotlight moving")
            print("ALL")

            choice = input("Enter your choice: ")

            if choice == '0':
                return
            elif choice == '1':
                self._STB_spotlight_zoom_in_out_button()
            elif choice == '2':
                self._STB_spotlight_zoom_in_out_fingers()
            elif choice == '3':
                self._STB_spotlight_transparency()
            elif choice == '4':
                self._STB_spotlight_move()
            elif choice.lower() == 'all':
                self.STB_spotlight_all()
            else:
                print("Invalid option")
