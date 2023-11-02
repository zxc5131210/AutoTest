from abc import ABC, abstractmethod


class AbstractReporter(ABC):
    @abstractmethod
    def succeed_step(self, steps, msg: str) -> None:
        pass

    @abstractmethod
    def fail_step(self, steps, msg: str) -> None:
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


class DeviceInfo(ABC):
    @abstractmethod
    def model(self):
        pass

    @abstractmethod
    def fw_version(self):
        pass

    @abstractmethod
    def app_version(self):
        pass
