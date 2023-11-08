from abc import ABC, abstractmethod


MODEL = None
FW_VERSION = None
APP_VERSION = []


class AbstractReporter(ABC):
    @abstractmethod
    def succeed_step(self, steps, msg: str) -> None:
        pass

    @abstractmethod
    def fail_step(self, steps, msg: str) -> None:
        pass

    @abstractmethod
    def add_category(self, msg: str):
        pass

    @abstractmethod
    def test_case(self, msg: str) -> None:
        pass

    @abstractmethod
    def test_title(self, msg: str) -> None:
        pass

    @abstractmethod
    def add_device_info(self, model, fw_version, app_version):
        pass

    @abstractmethod
    def save_report(self):
        pass
