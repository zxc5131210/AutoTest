"""screen lock test case"""


class ScreenLock:

    def __init__(self, event_gen, logger, driver):
        self.event_gen = event_gen
        self.logger = logger
        self.driver = driver

    def _screen_lock_all(self):
        self._screen_lock_set_password()
        self._screen_lock_change_password()
        self._screen_lock_remove_password()
        self._screen_lock_reveal_password()

    def _screen_lock_set_password(self):
        self.logger.Test('Set Password')
        self.event_gen.generate_event(
            json_path='Test_Jason/ScreenLock/screenLock_set_password.json', driver=self.driver)

    def _screen_lock_change_password(self):
        self.logger.Test('Change Password')
        self.event_gen.generate_event(
            json_path='Test_Jason/ScreenLock/screenLock_change_password.json', driver=self.driver)

    def _screen_lock_remove_password(self):
        self.logger.Test('Remove Password')
        self.event_gen.generate_event(
            json_path='Test_Jason/ScreenLock/screenLock_remove_password.json', driver=self.driver)

    def _screen_lock_reveal_password(self):
        self.logger.Test('Reveal Password')
        self.event_gen.generate_event(
            json_path='./Test_Jason/ScreenLock/screenLock_reveal_password.json', driver=self.driver)

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
                self._screen_lock_set_password()
            elif choice == '2':
                self._screen_lock_change_password()
            elif choice == '3':
                self._screen_lock_remove_password()
            elif choice == '4':
                self._screen_lock_reveal_password()
            elif choice.lower() == 'all':
                self._screen_lock_all()
            else:
                print("Invalid option")
