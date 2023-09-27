"""STB tools test case"""
from STBToolsFreezer import Freezer
from STBToolsSpotlight import Spotlight
from STBToolsStopwatch import Stopwatch
from STBToolsTimer import Timer
from STBToolsMarker import Marker


class STBTools:

    def __init__(self, event_gen, logger, driver):
        self.event_gen = event_gen
        self.logger = logger
        self.driver = driver

    def run(self):
        while True:
            print("STB tools Options:")
            print("0: Back to main menu")
            print("1: Freezer")
            print("2: Spotlight")
            print("3: Stopwatch")
            print("4: Timer")
            print("5: Marker")
            print("ALL")

            choice = input("Enter your choice: ")

            if choice == '0':
                return
            elif choice == '1':
                Freezer(self.event_gen, self.logger, self.driver).run()
            elif choice == '2':
                Spotlight(self.event_gen, self.logger, self.driver).run()
            elif choice == '3':
                Stopwatch(self.event_gen, self.logger, self.driver).run()
            elif choice == '4':
                Timer(self.event_gen, self.logger, self.driver).run()
            elif choice == '5':
                Marker(self.event_gen, self.logger, self.driver).run()
                pass
            elif choice.lower() == 'all':
                pass
            else:
                print("Invalid option")
