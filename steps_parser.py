import json
from locator import locator


class parseSteps:
    @staticmethod
    def read_json(json_path) -> dict:
        with open(json_path, encoding="utf-8") as flow:
            flow = json.load(flow)["steps"]
            return flow


class ProcessStep:
    @staticmethod
    def assort_element(element, driver):
        if element in locator:
            element = driver(resourceId=locator[element])
        return element
