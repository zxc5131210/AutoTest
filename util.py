import json

from locator import locator


def parse_step(json_path) -> dict:
    with open(json_path, encoding="utf-8") as flow:
        flow = json.load(flow)["steps"]
        return flow


def assort_element(element, gesture, driver):
    try:
        if element in locator:
            return driver(resourceId=locator[element])
        if "xpath" in gesture:
            return driver.xpath(element)
        elif "description" in gesture:
            return driver(description=element)
        elif "text" in gesture:
            return driver(text=element)
        elif "classname" in gesture:
            return driver(className=element)
    except Exception:
        return element
