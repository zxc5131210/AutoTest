class Strategy:
    def __init__(
        self, event_gen: object, driver: object, html_report: object
    ) -> object:
        self.event_gen = event_gen
        self.html_report = html_report
        self.driver = driver

    def run(self):
        pass

    def run_all(self):
        pass
