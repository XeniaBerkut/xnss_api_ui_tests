import json
import time


def make_test_data_uniq(data) -> str:
    return str(time.time_ns() % 1000000) + data


def get_test_data_from_json(test_data_file_name: str) -> dict:
    with open(test_data_file_name, "r") as f:
        test_data = json.load(f)
    return test_data
