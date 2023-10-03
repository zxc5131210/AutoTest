"""STB tools test case"""
from STBToolsFreezer import Freezer
from STBToolsSpotlight import Spotlight
from STBToolsStopwatch import Stopwatch
from STBToolsTimer import Timer
from STBToolsMarker import Marker
from STBToolsScreenshot import Screenshot


class STBTools:
    def __init__(self, event_gen, logger, driver):
        self.event_gen = event_gen
        self.logger = logger
        self.driver = driver

    def STB_tools_all(self):
        Freezer(self.event_gen, self.logger, self.driver).STB_freezer_all()
        Spotlight(self.event_gen, self.logger, self.driver).STB_spotlight_all()
        Stopwatch(self.event_gen, self.logger, self.driver).STB_stopwatch_all()
        Timer(self.event_gen, self.logger, self.driver).STB_timer_all()
        Marker(self.event_gen, self.logger, self.driver).STB_marker_all()
        Screenshot(self.event_gen, self.logger, self.driver).STB_screenshot_all()

    def run(self):
        while True:
            print("STB tools Options:")
            print("0: Back to main menu")
            print("1: Freezer")
            print("2: Spotlight")
            print("3: Stopwatch")
            print("4: Timer")
            print("5: Marker")
            print("6: Screenshot")
            print("ALL")

            choice = input("Enter your choice: ")

            if choice == "0":
                return
            elif choice == "1":
                Freezer(self.event_gen, self.logger, self.driver).run()
            elif choice == "2":
                Spotlight(self.event_gen, self.logger, self.driver).run()
            elif choice == "3":
                Stopwatch(self.event_gen, self.logger, self.driver).run()
            elif choice == "4":
                Timer(self.event_gen, self.logger, self.driver).run()
            elif choice == "5":
                Marker(self.event_gen, self.logger, self.driver).run()
            elif choice == "6":
                Screenshot(self.event_gen, self.logger, self.driver).run()
            elif choice.lower() == "all":
                self.STB_tools_all()
            else:
                print("Invalid option")
