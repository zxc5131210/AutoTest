"""Freezer test case"""


class Freezer:

    def __init__(self, event_gen, logger, driver):
        self.event_gen = event_gen
        self.logger = logger
        self.driver = driver

    def STB_freezer_all(self):
        self._STB_freezer_reboot_to_use()
        self._STB_freezer_zoom_in_out_button()
        self._STB_freezer_zoom_in_out_fingers()
        self._STB_freezer_zoom_mix()
        self._STB_freezer_default_button()

    def _STB_freezer_zoom_in_out_button(self):
        self.logger.Test('STB Freezer-zoom in & out by button')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/Tools/Freezer/STB_freezer_zoom_in_out_button.json', driver=self.driver)

    def _STB_freezer_zoom_in_out_fingers(self):
        self.logger.Test('STB Freezer-zoom in & out by fingers')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/Tools/Freezer/STB_freezer_zoom_in_out_fingers.json', driver=self.driver)

    def _STB_freezer_zoom_mix(self):
        self.logger.Test('STB Freezer-zoom in button first than fingers')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/Tools/Freezer/STB_freezer_zoom_mix.json', driver=self.driver)

    def _STB_freezer_default_button(self):
        self.logger.Test('STB Freezer-default screen button')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/Tools/Freezer/STB_freezer_default_button.json', driver=self.driver)

    def _STB_freezer_reboot_to_use(self):
        self.logger.Test('STB Freezer-reboot to use')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/Tools/Freezer/STB_freezer_reboot_to_use.json', driver=self.driver)

    def run(self):
        while True:
            print("Freezer Options:")
            print("0: Back to main menu")
            print("1: Zoom in & out, by button")
            print("2: Zoom in & out, by fingers")
            print("3: Zoom in, button first than fingers")
            print("4: default screen button")
            print("5: reboot to freezer")
            print("ALL")

            choice = input("Enter your choice: ")

            if choice == '0':
                return
            elif choice == '1':
                self._STB_freezer_zoom_in_out_button()
            elif choice == '2':
                self._STB_freezer_zoom_in_out_fingers()
            elif choice == '3':
                self._STB_freezer_zoom_mix()
            elif choice == '4':
                self._STB_freezer_default_button()
            elif choice == '5':
                self._STB_freezer_reboot_to_use()
            elif choice.lower() == 'all':
                self.STB_freezer_all()
            else:
                print("Invalid option")
