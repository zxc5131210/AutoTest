import logging
import csv
from datetime import datetime

LOGGING_LEVEL = logging.DEBUG
DATE_FORMAT = '%Y%m%d %H:%M:%S'
FORMAT = '%(asctime)s %(levelname)-2s %(message)s'


class Logger:

    def __init__(self, log_file=f'log-{datetime.now()}.csv') -> None:
        self.logger = logging
        self.logger.basicConfig(
            level=LOGGING_LEVEL,
            format=FORMAT,
            datefmt=DATE_FORMAT
        )
        self.log_file = log_file

    def debug(self, msg: str) -> None:
        self.logger.debug(msg)

    def info(self, msg: str) -> None:
        self.logger.info(msg)
        self._write_to_csv('INFO', msg, 'Complete')

    def warning(self, msg: str) -> None:
        self.logger.warning(msg)
        self._write_to_csv('WARNING', msg)

    def error(self, msg: str) -> None:
        self.logger.error(msg)
        self._write_to_csv('ERROR', msg, 'Fail')

    def critical(self, msg: str) -> None:
        self.logger.critical(msg)
        self._write_to_csv('CRITICAL', msg)

    def _write_to_csv(self, level: str, msg: str, status: str) -> None:
        with open(self.log_file, 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([level, msg, status])


if __name__ == '__main__':
    logger = Logger()
