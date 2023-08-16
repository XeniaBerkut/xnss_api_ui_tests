import time


def make_test_data_uniq(data) -> str:
    return str(time.time_ns() % 1000000) + data
