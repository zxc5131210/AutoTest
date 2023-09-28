"""Marker test case"""


class Marker:

    def __init__(self, event_gen, logger, driver):
        self.event_gen = event_gen
        self.logger = logger
        self.driver = driver

    def STB_marker_all(self):
        self._STB_marker_selector()
        self._STB_marker_pen()
        self._STB_marker_highlighter()
        self._STB_marker_eraser()
        self._STB_marker_undo_redo()
        self._STB_marker_delete()
        self._STB_marker_save()
        self._STB_marker_close()
        self._STB_marker_moving()

    def _STB_marker_selector(self):
        self.logger.Test('STB marker-selector')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/Tools/Marker/STB_marker_selector.json', driver=self.driver)

    def _STB_marker_pen(self):
        self.logger.Test('STB marker-pen')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/Tools/Marker/STB_marker_pen.json', driver=self.driver)

    def _STB_marker_highlighter(self):
        self.logger.Test('STB marker-highlighter')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/Tools/Marker/STB_marker_highlighter.json', driver=self.driver)

    def _STB_marker_eraser(self):
        self.logger.Test('STB marker-eraser')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/Tools/Marker/STB_marker_eraser.json', driver=self.driver)

    def _STB_marker_undo_redo(self):
        self.logger.Test('STB marker-undo & redo')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/Tools/Marker/STB_marker_undo_redo.json', driver=self.driver)

    def _STB_marker_delete(self):
        self.logger.Test('STB marker-delete')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/Tools/Marker/STB_marker_delete.json', driver=self.driver)

    def _STB_marker_save(self):
        self.logger.Test('STB marker-save')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/Tools/Marker/STB_marker_save.json', driver=self.driver)

    def _STB_marker_close(self):
        self.logger.Test('STB marker-close')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/Tools/Marker/STB_marker_close.json', driver=self.driver)

    def _STB_marker_moving(self):
        self.logger.Test('STB marker-moving')
        self.event_gen.generate_event(
            json_path='./Test_Jason/STB/Tools/Marker/STB_marker_moving.json', driver=self.driver)

    def run(self):
        while True:
            print("Marker Options:")
            print("0: Back to main menu")
            print("1: selector")
            print("2: pen")
            print("3: highlighter")
            print("4: eraser")
            print("5: undo & redo")
            print("6: delete")
            print("7: save")
            print("8: close")
            print("9: moving")
            print("ALL")
            choice = input("Enter your choice: ")
            if choice == '0':
                return
            elif choice == '1':
                self._STB_marker_selector()
            elif choice == '2':
                self._STB_marker_pen()
            elif choice == '3':
                self._STB_marker_highlighter()
            elif choice == '4':
                self._STB_marker_eraser()
            elif choice == '5':
                self._STB_marker_undo_redo()
            elif choice == '6':
                self._STB_marker_delete()
            elif choice == '7':
                self._STB_marker_save()
            elif choice == '8':
                self._STB_marker_close()
            elif choice == '9':
                self._STB_marker_moving()
            elif choice.lower() == 'all':
                self._STB_marker_all()
            else:
                print("Invalid option")

