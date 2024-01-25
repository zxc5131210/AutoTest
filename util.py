import json
from locator import locator


def parse_step(json_path) -> dict:
    with open(json_path, encoding="utf-8") as flow:
        flow = json.load(flow)["steps"]
        return flow


def assort_element(element, gesture, driver):
    if element in locator:
        element = driver(resourceId=locator[element])
        return element
    if "xpath" in gesture:
        element = driver.xpath(element)
        return element
    elif "description" in gesture:
        element = driver(description=element)
        return element
    elif "text" in gesture:
        element = driver(text=element)
        return element
    elif "classname" in gesture:
        element = driver(className=element)
        return element
