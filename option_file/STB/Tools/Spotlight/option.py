"""Spotlight test case"""
import item_strategy


class Spotlight(item_strategy.Strategy):
    menu_dict = {
        "0": "Back to main menu",
        "1": "Zoom in & out, by button",
        "2": "Zoom in & out, by fingers",
        "3": "Transparency dark and light",
        "4": "Spotlight moving",
        "all": "all Test",
    }
    folder_path = "option_file/STB/Tools/Spotlight"

    def __init__(self, event_gen, logger, driver):
        super().__init__(event_gen, logger, driver)

    def _STB_spotlight_zoom_in_out_button(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_spotlight_zoom_in_out_button.json",
            driver=self.driver,
        )
        self.report["category"] = "STB"
        self.logger.Test("STB Spotlight-use button to zoom in & zoom out")

    def _STB_spotlight_zoom_in_out_fingers(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_spotlight_zoom_in_out_fingers.json",
            driver=self.driver,
        )
        self.report["category"] = "STB"
        self.logger.Test("STB Spotlight-use fingers to zoom in & zoom out")

    def _STB_spotlight_transparency(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_spotlight_transparency.json",
            driver=self.driver,
        )
        self.report["category"] = "STB"
        self.logger.Test("STB Spotlight-Transparency dark and light")

    def _STB_spotlight_move(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_spotlight_move.json",
            driver=self.driver,
        )
        self.report["category"] = "STB"
        self.logger.Test("STB Spotlight-drag to move the spotlight")

    def run_all(self):
        self.logger.test_title("---STB Tool - Spotlight---")
        self._STB_spotlight_zoom_in_out_button()
        self._STB_spotlight_zoom_in_out_fingers()
        self._STB_spotlight_transparency()
        self._STB_spotlight_move()

    def run(self):
        while True:
            for option, test in self.menu_dict.items():
                print(f"{option}: {test}")
            choice = input("Enter your choice: ").lower()
            match choice:
                case "0":
                    return
                case "1":
                    self._STB_spotlight_zoom_in_out_button()
                case "2":
                    self._STB_spotlight_zoom_in_out_fingers()
                case "3":
                    self._STB_spotlight_transparency()
                case "4":
                    self._STB_spotlight_move()
                case "all":
                    self.run_all()
                case _:
                    print("Invalid option")
