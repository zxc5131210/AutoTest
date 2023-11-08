class Strategy:
    def __init__(self, event_gen: object, driver: object, reporter: object) -> object:
        self.event_gen = event_gen
        self.reporter = reporter
        self.driver = driver

    def run(self):
        pass

    def run_all(self):
        pass
