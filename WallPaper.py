"""wall paper test case"""


class WallPaper:

    def __init__(self, event_gen, logger, driver):
        self.event_gen = event_gen
        self.logger = logger
        self.driver = driver

    def _wallpaper_all(self):
        self._wallpaper_by_default()
        self._wallpaper_by_update()

    def _wallpaper_by_default(self):
        self.logger.Test('Change By_default')
        self.event_gen.generate_event(
            json_path='./Test_Jason/vLauncher/Wallpaper/wallpaper_By_default.json', driver=self.driver)

    def _wallpaper_by_update(self):
        self.logger.Test('Change By_update')
        self.event_gen.generate_event(
            json_path='./Test_Jason/vLauncher/Wallpaper/wallpaper_By_update.json', driver=self.driver)

    def run(self):
        while True:
            print("Wallpaper Options:")
            print("0: Back to main menu")
            print("1: Change By_default")
            print("2: Change By_update")
            print("ALL")

            choice = input("Enter your choice: ")

            if choice == '0':
                return
            elif choice == '1':
                self._wallpaper_by_default()
            elif choice == '2':
                self._wallpaper_by_update()
            elif choice.lower() == 'all':
                self._wallpaper_all()
            else:
                print("Invalid option")
