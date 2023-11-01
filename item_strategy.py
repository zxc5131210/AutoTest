class Strategy:
    def __init__(self, event_gen: object, logger: object, driver: object) -> object:
        self.event_gen = event_gen
        self.report = logger.report_data
        self.logger = logger
        self.driver = driver

    def run(self):
        pass

    def run_all(self):
        pass
