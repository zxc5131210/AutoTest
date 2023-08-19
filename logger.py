"""
log file setting
"""
import logging


LOGGING_LEVEL = logging.DEBUG
DATE_FORMAT = '%Y%m%d %H:%M:%S'
FORMAT = '%(asctime)s %(levelname)-2s %(message)s'


class Logger:

    def __init__(self) -> None:
        self.logger = logging
        self.logger.basicConfig(
            level=LOGGING_LEVEL,
            format=FORMAT,
            datefmt=DATE_FORMAT
        )

    def debug(self, msg: str) -> None:
        self.logger.debug(msg)

    def info(self, msg: str) -> None:
        self.logger.info(msg)

    def warring(self, msg: str) -> None:
        self.logger.warning(msg)

    def error(self, msg: str) -> None:
        self.logger.error(msg)

    def critical(self, msg: str) -> None:
        self.logger.critical(msg)


if __name__ == '__main__':
    logger = Logger()
    logger.info('aaa')
