"""recent app test case"""


class RecentApp:

    def __init__(self, event_gen, logger, driver):
        self.event_gen = event_gen
        self.logger = logger
        self.driver = driver

    def recent_app_all(self):
        self._recent_app_clear_app()
        self._recent_app_clear_all_btn()
        
    def _recent_app_clear_app(self):
        self.logger.Test('recent-clear app')
        self.event_gen.generate_event(
            json_path='./Test_Jason/vLauncher/recentApp/recentApp_clear_app.json', driver=self.driver)

    def _recent_app_clear_all_btn(self):
        self.logger.Test('recent-clear all button')
        self.event_gen.generate_event(
            json_path='./Test_Jason/vLauncher/recentApp/recentApp_clear_all.json', driver=self.driver)

    def run(self):
        while True:
            print("Recent App Options:")
            print("0: Back to main menu")
            print("1:clear app")
            print("2:clear all button")
            print("ALL")

            choice = input("Enter your choice: ")

            if choice == '0':
                return
            elif choice == '1':
                self._recent_app_clear_app()
            elif choice == '2':
                self._recent_app_clear_all_btn()
            elif choice.lower() == 'all':
                self.recent_app_all()
            else:
                print("Invalid option")
