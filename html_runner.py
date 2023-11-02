from datetime import datetime
from generate_html_report import TestReport
import abstract_reporter
from abstract_reporter import AbstractReporter

MODEL = None
FW_VERSION = None
APPVERSION = []


class HTMLReporter(AbstractReporter):
    pass_log = []

    report_data = {
        "category": "STB",
        "subcategory": "None",
        "testcase": None,
        "detail": None,
        "steps": {},
        "status": None,
    }

    def __init__(self) -> None:
        self.report = TestReport()

    def succeed_step(self, steps, msg: str) -> None:
        self.pass_log.append("success")
        self.report_data["steps"][f"steps{steps}: {msg}"] = "Pass"

    def fail_step(self, steps, msg: str) -> None:
        self.pass_log.append("fail")
        self.report_data["steps"][f"steps:{steps} {msg}"] = "Fail"

    def test_case(self, msg: str):
        self.add_device_info(
            abstract_reporter.model,
            abstract_reporter.fw_version,
            abstract_reporter.app_version,
        )
        self.add_entry(msg)
        self.save_report()
        self.pass_log.clear()

    def test_title(self, msg: str) -> None:
        self.report_data["subcategory"] = msg

    def add_entry(self, msg: str) -> None:
        status = "Fail" if "fail" in self.pass_log else "Pass"
        self.report_data.update(
            {
                "testcase": msg,
                "detail": msg,
                "status": status,
                "steps": self.report_data.get("steps", {}),
            }
        )
        self.report.add_entry(
            category=self.report_data["category"],
            subcategory=self.report_data["subcategory"],
            testcase=self.report_data["testcase"],
            detail=self.report_data["detail"],
            steps=self.report_data["steps"],
            status=self.report_data["status"],
        )

    def add_device_info(self, model, fw_version, app_version):
        self.report.add_version_info(model, fw_version, app_version)

    def save_report(self) -> None:
        self.report.save_to_file(
            f"./html_report/Automation{datetime.now().date()}.html"
        )
        self.report_data["testcase"] = None
        self.report_data["steps"] = {}
        self.report_data["status"] = None
