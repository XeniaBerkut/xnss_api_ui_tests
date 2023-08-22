import json
import os
import pytest
import requests

from api.entities.user import User
from api.enums.endpoints import Endpoints
from helpers.test_data_helpers import get_test_data_from_json
from src.helpers.logger import Logger

logger = Logger(logging_level='DEBUG')


@pytest.mark.order(1)
def test_token_validation(partner_token):
    logger.info("Set header")
    headers: dict = get_test_data_from_json(os.path.join(
        os.path.dirname(__file__),
        "test_authorisation_data_headers.json"))
    headers["Authorization"] = partner_token
    logger.info("Get auth request")
    response = requests.get(
        Endpoints.TOKEN.value,
        headers=headers
    )
    logger.info("Check if status_code is correct")
    assert response.status_code == 200, \
        f'Expected status code 200, but was {response.status_code}. '


data_auth_fail = get_test_data_from_json(os.path.join(
    os.path.dirname(__file__),
    "test_authorisation_data.json"))


@pytest.mark.order(1)
@pytest.mark.parametrize("test_case",
                         data_auth_fail,
                         ids=[data["test_case_title"] for data in data_auth_fail])
def test_authorisation_faulty(test_case: dict):
    logger.info("Set header and body")
    headers: dict = get_test_data_from_json(os.path.join(
        os.path.dirname(__file__),
        "test_authorisation_data_headers.json"))
    user = User(**test_case["data"])

    logger.info("Request authorisation")
    response = requests.post(
        Endpoints.AUTH.value,
        headers=headers,
        data=user.to_json()
    )
    logger.debug(f"Print response {response.json()}")
    logger.info("Check if status_code is correct")
    assert response.status_code == test_case["expected_response"], \
        f'Expected {test_case["expected_response"]}, but was {response.status_code}'
