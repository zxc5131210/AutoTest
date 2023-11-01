"""Marker test case"""
import item_strategy


class Marker(item_strategy.Strategy):
    menu_dict = {
        "0": "Back to main menu",
        "1": "selector",
        "2": "pen",
        "3": "highlighter",
        "4": "eraser",
        "5": "undo & redo",
        "6": "delete",
        "7": "save",
        "8": "close",
        "9": "moving",
        "all": "all Test",
    }
    folder_path = "option_file/STB/Tools/Marker"

    def __init__(self, event_gen, logger, driver):
        super().__init__(event_gen, logger, driver)

    def _STB_marker_selector(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_marker_selector.json",
            driver=self.driver,
        )
        self.report["category"] = "STB"
        self.logger.Test("STB marker-selector")

    def _STB_marker_pen(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_marker_pen.json",
            driver=self.driver,
        )
        self.report["category"] = "STB"
        self.logger.Test("STB marker-pen")

    def _STB_marker_highlighter(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_marker_highlighter.json",
            driver=self.driver,
        )
        self.report["category"] = "STB"
        self.logger.Test("STB marker-highlighter")

    def _STB_marker_eraser(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_marker_eraser.json",
            driver=self.driver,
        )
        self.report["category"] = "STB"
        self.logger.Test("STB marker-eraser")

    def _STB_marker_undo_redo(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_marker_undo_redo.json",
            driver=self.driver,
        )
        self.report["category"] = "STB"
        self.logger.Test("STB marker-undo & redo")

    def _STB_marker_delete(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_marker_delete.json",
            driver=self.driver,
        )
        self.report["category"] = "STB"
        self.logger.Test("STB marker-delete")

    def _STB_marker_save(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_marker_save.json",
            driver=self.driver,
        )
        self.report["category"] = "STB"
        self.logger.Test("STB marker-save")

    def _STB_marker_close(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_marker_close.json",
            driver=self.driver,
        )
        self.report["category"] = "STB"
        self.logger.Test("STB marker-close")

    def _STB_marker_moving(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_marker_moving.json",
            driver=self.driver,
        )
        self.report["category"] = "STB"
        self.logger.Test("STB marker-moving")

    def run_all(self):
        self.logger.test_title("---STB Tool - Marker---")
        self._STB_marker_selector()
        self._STB_marker_pen()
        self._STB_marker_highlighter()
        self._STB_marker_eraser()
        self._STB_marker_undo_redo()
        self._STB_marker_delete()
        self._STB_marker_save()
        self._STB_marker_close()
        self._STB_marker_moving()

    def run(self):
        while True:
            for option, test in self.menu_dict.items():
                print(f"{option}: {test}")
            choice = input("Enter your choice: ").lower()
            match choice:
                case "0":
                    return
                case "1":
                    self._STB_marker_selector()
                case "2":
                    self._STB_marker_pen()
                case "3":
                    self._STB_marker_highlighter()
                case "4":
                    self._STB_marker_eraser()
                case "5":
                    self._STB_marker_undo_redo()
                case "6":
                    self._STB_marker_delete()
                case "7":
                    self._STB_marker_save()
                case "8":
                    self._STB_marker_close()
                case "9":
                    self._STB_marker_moving()
                case "all":
                    self.run_all()
                case _:
                    print("Invalid option")
