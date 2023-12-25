from datetime import datetime
from generate_html_report import TestReport
import abstract_reporter
from abstract_reporter import AbstractReporter


class ReportData:
    def __init__(self, category, subcategory, testcase, detail, steps, status):
        self.category = category
        self.subcategory = subcategory
        self.testcase = testcase
        self.detail = detail
        self.steps = steps
        self.status = status

    def add_steps(self, steps, msg, status):
        steps_key = f"steps {steps} : {msg}"
        self.steps[steps_key] = status


class HTMLReporter(AbstractReporter):
    def __init__(self) -> None:
        self.report = TestReport()
        self.report_data = ReportData("STB", "NONE", None, None, {}, None)

    def succeed_step(self, steps, msg):
        self._add_step(steps, msg, "Pass")

    def fail_step(self, steps, msg):
        self._add_step(steps, msg, "Fail")

    def _add_step(self, steps, msg, status):
        self.report_data.add_steps(steps, msg, status)

    def add_category(self, msg: str):
        self.report_data.category = msg

    def test_case(self, msg: str):
        self.add_device_info(
            abstract_reporter.MODEL,
            abstract_reporter.FW_VERSION,
            abstract_reporter.APP_VERSION,
        )
        self._add_entry(msg)
        self.save_report()

    def test_title(self, msg: str) -> None:
        self.report_data.subcategory = msg

    def _add_entry(self, msg: str) -> None:
        status = "Fail" if "Fail" in self.report_data.steps.values() else "Pass"
        self.report_data.testcase = msg
        self.report_data.detail = msg
        self.report_data.status = status
        self.report_data.steps = self.report_data.steps
        self.report.add_entry(self.report_data)

    def add_device_info(self, model, fw_version, app_version):
        self.report.add_version_info(model, fw_version, app_version)

    def save_report(self) -> None:
        self.report.save_to_file(
            f"./html_report/Automation_{datetime.now().date()}.html"
        )
        self.report_data.testcase = None
        self.report_data.steps = {}
        self.report_data.status = None
