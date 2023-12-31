import json
import os
import time


def make_test_data_unique(data) -> str:
    return str(time.time_ns() % 1000000) + data


def get_test_data_from_json(test_data_file_name: str) -> dict:
    json_path = os.path.join(test_data_file_name)
    with open(json_path, "r") as json_file:
        test_data = json.load(json_file)
    return test_data
