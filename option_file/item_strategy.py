class Strategy:
    option_menu = "Back to previous page"
    option_all = "All Test"

    def __init__(self, event_gen: object, driver: object, reporter: object):
        self.event_gen = event_gen
        self.reporter = reporter
        self.driver = driver

    def run(self, test_case):
        pass

    def run_all(self):
        pass

    def print_option(self):
        pass

    def run_with_interaction(self):
        pass
