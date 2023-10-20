"""
log and csv output setting
"""
import logging
import csv
from datetime import datetime
from HTMLReport import TestReport

LOGGING_LEVEL = logging.DEBUG
DATE_FORMAT = "%Y%m%d %H:%M:%S"
FORMAT = "%(asctime)s %(levelname)-2s %(message)s"
pass_log = []
report_data = {
    "category": "STB",
    "subcategory": None,
    "testcase": None,
    "detail": None,
    "steps": {},
    "status": None,
}


class Logger:
    def __init__(self, log_file=f"./Log/log-{datetime.now()}.csv") -> None:
        self.logger = logging
        self.logger.basicConfig(level=LOGGING_LEVEL, format=FORMAT, datefmt=DATE_FORMAT)
        self.log_file = log_file
        self.pass_log = pass_log
        self.report = TestReport()

    def debug(self, msg: str) -> None:
        self.logger.debug(msg)

    def info(self, steps, msg: str) -> None:
        """

        @param steps: sequence
        @param msg: operate
        @return status: success
        """
        self.logger.info(msg)
        self._describe_to_csv(f"steps:{steps}", msg, "Success")
        pass_log.append("success")
        report_data["steps"][f"steps{steps}: {msg}"] = "Pass"

    def warning(self, msg: str) -> None:
        self.logger.warning(msg)
        self._describe_to_csv("WARNING", msg, "Warning")

    def error(self, steps, msg: str) -> None:
        """

        @param steps: sequence
        @param msg: error msg
        @return status: fail
        """
        self.logger.error(msg)
        self._describe_to_csv(f"steps:{steps}", msg, "Fail")
        pass_log.append("fail")
        report_data["steps"][f"steps:{steps} {msg}"] = "Fail"

    def critical(self, msg: str) -> None:
        self.logger.critical(msg)
        self._write_to_csv("CRITICAL", msg, "Critical")

    # log to csv file
    def _write_to_csv(self, level: str, msg: str, status: str) -> None:
        with open(self.log_file, "a", encoding="utf-8", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([level, msg, status])

    def _describe_to_csv(self, level: str, msg: str, status: str) -> None:
        with open(self.log_file, "a", encoding="utf-8", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([""] * 2 + [level, msg, status])

    def Test(self, msg: str) -> None:
        status = "Fail" if "fail" in pass_log else "Pass"

        self._write_to_csv("", msg, status)
        report_data.update(
            {
                "testcase": msg,
                "detail": msg,
                "status": status,
                "steps": report_data.get("steps", {}),
            }
        )

        self.report.add_entry(
            category=report_data["category"],
            subcategory=report_data["subcategory"],
            testcase=report_data["testcase"],
            detail=report_data["detail"],
            steps=report_data["steps"],
            status=report_data["status"],
        )

        self.report.save_to_file("test_report.html")
        self.initialize_data()

    @staticmethod
    def initialize_data():
        report_data["testcase"] = None
        report_data["steps"] = {}
        report_data["status"] = None

    def test_title(self, msg: str) -> None:
        self._write_to_csv(msg, "", "")
        report_data["subcategory"] = msg


if __name__ == "__main__":
    logger = Logger()
    report = TestReport()
