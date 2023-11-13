"""Marker test case"""
from option_file import item_strategy


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

    def __init__(self, event_gen, driver, reporter):
        super().__init__(event_gen, driver, reporter)

    def _STB_marker_selector(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/selector.json",
            driver=self.driver,
        )
        self.reporter.add_category("STB")
        self.reporter.test_case("marker-selector")

    def _STB_marker_pen(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/pen.json",
            driver=self.driver,
        )
        self.reporter.add_category("STB")
        self.reporter.test_case("marker-pen")

    def _STB_marker_highlighter(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/highlighter.json",
            driver=self.driver,
        )
        self.reporter.add_category("STB")
        self.reporter.test_case("marker-highlighter")

    def _STB_marker_eraser(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/eraser.json",
            driver=self.driver,
        )
        self.reporter.add_category("STB")
        self.reporter.test_case("marker-eraser")

    def _STB_marker_undo_redo(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/undo_redo.json",
            driver=self.driver,
        )
        self.reporter.add_category("STB")
        self.reporter.test_case("marker-undo & redo")

    def _STB_marker_delete(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/delete.json",
            driver=self.driver,
        )
        self.reporter.add_category("STB")
        self.reporter.test_case("marker-delete")

    def _STB_marker_save(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/save.json",
            driver=self.driver,
        )
        self.reporter.add_category("STB")
        self.reporter.test_case("marker-save")

    def _STB_marker_close(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/close.json",
            driver=self.driver,
        )
        self.reporter.add_category("STB")
        self.reporter.test_case("marker-close")

    def _STB_marker_moving(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/moving.json",
            driver=self.driver,
        )
        self.reporter.add_category("STB")
        self.reporter.test_case("marker-moving")

    def run_all(self):
        self.reporter.test_title("---STB Tool - Marker---")
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
