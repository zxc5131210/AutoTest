from event_generator import EventGen
from logger import Logger


class ScreenLock(event_gen, logger, driver):

    def screen_lock_ALL(self):
        self.event_gen.generate_event(
            json_path='./Test_Jason/ScreenLock/screenLock_all.json', driver=self.driver)

    def screen_lock_setPassword(self):
        self.logger.Test('Set Password')
        self.event_gen.generate_event(
            json_path='./Test_Jason/ScreenLock/screenLock_setPassword.json', driver=self.driver)

    def screen_lock_changePassword(self):
        self.logger.Test('Change Password')
        self.event_gen.generate_event(
            json_path='./Test_Jason/ScreenLock/screenLock_changePassword.json', driver=self.driver)

    def screen_lock_removePassword(self):
        self.logger.Test('Remove Password')
        self.event_gen.generate_event(
            json_path='./Test_Jason/ScreenLock/screenLock_removePassword.json', driver=self.driver)

    def run(self):
        while True:
            print("ScreenLock Options:")
            print("0: Back to main menu")
            print("1: Set Password")
            print("2: Change Password")
            print("3: Remove Password")
            print("ALL")

            choice = input("Enter your choice: ")

            if choice == '0':
                return
            elif choice == '1':
                self.screen_lock_setPassword(self.driver)
            elif choice == '2':
                self.screen_lock_changePassword(self.driver)
            elif choice == '3':
                self.screen_lock_removePassword(self.driver)
            elif choice.lower() == 'all':
                self.screen_lock_ALL(self.driver)
            else:
                print("Invalid option")
