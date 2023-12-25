import os
import glob


class FolderProcessor:
    EXCLUDE_FILES = ["__pycache__", ".DS_Store", "Customized"]

    def __init__(
        self, event_gen: object, driver: object, reporter: object, root_folder
    ):
        self.event_gen = event_gen
        self.reporter = reporter
        self.driver = driver
        self.root_folder = root_folder

    @staticmethod
    def _display_files(file_dict):
        # Display a numbered list of files in the folder
        for i, file_name in file_dict.items():
            display_name = (
                os.path.splitext(file_name)[0]
                if file_name.endswith(".json")
                else file_name
            )
            print(f"{i}: {display_name}")

    @staticmethod
    def _get_user_choice():
        # Get user input for file selection
        return input("Enter the number to select a file :")

    def _handle_selected_file(self, folder_path, selected_file):
        # Construct the file path and perform actions accordingly
        file_path = os.path.join(folder_path, selected_file)
        # Exclude the ".json" extension
        display_name = os.path.splitext(selected_file)[0]
        if os.path.isfile(file_path) and file_path.endswith(".json"):
            self.perform_function(file_path, display_name)
        elif os.path.isdir(file_path):
            self._parse_folder(file_path)
        else:
            print("Selected path is neither a file nor a folder.")

    def perform_function(self, file_path, display_name):
        self.event_gen.generate_event(
            json_path=f"{file_path}",
            driver=self.driver,
        )
        self._write_to_report(file_path, display_name)

    def _write_to_report(self, file_path, display_name):
        folder_name = os.path.basename(os.path.dirname(file_path))
        # use project name to category
        self.reporter.add_category(self._get_category(file_path))
        # use folder name to title
        self.reporter.test_title(folder_name)
        # json file name to testcase name
        self.reporter.test_case(display_name)

    @staticmethod
    def _get_category(file_path):
        if "Quicksettings" in file_path:
            return "Quicksettings"
        elif "Authenticator" in file_path:
            return "Authenticator"
        elif "Wallpaper" in file_path:
            return "Wallpaper"
        elif "STB" in file_path:
            return "STB"
        elif "ScreenLock" in file_path:
            return "ScreenLock"
        elif "vLauncher" in file_path:
            return "vLauncher"

    def _parse_folder(self, folder_path):
        while True:
            files = [
                file
                for file in os.listdir(folder_path)
                if all(file != i for i in self.EXCLUDE_FILES)
            ]
            file_dict = {str(i): file for i, file in enumerate(files)}
            print("-1 : Previous page / Exit")
            self._display_files(file_dict)
            print(f"{len(file_dict)} : All Test")
            choice = self._get_user_choice()
            if choice == "-1":
                return
            if choice == str(len(file_dict)):
                self._run_all(folder_path)
            if choice in file_dict:
                selected_file = file_dict[choice]
                self._handle_selected_file(folder_path, selected_file)
            else:
                print("Invalid choice. Please enter a valid number.")

    def run(self):
        self._parse_folder(self.root_folder)

    def _run_all(self, folder_path=None):
        if folder_path is None:
            folder_path = self.root_folder
        # Use glob to find all JSON files directly
        json_files = glob.glob(os.path.join(folder_path, "**/*.json"), recursive=True)
        for file_path in json_files:
            # Extract display_name from the file_path, excluding ".json" extension
            display_name = os.path.splitext(os.path.basename(file_path))[0]
            if not any(
                excluded_item in file_path for excluded_item in self.EXCLUDE_FILES
            ):
                self.perform_function(file_path, display_name)
