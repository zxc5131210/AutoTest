import os
import glob

import abstract_reporter


class FolderParser:
    EXCLUDE_FILES = ["__pycache__", ".DS_Store", "Customized", "SSO"]

    def __init__(self, event_gen, driver, reporter, root_folder, run_type):
        self.event_gen = event_gen
        self.reporter = reporter
        self.driver = driver
        self.root_folder = root_folder
        self.run_type = run_type
        self.CATEGORY_MAPPING = dict((key, key) for key in abstract_reporter.APP_LIST.keys())

    @staticmethod
    def __display_files(file_dict):
        # Display a numbered list of files in the folder
        for i, file_name in file_dict.items():
            display_name = (
                os.path.splitext(file_name)[0]
                if file_name.endswith(".json")
                else file_name
            )
            print(f"{i}: {display_name}")

    @staticmethod
    def __get_user_choice():
        # Get user input for file selection
        return input("Enter the number to select a file :")

    def __handle_selected_file(self, folder_path, selected_file):
        # Construct the file path and perform actions accordingly
        file_path = os.path.join(folder_path, selected_file)
        # Exclude the ".json" extension
        display_name = os.path.splitext(selected_file)[0]
        if os.path.isfile(file_path) and file_path.endswith(".json"):
            self.perform_function(file_path, display_name)
        elif os.path.isdir(file_path):
            self.__parse_folder(file_path)
        else:
            print("Selected path is neither a file nor a folder.")

    def perform_function(self, file_path, display_name):
        self.event_gen.generate_event(
            json_path=f"{file_path}",
            driver=self.driver,
        )
        self.__write_to_report(file_path, display_name)

    def __write_to_report(self, file_path, display_name):
        folder_name = os.path.basename(os.path.dirname(file_path))
        # use project name to category
        self.reporter.add_category(self.__get_category(file_path))
        # use folder name to title
        self.reporter.test_title(folder_name)
        # json file name to testcase name
        self.reporter.test_case(display_name)

    def __get_category(self, file_path):
        for keyword, category in self.CATEGORY_MAPPING.items():
            if keyword in file_path:
                return category
        return None

    def __parse_folder(self, folder_path):
        while True:
            files = [
                file
                for file in os.listdir(folder_path)
                if all(file != i for i in self.EXCLUDE_FILES)
            ]
            file_dict = {str(i): file for i, file in enumerate(files)}
            print("-1 : Previous page / Exit")
            self.__display_files(file_dict)
            print(f"{len(file_dict)} : All Test")
            choice = self.__get_user_choice()
            if choice == "-1":
                return
            if choice == str(len(file_dict)):
                self.run_type = "all"
                self.run(folder_path)
            if choice in file_dict:
                selected_file = file_dict[choice]
                self.__handle_selected_file(folder_path, selected_file)
            else:
                print("Invalid choice. Please enter a valid number.")

    def run(self, folder_path=None):
        if self.run_type == "all":
            if folder_path is None:
                folder_path = self.root_folder
            # Use glob to find all JSON files directly
            json_files = glob.glob(
                os.path.join(folder_path, "**/*.json"), recursive=True
            )
            for file_path in json_files:
                # Extract display_name from the file_path, excluding ".json" extension
                display_name = os.path.splitext(os.path.basename(file_path))[0]
                if not any(
                    excluded_item in file_path for excluded_item in self.EXCLUDE_FILES
                ):
                    self.perform_function(file_path, display_name)
        else:
            self.__parse_folder(self.root_folder)
