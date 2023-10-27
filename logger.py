import logging
import csv
from datetime import datetime
from HTMLReport import TestReport

LOGGING_LEVEL = logging.DEBUG
DATE_FORMAT = "%Y%m%d %H:%M:%S"
FORMAT = "%(asctime)s %(levelname)-2s %(message)s"
pass_log = []


class CSVLogger:
    def __init__(self, log_file: str) -> None:
        self.log_file = log_file

    def write(self, level: str, msg: str, status: str) -> None:
        with open(self.log_file + ".csv", "a", encoding="utf-8", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([level, msg, status])

    def write_overview(self, level: str, msg: str, status: str) -> None:
        with open(
            self.log_file + "overview.csv", "a", encoding="utf-8", newline=""
        ) as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([level, msg, status])

    def describe(self, level: str, msg: str, status: str) -> None:
        with open(self.log_file + ".csv", "a", encoding="utf-8", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([""] * 2 + [level, msg, status])


class Logger:
    report_data = {
        "category": "STB",
        "subcategory": "None",
        "testcase": None,
        "detail": None,
        "steps": {},
        "status": None,
    }

    def __init__(self, log_file=f"./Log/log-{datetime.today()}") -> None:
        self.logger = logging
        self.logger.basicConfig(level=LOGGING_LEVEL, format=FORMAT, datefmt=DATE_FORMAT)
        self.csv_logger = CSVLogger(log_file)  # 初始化 CSVLogger
        self.reporter = HTMLReporter()

    def debug(self, msg: str) -> None:
        self.logger.debug(msg)

    def info(self, steps, msg: str) -> None:
        self.logger.info(msg)
        self.csv_logger.describe(f"steps:{steps}", msg, "Success")
        pass_log.append("success")
        Logger.report_data["steps"][f"steps{steps}: {msg}"] = "Pass"

    def warning(self, msg: str) -> None:
        self.logger.warning(msg)
        self.csv_logger.describe("WARNING", msg, "Warning")

    def error(self, steps, msg: str) -> None:
        self.logger.error(msg)
        self.csv_logger.describe(f"steps:{steps}", msg, "Fail")
        pass_log.append("fail")
        self.report_data["steps"][f"steps:{steps} {msg}"] = "Fail"

    def critical(self, msg: str) -> None:
        self.logger.critical(msg)
        self.csv_logger.write("CRITICAL", msg, "Critical")

    def Test(self, msg: str) -> None:
        status = "Fail" if "fail" in pass_log else "Pass"
        self.csv_logger.write("", msg, status)
        self.csv_logger.write_overview("", msg, status)
        self.reporter.add_entry(msg)
        self.reporter.save_report()
        pass_log.clear()

    def test_title(self, msg: str) -> None:
        self.csv_logger.write(msg, "", "")
        self.csv_logger.write_overview(msg, "", "")
        self.report_data["subcategory"] = msg


class HTMLReporter:
    def __init__(self) -> None:
        self.report = TestReport()

    def add_entry(self, msg: str) -> None:
        status = "Fail" if "fail" in pass_log else "Pass"
        Logger.report_data.update(
            {
                "testcase": msg,
                "detail": msg,
                "status": status,
                "steps": Logger.report_data.get("steps", {}),
            }
        )

        self.report.add_entry(
            category=Logger.report_data["category"],
            subcategory=Logger.report_data["subcategory"],
            testcase=Logger.report_data["testcase"],
            detail=Logger.report_data["detail"],
            steps=Logger.report_data["steps"],
            status=Logger.report_data["status"],
        )

    def save_report(self) -> None:
        self.report.save_to_file(f"Automation{datetime.now().date()}.html")
        Logger.report_data["testcase"] = None
        Logger.report_data["steps"] = {}
        Logger.report_data["status"] = None


if __name__ == "__main__":
    logger = Logger()
