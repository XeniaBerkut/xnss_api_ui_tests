import logging
import sys

import pytest
import requests
from helpers.test_data_helpers import get_test_data_from_json


logger = logging.getLogger()
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


data_authorisation: dict = get_test_data_from_json("test_authorisation_data.json")


@pytest.mark.order(1)
@pytest.mark.parametrize("test_case",
                         data_authorisation,
                         ids=[data["test_case_title"] for data in data_authorisation])
def test_authorisation(test_case: dict):
    logging.info("Set header and body")
    headers = {
        "Accept": "application/json"
    }
    body = test_case["data"]
    logging.info("Post auth request")
    response = requests.post(
        "https://my.exnessaffiliates.com/api/v2/auth/",
        json=body,
        headers=headers)
    logging.info("Check if status_code is correct")
    assert response.status_code == test_case["expected_response"], \
        f'Expected {test_case["expected_response"]}, but was {response.status_code}'
    # почеум-то не пишет это сообщение
