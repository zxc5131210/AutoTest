"""STB test case"""
from RecentApp import RecentApp
from STBToolsFreezer import Freezer
from STBToolsSpotlight import Spotlight
from STBToolsStopwatch import Stopwatch


class STB:

    def __init__(self, event_gen, logger, driver):
        self.event_gen = event_gen
        self.logger = logger
        self.driver = driver

    def _STB_all(self):
        # STB root_view
        self._STB_back_btn()
        self._STB_homepage_btn()
        RecentApp(event_gen=self.event_gen, logger=self.logger,
                  driver=self.driver).recent_app_all()
        self._STB_element_in_all_apps()
        self._STB_apps_add_delete_app_in_shortcut()
        self._STB_apps_order_in_shortcut()
        self._STB_tools_add_delete_app_in_shortcut()
        self._STB_tools_order_in_shortcut()
        # STB Tools
        Freezer(event_gen=self.event_gen, logger=self.logger,
                driver=self.driver).STB_freezer_all()
        Spotlight(event_gen=self.event_gen, logger=self.logger,
                  driver=self.driver).STB_spotlight_all()
        Stopwatch(event_gen=self.event_gen, logger=self.logger,
                  driver=self.driver).STB_stopwatch_all()
        # self._STB_timer_all()
        # self._STB_marker_all()

    # STB_first class

    def _STB_back_btn(self):
        self.logger.Test('STB-back button')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/FirstClass/STB_back_button.json', driver=self.driver)

    def _STB_homepage_btn(self):
        self.logger.Test('STB-homepage button')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/FirstClass/STB_homepage_button.json', driver=self.driver)

    # STB_Second class

    def _STB_element_in_all_apps(self):
        self.logger.Test('STB_apps-element in all apps')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/SecondClass/STB_app_show_in_all_apps.json', driver=self.driver)

    def _STB_apps_add_delete_app_in_shortcut(self):
        self.logger.Test('STB_apps-add & delete apps in shortcut')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/SecondClass/STB_add_delete_app_shortcut.json', driver=self.driver)

    def _STB_apps_order_in_shortcut(self):
        self.logger.Test('STB_apps-app order in shortcut')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/SecondClass/STB_app_order_in_shortcut.json', driver=self.driver)

    # STB_Third class

    def _STB_tools_add_delete_app_in_shortcut(self):
        self.logger.Test('STB_tools-add & delete apps in shortcut')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/ThirdClass/STB_add_delete_app_shortcut.json', driver=self.driver)

    def _STB_tools_order_in_shortcut(self):
        self.logger.Test('STB_tools-app order in shortcut')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/ThirdClass/STB_app_order_in_shortcut.json', driver=self.driver)

    def run(self):
        while True:
            print("STB Options:")
            print("0: Back to main menu")
            print("1: back button")
            print("2: homepage button")
            print("3: recent app")
            print("4: element in all apps")
            print("5: add & delete apps in shortcut")
            print("6: app order in shortcut")
            print("7: add & delete tools in shortcut")
            print("8: tools order in shortcut")
            print("9: STB tools")
            print("ALL")

            choice = input("Enter your choice: ")

            if choice == '0':
                return
            elif choice == '1':
                self._STB_back_btn()
            elif choice == '2':
                self._STB_homepage_btn()
            elif choice == '3':
                RecentApp(self.event_gen, self.logger, self.driver).run()
            elif choice == '4':
                self._STB_element_in_all_apps()
            elif choice == '5':
                self._STB_apps_add_delete_app_in_shortcut()
            elif choice == '6':
                self._STB_apps_order_in_shortcut()
            elif choice == '7':
                self._STB_tools_add_delete_app_in_shortcut()
            elif choice == '8':
                self._STB_tools_order_in_shortcut()
            elif choice == '9':
                pass
            elif choice.lower() == 'all':
                self._STB_all()
            else:
                print("Invalid option")
