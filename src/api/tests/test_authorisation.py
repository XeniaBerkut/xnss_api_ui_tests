import logging
import sys

import pytest
import requests
from requests.models import Response

from helpers.test_data_helpers import get_test_data_from_json


logger = logging.getLogger()
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

ENDPOINT = "https://my.exnessaffiliates.com/api"





@pytest.mark.order(1)
def test_token_validation():
    logging.info("Set header")
    headers = {
        "Accept": "application/json",
        "Authorization": get_token()
    }
    logging.info("Get auth request")
    response = requests.get(
        ENDPOINT + "/v2/auth/token/",
        headers=headers
    )
    logging.info("Check if status_code is correct")
    assert response.status_code == 200, \
        f'Expected status code 200, but was {response.status_code}'


data_auth_fail = get_test_data_from_json("test_authorisation_data.json")


@pytest.mark.order(1)
@pytest.mark.parametrize("test_case",
                         data_auth_fail,
                         ids=[data["test_case_title"] for data in data_auth_fail])
def test_authorisation_faulty(test_case: dict):
    logging.info("Set header and body")
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    body = test_case["data"]

    logging.info("Request authorisation")
    response = requests.post(
        ENDPOINT + "/v2/auth/",
        headers=headers,
        data=body
    )
    logging.debug(f"Print response {response.json()}")
    logging.info("Check if status_code is correct")
    assert response.status_code == test_case["expected_response"], \
        f'Expected {test_case["expected_response"]}, but was {response.status_code}'
