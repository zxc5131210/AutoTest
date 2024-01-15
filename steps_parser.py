import json


class Step:
    @staticmethod
    def read_json(json_path) -> dict:
        with open(json_path, encoding="utf-8") as flow:
            flow = json.load(flow)["steps"]
            return flow


class ProcessStep:
    def __init__(self, step, driver):
        self.step = step
        self.driver = driver

    #
    # def define_event(self):
    #     for event in Step.parse_event:
    #         json_sequence = event["sequence"]
    #         json_describe = event["describe"]
    #         json_element = event["element"]
    #         json_gesture = event["gesture"]
    #         location_x = event["x"]
    #         location_y = event["y"]
    #
    #     print(json_sequence)
