"""edit launcher test case"""


class EditLauncher:

    def __init__(self, event_gen, logger, driver):
        self.event_gen = event_gen
        self.logger = logger
        self.driver = driver

    def _edit_launcher_all(self):
        self.event_gen.generate_event(
            json_path='./Test_Jason/vLauncher/Edit_Launcher/editLauncher_all.json', driver=self.driver)

    def _edit_launcher_add_app(self):
        self.logger.Test('Add_delete_re-range app on hot seat')
        self.event_gen.generate_event(
            json_path='./Test_Jason/vLauncher/Edit_Launcher/editLauncher_add_delete_re-rangeApps.json', driver=self.driver)

    def _edit_launcher_find_all(self):
        self.logger.Test('install Testapp and find in all apps')
        self.event_gen.generate_event(
            json_path='./Test_Jason/vLauncher/Edit_Launcher/editLauncher_find_apps_in_All.json', driver=self.driver)

    def run(self):
        while True:
            print("Edit Launcher Options:")
            print("0: Back to main menu")
            print("1: Add_delete_re-range app on hot seat")
            print("2:install Testapp and find in all apps")
            print("ALL")

            choice = input("Enter your choice: ")

            if choice == '0':
                return
            elif choice == '1':
                self._edit_launcher_add_app()
            elif choice == '2':
                self._edit_launcher_find_all()
            elif choice.lower() == 'all':
                self._edit_launcher_all()
            else:
                print("Invalid option")
