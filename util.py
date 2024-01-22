import json
from locator import locator


def parse_step(json_path) -> dict:
    with open(json_path, encoding="utf-8") as flow:
        flow = json.load(flow)["steps"]
        return flow


def assort_element(element, driver):
    if element in locator:
        element = driver(resourceId=locator[element])
    return element
